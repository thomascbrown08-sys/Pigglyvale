# ART QUEUE — the only art file you need open

**This is the master list for image generation.** If a prompt is not in this file, it is not current.
Every other prompt file on this project is either finished work or an archive, and each one now says so at
the top.

---

## How to use this

1. Work down **§1** in order. Each entry is **one fenced block = one roll.** Nothing is assembled from
   anywhere else and nothing refers to another section.
2. **Attach the files listed above the block.** That line is not optional — a named character with no
   reference attached comes back the wrong species. It has happened twice.
3. Paste the whole block into the image tool. **Do not add a negative prompt.** There is no negative field;
   everything named gets drawn, so every exclusion in these blocks is already written as a positive fact.
4. Save the result under the **exact filename in the heading**, into `images/_reference/`.
5. Move the line to **§2** when it is approved.

**Roll each one two or three times and keep the clearest, not the prettiest.** A reference sheet's whole job
is to be plain: neutral pose, flat background, face readable, nothing in the hands. Whatever is in the
reference leaks into everything generated from it later.

---

## 1. TO ROLL — two, and neither blocks anything

**The seven-item queue of 2026-09-04 is cleared.** Every character who appears in Episode 003 now has a
sheet, so nothing here is holding up the script or the episode art.

---

### 1 · `ambrose-and-quill-pair.png` — 4:3 — *the one worth doing*

**Attach:** `ambrose-sheet.png`, `quill-sheet.png`

Ambrose was specified as short and wide — *not much taller than Miss Quill and roughly twice as wide* — and
his solo sheet could not carry that, because one figure on a flat background has nothing to be short
relative to. This is the fix, and it is the same job `scale-pair.png` does for Carolyn and Thomas.

```
Warm storybook illustration in gouache and soft ink linework, hand-painted texture, visible brush edges.
Sun-warmed palette of deep plum, mango gold, guava pink, herb green and buttermilk paper. Even flat lighting
with no cast shadows. Flat-ish depth and light rendering. Both characters are clearly animal-faced people.

This picture contains two characters standing side by side against a flat buttermilk background, facing
forward, arms at their sides, neutral expressions, hands empty. Nothing else is in the frame.

On the left, an elderly anthropomorphic tortoise. Loose leathery grey-green skin folding at the neck, a
blunt beaked mouth, small deep-set dark eyes under heavy hooded lids, a broad domed shell in weathered olive
and horn brown. A loose pale linen shirt open at the collar, soft olive work trousers turned up at the cuff,
and a wide flat straw hat pushed back off his face so his eyes are visible. He is built low and wide: short
thick limbs, a heavy body close to the ground, broad across the shell.

On the right, a hedgehog woman in her fifties. Short soft dense spines sweeping back close against her head
and shoulders. Wire-rimmed half-moon spectacles, a plum-grey bodice buttoned to the throat with a white
collar and cuffs, a small green ribbon at the collar, an olive-green skirt. She is small, round and stands
very upright.

Their heads are level with each other. He is only very slightly taller than she is, and he is roughly twice
her width. His silhouette is low and horizontal; hers is narrow and vertical. If he looks tall beside her,
the image is wrong.

4:3, both figures full body with a little headroom above both.
```

---

### 2 · `ambrose-key-beats.png` — 16:9 — *later, and only if a scene needs it*

**Attach:** `ambrose-portrait.png`

```
Warm storybook illustration in gouache and soft ink linework, hand-painted texture, visible brush edges.
Sun-warmed palette of deep plum, mango gold, guava pink, herb green and buttermilk paper. Even flat lighting
with no cast shadows. The character is a clearly animal-faced person.

An expression reference strip. The same elderly tortoise's head and shoulders repeated three times against a
flat buttermilk background, identical in style and costume, straw hat pushed back off his face throughout.

First: listening, and deliberately not yet deciding. Eyes steady and on the speaker, hooded lids relaxed,
mouth closed and level.

Second: correcting somebody much younger than him, kindly. Eyes direct, brow untroubled, chin level, no
triumph anywhere in it — this is a face doing somebody a favour, not winning something.

Third: finding out he was wrong, and knowing it, in the second before he says so. Eyes lowered a fraction
and then lifted again, mouth closed, entirely undefended.

Convey the expression through eye shape, lid height, brow and head angle rather than the mouth, which on a
beaked face does not move much.

Wide, 16:9, three evenly spaced heads at the same scale, single row.
```

*Not needed until an episode makes his face carry a beat. Worth having before the one where he corrects
Thomas, since the whole scene turns on face two.*

---

## 2. DONE — approved and filed in `images/_reference/`

No prompts here. This is the record, so you can see at a glance who is finished.

| Character | Files | Status |
|---|---|---|
| **Carolyn** | `carolyn-portrait` · `carolyn-sheet` · `carolyn-expressions` · `carolyn-key-beats` · `carolyn-apology` | **Complete.** |
| **Thomas** | `thomas-portrait` · `thomas-sheet` · `thomas-expressions` · `thomas-key-beats` | **Complete.** |
| **Carolyn + Thomas** | `scale-pair` | **Complete.** Holds the 1.4× height / 2× width ratio. |
| **Old Ambrose** | `ambrose-portrait` · `ambrose-sheet` | **Approved 2026-09-04.** Costume amended in canon to match: shirt and work trousers, not a smock. Height not carried by the sheet — see queue item 1. |
| **Auntie Yolanda** | `yolanda-sheet` · `yolanda-crop` | **Approved 2026-09-04.** The half-raised wing in the three-quarter view came through, which is what she needed. |
| **Miss Quill** | `quill-sheet` · `quill-crop` · `quill-face-crop` | **Approved 2026-09-04.** Spines a little longer than the crops; consistent across all three views, so it stands. |
| **Marisol Vega** | `marisol-sheet` · `marisol-crop` | **Approved 2026-09-04.** Matches the crop closely. |
| **Pim** | `pim-sheet` · `pim-crop` | **Approved 2026-09-04.** |
| **Fig Bramblewick** | `fig-sheet` · `fig-crop` | **Approved 2026-09-04.** |

**Every character who appears in Episode 003 has a sheet.** The crops are kept because they are still the
best reference for a specific pose or expression, but the sheets are now the identity anchors.

**Episode art:** Episodes 001 and 002 are both complete — six slots each, all approved, in
`images/ep-001/` and `images/ep-002/`. Nothing outstanding.

---

## 3. BLOCKED — cannot be rolled yet

Not in the queue because there is nothing to write a prompt from.

| Character | What is missing | Blocks |
|---|---|---|
| **Bruno "Buckets" Marrow** | No appearance token block in the bible, and no crop. He is an otter, young, charming, always with a cart — that is all that exists. | Episode 004 |
| **Gus Thornapple** | No appearance token block. An old boar. | nothing yet |
| **Beatrix Hollyhock** | No appearance token block. A pig, flour to the elbows. | nothing yet |
| **Donna** | Species only (a deer). Engine, role and flaw all undecided. | nothing yet |
| **Dot, Sorrel, Bean** | Names only. Group sheet when an episode needs all four Bramblewicks. | nothing yet |

**To unblock Bruno:** write his token block into `series-bible_v4.md` §3, then he joins this queue. He is
needed before Episode 004 and is the only one on this list that blocks anything.

---

## 4. LATER — nothing is waiting on these

- **Episode 003 illustration slots** — six, after the script exists. Prompts get written then, in a
  per-episode file, using the pattern in `prompts/ep-002-prompts.md`.
- **Dojo mask art** — painted masks on pegs in the practice yard, storybook style. Entirely optional; the
  SVG icons are navigation and do not need replacing.

---

## 5. The rules, in one place

These caused every failure so far. They are in `series-bible_v4.md` §5b as pipeline rules 9–18; this is the
short version.

- **No negative prompts.** One text box, everything named gets drawn. Naming a thing to forbid it draws it.
- **Every character named in a prompt has a reference attached.** No exceptions, including characters who
  came out fine last time.
- **Paste one block. Never a whole file.** A file with several characters in it puts all of them in frame.
- **Say species in shape terms.** *Hedgehog* is not enough — write *short soft dense spines sweeping back
  close against the head*, or you get a porcupine.
- **Small characters read as children.** Give a fraction against a named character and say *grown woman at
  full adult proportion.* Never write the word *child* to exclude one.
- **State Thomas's scale in every shared frame:** 1.4× Carolyn's height, twice her width.
- **A solo sheet cannot hold scale.** It holds face, costume, and proportion-to-itself. Height *between*
  characters needs a pair image, or a sentence in every shared composition block. Ambrose's sheet lost his
  short-and-wide build for exactly this reason and nothing was done wrong.
- **Crops off failed images are legitimate references.** Three of the ones in use came from rolls that were
  unusable as pictures.
