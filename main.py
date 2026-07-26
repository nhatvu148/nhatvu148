import datetime
import json
import os
import random
import re
import sys

import matplotlib.pyplot as plt
import numpy as np
import requests
from dotenv import load_dotenv

load_dotenv()

waka_key = os.getenv("INPUT_WAKATIME_API_KEY")

# 7 days is too noisy to be representative — a single week spent on docs or CI
# config buries the languages actually worked in. 30 days smooths that out.
WAKA_RANGE = "last_30_days"

# WakaTime counts every file type it sees, so markup, config and data formats
# dominate the ranking without saying anything about what was built. Drop them
# and chart programming languages only. Matched case-insensitively.
EXCLUDED_LANGUAGES = {
    "markdown", "json", "yaml", "toml", "ini", "xml", "csv", "tsv",
    "text", "plain text", "other", "docker", "dockerfile", "makefile",
    "git ignore", "gitignore", "git config", "editorconfig", "log",
    "env file", "dotenv", "requirements.txt", "lock", "conf", "properties",
    "binary", "image (svg)", "image (png)",
}

# How many bars to draw
TOP_N = 5


def humanize(seconds: float) -> str:
    """Formats a duration the way WakaTime does: '7 hrs 2 mins'."""
    total_minutes = int(seconds // 60)
    hours, minutes = divmod(total_minutes, 60)
    if not hours:
        return f"{minutes} min" if minutes == 1 else f"{minutes} mins"
    hrs = "hr" if hours == 1 else "hrs"
    mins = "min" if minutes == 1 else "mins"
    return f"{hours} {hrs} {minutes} {mins}"


def compose_header(data: list) -> tuple:
    """Returns (title, subtitle) for the chart.

    The title carries the charted range; the subtitle carries the figures that
    used to live in a separate wakatime.com badge — daily average and all-time
    total — so the graph is the single source of these numbers.
    """
    range_end = datetime.datetime.strptime(data[4], "%Y-%m-%dT%H:%M:%SZ")
    range_start = datetime.datetime.strptime(data[3], "%Y-%m-%dT%H:%M:%SZ")
    title = (
        f"{range_start.strftime('%d %B, %Y')} to {range_end.strftime('%d %B, %Y')}"
        f" — {data[5]} of code"
    )

    parts = []
    if data[6]:
        parts.append(f"{data[6]} daily average")
    if data[7]:
        parts.append(f"{data[7]} all time")
    subtitle = "  ·  ".join(parts)

    print("range header created")
    return title, subtitle


def make_graph(data: list):
    """Make progress graph from API graph"""
    fig, ax = plt.subplots(figsize=(10, 2))
    with open("colors.json") as json_file:
        color_data = json.load(json_file)
    y_pos = np.arange(len(data[0]))
    bars = ax.barh(y_pos, data[2])
    ax.set_yticks(y_pos)
    ax.get_xaxis().set_ticks([])
    ax.set_yticklabels(data[0], color="#586069")
    title, subtitle = compose_header(data)
    # pad leaves room for the subtitle to sit between the title and the bars
    ax.set_title(title, color="#586069", pad=22 if subtitle else 6)
    if subtitle:
        ax.text(
            0.5, 1.02, subtitle,
            transform=ax.transAxes,
            ha="center", va="bottom",
            color="#8b949e", fontsize=8,
        )
    ax.invert_yaxis()
    # Autoscaling makes the longest bar span the full axis, which pushes its
    # duration label past the edge where it gets clipped — so the top language,
    # the one that matters most, ends up the only bar without a number.
    # Reserve headroom for the labels instead.
    # Headroom scales with the longest label so it can't be truncated: the text
    # is drawn in axis space, so a fixed multiplier fits "5 hrs" but clips
    # "12 hrs 47 mins".
    longest_label = max((len(t) for t in data[1]), default=0)
    ax.set_xlim(0, max(data[2]) * (1 + 0.030 * longest_label))
    plt.box(False)
    for i, bar in enumerate(bars):
        if data[0][i] in color_data:
            bar.set_color(color_data[data[0][i]]["color"])
        else:
            bar.set_color(
                "#" + "".join([random.choice("0123456789ABCDEF")
                               for j in range(6)])
            )
        x_value = bar.get_width()
        y_values = bar.get_y() + bar.get_height() / 2
        plt.annotate(
            data[1][i],
            (x_value, y_values),
            xytext=(4, 0),
            textcoords="offset points",
            va="center",
            ha="left",
            color="#586069",
            annotation_clip=False,
        )
    plt.savefig("images/stat.svg", bbox_inches="tight", transparent=True)
    # GitHub's image proxy refuses to render SVGs that contain a DOCTYPE /
    # external DTD reference, so strip it out of matplotlib's output.
    with open("images/stat.svg", "r", encoding="utf-8") as svg_file:
        svg = svg_file.read()
    svg = re.sub(r"<!DOCTYPE[^>]*>\s*", "", svg, flags=re.DOTALL)
    with open("images/stat.svg", "w", encoding="utf-8") as svg_file:
        svg_file.write(svg)
    print("new image generated")


def get_all_time() -> str:
    """All-time coding total, e.g. '6,710 hrs 12 mins'.

    Fail-open: this is decoration on top of the graph, and the workflow runs
    unattended every 6 hours. A hiccup here should cost the subtitle, not the
    whole refresh.
    """
    try:
        res = requests.get(
            "https://wakatime.com/api/v1/users/current/all_time_since_today"
            f"?api_key={waka_key}",
            timeout=30,
        ).json()["data"]
    except Exception as err:  # noqa: BLE001 - any failure degrades the same way
        print(f"warning: all-time total unavailable ({err}); omitting from subtitle")
        return ""
    # A freshly-computed range can come back partial; better no figure than a
    # wrong one that silently understates years of history.
    if not res.get("is_up_to_date"):
        print("warning: all-time total not up to date; omitting from subtitle")
        return ""
    return res.get("text", "")


def get_stats() -> list:
    """Gets API data and returns markdown progress"""
    data = requests.get(
        f"https://wakatime.com/api/v1/users/current/stats/{WAKA_RANGE}"
        f"?api_key={waka_key}"
    ).json()

    try:
        lang_data = data["data"]["languages"]
        start_date = data["data"]["start"]
        end_date = data["data"]["end"]
    except KeyError:
        print("error: please add your WakaTime API key to the Repository Secrets")
        sys.exit(1)

    # Longer ranges are computed lazily; the first request kicks off the job and
    # returns a partial payload. Bail rather than commit a half-built chart.
    if data["data"].get("status") not in (None, "ok"):
        print(f"error: WakaTime range still {data['data'].get('status')}, try again later")
        sys.exit(1)

    languages = [
        lang for lang in lang_data
        if lang["name"].strip().lower() not in EXCLUDED_LANGUAGES
    ]
    if not languages:
        print("error: every language was filtered out — check EXCLUDED_LANGUAGES")
        sys.exit(1)

    top = languages[:TOP_N]
    lang_list = [lang["name"] for lang in top]
    time_list = [lang["text"] for lang in top]
    # Re-base the percentages on the languages actually charted, so the bars
    # fill the axis instead of being squashed by the filtered-out formats.
    charted_seconds = sum(lang["total_seconds"] for lang in top)
    percent_list = [
        lang["total_seconds"] / charted_seconds * 100 for lang in top
    ]

    dropped = len(lang_data) - len(languages)
    print(f"coding data collected ({dropped} non-code formats filtered out)")
    return [lang_list, time_list, percent_list,
            start_date, end_date, humanize(charted_seconds),
            data["data"].get("human_readable_daily_average", ""),
            get_all_time()]


if __name__ == "__main__":
    waka_stat = get_stats()
    make_graph(waka_stat)
    print("python script run successfully")
