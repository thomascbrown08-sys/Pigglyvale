# The Workbench — Pigglyvale

> **Version 3 · 2026-09-02 · supersedes v2 (2026-09-02)**
> *Changed in this version:* reconciled against the actual site folder. Three §1 entries and two §2 entries
> were stale — the site had moved ahead of the snapshot v2 was written from. See §5. Companion canon files
> are now `series-bible_v4.md` and `the-arc-room_v2.md`.

**Production detail for Pigglyvale.** For priorities, dependencies and what to do first, see **`TODO.md`**
at the root — that is the master list and it points here. Update this file whenever something ships.

Companion files: `series-bible_v4.md` (canon) · `docs/the-arc-room_v2.md` (planning) ·
`docs/site-conventions.md` (structure).

---

## 0. If you have been away — read this first

Nothing is broken and nothing is urgent. Both episodes are shipped, complete with art, and the site
validates clean. Work in this order when you come back.

| | Do this | Why now |
|---|---|---|
| **1** | ~~Approve Ambrose's token block~~ | **Done 2026-09-02.** Canon. |
| **2** | **Work down `prompts/ART-QUEUE.md`** | Seven rolls, one paste-block each. Items 1–2 are Ambrose, item 3 is Yolanda, who leads 003. |
| **3** | **Hand off Episode 003** using `docs/EPISODE-003-HANDOFF.md` | File list and starter prompt are written. Fresh chat. |
| **4** | ~~Episode 001 repair beat~~ | **Done.** Wired in, close renumbered, pager pointed forward. |
| **5** | Write Bruno's token block | Blocks Episode 004, not 003. `ART-QUEUE.md` §3. |

**Only the art queue blocks anything.** If you have one evening, spend it there.

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
- [x] **Mind-Reader drill one rebuilt as transcript** — Yolanda named as the wearer, outcomes played out
      as dialogue, analysis pinned to specific lines via `.beat-note`, Ambrose cut to two sentences. This is
      now the house pattern; the first draft was too abstract to follow.
- [x] **Mind-Reader is fully uniform** — both drills are transcripts with pinned notes, and the case closes
      with a prayer. This page is the reference implementation.
- [x] **Prayers designed and added to both cases.** Rule: never petition for the skill. See design doc.
- [ ] **Apply the transcript pattern to the rest** — Mind-Reader drill two, and all four Helper drills.
      They still use narrated summary and read as over-explained beside the rebuilt one.
- [ ] **The Mind-Reader still wants four drills** — a second *done to you* where you must answer in front
      of other people, and a second *you wear it* where the reading is about somebody's feelings toward a
      third party rather than toward you.
- [x] **The Weather-Keeper built** — white *and* yellow belts, four drills each, Romans 12:18 and 1 Cor
      3:6–7. Three masks live, four belts between them.
- [x] **Keep Your Heart cross-links added** — every Pigglyvale page that raises a problem now offers two
      doors: My Toolbox for the clinical name, Keep Your Heart for the fuller Christian treatment. Traffic
      is one-way and stays that way.
- [x] **Toolbox cross-links added** to all three anatomy pages, under *If you want the clinical words for
      it*. Codependency, Parentification, Nowhere safe to fail, Disorganized attachment, DARVO — all live
      on the Toolbox already. Pigglyvale points out; the Toolbox does not point back.
- [x] **Every leaf is now uniform** — Helper converted to transcripts, and the duplicated *taking it off*
      section removed from the Helper and Mind-Reader leaves, since it lives on the anatomy pages. Five
      leaves, all transcript-style, all closing on a prayer.
- [ ] **Mind-Reader wants two more drills** — it is the only mask with two rather than four.
- [x] **The Long Winter built** — green belt, four drills, John 5:6–8. Four masks live: Helper (white),
      Weather-Keeper (white + yellow), Mind-Reader (green), Long Winter (green).
- [x] **The Long Winter, brown belt** — the wing's first brown case. The masked player is unnamed
      throughout, deliberately: the covered face *is* the epistemics. Anchor 1 Thess 5:14.
- [ ] **The Turn** — brown belt. *(Lower priority now — the Long Winter's brown belt already demonstrates
      the two-escalator rule and the Watch in practice.)* The case that justifies the belt ladder. Masked figure stays masked
      throughout. Genesis 3 and 1 Kings 18:17–18.
- [ ] **The Rulebook** (Miss Quill) — the other-facing case at yellow or green.
- [ ] **The Joke** (Bruno, in costume, deliberately not canon) — proves the wing can hold what the kingdom
      cannot.
- [ ] **The Standard** — later. Discernment about when to speak and when not to; Ephesians 4:15.
- [ ] **Mask art** — one image per mask, reused across every case featuring it. None rolled. Cost does not
      scale with content, unlike episode art.

---

## 1. Images to roll

> **Moved.** This section is now **`prompts/ART-QUEUE.md`** — the single master art file, with every
> outstanding roll written as a self-contained copy-paste block, the attachments named per roll, a DONE
> table, and a BLOCKED table for characters with no tokens yet.
>
> Nothing about art lives in this file any more. Old Ambrose's tokens were approved on 2026-09-02 and he is
> queue items 1 and 2.


---

## 2. Decisions to make

**Story**

- [ ] **Theft is double-booked.** Bible §9 ties it to Arc A and the Watch; the bench arc wants it as Season
      Two's first case. It cannot be both.
- [ ] **How long is Season One?** The latency ladder has four rungs; episode count sets the spacing.
- [ ] **Where does the Season One plant go** — the badly-and-quickly-resolved dispute that pays off in
      Season Two. Needs a host episode in the back half.
- [ ] **Donna's engine and role.** *(Also open: whether Donna is the ward in Arc D. See the brief §8 —
      a deer in a kingdom of pigs puts belonging-without-matching on the page, but it may be too on-the-nose
      and it spends a character who might be wanted elsewhere.)*
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
| **Later, told in advance** | **Arc D, the ward.** Now has a planning brief: `docs/THE-WARD-ARC-BRIEF.md`. Not to be written until the five criteria in its §7 are all true — Season Two is probably still too early. Needs a **dedicated planning chat**, and needs the Abandonment Protocol amended before any spine exists. |

---

## 4. Logged, not scheduled

- **The loaf that was not there before** — an episode against the zero-sum assumption, via Beatrix and
  Marisol. Full brief in `series-bible_v4.md` §9e, including the three guards and Proverbs 11:26. Pairs with
  the theft episode: trade creates, taking moves.

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
