# Handoff — Episode 003 — ~~LIVE~~ **DISCHARGED 2026-09-05**

> **This handoff has been used and the episode has shipped.** *Quantity Not Stated* is at
> `episodes/ep-003-quantity-not-stated.html`, with `prompts/ep-003-prompts.md` and `series-bible_v5.md`.
> Keep this file as the worked example of what a handoff needs to contain — §3, *things the new session
> will get wrong unless told*, was the part that earned its place — but do not work from it. The current
> state is in `TODO.md` and `the-workbench_v4.md`.
>
> **Two things in it went stale between writing and use**, both worth knowing before the next handoff is
> written: the Dojo path in §3 predates the room → mask → belt restructure, and §4's "every character who
> could appear in this episode has a reference" was true of the cast as planned and not of the cast as
> written — Gus Thornapple turned up in three scenes with no token block, and had to be kept out of the art.

Everything a fresh chat needs to write *Episode 003 · Arc C · saying the expectation out loud.*
Start a **new** conversation. Do not continue an old one — the durable state is in these files, which is
what a bible is for.

---

## 1. Files to attach

Attach all six. They are small, and each one is load-bearing.

| File | Why it has to be there |
|---|---|
| `series-bible_v4.md` | Canon. Characters, appearance tokens, the Keep, the ledger, the Season Clock, nineteen pipeline rules. **Check the version header first** — if it does not say v4, you have a stale copy. |
| `docs/the-arc-room_v2.md` | The Arc C spine is §3. The season machinery is §4. The case-study design is §5. |
| `the-workbench_v3.md` | What is outstanding and what has been decided. Prevents redoing finished work. |
| `docs/site-conventions.md` | Left nav pane, no local CSS, sequential episode order, path conventions. |
| `episodes/_TEMPLATE.html` | The current page skeleton. It is up to date — copy it, do not rebuild it. |
| `episodes/ep-002-the-column-nobody-read.html` | The worked example of every section at full current quality. The one to imitate. |

**Optional but useful:** `prompts/ep-002-prompts.md` — its opening section explains the image tool's one
real constraint, and slots 02 and 05 are the two best prompts written for this project.

---

## 2. The starter prompt

> Write Pigglyvale Episode 003 — Arc C, saying the expectation out loud. The spine is in
> `the-arc-room_v2.md` §3 under *Arc C*. Read `series-bible_v4.md` first; check its version header.
>
> Auntie Yolanda Plum leads. She and Carolyn take on a shared project, and halfway through each of them
> describes what they agreed and the two accounts are completely different. Neither is lying. Neither ever
> said it. The fix is the running gag paying off — they write it down, and Miss Quill's ledger becomes the
> hero, which moves Quill one more step without moving her a whole ring.
>
> Two things are mandatory and both are in Open Threads. **The episode opens with Thomas owning the
> correction Ambrose gave him in the Episode 002 Advisor's Notes** — he was told he had liked Marisol rather
> than read her, and he did not finish owning it. That discharges the second half of the apology rule.
> **And Carolyn's arc holds this episode**, because Thomas's advances: never resolve both in one episode.
>
> Derivation is Luke 14:28, the man who sits down first to count the cost. Show the reasoning: counting the
> cost out loud before starting is ordinary prudence, not pessimism.
>
> Deliver the episode HTML built from `_TEMPLATE.html`, and a prompt file with six self-contained image
> slots. Update the bible afterwards — ledger row, Season Clock row, established facts, running gags, Open
> Threads — and ship it as `series-bible_v5.md`.

---

## 3. Things the new session will get wrong unless told

**Register.** The analysis is bounded by scope, not word count (bible §9b). The story is capped: 1,800–2,200
words. Episode 002's Advisor's Notes run about 1,100 words and that is correct, not bloated.

**The image tool has no negative field.** One text box; everything named gets drawn. Every exclusion is
written as a positive fact. To keep a character out of a frame, do not name them and do not attach their
sheet. Pipeline rules 13, 14, 16, 17.

**Attach a reference for every character named in a slot.** No exceptions. Yolanda has `yolanda-crop.png`,
Pim has `pim-crop.png`, Quill has two crops. **Old Ambrose has nothing** — see §4 below.

**The Washing-Up markup is `.setting` / `p.line` / `span.who` / `<em>`.** Not `.wu-*`. That was harmonised
to match the Keep page, which had it first.

**Movement card:** run `python3 tools/movement_card.py` and paste the output block. Do not hand-write the
SVG. Inward moves are described in plain words, never numbered; the numbered ladder is the outward one.

**The Keep never appears in the story.** It lives in the Advisor's Notes via the Movement card. The story
stays story.

**Second-order thinking, the Keep's ladder, and the harm engines are never named on the site.** Taught
through plot mechanism only.

---

## 4. ~~The one thing that could block the episode~~ — cleared 2026-09-04

**Old Ambrose is drawn.** `ambrose-portrait.png` and `ambrose-sheet.png` are approved and filed, along with
sheets for Yolanda, Quill, Marisol, Pim and Fig. Every character who could appear in this episode has a
reference. Nothing blocks the script or the art.

Two things carried forward from when this was a problem:

- **He can now be staged.** The earlier workaround — keeping Ambrose off the page and letting Thomas own the
  correction in his own voice — is no longer *necessary*. It may still be *better*: a correction landing in
  Thomas's own mouth is stronger than watching it happen. That is now a craft choice rather than a
  constraint.
- **His height is not carried by his sheet.** He is canonically only slightly taller than Miss Quill and
  about twice her width, and a solo sheet cannot hold that. **Any frame with Ambrose and another character
  must state the ratio in the composition block**, exactly as Thomas's frames do. See
  `prompts/ART-QUEUE.md` item 1 for the pair image that would fix it permanently.

---

## 5. Where Episode 003 sits

From `the-arc-room_v2.md` §6:

| | |
|---|---|
| 003 — **Arc C, expectations** | Comic, low-stakes. Thomas owns the 002 correction. Quill moves one more step. |
| 004 — Arc A, the Watch | Needs two clean Movement cards read first. Bruno does not repent inside the episode. |
| 005 — Arc B, the offer | Structural, no antagonist. Rests the register after 004. |
| somewhere 003–005 | The two-hundred-word Pim beat: *"You don't lose your seat here. You might lose the spoon for a week."* |

The Pim beat can live in 003 if it fits at low stakes. It does not have to.
