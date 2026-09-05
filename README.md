# The Chronicles of Pigglyvale — complete site

> **Build v5 · 2026-09-05 · supersedes v1 (Episode Two + the Dojo).**
> *Also in this build:* **the theft double-booking is resolved and the Watch's name is settled.** Theft runs
> as one thread across two seasons rather than two episodes competing for one plot, and **Episode 004 is now
> blocked on nothing.** Planning is **`docs/the-arc-room_v3.md`**.
>
> *Also in this build:* **Bruno's and Gus's appearance token blocks are approved and canon**
> (`series-bible_v7.md` §3), which moves both out of the art queue's BLOCKED table and into it as rollable
> items 3 and 4. Episode 004's script is no longer blocked on art — only on the theft ruling. Canon is now
> **`series-bible_v7.md`** and production is **`the-workbench_v6.md`**; both must be re-pasted into Project
> Knowledge.
>
> *Also in this build:* a **full cross-site link audit** — all 22 outbound links re-checked against the live
> Keep Your Heart and My Toolbox indexes; **all resolve and every label still matches its target's live
> title**, so the KYH renumbering did not break anything here. Three now-shipped KYH chapters were linked in
> for the first time (Ch 16 · Repair ×2, Ch 14 · Anger ×1). `docs/CROSS-SITE-RULES.md` is now **v3** and must
> be re-pasted into Project Knowledge.
>
> *Added:* Episode Three, *Quantity Not Stated* — page, six image prompts, `images/ep-003/`, and its
> Movement card generated from `tools/movement_card.py`. Wiring updated: `assets/episodes.js`, `index.html`, and Episode Two's forward
> pager. `TODO.md` rewritten — **Episode Four is blocked on Bruno's sheet and the theft ruling.**
> *Not included:* Episode Three's six images. The page is complete and waiting for them.

Everything is in here. Unzip, upload the whole folder, done.

```
TODO.md                 ← START HERE. Master list, priorities, dependencies.
index.html
series-bible_v7.md      canon — continuity, characters, pipeline rules
the-workbench_v6.md     production detail behind the master list
assets/          style.css · episodes.js · dojo.js
episodes/        ep-001 · ep-002 · ep-003 · _TEMPLATE.html
dojo/            the practice yard — masks, belts, drills
pages/           the-map-of-the-keep.html
prompts/         ART-QUEUE.md ← all art · 00-reference-sheets.md
                 ep-002-prompts.md · ep-003-prompts.md
tools/           movement_card.py · dojo_icons.py
docs/            site-conventions.md · the-arc-room_v3.md · the-dojo-design.md
                 CROSS-SITE-RULES.md · THE-WARD-ARC-BRIEF.md
                 EPISODE-003-HANDOFF.md (spent) · HANDOFF.md (historical)
images/          _reference/ · keep/ · ep-001/ · ep-002/ · ep-003/ (empty)
```

**Superseded files are kept, not overwritten.** Every prior bible, workbench and arc room is still in here.
**The current set is `series-bible_v7.md`, `the-workbench_v6.md` and `docs/the-arc-room_v3.md`.** The
filename carries the version and so does the block at the top of each file — check both before working from
any copy.

---

## Where to start

**`TODO.md`.** It is the master list: what is blocking, what is unblocked, which way the dependencies run,
and which file holds the detail for each item. Everything else is a sublist it points at.

## Before it goes live — one thing

**Episode Three has no art yet.** The page is complete and links six images that do not exist, so those
six plates will be blank until the files land in `images/ep-003/`. Everything about them is pre-written —
filenames, alt text, prompts — so it is a drop-in, not an edit. See `images/ep-003/PLACEHOLDER.md` and
`prompts/ep-003-prompts.md`.

Episodes One and Two are both fully illustrated. Episode One remains at five referenced slots with a sixth
image (`05-repair.png`) sitting unreferenced in its folder, by instruction; see
`images/ep-001/PLACEHOLDER.md`.

Before writing any new prompt, read the opening section of `prompts/ep-002-prompts.md`. **This image tool
has no negative-prompt field** — one text box, everything named gets drawn — so the old `[NEGATIVE]` blocks
were summoning the very things they were meant to exclude. That file is written in the corrected style: one
self-contained box per slot, no negative blocks, every exclusion stated as a positive fact, and a reference
attached for every character named in the frame. `images/ep-001/` still
needs its five files; Episode One's prompts were never in the project, so its placeholder file lists the
subjects rather than the prompts.

*(Two items that used to sit here are resolved: `patterns/contingent-worth.html` is live on My Toolbox and
Episode Two's links point at it, and Quill and Marisol both have proper reference sheets as of
2026-09-04.)*

---

## What was rebuilt rather than recovered

The handoff listed several files to paste into the project. Some of them did not arrive, so they were
reconstructed here from the specification in `docs/the-arc-room_v3.md` and `docs/HANDOFF.md`. **If you still
have the originals from that session, paste them over these.** They are, in order of how much guessing was
involved:

| File | What happened |
|---|---|
| `pages/the-map-of-the-keep.html` | **No longer reconstructed — the original was supplied and now stands.** An earlier version in this folder was a summary written from `docs/the-arc-room_v3.md`; it has been discarded entirely. The live page is the author's `v3`, unaltered except for four file paths and two pager links repointed to this folder structure. Its CSS is in `assets/style.css` under *THE KEEP*. Masthead and footer standardised to match the rest of the site. |
| `assets/style.css` | The original, plus four component blocks at the foot — the Washing-Up, the Movement card, the Toolbox citation, and the Keep — plus the `.layout` / `.epnav` rules, which Episode One's markup already used but which were missing from the project copy. **If the previous session's stylesheet was ever pasted in, check for duplicate class names.** |
| `assets/episodes.js` | Both episode pages load it and it was not in the project. Adding an episode is one line in the `EPISODES` array. |
| `tools/movement_card.py` | Rebuilt from the arc room's three-elements spec. Run it, paste the block into the Notes. The Episode Two card on the page is this script's own output, so the two cannot drift. |
| `series-bible_v7.md` | No longer reconstructed. The author's v3 was supplied and now stands; every version since logs its own changes in its own header. `docs/002-bible-delta.md` records what Episode Two added. |
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

## Adding an episode

Episode Three was built this way and is the current worked example.

1. Copy `episodes/_TEMPLATE.html`. It already has the left navigation pane wired in.
2. Add one line to the `EPISODES` array in `assets/episodes.js`.
3. Add a `.plate` block to the `.plates` grid in `index.html` — at the **end** of the episode run, above
   the Map of the Keep. Episodes are listed in sequence, oldest first; see `docs/site-conventions.md` §2.
4. Point the **previous** episode's pager forward. It ships saying *"Episode N, shortly"* and stays that way
   unless somebody remembers.
5. Edit `MOVES` in `tools/movement_card.py`, run it, paste the block into the Notes. Never hand-write the
   SVG — the card on the page and the script's output are byte-equivalent, which is the only thing keeping
   them from drifting. A leg from a ring **to itself** renders as a bare dot, which is how Episode Three
   draws a character whose standing deliberately did not move.
6. Create `images/ep-00N/` with a `PLACEHOLDER.md` listing the slots.
7. Update the ledger, the Season Clock, the facts, the gags and Open Threads, and ship the bible as the next
   version number rather than editing in place.

**Episode Four is blocked.** Bruno is its lead and has never been drawn, and the theft double-booking has
to be ruled on first. Both are P0 in `TODO.md`.
