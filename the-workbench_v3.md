# The Workbench — Pigglyvale

> **Version 3 · 2026-09-02 · supersedes v2 (2026-09-02)**
> *Changed in this version:* reconciled against the actual site folder. Three §1 entries and two §2 entries
> were stale — the site had moved ahead of the snapshot v2 was written from. See §5. Companion canon files
> are now `series-bible_v4.md` and `the-arc-room_v2.md`.

**The single place to look for outstanding tasks.** Pigglyvale only. Update whenever something ships.

Companion files: `series-bible_v4.md` (canon) · `docs/the-arc-room_v2.md` (planning) ·
`docs/site-conventions.md` (structure).

---

## 0. If you have been away — read this first

Nothing is broken and nothing is urgent. Both episodes are shipped, complete with art, and the site
validates clean. Work in this order when you come back.

| | Do this | Why now |
|---|---|---|
| **1** | **Approve or amend Old Ambrose's token block** (`series-bible_v4.md` §3, marked PROPOSED) | He opens Episode 003 and cannot be drawn. Ten minutes of reading, and it unblocks the roll. |
| **2** | **Roll `ambrose-portrait.png` + `ambrose-sheet.png`** | Rule 9: the sheet goes before the episode art. He is owed one anyway — witness line, bench arc. |
| **3** | **Roll `yolanda-sheet.png`** | She leads Episode 003. `yolanda-crop.png` will carry her, but a lead character deserves a sheet. |
| **4** | **Hand off Episode 003** using `docs/EPISODE-003-HANDOFF.md` | File list and starter prompt are written. Fresh chat. |
| **5** | Decide the Episode 001 repair beat (§1 below) | Two minutes, and it is purely yours. |
| **6** | Roll `quill-sheet.png`, `marisol-sheet.png`, `pim-sheet.png` | Owed, not blocking. Crops are carrying all three. |
| **7** | Write Bruno's token block | Blocks Episode 004, not 003. |

**Steps 1 and 2 are the only ones that block anything.** If you have one evening, spend it there.

Decisions in §2 can wait — none of them blocks Episode 003, and two of them (season length, the Season One
plant) are easier to answer after another episode exists.

---

## 0b. The Dojo — new wing, specimen built

Design rules in `docs/the-dojo-design.md`. Read that before writing any case.

- [x] **Specimen case built** — `dojo/white-01-the-helper.html`, plus `dojo/index.html` (belt board and mask
      list). Wired into the masthead, the front page and the sidebar. Text-only; no art needed.
- [ ] **React to the specimen.** Does the shape carry? The parts most worth judging: the mask card's four
      fields, whether the *further along the same road* fourth response earns its place, and whether the
      closing self-facing section lands as a gift rather than an instrument.
- [x] **Rebuilt as interactive** — `assets/dojo.js`, choices with consequences, Ambrose as sensei. Labels
      withheld until after the outcome. Progressive enhancement: works with JS off.
- [x] **The Mind-Reader** — green belt, built. `dojo/green-01-the-mind-reader.html`.
- [x] **Restructured into a tree** — room → mask → belt. Front page is a mask shelf; belts and escalators
      moved to `how-the-belts-work.html`; mask cards moved onto branch pages, so the leaves are drills only.
- [x] **SVG art layer** — mask icons (blank face where no case exists yet), belt swatches, the practice
      ring, the ditches-and-road cross-section. Generator: `tools/dojo_icons.py`.
- [x] **Reframed as training, not lookup.** The room now sorts masks by *what you fold against* rather
      than by what somebody else does, and the anatomy moved to its own `under-*.html` page so the branch is
      short and the ring is two clicks from the front door.
- [ ] **Painted mask art** — optional, later. A row of masks on pegs in the yard, storybook style. The SVG
      layer is navigation and does not need replacing.
- [x] **The Helper expanded to four drills** — two per perspective, differing on one axis each. The
      pattern is documented in the design doc; it is the shape every case should now follow.
- [ ] **The Mind-Reader needs the same treatment** — it has two drills and wants four. Suggested axes: a
      second *done to you* where the reader must answer in front of other people, and a second *you wear it*
      where the reading is about somebody's feelings toward a third party rather than toward you.
- [ ] **The Turn** — brown belt. The case that justifies the belt ladder. Masked figure stays masked
      throughout. Genesis 3 and 1 Kings 18:17–18.
- [ ] **The Rulebook** (Miss Quill) — the other-facing case at yellow or green.
- [ ] **The Joke** (Bruno, in costume, deliberately not canon) — proves the wing can hold what the kingdom
      cannot.
- [ ] **The Standard** — later. Discernment about when to speak and when not to; Ephesians 4:15.
- [ ] **Mask art** — one image per mask, reused across every case featuring it. None rolled. Cost does not
      scale with content, unlike episode art.

---

## 1. Images to roll

> **Prompt harness reminder.** The tool in use from Episode Two on has **one text box and no negative
> field.** Everything named gets drawn. State every exclusion as a positive fact — *her eyes are dry and her
> mouth is closed*, not *no tears*. To keep a character out of a frame, do not name them and do not attach
> their sheet. Paste one slot at a time, never a whole prompt file. Bible §5, pipeline rules 13–17.

### Priority — cleared

**1. ~~Episode 001's repair beat~~ — done, 2026-09-02.**

The image was in the folder the whole time; only the wiring was missing. `05-repair.png` now sits after the
butterflies paragraph and the close was renumbered `06-close.png`, so Episode One matches the six-slot
contract used from 002 on. Both episodes are now complete art, six slots each.

~~*Still open:* Episode One's pager reads "Episode Two, shortly".~~ **Done 2026-09-02** — it points at
Episode Two. Every pager on the site now resolves to a real page.

### Round Five — already named in the bible as owed

**2. `quill-sheet.png`** — tokens are canon and amended to what the art actually reproduces; running on
`quill-crop.png` + `quill-face-crop.png`. Carry rule 10 in its corrected form: state her height as a fraction
against a named character in frame and say *a grown woman at full adult proportion, a broad settled body,
short limbs, a lined face*. Do **not** write the word *child* anywhere in the prompt — there is no negative
field, and naming it draws it.

**3. `marisol-sheet.png`** — tokens canon, running on `marisol-crop.png`. Rule 9 says the sheet goes before
the episode art, not after; 002 proved it.

### New — Season Two's blocker

**4. Old Ambrose — tokens first, then a sheet.**
He has **no appearance tokens and no reference of any kind.** All that exists: tortoise, retired, keeps bees,
brings dark honey when he means to correct somebody. He corrects Thomas in the Notes, carries the
once-a-season witness line, and is cast in the bench arc — load-bearing in three places and undrawable.
Write the token block into the bible first; roll second.

**5. `carolyn-bench.png` — three faces, Season Two.**
Nothing in her five existing files covers judging. The nearest is *level and resolute*, which is her
**boundary** face — deciding for herself. Ruling on someone else is a different muscle, and per the series'
own rule we should not write it before there is a picture of it.

1. **Listening to a case** — attentive, deliberately withholding judgment, not yet persuaded.
2. **Ruling against someone she loves** — level, kind, unhappy, certain. Not stern, not apologetic.
3. **Realising she got one wrong** — the moment before she says so.

Positive-form exclusions throughout; #3 will otherwise come back crying.

### Proper sheets — still on rough crops

**Crops now exist for all of these except Bruno, Gus and Beatrix.** v2 of this file assumed `pim-crop.png`,
`yolanda-crop.png` and `fig-crop.png` were already in `images/_reference/`; they were not, and Episode 003
would have run Yolanda with nothing attached, which pipeline rule 16 says returns the wrong species. They
were cut from the Episode 001 art on 2026-09-02 and are there now. **Episode 003 is unblocked.**

Roll each proper sheet the first time the character carries a scene; attach `carolyn-sheet.png` for style
every time.

- **Auntie Yolanda Plum** — needed for **Arc C / Episode 003**, next in the sequence. Running on
  `yolanda-crop.png`, which is a good full figure with the wings out.
- **Pim** — highest value after Yolanda. She carries Season One's growth proof and the two-hundred-word beat
  in 003–005. Running on `pim-crop.png`.
- **Fig Bramblewick** — running on `fig-crop.png`.
- **Bruno "Buckets" Marrow** — **no crop, never drawn.** Needed for Arc A (004) and again as the bench arc's
  defendant. Tokens exist in bible §3 but no appearance block — same shape of gap as Ambrose, one episode
  further out. Write tokens, then roll, before 004.
- **Gus Thornapple** · **Beatrix Hollyhock** — no crops, no appearance blocks, lower priority.

### Not yet — blocked on a decision

- **Donna (deer)** — engine, role and flaw still open. Bible §9 proposes flight-response, which would be the
  series' first, and flags the Abandonment Protocol. Settle before rolling.
- **Bramblewick litter** (Dot, Sorrel, Bean) — names only. Group sheet when an episode needs all four.
- **Episode 003 slots 01–06** — after the script.

---

## 2. Decisions to make

**Story**

- [ ] **Theft is double-booked.** Bible §9 ties it to Arc A and the Watch; the bench arc wants it as Season
      Two's first case. It cannot be both.
- [ ] **How long is Season One?** The latency ladder has four rungs; episode count sets the spacing.
- [ ] **Where does the Season One plant go** — the badly-and-quickly-resolved dispute that pays off in
      Season Two. Needs a host episode in the back half.
- [ ] **Donna's engine and role.**
- [ ] **"The Watch" as a name** — protective or punitive? Canon by default; *The Gate* and *The Threshold*
      were the alternatives. A find-and-replace if it lands wrong, and it gets more expensive every episode.
- [ ] **Miss Quill's rewritten grant rule** is due in a month of story time and should appear on the page
      rather than be mentioned. Which episode?

**Craft**

- [ ] **The `presuppositions.md` trial.** Eight assumptions drafted in conversation, not yet written to a
      file. Agreed test: run as read-only reference for two episodes and see whether it changes any actual
      sentence. If yes, fold #5 (*true and kind, not whether it worked*), #6 (*never do to a person what you
      would not describe to them*), and #7 (*episode closes an incident, season changes a disposition*) into
      the `pigglyvale` skill; leave the rest as data. If nothing changes, it was redundant.
- [ ] **Confirm the three-rung ladder is never named on the site** — mechanism only, same as second-order
      thinking.

**Site**

- [x] ~~`_TEMPLATE.html` is behind the current spine~~ — **done.** It now carries six image slots, the
      Washing-Up in canonical markup, a Movement card placeholder, the Toolbox block, and the left nav pane.
      Copy it and it starts right.
- [x] ~~`index.html` — confirm oldest first~~ — **done and verified.** Episode One, Episode Two, then the Map
      of the Keep. The shelf note says so, and the comment inside the file tells the next session to add new
      episodes at the *end* of the run.
- [ ] **`patterns/contingent-worth.html`** in My Toolbox still does not exist; 002's case study motivates it
      and both deep links are parked on the Toolbox index until it does. *(Verified 2026-09-02: the Toolbox
      uses `/patterns/<slug>.html` and has no such page.)*
- [ ] **Old Ambrose's token block** — a proposal is now drafted in `series-bible_v4.md` §3, marked PROPOSED.
      Approve or amend it, then roll a sheet. He is load-bearing in three places and undrawable until this
      is done.

---

## 3. Sequenced work

From arc room §6. Not decisions — just what is next.

| | |
|---|---|
| **003 — Arc C, expectations** | Opens with Thomas owning the 002 correction, discharging the second half of the apology rule. Yolanda-led. Quill moves one more step. |
| **004 — Arc A, the Watch** | Needs two clean Movement cards read first. Bruno does not repent. |
| **005 — Arc B, the offer** | Structural, no antagonist, rests the register after 004. |
| *Somewhere 003–005* | The two-hundred-word Pim beat — *"You don't lose your seat here. You might lose the spoon for a week."* |
| **Later, told in advance** | Arc D, the ward. |

---

## 4. Logged, not scheduled

- **College or food-establishment setting** — bakery or Marisol's pitch is the cheaper, more canon-consistent
  route than inventing a college in Snouton.
- **The butterfly motif** — reserved for the day Carolyn says something in the first person in a story.
- **Quill's backstory** — order once saved her when nothing else did. Reveal slowly, maybe season two.

---

## 5. Corrections carried forward

### v2 → v3 (reconciled against the actual site folder)

| v2 said | Actually |
|---|---|
| Ep. 001's repair image "may be half-done" | The image is good and the wiring was done, then **reverted at your instruction**. It is a decision, not a task. |
| Pim / Yolanda / Fig are "still on rough crops" | Those crops **did not exist.** Cut from the Ep. 001 art on 2026-09-02; they exist now, and 003 was blocked without them. |
| `_TEMPLATE.html` is behind the spine | Rebuilt. Six slots, Washing-Up, Movement card, Toolbox, left nav. |
| `index.html` — confirm ordering | Confirmed and shipped: sequential, oldest first, both episodes present. |
| Bruno grouped with characters "on rough crops" | Bruno has **no crop and no appearance block.** Same gap as Ambrose, due before 004. |

### v1 → v2 (kept for the record)

Recorded so the same errors are not reintroduced from an old copy.

| v1 said | Actually |
|---|---|
| Roll Ep. 001's repair image | A sixth image already exists in the folder, unused. Check before rolling. |
| Quill's sheet "may already exist" | Crops exist and tokens are canon; the **sheet** is owed, and the bible already says so (Round Five). |
| Add exclusions to the negative block | The current tool has **no negative field.** Naming a thing to forbid it draws it. Positive form only. |
| Donna needs an engine decided | Still true, but the bible already proposes one — flight response — with the Abandonment Protocol flagged. |
