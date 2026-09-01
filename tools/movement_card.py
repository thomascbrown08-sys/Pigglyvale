#!/usr/bin/env python3
"""
movement_card.py — build one episode's Movement card as inline SVG.

The arc room refers to this tool as already generated; it was not in the
project, so it has been rebuilt from the spec in `docs/the-arc-room.md`:

    Three elements only.
      - where they stood   (a dot on one ring)
      - where they ended   (a dot on another)
      - the path between   (this is the part that teaches)

    Two path types:
      clean : a solid line, one ring at a time
      skip  : a dashed arc leaping inward with no rungs, then a hard
              snap back out to the outer edge

Writing a card is filling in values, not drawing anything.

Usage
-----
    python3 tools/movement_card.py                 # prints Episode 002's card
    python3 tools/movement_card.py > card.svg      # paste into the Notes

Editing
-------
Change RINGS and MOVES at the top of the file, then re-run. Colours are
CSS custom properties, so the card inherits the site palette and needs no
stylesheet of its own beyond the .movement block in assets/style.css.
"""

import math
import sys

# --- the Keep, outermost first --------------------------------------------
# Ring 1 is innermost. There is deliberately no numbered rung system: a clean
# move is described in plain words in the legend, never labelled with a number.

RINGS = {
    6: "the Road",
    5: "Marketrow",
    4: "the Great Hall",
    3: "the Inner Court",
    2: "the Long Table",
    1: "the Hearth",
}

# --- this episode ---------------------------------------------------------

TITLE = "The Movement Card — Episode Two"

MOVES = [
    {
        "who": "Marisol Vega",
        "note": ["Road to Long Table, four rings,",
                 "none of them earned. Then out to Marketrow."],
        "angle": 200,          # degrees, where on the chart this move sits
        "legs": [
            # (from_ring, to_ring, style, colour-var[, end_angle])
            (6, 2, "skip", "--mango"),
            (2, 5, "clean", "--guava", 243),   # snap back, fanned out
        ],
    },
    {
        "who": "Delphine Quill",
        "note": ["Great Hall to Inner Court.",
                 "One ring. Twenty years."],
        "angle": 20,
        "legs": [
            (4, 3, "clean", "--sofrito"),
        ],
    },
]

CAPTION = (
    "Two movements this fortnight. The big one is drawn with a broken line, "
    "because nothing was underneath it — four rings inward in a fortnight, on "
    "three delightful weeks and a smell of good bread, and then straight back "
    "out to the edge the moment any weight came on. The other one is the tick "
    "mark in the corner. It took twenty years, it moved one ring, and it is "
    "the only one of the two that will still be there next spring."
)

# --- geometry -------------------------------------------------------------

CX, CY = 200, 210
RING_STEP = 25
W, H = 520, 420
LEGEND_X = 372


def radius(ring):
    return ring * RING_STEP


def point(ring, angle_deg):
    a = math.radians(angle_deg)
    r = radius(ring)
    return (round(CX + r * math.cos(a), 1), round(CY - r * math.sin(a), 1))


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def build():
    out = []
    a = out.append

    a('<svg class="movement-svg" viewBox="0 0 %d %d" role="img"' % (W, H))
    a('     xmlns="http://www.w3.org/2000/svg" aria-labelledby="mc-title mc-desc">')
    a('  <title id="mc-title">%s</title>' % esc(TITLE))
    a('  <desc id="mc-desc">A %d-ring diagram of the Keep showing this '
      'episode\'s movements.</desc>' % len(RINGS))

    # rings
    a('  <g fill="none" stroke="var(--ink-soft)" stroke-opacity="0.28" '
      'stroke-width="1">')
    for ring in sorted(RINGS, reverse=True):
        a('    <circle cx="%d" cy="%d" r="%d"/>' % (CX, CY, radius(ring)))
    a('  </g>')

    # ring labels, stacked up the vertical axis
    a('  <g font-family="Literata, Georgia, serif" font-size="9.5" '
      'fill="var(--ink-soft)" text-anchor="middle">')
    for ring in sorted(RINGS, reverse=True):
        y = CY - radius(ring) + 6
        a('    <text x="%d" y="%d">%d · %s</text>'
          % (CX, y, ring, esc(RINGS[ring])))
    a('  </g>')

    # moves
    for m in MOVES:
        ang = m["angle"]
        prev_angle = ang
        a('  <!-- %s -->' % esc(m["who"]))
        for leg in m["legs"]:
            frm, to, style, colour = leg[:4]
            a2 = leg[4] if len(leg) > 4 else ang
            a1 = prev_angle if style == "clean" and len(leg) > 4 else ang
            p1, p2 = point(frm, a1), point(to, a2)
            prev_angle = a2
            if style == "skip":
                # bow the arc so a long leap reads as a leap, not a radius
                mx, my = (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2
                qx, qy = round(mx - (CY - my) * 0.35, 1), round(my - 45, 1)
                a('  <path d="M %s %s Q %s %s %s %s" fill="none" '
                  'stroke="var(%s)" stroke-width="2.5" stroke-dasharray="7 6" '
                  'stroke-linecap="round"/>'
                  % (p1[0], p1[1], qx, qy, p2[0], p2[1], colour))
            else:
                a('  <path d="M %s %s L %s %s" fill="none" stroke="var(%s)" '
                  'stroke-width="2.5" stroke-linecap="round"/>'
                  % (p1[0], p1[1], p2[0], p2[1], colour))
        # dots: start small, finish larger
        first = m["legs"][0]
        a('  <circle cx="%s" cy="%s" r="4.5" fill="var(%s)"/>'
          % (point(first[0], ang) + (first[3],)))
        for i, leg in enumerate(m["legs"]):
            frm, to, style, colour = leg[:4]
            a2 = leg[4] if len(leg) > 4 else ang
            r = 5.5 if i == len(m["legs"]) - 1 else 5
            a('  <circle cx="%s" cy="%s" r="%s" fill="var(%s)"/>'
              % (point(to, a2) + (r, colour)))

    # legend
    y = 232
    a('  <line x1="%d" y1="215" x2="%d" y2="325" stroke="var(--ink-soft)" '
      'stroke-opacity="0.3" stroke-width="1"/>' % (LEGEND_X - 20, LEGEND_X - 20))
    for m in MOVES:
        a('  <text x="%d" y="%d" font-family="Fraunces, Georgia, serif" '
          'font-size="11.5" fill="var(--ink)">%s</text>'
          % (LEGEND_X, y, esc(m["who"])))
        for i, line in enumerate(m["note"]):
            a('  <text x="%d" y="%d" font-family="Literata, Georgia, serif" '
              'font-size="9.5" fill="var(--ink-soft)">%s</text>'
              % (LEGEND_X, y + 16 + i * 12, esc(line)))
        y += 54

    a('</svg>')
    return "\n".join(out)


def wrapped():
    return (
        '<div class="movement">\n'
        '  <h3 class="movement-title">%s</h3>\n\n%s\n\n'
        '  <p class="movement-caption">%s</p>\n'
        '</div>' % (esc(TITLE), build(), esc(CAPTION))
    )


if __name__ == "__main__":
    sys.stdout.write(wrapped() + "\n")
