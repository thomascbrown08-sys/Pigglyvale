# Handoff — Episode 003

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

## 4. The one thing that could block the episode

**Old Ambrose opens Episode 003 and has never been drawn.**

The episode must open with Thomas owning Ambrose's correction. If that beat is a scene rather than a
reported memory, Ambrose is in a frame — and pipeline rule 16 says a character named in a slot with nothing
attached comes back the wrong species. There is no crop and no sheet.

A **proposed** token block is in `series-bible_v4.md` §3, marked PROPOSED. Three ways through, in order of
preference:

1. **Approve the tokens and roll `ambrose-portrait.png` and `ambrose-sheet.png` before the episode art.**
   Cleanest, and he is owed a sheet regardless — he carries the once-a-season witness line and is cast in
   the Season Two bench arc.
2. **Write the opening so Ambrose is not in frame.** Thomas owns it in the Washing-Up or in his own Notes,
   with Ambrose referred to and not drawn. Legitimate, and arguably better: the correction landing in
   Thomas's own voice is stronger than staging it.
3. Write the script first and roll art later. Workable, but rule 9 says the sheet goes before the episode
   art, and Episode 002 proved what happens otherwise.

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
