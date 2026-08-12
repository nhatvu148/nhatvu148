#!/usr/bin/env python3
"""Generate the profile banner with stroke-order animation for 喃哪越.

Stroke data: hanzi-writer-data (makemeahanzi), 1024-unit em square with the
y-axis pointing UP, so every glyph needs scale(s,-s) and a shift to land in
SVG's y-down space.

Each stroke ships as an outline path plus a median (its centreline). The
animation masks the outline with the median drawn as a thick line whose
stroke-dashoffset runs to zero — the mask sweeps along the stroke's path, so
the ink appears the way it is written rather than simply fading in.

Masks, not clipPaths: a clipPath uses fill geometry only and ignores stroke
width, so a stroked median clips to nothing.
"""
import json
import math
import urllib.parse
import urllib.request

CHARS = "喃哪越"
# #DEA584 is Rust's language colour on GitHub, and the colour of 武 in the
# avatar — so the banner is keyed to the identity that is already there rather
# than to a hue I picked. On white it is too pale to carry a hairline, so the
# light theme darkens it to #A95B2D: same hue (22°) and saturation, lower
# lightness, so it still reads as the same colour rather than a second one.
RUST = "#DEA584"
RUST_DEEP = "#A95B2D"
DARK = dict(bg="#0D1117", ink=RUST, ink_op="0.32", ghost_op="0.09", rule=RUST, h1="#E6EDF3", body="#8B949E")
LIGHT = dict(bg="#FFFFFF", ink=RUST, ink_op="0.40", ghost_op="0.11", rule=RUST_DEEP, h1="#1F2328", body="#59636E")

SIZE = 104          # rendered em size, matching the type it sits beside
GRID = 1024         # hanzi-writer coordinate grid
TOP_Y = 900         # glyph top in the data's y-up space
BAND_H = 180
RIGHT = 1150        # right edge, as the old right-anchored <text>

# Roughly half speed. At 0.22s a stroke the hand looked hurried and the eye
# could not follow the order, which is the only reason to draw strokes at all.
STROKE_DUR = 0.17    # per stroke
# Strictly sequential. An earlier version OVERLAPPED strokes (begin advanced by
# DUR - GAP) to make it "read as one hand" — but a hand writes one stroke at a
# time, and the overlap destroyed the very order the animation exists to show.
STROKE_PAUSE = 0.03  # dead time between strokes, as the brush lifts
CHAR_PAUSE = 0.18    # longer beat between characters, as the hand moves across
LEAD_IN = 0.30       # a beat before the first mark, so it does not start mid-blink
# Mask line width, in grid units. A mask only ever applies to its OWN stroke
# outline, so a wide line cannot leak into a neighbour.
#
# The cap MUST be butt, not round. With the dash fully offset the dash length is
# zero, but a round cap still paints a disc of radius MASK_W/2 at the path's
# start — so every one of the 33 strokes leaked a blob from the first frame,
# whatever its scheduled begin time. That, not the ordering, was why the
# animation looked like scattered fragments.
MASK_W = 200


def fetch(ch):
    url = f"https://cdn.jsdelivr.net/npm/hanzi-writer-data@2.0.1/{urllib.parse.quote(ch)}.json"
    with urllib.request.urlopen(url, timeout=20) as r:
        return json.load(r)


def median_path(points):
    """Median polyline as a path `d`, plus its length for the dash sweep."""
    d = f"M {points[0][0]} {points[0][1]}"
    total = 0.0
    for (x0, y0), (x1, y1) in zip(points, points[1:]):
        d += f" L {x1} {y1}"
        total += math.hypot(x1 - x0, y1 - y0)
    # A single-point median (rare, tiny dots) has no length to sweep; give it a
    # nudge so the dash animation still has something to travel.
    return d, max(total, 1.0)


def build(theme):
    data = [fetch(c) for c in CHARS]
    s = SIZE / GRID
    y0 = (BAND_H - SIZE) / 2
    x0 = RIGHT - SIZE * len(CHARS)

    defs, body = [], []
    clock = LEAD_IN          # advances across the whole line, not per character
    for ci, glyph in enumerate(data):
        gx = x0 + ci * SIZE
        # translate into place, flip the y-axis, then drop the glyph's top edge
        # to the origin.
        tf = f"translate({gx:.2f} {y0:.2f}) scale({s:.6f} {-s:.6f}) translate(0 {-TOP_Y})"
        parts = []
        for si, (outline, med) in enumerate(zip(glyph["strokes"], glyph["medians"])):
            mid = f"m{ci}_{si}"
            d, length = median_path(med)
            begin = clock + si * (STROKE_DUR + STROKE_PAUSE)
            defs.append(
                f'<mask id="{mid}" maskUnits="userSpaceOnUse" x="-200" y="-400" '
                f'width="1600" height="1800">'
                f'<path d="{d}" fill="none" stroke="#fff" stroke-width="{MASK_W}" '
                f'stroke-linecap="butt" stroke-linejoin="round" '
                # dasharray, not dashoffset. Hiding via dashoffset relies on the
                # offset exactly matching the path length the BROWSER computes;
                # any disagreement leaves a sliver of ink showing before the
                # stroke's turn. A zero-length dash cannot render at all, whatever
                # the length turns out to be.
                f'stroke-dasharray="0 {length + 8:.1f}">'
                f'<animate attributeName="stroke-dasharray" from="0 {length + 8:.1f}" '
                f'to="{length + 8:.1f} 0" '
                f'begin="{begin:.3f}s" dur="{STROKE_DUR}s" fill="freeze"/>'
                f"</path></mask>"
            )
            parts.append(f'<path d="{outline}" mask="url(#{mid})"/>')
        clock += len(glyph["strokes"]) * (STROKE_DUR + STROKE_PAUSE) + CHAR_PAUSE
        ghost = "".join(f'<path d="{o}"/>' for o in glyph["strokes"])
        body.append(
            f'<g transform="{tf}" fill="{theme["ink"]}">'
            f'<g fill-opacity="{theme["ghost_op"]}">{ghost}</g>'
            f'<g fill-opacity="{theme["ink_op"]}">' + "".join(parts) + "</g>"
            "</g>"
        )

    sans = ("ui-sans-serif,-apple-system,'Segoe UI',Helvetica,Arial,sans-serif")
    lines = [
        (76, 34, "600", theme["h1"], "Developer tools in Rust", 0.0),
        (112, 19, "400", theme["body"], "Agentic coding assistants · MCP servers · AI code review", 0.10),
        (142, 19, "400", theme["body"], "— and a dictionary for a script almost nobody can read anymore", 0.18),
    ]
    text = "".join(
        f'<text x="60" y="{y}" font-family="{sans}" font-size="{fs}" '
        f'font-weight="{fw}" fill="{fill}">{label}'
        f'<animate attributeName="opacity" from="0" to="1" begin="{b}s" dur="0.7s" fill="freeze"/>'
        f'<animateTransform attributeName="transform" type="translate" from="0 7" to="0 0" '
        f'begin="{b}s" dur="0.7s" fill="freeze" calcMode="spline" keyTimes="0;1" '
        f'keySplines="0.2 0.7 0.3 1"/>'
        f"</text>"
        for y, fs, fw, fill, label, b in lines
    )

    total = clock - CHAR_PAUSE + STROKE_DUR
    rule = (
        f'<rect x="0" y="177" width="1200" height="3" fill="{theme["rule"]}">'
        f'<animateTransform attributeName="transform" type="scale" from="0 1" to="1 1" '
        f'begin="{total:.2f}s" dur="0.9s" fill="freeze" calcMode="spline" '
        f'keyTimes="0;1" keySplines="0.4 0 0.2 1"/></rect>'
    )

    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 180" width="1200" '
        'height="180" role="img" aria-label="Vu Nguyen — developer tools in Rust, and a '
        'dictionary for a script almost nobody can read anymore">\n'
        "  <!-- 喃哪越 Nôm Na Việt (U+5583 U+54EA U+8D8A) drawn in stroke order.\n"
        "       Stroke outlines and medians from hanzi-writer-data (makemeahanzi),\n"
        "       CC BY-SA. Animated with SMIL because GitHub's SVG sanitiser strips\n"
        "       <style> blocks — a CSS version renders completely static.\n"
        "       Each mask sweeps a thick line along the stroke's centreline, so the\n"
        "       ink appears as it is written. Plays once. -->\n"
        f"  <rect width=\"1200\" height=\"{BAND_H}\" fill=\"{theme['bg']}\"/>\n"
        "  <defs>" + "".join(defs) + "</defs>\n  "
        + "".join(body) + "\n  " + text + "\n  " + rule + "\n</svg>\n"
    )


if __name__ == "__main__":
    import os
    import sys

    # Defaults to images/ next to this script's repo root, so `task banner`
    # needs no argument; pass one to render somewhere else while iterating.
    default = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "images")
    out = sys.argv[1] if len(sys.argv) > 1 else default
    open(f"{out}/banner-dark.svg", "w").write(build(DARK))
    open(f"{out}/banner-light.svg", "w").write(build(LIGHT))
    print("  written to", out)
