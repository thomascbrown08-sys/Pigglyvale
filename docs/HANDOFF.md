# Handoff — everything standing between here and Episode 002

> **HISTORICAL RECORD — 2026-09-01. Do not work from this file.**
> This was the handoff into the Episode 002 session. Its checklist is complete and its filenames predate
> the versioning convention. Kept because it documents what was intended at the time. For current tasks see
> `the-workbench_v3.md`; for canon see `series-bible_v4.md`.

## 1. Put these in the project

So a fresh session has the whole picture without needing this conversation.

- [ ] `series-bible.md` — replace. Now carries §6b the Keep, §6c House Rules, §6d the Second Question,
      §6e Open Threads, the cuffs ruling, and new Established Facts.
- [ ] `voice-for-carolyn.md` — new. Governs all analysis prose.
- [ ] `the-arc-room.md` — new. 002 spine, the four arcs, the case-study design.
- [ ] `00-reference-sheets.md` — replace. Cuffs settled, plus Round Five.
- [ ] `index.html` and `episodes/001-the-small-yeses.html` — upload as structural reference. I have your
      stylesheet but not your page skeletons, and without them I am guessing at your markup.

## 2. Onto the site

- [ ] `SKILL.md` — replace with the version from this session. Header intact, five amendments merged.
      *(Discard `skill-amendments.md`. It was a change-list, not a file to paste — that is what threw the
      frontmatter error.)*
- [ ] `assets/style.css` — replace. Three new components: the Keep chart, the Movement card, the
      Washing-Up.
- [ ] `pages/the-map-of-the-keep.html` — new page.
- [ ] `images/keep/01-keep-aerial.png` and `02-carolyn-gate.png` — use the **cropped** gate image; the
      uncropped one has a human at the right edge.
- [ ] `tools/movement_card.py` — new.
- [ ] Link the Keep from the index. Snippet below.

### Index snippet

Uses classes already in the stylesheet, so it drops straight into the `.plates` grid:

```html
<a class="plate" href="pages/the-map-of-the-keep.html">
  <img src="images/keep/02-carolyn-gate.png" alt="Carolyn in her kitchen doorway at dusk, holding out a
       covered dish, warm and completely level.">
  <span class="plate-number">A Chart from the Kingdom</span>
  <h3 class="plate-title">The Map of the Keep</h3>
  <p class="plate-blurb">Six rooms, working inward, and one mark that can be set anywhere. Carolyn drew it
     on the back of a bread list, the Friday after Fair Week.</p>
  <p class="plate-lesson">Who gets which key, and how anybody moves</p>
</a>
```

A nav link in the masthead as well — `<a href="pages/the-map-of-the-keep.html">The Keep</a>` — since the
episodes will point back at it constantly.

## 3. Art, which has lead time

Roll these **before** the 002 illustrations, not alongside them. Prompts are in Round Five.

- [ ] `quill-sheet.png` · `quill-portrait.png`
- [ ] `marisol-sheet.png` · `marisol-portrait.png`
- [ ] `quill-key-beats.png` — **the one that matters.** Face three is the butterfly moment and there is no
      picture of what that looks like on a hedgehog. The model will offer two wrong answers, a crying woman
      or a sour one. Extra negatives are in the prompt.
- [ ] Approve or amend the two proposed token blocks, then paste them into bible §3.

Check the pair against each other before approving: if Marisol and Carolyn could be sisters, roll again.

## 4. Open, and genuinely optional

- **"The Watch"** as a name — I asked once whether it reads protective or punitive, and never got a ruling.
  It is canon by default now. If it lands wrong it is a find-and-replace; *the Gate* and *the Threshold*
  were the alternatives.
- **Episode 001** — my recommendation is to leave it entirely alone. Do not retro-fit the register or the
  page order. Series drift forward, and 002 reading differently from 001 is normal and fine.

## 5. Then start a fresh chat

Not this one and not the original. Both are long, and the durable state is in the files now — which is the
entire point of keeping a bible. A clean session, with the skill firing correctly against a current bible,
will write a better episode than either thread would.

Say something like: *write Pigglyvale Episode 002, The Column Nobody Read — the spine is in the-arc-room.md.*
The skill will pick it up from there.
