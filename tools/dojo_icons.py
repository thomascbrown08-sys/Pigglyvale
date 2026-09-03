FACE = ('<path class="m-face" d="M4 15 C4 6 18 3 32 3 C46 3 60 6 60 15 '
        'C60 28 51 40 32 40 C13 40 4 28 4 15 Z"/>'
        '<ellipse class="m-eye" cx="21" cy="17" rx="6.5" ry="4.6"/>'
        '<ellipse class="m-eye" cx="43" cy="17" rx="6.5" ry="4.6"/>')

MARKS = {
 "helper":     '<path class="m-mark" d="M14 30 C20 37 26 38 32 34"/>'
               '<path class="m-mark" d="M50 30 C44 37 38 38 32 34"/>',
 "mindreader": '<ellipse class="m-mark-f" cx="32" cy="9" rx="4.6" ry="3.2"/>'
               '<path class="m-mark" d="M25 6 L21 3"/><path class="m-mark" d="M39 6 L43 3"/>',
 "turn":       '<path class="m-mark" d="M22 32 C26 38 40 38 43 31"/>'
               '<path class="m-mark" d="M43 31 L46 35"/><path class="m-mark" d="M43 31 L38 32"/>',
 "longwinter": '<path class="m-mark" d="M18 3 L15 10"/><path class="m-mark" d="M27 2 L24 9"/>'
                 '<path class="m-mark" d="M37 2 L34 9"/><path class="m-mark" d="M46 3 L43 10"/>'
                 '<path class="m-mark" d="M20 32 C26 29 38 29 44 32"/>',
 "weatherkeeper": '<path class="m-mark" d="M15 9 C19 5 23 13 27 9"/>'
                   '<path class="m-mark" d="M30 8 C34 4 38 12 42 8"/>'
                   '<path class="m-mark" d="M45 10 C48 7 51 13 54 10"/>',
 "peacemaker": '<path class="m-mark" d="M22 31 C26 35 38 35 42 31"/>',
 "softener":   '<path class="m-mark" d="M18 32 C24 28 40 36 46 31"/>',
 "rulebook":   '<path class="m-mark" d="M20 31 L44 31"/><path class="m-mark" d="M24 35 L40 35"/>',
 "expert":     '<circle class="m-mark" cx="21" cy="17" r="8"/>'
               '<circle class="m-mark" cx="43" cy="17" r="8"/>'
               '<path class="m-mark" d="M29 17 L35 17"/>',
 "joke":       '<path class="m-mark" d="M20 28 C26 37 38 37 44 28"/>'
               '<path class="m-mark" d="M20 28 L44 28"/>',
 "ledger":     '<path class="m-mark" d="M23 29 L23 36"/><path class="m-mark" d="M28 29 L28 36"/>'
               '<path class="m-mark" d="M33 29 L33 36"/><path class="m-mark" d="M38 29 L44 33"/>',
 "standard":   '<path class="m-mark" d="M17 9 L47 9"/><path class="m-mark" d="M23 9 L23 13"/>'
               '<path class="m-mark" d="M32 9 L32 14"/><path class="m-mark" d="M41 9 L41 13"/>',
}

def mask_icon(key=None, cls=""):
    mark = MARKS.get(key, "")
    blank = " is-blank" if not mark else ""
    return ('<svg class="mask-icon%s %s" viewBox="0 0 64 44" role="img" '
            'aria-hidden="true" xmlns="http://www.w3.org/2000/svg">%s%s</svg>'
            % (blank, cls, FACE, mark))

def belt_swatch(colour_class):
    return ('<svg class="belt-swatch %s" viewBox="0 0 64 22" role="img" aria-hidden="true" '
            'xmlns="http://www.w3.org/2000/svg">'
            '<rect class="b-band" x="0" y="6" width="64" height="10" rx="2"/>'
            '<rect class="b-edge" x="0.5" y="6.5" width="63" height="9" rx="2"/>'
            '<path class="b-knot" d="M24 3 L40 3 L40 19 L24 19 Z" rx="2"/>'
            '<path class="b-edge" d="M24 3 L40 3 L40 19 L24 19 Z"/>'
            '</svg>' % colour_class)

RING = ('<div class="ring-art">'
        '<svg viewBox="0 0 320 130" role="img" aria-label="The practice ring: a swept circle of packed '
        'earth with a rope strung round it." xmlns="http://www.w3.org/2000/svg">'
        '<ellipse class="r-ground" cx="160" cy="76" rx="146" ry="46"/>'
        '<ellipse class="r-rope" cx="160" cy="72" rx="132" ry="38"/>'
        '<rect class="r-post" x="24" y="52" width="6" height="34" rx="2"/>'
        '<rect class="r-post" x="290" y="52" width="6" height="34" rx="2"/>'
        '<rect class="r-post" x="157" y="30" width="6" height="26" rx="2"/>'
        '<path class="r-mark" d="M112 88 C132 82 148 82 166 88"/>'
        '<path class="r-mark" d="M150 98 C166 93 182 93 198 98"/>'
        '</svg></div>')
