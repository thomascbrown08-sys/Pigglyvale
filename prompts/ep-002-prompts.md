# Episode 002 — *The Column Nobody Read* — image prompts

**Rewritten after the first two hero attempts. Read the next section before rolling anything.**

---

## What went wrong, and the two rules that come out of it

The second hero attempt put a small grey-haired figure in a grey suit and spectacles into the middle of the
frame — a character who does not exist — and it put Carolyn in the picture wearing her tiara, her locs, her
gold cuffs and her butterfly apron, when the prompt had a block explicitly asking for none of those things.

That is not the model misbehaving. It is the model doing what it was told. **This tool has no
negative-prompt field.** There is one text box, and everything named in it gets drawn. So a block reading
*"[NEGATIVE] tiara, crown, locs, butterfly embroidery"* is not an exclusion list. It is a shopping list, and
it is the most reliable way to summon the exact thing you are trying to keep out — which is what happened,
twice.

The same explains the rest. The standing negative block has carried *"uncanny human faces"* since Episode
One; the grey-suited man is an uncanny human face. It carries *"text or lettering"*; lettering keeps
appearing on book spines. It carries *"props"*; props keep arriving.

Hence two rules, and they govern this whole file:

> **1. Roll one box at a time. Paste one slot and nothing else.**
> Every slot below is self-contained — style, cast, scene, composition, mood, with the character
> descriptions written inline. Nothing needs assembling from the top of the file, because assembling from
> the top of the file is how everyone in the kingdom ended up in one picture.
>
> **2. There are no negative blocks in this file, and none should be added.**
> Every exclusion is rewritten as a positive statement of what *is* in the frame. To keep a character out,
> do not name them and do not attach their sheet. That is the whole method and it is the only one that works
> with this tool.

**About the old blocks.** `series-bible_v4.md` §5 still carries a `[NEGATIVE]` block. It was written for a tool
that had a negative field, and it worked there. Do not paste it into this one. The positive-form **STYLE**
paragraph used in every slot below replaces it.

**What is already right.** The second attempt got Marisol exactly correct — silver hair, indigo headwrap,
gold hoop, blue-striped shirt, floury oatmeal smock, about fifty, and unmistakably not Carolyn. She has been
cropped out and saved as `images/_reference/marisol-crop.png`. **Attach that crop to every prompt she
appears in** until a proper sheet exists. The token block works; it was the scaffolding around it that
broke.

**The Quill oversight, and the crop that fixes it.** The first rewrite of this file told you to attach
Marisol's crop and said nothing about Quill — because `quill-portrait.png` has never been rolled, so there
was nothing to name. That was the wrong call and it produced exactly the failure it should have predicted:
with no reference holding her, Quill came back as a **male porcupine in a grey cardigan**. Species, sex and
costume all drifted at once, which is what always happens when a named character in a frame has no picture
attached.

She had already been drawn correctly four times. So she has now been cropped out of her own good images:

- **`images/_reference/quill-crop.png`** — full figure, standing, from `03-beat.png`. Use this one first.
- **`images/_reference/quill-face-crop.png`** — seated, close, from `05-repair.png`. Attach alongside when
  the face matters.

**Attach at least one of them to every prompt Quill appears in.** The rule underneath is simple and it now
applies to every character in this file: *if a character is named in a slot, a picture of that character is
attached to that slot.* No exceptions, including for characters who "have already come out fine."

**Status: all six slots are done and approved.** Everything below is kept as the record of what produced
them, and as the pattern for Episode Three. `05-repair.png` is the best image on the site and `03-beat.png`
is the best composition; both prompts are worth reading before writing new ones.

---

## 01 · `01-hero.png` — 16:9 — Marisol arrives  ·  **DONE, approved**

*Attach: `images/_reference/marisol-crop.png`. **Attach nothing of Carolyn's.***

> **STYLE.** Warm storybook illustration in gouache and soft ink linework, hand-painted texture, visible
> brush edges. Sun-warmed palette of deep plum, mango gold, guava pink, herb green and buttermilk paper.
> Rounded, friendly character shapes; soft directional late-morning light; flat-ish depth and light
> rendering. A children's picture book with adult compositional care. Every character in the frame is a
> clearly animal-faced person, with a snout, bill or muzzle visible on every single face. Any sign or paper
> in the frame is blank.
>
> **CAST.** This picture contains **two named characters** and a background crowd, and nobody else.
>
> **The baker.** A pig woman of about fifty: tall, lean and weathered, dusty rose-grey skin, a broad flat
> snout, small dark eyes with deep laugh lines, close-cropped silver hair under a faded indigo headwrap, one
> small gold hoop earring, a sleeveless oatmeal canvas smock stained with flour worn over a narrow
> blue-striped shirt, bare floury forearms. She stands with her hands on her hips, mid-greeting, entirely at
> ease.
>
> **The drake.** An enormous mallard drake standing upright on orange webbed feet, with a true duck body
> rather than a humanoid one — no arms, wings folded at his sides. Iridescent green head, crisp white neck
> ring, chestnut breast, dappled grey flanks, small round gold spectacles, a deep-plum sash across his chest
> with a gold compass-rose emblem. He stands at the near edge of the crowd, watching the baker with open
> approval.
>
> **The crowd.** Eight or nine townsfolk drifting toward her from the stalls, **almost all of them pigs**,
> with one goose and one otter among them. They are in the middle distance, plainly dressed, and none of
> them wears a crown, a tiara, or an embroidered apron.
>
> **SCENE.** The top of a small market street on a bright morning. The baker has just set down the handles
> of a two-wheeled wooden handcart carrying a barrel-shaped domed clay oven, sooted and glowing at the
> mouth, a thin line of smoke going up from its chimney. Striped awnings, open baskets of dried red and
> green chiles, warm stone underfoot.
>
> **COMPOSITION.** Wide, 16:9. The baker and her oven off-centre left; the crowd curving in from the right
> so the eye travels down the street. Full figures, low sun down the road behind her. The drake is 1.4 times
> the height and twice the width of any pig in the frame, and his head clears the awnings.
>
> **MOOD.** An arrival. Bright, busy, and genuinely welcome.

---

## 02 · `02-beat.png` — 4:3 — the register, being kept  ·  **DONE, approved**

*Attach: `quill-crop.png`, `quill-face-crop.png`, `carolyn-portrait.png`, `marisol-crop.png`, and
`images/ep-002/02-beat-ROOM-REFERENCE.png` — that last one got the Kitchen Royal exactly right and is worth
attaching purely for the room.*

> **STYLE.** *(the STYLE paragraph from slot 01, verbatim)*
>
> **CAST.** This picture contains **three characters** and nobody else.
>
> **The princess.** A pig woman with warm caramel-brown skin, a soft pink snout, large dark eyes with full
> lashes, floppy ears set high on her head, long dark locs past her shoulders with small gold cuffs banded
> along them, a slender gold tiara set with a single amber stone, a mango-gold dress with three-quarter
> sleeves under a deep-plum apron embroidered with butterflies and green vines. Short, round and warm. She
> stands at the worktable signing a page, mid-conversation, unbothered.
>
> **The record-keeper.** **A hedgehog woman** — matching the attached crop exactly. **Her spines are
> short and soft and dense, sweeping back close against her head and shoulders in a smooth rounded shape.**
> A pale cream muzzle, a small dark nose, warm brown eyes behind wire-rimmed half-moon spectacles, round
> cheeks. **She is plainly a woman:** a soft rounded face, and a plum-grey bodice buttoned to the throat
> with a crisp white collar, white cuffs, a small green ribbon tied at her collar, and an olive-green skirt.
> A pencil in her hand. **She is in her fifties and at full adult proportion — a small round body, short
> limbs, and she stands very upright. Standing beside the princess her head reaches the princess's shoulder:
> about two-thirds the princess's height, and clearly a grown woman rather than a young one.** A large
> ledger lies open flat on the table in front of her, its pages ruled and blank, and she is waiting.
>
> **The baker.** The tall, lean, silver-haired pig woman in the indigo headwrap and the floury oatmeal
> smock, at a second table by the window, working a piece of dough with both hands, sleeves rolled, absorbed
> in her own work and not part of the conversation.
>
> **SCENE.** The Kitchen Royal. Whitewashed walls; **a long scrubbed wooden worktable**, well used, running
> across the room; copper pots hanging from an iron rail; braids of garlic and bunched herbs hung to dry; a
> rack of wooden spoons on the wall; wooden shutters standing open onto green. The ledger's pages are ruled
> and blank.
>
> **COMPOSITION.** 4:3. Three figures with the wooden worktable running across the frame. The open ledger is
> the brightest thing in the picture. The furniture is ordinary kitchen scale — the table comes to the
> princess's hip.
>
> **MOOD.** Ordinary administration on a good day. Comic in its smallness. Nobody is worried about anything.

---

## 03 · `03-beat.png` — 4:3 — Marketrow, and the wrong listener

*Already good. Written out for completeness; roll only if you want to.*

*Attach: `marisol-crop.png`, `quill-crop.png`.*

> **STYLE.** *(as slot 01)*
>
> **CAST.** The tall lean silver-haired baker in the indigo headwrap and floury oatmeal smock; a small,
> upright hedgehog woman in a jacket buttoned to the throat and half-moon spectacles, a shopping basket on
> one arm; and six or seven laughing townsfolk, **all of them pigs**. Nobody else.
>
> **SCENE.** Midday at the market. The baker stands among barrels of coloured spice with the ring of pigs
> around her, mid-story, one arm out, delighted, all of them laughing. Beyond the barrels, a little apart
> from the group, the hedgehog has stopped walking. She is looking straight ahead rather than at the group.
> Her face is neutral and composed — the ordinary face of somebody who has simply stopped.
>
> **COMPOSITION.** 4:3. The laughing group fills the left two-thirds in warm daylight. The hedgehog stands
> alone in the right third with a little clear space around her that nobody else has. Both are in the same
> bright midday light.
>
> **MOOD.** A joke landing on one person differently from everybody else, in a bright market, in the middle
> of the day.

---

## 04 · `04-beat.png` — 4:3 — the records room

*Already good. Roll only if you want to.*

*Attach: `quill-crop.png`, `quill-face-crop.png`, `carolyn-key-beats.png`.*

> **STYLE.** *(as slot 01)*
>
> **CAST.** Two characters and nobody else: the small hedgehog record-keeper, and the pig princess with her
> locs tied back in a green cloth.
>
> **SCENE.** A small records room, late afternoon. Shelves of bound ledgers with plain unmarked spines; a
> high window standing open; dust turning in the light. The hedgehog sits behind a desk with a big ledger
> open in front of her, its pages ruled and blank, her pencil set down and squared to the edge of the page.
> Her chin is level and her face is calm. The princess stands on the other side of the desk with one hand on
> the desk edge, her mouth closed and her weight back — she has just stopped talking, and the sharpness is
> going out of her face.
>
> **COMPOSITION.** 4:3, from a little above desk height so the seated hedgehog is not made small by the
> angle. The desk runs between them. Real air between the two figures.
>
> **MOOD.** The second after a sharp thing has been said and heard. Quiet. Both of them are people.

---

## 05 · `05-repair.png` — 4:3 — **the repair. Already the best image on the site.**

*Do not re-roll unless something is actually wrong with it.*

*Attach: `carolyn-apology.png`, `quill-face-crop.png`.*

> **STYLE.** *(as slot 01)*
>
> **CAST.** Two characters and nobody else: the pig princess and the hedgehog record-keeper.
>
> **SCENE.** The records room a few minutes later, in warmer light. Both are **seated**, facing each other
> across the corner of the desk. The princess sits with her hands loose in her lap, reaching for nothing,
> looking directly at the hedgehog. **Her eyes are dry and clear, her mouth is closed, her chin is level,
> her brows are soft and open. She is calm and steady — a composed face, an honest one, not an upset one.**
> The hedgehog sits forward on her chair with both hands flat on her knees and her spines lying flat,
> listening, receiving it, not yet answering. On the shelf behind them, three small yellow butterflies; one
> has settled on the spine of an old ledger. The book spines are plain and unmarked.
>
> **COMPOSITION.** 4:3, both figures at the same eye level, close but not crowded. The butterflies are
> small, ordinary and unremarked, sitting in the background in plain daylight.
>
> **MOOD.** Level, steady and quiet. An apology is a calmer thing than distress, not a sadder one.

---

## 06 · `06-close.png` — 4:3 — the Long Table, and two people leaving it

*Already good. Roll only if you want to.*

*Attach: `thomas-portrait.png`, `scale-pair.png`.*

> **STYLE.** *(as slot 01, with the light changed to dusk)*
>
> **CAST.** An enormous mallard drake in a deep-plum sash with a gold compass-rose emblem and small round
> gold spectacles; a long table of townsfolk, **overwhelmingly pigs**; and, far up the lane and small in the
> frame, seen from behind, a short round pig woman in a plum apron walking away beside a very small
> hedgehog.
>
> **SCENE.** A stone courtyard at dusk with paper lanterns strung overhead in warm gold and plum. A long
> table runs down the frame with **wooden benches down both sides**, crowded with pigs eating: split loaves
> of soft golden bread, a big pot of rice with pigeon peas, a dish of greens. The drake sits at the near end
> at **his own separate small table**, set apart from the long one because he does not fit on a bench.
> Beyond the courtyard the lane runs off into the blue dark, and the two small figures are on it, the pig
> woman carrying a covered plate.
>
> **COMPOSITION.** 4:3. The lit table fills the lower two-thirds. The lane and the two departing figures sit
> small in the upper right, beyond the lantern light. The drake is 1.4 times the height and twice the width
> of any pig at the table, and his head rises well above the seated crowd.
>
> **MOOD.** A warm, full, noisy table, and two people quietly leaving it to go and do something.

---

# The reference sheets, still to be rolled

Worth doing even now: the next episode will need them, and a crop is a stopgap. Same rules — one box at a
time, no negative blocks.

## `marisol-sheet.png` — 16:9

*Attach `marisol-crop.png` only.*

> **STYLE.** *(as slot 01, with even flat lighting and no cast shadows)*
>
> **SCENE.** A character reference sheet. **One character only**, shown three times standing in a row: front
> view, three-quarter view, side view, identical in all three. A pig woman of about fifty: tall, lean,
> weathered, dusty rose-grey skin, a broad flat snout, small dark eyes with deep laugh lines, close-cropped
> silver hair under a faded indigo headwrap, one small gold hoop earring, a sleeveless oatmeal canvas smock
> stained with flour over a narrow blue-striped shirt, bare forearms. Arms at her sides, neutral expression,
> hands empty. A flat buttermilk background, and nothing else at all in the frame.
>
> **COMPOSITION.** Wide, 16:9, full body, three figures the same height and evenly spaced.
>
> **MOOD.** Neutral and clear. A working document.

## `marisol-portrait.png` — 1:1

The same character paragraph. A single head-and-shoulders portrait facing slightly left, calm neutral
expression, flat buttermilk background, even soft light, hands out of frame.

## `quill-sheet.png` — 16:9

*Attach `quill-crop.png` and `quill-face-crop.png`.*

> **SCENE.** A character reference sheet. **One character only**, shown three times standing in a row:
> front, three-quarter, side, identical in all three. A hedgehog woman in her fifties: dark-tipped
> brown-grey spines swept neatly back, a pale cream muzzle, small round black eyes behind wire-rimmed
> half-moon spectacles, a high-collared jacket buttoned to the throat over a starched cream blouse, a pencil
> behind one ear. **She is a grown woman at full adult proportion — a broad settled body, short limbs, a
> lined and composed face. She is short, about two-thirds the height of a grown pig woman, and she carries
> herself very upright.** Flat buttermilk background, hands empty, nothing else in the frame.
>
> **COMPOSITION.** Wide, 16:9, full body, three figures evenly spaced.

## `quill-key-beats.png` — 16:9 — the one that matters

*Attach `quill-face-crop.png`.*

> **SCENE.** An expression reference strip: the same hedgehog woman's head and shoulders repeated three
> times against a flat buttermilk background, in this order.
>
> **(1)** Reading out a rule she knows is right — composed and closed, spines slightly up, chin level, a
> face with no unkindness in it at all. She is simply correct.
> **(2)** Apologizing, sincerely and awkwardly — a face doing this for the first time. Chin level, mouth
> closed, eyes lifted and looking directly at the other person, eyes dry and clear.
> **(3)** Being seen — hearing something true about herself, said kindly. Her spines have gone completely
> flat, her eyes are steady and open, her face is entirely undefended. She is not smiling, and her eyes are
> dry. This is the quietest of the three.
>
> **COMPOSITION.** Wide, 16:9, three evenly spaced heads at the same scale, single row.
>
> *Face three is the one to keep rolling for. The tool will offer two easy answers — a weeping face or a
> sour one — and both are wrong in the same way. What is happening is that a wall came down: the spines go
> flat, and the eyes stay up and dry.*
