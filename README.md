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
docs/            site-conventions.md · the-arc-room.md · HANDOFF.md · 002-bible-delta.md
images/          _reference/ · keep/ · ep-001/ · ep-002/
```

---

## Before it goes live — three things

**1. Both episodes have their art.** Episode Two has all six slots filled and approved. Episode One is
unchanged from the project version — five slots, original markup — with a sixth image (`05-repair.png`)
sitting in the folder unreferenced, because adding it would mean editing an episode the handoff said to
leave alone. See `images/ep-001/PLACEHOLDER.md`.

Before writing any new prompt, read the opening section of `prompts/ep-002-prompts.md`. **This image tool
has no negative-prompt field** — one text box, everything named gets drawn — so the old `[NEGATIVE]` blocks
were summoning the very things they were meant to exclude. That file is written in the corrected style: one
self-contained box per slot, no negative blocks, every exclusion stated as a positive fact, and a reference
attached for every character named in the frame. `images/ep-001/` still
needs its five files; Episode One's prompts were never in the project, so its placeholder file lists the
subjects rather than the prompts.

**2. The Toolbox links point at the index, not at a pattern page.** `patterns/contingent-worth.html` does
not exist on My Toolbox yet. Both links in Episode Two go to the index for now, with the future URL sitting
in an HTML comment right beside them — when you write that page, swap the two `href`s and delete the
comment. Pigglyvale points at the Toolbox; the Toolbox never points back.

**3. Quill and Marisol still have no proper reference sheets** — only crops cut from their own good
episode images (`marisol-crop.png`, `quill-crop.png`, `quill-face-crop.png`). Those crops carried all six
Episode Two illustrations and are fine to keep using, but roll the sheets before Episode Three. The prompts
are at the foot of `prompts/ep-002-prompts.md`.

---

## What was rebuilt rather than recovered

The handoff listed several files to paste into the project. Some of them did not arrive, so they were
reconstructed here from the specification in `docs/the-arc-room.md` and `docs/HANDOFF.md`. **If you still
have the originals from that session, paste them over these.** They are, in order of how much guessing was
involved:

| File | What happened |
|---|---|
| `pages/the-map-of-the-keep.html` | **No longer reconstructed — the original was supplied and now stands.** An earlier version in this folder was a summary written from `docs/the-arc-room.md`; it has been discarded entirely. The live page is the author's `v3`, unaltered except for four file paths and two pager links repointed to this folder structure. Its CSS is in `assets/style.css` under *THE KEEP*. Masthead and footer standardised to match the rest of the site. |
| `assets/style.css` | The original, plus four component blocks at the foot — the Washing-Up, the Movement card, the Toolbox citation, and the Keep — plus the `.layout` / `.epnav` rules, which Episode One's markup already used but which were missing from the project copy. **If the previous session's stylesheet was ever pasted in, check for duplicate class names.** |
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

## Before adding any page

Read `docs/site-conventions.md`. It carries the standing structural rules — the left navigation pane on
every content page, no local CSS, one masthead and footer, and how relative paths work here.

## Adding Episode Three

1. Copy `episodes/_TEMPLATE.html`. It already has the left navigation pane wired in.
2. Add one line to the `EPISODES` array in `assets/episodes.js`.
3. Add a `.plate` block to the `.plates` grid in `index.html` — at the **end** of the episode run, above
   the Map of the Keep. Episodes are listed in sequence, oldest first; see `docs/site-conventions.md` §2.
4. Edit `MOVES` in `tools/movement_card.py`, run it, paste the block into the Notes.
5. Update the ledger, the facts, the gags and Open Threads in `series-bible.md`.

Episode Three opens with Thomas owning the correction Ambrose gave him in the Episode Two Notes. That is
logged in Open Threads and it is the first thing on the list.
