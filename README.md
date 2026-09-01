# The Chronicles of Pigglyvale — complete site

Everything is in here. Unzip, upload the whole folder, done.

```
index.html
series-bible.md
assets/          style.css · episodes.js
episodes/        ep-001 · ep-002 · _TEMPLATE.html
pages/           the-map-of-the-keep.html
prompts/         00-reference-sheets.md · ep-002-prompts.md
tools/           movement_card.py
docs/            the-arc-room.md · HANDOFF.md · 002-bible-delta.md
images/          _reference/ · keep/ · ep-001/ · ep-002/
```

---

## Before it goes live — three things

**1. Two image folders are empty.** `images/ep-001/` and `images/ep-002/` each need six files. Roll them
from `prompts/ep-002-prompts.md` (Episode One's prompts were not in the project) and drop them in under the
exact names listed in the placeholder file inside each folder. The pages already point at those names, so
nothing needs editing.

**2. Two link placeholders.** Search the whole folder for `{{TOOLBOX_URL}}` — three hits, all in
`episodes/ep-002-the-column-nobody-read.html` and `episodes/_TEMPLATE.html`. Replace with the My Toolbox
base URL. Pigglyvale points at the Toolbox; the Toolbox never points back.

**3. The reference sheets for Quill and Marisol have not been rolled.** Round Five prompts are at the foot
of `prompts/ep-002-prompts.md`. Roll and approve those *before* the six episode illustrations, or the two
new characters will drift between images.

---

## What was rebuilt rather than recovered

The handoff listed several files to paste into the project. Some of them did not arrive, so they were
reconstructed here from the specification in `docs/the-arc-room.md` and `docs/HANDOFF.md`. **If you still
have the originals from that session, paste them over these.** They are, in order of how much guessing was
involved:

| File | What happened |
|---|---|
| `pages/the-map-of-the-keep.html` | **Most reconstructed.** Built from the ring names the arc room states outright (Road, Marketrow, Great Hall, Inner Court, Long Table), the seat/keys rule, the skip-versus-step contrast, and the Watch. **Two guesses, both marked `GUESS` in the source:** the name of ring 1 (*the Kitchen*), and the absence of a numbered rung system. |
| `assets/style.css` | The original, plus three new components at the foot — the Washing-Up, the Movement card, the Toolbox citation — plus the `.layout` / `.epnav` rules, which Episode One's markup already used but which were missing from the project copy. **If the previous session's stylesheet was ever pasted in, check for duplicate class names.** |
| `assets/episodes.js` | Both episode pages load it and it was not in the project. Adding an episode is one line in the `EPISODES` array. |
| `tools/movement_card.py` | Rebuilt from the arc room's three-elements spec. Run it, paste the block into the Notes. The Episode Two card on the page is this script's own output, so the two cannot drift. |
| `series-bible.md` | The project copy was the pre-Keep version, missing §6b–§6e. Episode Two's material was added to it in place. `docs/002-bible-delta.md` lists exactly what was added, so if you paste in the newer bible you can re-apply it in five minutes. |
| `prompts/00-reference-sheets.md` | Unchanged from the project. Round Five now lives at the foot of `prompts/ep-002-prompts.md` instead. |

Not rebuilt, because nothing in the handoff describes it: `voice-for-carolyn.md`. The register rules quoted
inside the skill file were followed for all analysis prose.

---

## Two small notes on the assets

- `02carolyngate.png` and `02carolyngateCROP.png` in the project are **byte-identical** — same MD5. The
  cropped version shipped here as `images/keep/02-carolyn-gate.png`, but if the uncropped one really did
  have a human at the right edge, that crop never got saved. Worth a look.
- The reference sheets were renamed from their flat project names to the canonical hyphenated ones the bible
  and every prompt file expect (`carolynportrait.png` → `images/_reference/carolyn-portrait.png`, and so on).

---

## Adding Episode Three

1. Copy `episodes/_TEMPLATE.html`.
2. Add one line to the `EPISODES` array in `assets/episodes.js`.
3. Add a `.plate` block at the top of the `.plates` grid in `index.html`.
4. Edit `MOVES` in `tools/movement_card.py`, run it, paste the block into the Notes.
5. Update the ledger, the facts, the gags and Open Threads in `series-bible.md`.

Episode Three opens with Thomas owning the correction Ambrose gave him in the Episode Two Notes. That is
logged in Open Threads and it is the first thing on the list.
