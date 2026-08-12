#!/usr/bin/env python3
"""Generate images/shipping-{dark,light}.svg — releases per month, last 12.

Replaces the WakaTime graph, which measured hours TYPED. Hours are effort;
releases are output, and output is the thing a reader can act on. The shape of
the data is also the honest story here: quiet for months, then a surge — which
a bar per month shows and an hours-per-week widget cannot.

Reads the GitHub API for every repo in REPOS. Run by .github/workflows/
update-stats.yml alongside the WakaTime refresh, so it cannot go stale.
"""
import collections
import datetime
import json
import os
import subprocess
import urllib.request

REPOS = [
    "video-transcriber-mcp-rs",
    "pr-review-core",
    "kagoni",
    "x402-mcp-proxy",
    "kaniscope-action",
]
OWNER = "nhatvu148"
MONTHS = 12

# Same tokens as the banner, so the two read as one system rather than two
# decisions. See scripts/gen_banner.py.
RUST = "#DEA584"
RUST_DEEP = "#A95B2D"
DARK = dict(bg="#0D1117", bar=RUST, dim="#8B949E", h1="#E6EDF3", grid="#21262D")
LIGHT = dict(bg="#FFFFFF", bar=RUST_DEEP, dim="#59636E", h1="#1F2328", grid="#E4E7EB")

W, H = 1200, 150
PAD_L, PAD_R, PAD_T, PAD_B = 60, 60, 52, 34


def releases(repo):
    """Published release dates for one repo. Uses `gh` when available (it
    carries auth, so the rate limit is 5000/h rather than 60), else the
    anonymous API."""
    url = f"https://api.github.com/repos/{OWNER}/{repo}/releases?per_page=100"
    try:
        out = subprocess.run(
            ["gh", "api", f"repos/{OWNER}/{repo}/releases?per_page=100", "--jq", "[.[].published_at]"],
            capture_output=True, text=True, timeout=30,
        )
        if out.returncode == 0 and out.stdout.strip():
            return json.loads(out.stdout)
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass
    req = urllib.request.Request(url, headers={"User-Agent": "nhatvu148-profile"})
    tok = os.environ.get("GITHUB_TOKEN")
    if tok:
        req.add_header("Authorization", f"Bearer {tok}")
    with urllib.request.urlopen(req, timeout=30) as r:
        return [x["published_at"] for x in json.load(r)]


def build(theme, counts, months, total):
    peak = max(counts) or 1
    plot_w = W - PAD_L - PAD_R
    plot_h = H - PAD_T - PAD_B
    slot = plot_w / len(months)
    bar_w = min(slot * 0.55, 26)

    bars = []
    for i, (m, n) in enumerate(zip(months, counts)):
        x = PAD_L + slot * i + (slot - bar_w) / 2
        h = 0 if n == 0 else max(3, plot_h * n / peak)
        y = PAD_T + plot_h - h
        # A month with nothing shipped gets a baseline tick rather than nothing,
        # so the gap reads as measured rather than as missing data.
        if n == 0:
            bars.append(f'<rect x="{x:.1f}" y="{PAD_T + plot_h - 2:.1f}" width="{bar_w:.1f}" '
                        f'height="2" fill="{theme["grid"]}"/>')
        else:
            bars.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bar_w:.1f}" height="{h:.1f}" '
                        f'rx="1.5" fill="{theme["bar"]}">'
                        f'<animate attributeName="height" from="0" to="{h:.1f}" '
                        f'begin="{0.05 * i:.2f}s" dur="0.5s" fill="freeze" calcMode="spline" '
                        f'keyTimes="0;1" keySplines="0.2 0.7 0.3 1"/>'
                        f'<animate attributeName="y" from="{PAD_T + plot_h:.1f}" to="{y:.1f}" '
                        f'begin="{0.05 * i:.2f}s" dur="0.5s" fill="freeze" calcMode="spline" '
                        f'keyTimes="0;1" keySplines="0.2 0.7 0.3 1"/></rect>')
        # Label only the peak and the two ends — a label under every bar is
        # noise at this size.
        if n == peak or i in (0, len(months) - 1):
            bars.append(f'<text x="{x + bar_w / 2:.1f}" y="{H - PAD_B + 18:.0f}" text-anchor="middle" '
                        f'font-family="{SANS}" font-size="11" fill="{theme["dim"]}">{m[5:]}/{m[2:4]}</text>')
        if n == peak:
            bars.append(f'<text x="{x + bar_w / 2:.1f}" y="{y - 6:.1f}" text-anchor="middle" '
                        f'font-family="{SANS}" font-size="12" font-weight="600" '
                        f'fill="{theme["bar"]}">{n}</text>')

    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
        f'role="img" aria-label="{total} releases across {len(REPOS)} repositories in the last 12 months">\n'
        f'  <rect width="{W}" height="{H}" fill="{theme["bg"]}"/>\n'
        f'  <text x="{PAD_L}" y="30" font-family="{SANS}" font-size="15" font-weight="600" '
        f'fill="{theme["h1"]}">{total} releases in the last 12 months</text>\n'
        f'  <text x="{W - PAD_R}" y="30" text-anchor="end" font-family="{SANS}" font-size="13" '
        f'fill="{theme["dim"]}">{len(REPOS)} repositories</text>\n'
        f'  <line x1="{PAD_L}" y1="{PAD_T + plot_h:.0f}" x2="{W - PAD_R}" y2="{PAD_T + plot_h:.0f}" '
        f'stroke="{theme["grid"]}" stroke-width="1"/>\n  '
        + "".join(bars) + "\n</svg>\n"
    )


SANS = "ui-sans-serif,-apple-system,'Segoe UI',Helvetica,Arial,sans-serif"


def main(out_dir):
    dates = []
    for r in REPOS:
        dates += [datetime.date.fromisoformat(t[:10]) for t in releases(r)]
    today = datetime.date.today()
    months = []
    cur = today.replace(day=1)
    for _ in range(MONTHS):
        months.append(cur.strftime("%Y-%m"))
        cur = (cur - datetime.timedelta(days=1)).replace(day=1)
    months.reverse()

    per = collections.Counter(d.strftime("%Y-%m") for d in dates)
    counts = [per.get(m, 0) for m in months]
    total = sum(counts)

    for name, theme in (("dark", DARK), ("light", LIGHT)):
        open(os.path.join(out_dir, f"shipping-{name}.svg"), "w").write(build(theme, counts, months, total))
    print(f"  {total} releases across {len(REPOS)} repos → shipping-{{dark,light}}.svg")


if __name__ == "__main__":
    import sys
    default = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "images")
    main(sys.argv[1] if len(sys.argv) > 1 else default)
