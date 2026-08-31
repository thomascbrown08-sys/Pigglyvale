# Reference Sheets — do this once, before any episode art

A reference sheet is a plain, well-lit picture of a character that you **approve once and then attach to
every future prompt**. Its whole job is to stop the character from quietly changing between episodes.

Roll each of these as many times as you like and keep the one you like best. You are not looking for the
prettiest image. You are looking for the **clearest** one: neutral pose, plain background, face readable,
nothing in her hands. A dramatic, moody, beautifully lit shot makes a bad reference, because whatever is in
the reference tends to leak into everything you generate from it.

Save approved files into `images/_reference/` with the names given below.

**Order matters.** Do Carolyn first and approve her. Then generate Thomas with Carolyn's approved sheet
attached, so his style matches hers rather than drifting off on its own. Then do the scale pair last.

---

## Blocks used in every prompt below

**[STYLE LOCK]** — paste unchanged
> Warm storybook illustration, gouache and soft ink linework, hand-painted texture, visible brush edges.
> Sun-warmed palette: deep plum, mango gold, guava pink, herb green, buttermilk paper. Rounded, friendly
> character shapes. Soft directional light. Children's picture-book sensibility with adult compositional
> care. Flat-ish depth, no heavy rendering.

**[NEGATIVE]** — paste unchanged
> photorealism, 3D render, CGI, anime or manga styling, harsh shadows, dark or grim atmosphere, horror, text
> or lettering in the image, watermarks, extra limbs, uncanny human faces, busy background, props, heavy
> shadow.

---

## 1. `carolyn-sheet.png` — turnaround

**[CHARACTER]** an anthropomorphic pig woman, warm caramel-brown skin, large dark expressive eyes, long dark
locs gathered back with small gold cuffs, a slender gold tiara set with a single amber stone, a mango-gold
dress under a deep-plum apron embroidered with butterflies

**[SCENE]** A character reference sheet. The same character shown three times standing in a row: front view,
three-quarter view, and side view. Identical costume and proportions in all three. Flat buttermilk background,
no scenery, no props, nothing held in her hands. Even soft lighting with no dramatic shadow.

**[COMPOSITION]** Wide, 16:9, full body, all three figures the same height and evenly spaced.

**[MOOD]** Neutral and clear. A working document, not a portrait.

---

## 2. `carolyn-portrait.png` — single clean bust

Same **[CHARACTER]** block.

**[SCENE]** A single head-and-shoulders portrait of the character, facing slightly to the left, calm neutral
expression, flat buttermilk background, even soft light. Face fully visible. No props.

**[COMPOSITION]** Square, 1:1, head and shoulders filling most of the frame.

*(Some tools do better with one clean portrait than with a busy turnaround. Make both and use whichever your
tool responds to.)*

---

## 3. `thomas-sheet.png` — turnaround
*Attach the approved `carolyn-sheet.png` to this prompt so the style carries over.*

**[CHARACTER]** an enormous anthropomorphic mallard drake, iridescent green head, crisp white neck ring,
chestnut breast, broad and tall and slightly ridiculous in scale, wearing a plum advisor's sash and small
round spectacles

**[SCENE]** A character reference sheet in the same style as the attached image. The same character shown
three times standing in a row: front view, three-quarter view, side view. Identical costume in all three.
Flat buttermilk background, no scenery, no props. Even soft lighting.

**[COMPOSITION]** Wide, 16:9, full body, three figures evenly spaced.

**[MOOD]** Neutral and clear. Dignified, and just slightly too large for the frame.

---

## 4. `thomas-portrait.png` — single clean bust

Same as #2, with Thomas's character block. Attach `carolyn-portrait.png` for style.

---

## 5. `scale-pair.png` — the size relationship
*Attach both approved sheets.*

**[SCENE]** The two characters standing side by side against a flat buttermilk background, facing forward,
neutral expressions, arms at their sides. The drake is dramatically larger — a full head and shoulders taller
and much broader than the pig woman. Nothing else in the frame.

**[COMPOSITION]** 4:3, full body, both figures fully visible with a little headroom.

**[MOOD]** Plain and clear. This image exists only to fix how big he is next to her.

*This one matters more than it looks. Text will not hold a size relationship across thirty episodes — a
picture will.*

---

## Later, when you want them

Supporting cast sheets, in the same format, using the character blocks from `series-bible.md`:
Pim · Auntie Yolanda Plum · Miss Delphine Quill · Bruno "Buckets" Marrow · Old Ambrose ·
Beatrix Hollyhock · Gus Thornapple · the Bramblewick litter.

No rush. Generate each one the first time that character carries a scene, and attach Carolyn's sheet for
style each time.

---

# Round Two — two things still missing

The first five are approved and filed in `images/_reference/`. Two gaps remain.

## 6. `scale-pair.png` — REDO. He is not big enough.

The first attempt made Thomas about a head taller than Carolyn. The story needs him at roughly **1.7× her
height** — the duck who cannot fit through the side door and takes up the space of three at the Long Table.
Attach both approved portraits and be blunt about the proportion.

**[SCENE]** The two characters standing side by side against a flat buttermilk background, facing forward,
neutral expressions. **The drake is enormous — Carolyn's head reaches only to the middle of his chest, and he
is roughly twice her width.** He towers over her comically. She is short and round; he is vast. Nothing else
in the frame.

**[COMPOSITION]** 4:3, both figures full body with headroom above the drake. **His head occupies the top
third of the frame; hers sits near the middle.** If they look close to the same height, the image is wrong.

**[MOOD]** Plain, clear, and slightly absurd. This image exists only to fix how big he is.

*Check it against this: could this duck fail to fit through an ordinary doorway? If not, roll again.*

---

## 7. Expression strips — my omission, worth fixing

Neither sheet has an expression row, because I left it out of the prompts. It matters more than it sounds,
especially for Thomas: a bill has very little range, and half the emotional beats in this series land on him.
I need to know what *chastened* looks like on a duck before I write him being chastened.

### `carolyn-expressions.png`
*Attach `carolyn-portrait.png`.*

**[SCENE]** An expression reference strip. The same character's head and shoulders repeated six times in a
row against a flat buttermilk background, identical style and costume, showing six expressions in this order:
warm laughing · concentrating while cooking · gently amused · genuinely tired · quietly hurt · saying
something hard and meaning it. No props, no scenery.

**[COMPOSITION]** Wide, 16:9, six evenly spaced heads at the same scale.

### `thomas-expressions.png`
*Attach `thomas-portrait.png`.*

**[SCENE]** An expression reference strip. The same drake's head and shoulders repeated six times in a row
against a flat buttermilk background, identical style and sash, showing six expressions in this order:
pleased with himself · lecturing · alarmed · deflated · chastened and apologizing · quietly fond. Convey the
emotion through eye shape, brow, head angle, and posture rather than the bill, which does not move much.
No props, no scenery.

**[COMPOSITION]** Wide, 16:9, six evenly spaced heads at the same scale.

*The instruction about eyes and head angle is the important line in that prompt. Leave it in.*

---

## Note on Carolyn's forearm cuffs

The scale pair gave her wide gold cuffs on both forearms; the turnaround did not. The cuffs are better —
they rhyme with the gold bands in her locs. They are now part of her canonical token block, so the turnaround
is the odd one out. Not worth regenerating on its own; it will correct itself the next time you roll her.

---

# Round Three — one short roll, two expressions each

The scale pair is approved and the expression strips are filed. Between them, sixteen faces — and the two
faces this whole series is built on are not among them.

Both strips cover **receiving** emotion well (tired, hurt, worried, deflated, chastened) and **social**
emotion well (smug, amused, lecturing, alarmed). Neither covers:

- **Carolyn saying the hard thing.** Level, steady, kind, not angry and not apologetic. This is her boundary
  face. Every episode ends on it.
- **Thomas being tender.** Every one of his eight reads somewhere between smug and grumpy. His love for her
  is the engine of his entire flaw, and there is currently no picture of it.

Four faces. One roll each.

### `carolyn-key-beats.png`
*Attach `carolyn-portrait.png` and `carolyn-expressions.png`.*

**[SCENE]** An expression reference strip in the identical style to the attached images. The same character's
head and shoulders repeated three times against a flat buttermilk background, showing: **(1) level and
resolute — saying something difficult, kindly and without anger, chin steady, eyes direct; (2) tenderly
apologizing — looking softly upward at someone, sorry and entirely undefensive; (3) quietly proud of someone
else.** No props, no scenery.

**[COMPOSITION]** Wide, 16:9, three evenly spaced heads at the same scale, single row.

*Note for #1: she is not stern, and she is not pleading. She has simply decided, and it is kind. That middle
setting is the hardest one to draw and the most important one here.*

### `thomas-key-beats.png`
*Attach `thomas-portrait.png` and `thomas-expressions.png`.*

**[SCENE]** An expression reference strip in the identical style to the attached images. The same drake's
head and shoulders repeated three times against a flat buttermilk background, showing: **(1) quietly fond and
warm, watching someone he loves, crest feathers smooth, eyes soft; (2) apologizing sincerely — head lowered
but eyes lifted and looking directly at the person, not away; (3) delighted, mid-laugh, crest feathers
lifting.** Convey emotion through eye shape, brow, crest feathers and head angle rather than the bill.
No props, no scenery.

**[COMPOSITION]** Wide, 16:9, three evenly spaced heads at the same scale, single row.

*Note for #2: the existing "chastened" face looks away and down, which is shame. An apology looks at you.
That difference is the entire point of the beat, so it has to be visible on his face.*

---

# Round Four — the last one. Three faces, Carolyn only.

**Thomas is finished.** All three key beats landed, and the middle one — head lowered, eyes lifted, glasses
slid down his bill — is the best image in the entire reference set. Nothing more is needed for him.

Carolyn's strip delivered the resolute face and the warm face. What it did not deliver is **apologizing**,
because the model heard "sorry" and drew *crying* — four of the eight have tears. Grief and apology are
different things, and the difference is exactly what this series is trying to show: an apology is not falling
apart, it is looking someone in the eye and saying the true thing.

So: three faces, and the negative instructions are doing most of the work.

### `carolyn-apology.png`
*Attach `carolyn-portrait.png` and `carolyn-key-beats.png`.*

**[SCENE]** An expression reference strip in the identical style to the attached images. The same character's
head and shoulders repeated three times against a flat buttermilk background, showing:
**(1)** apologizing sincerely — chin level, mouth closed, gaze steady and directed straight at the person she
is speaking to, brows soft and open, entirely undefensive;
**(2)** the same apology from slightly below, as though she is seated on the floor looking gently upward at
someone smaller than her, warm and unhurried;
**(3)** listening while someone else apologizes to her — attentive, receiving it, not yet answering.
No props, no scenery.

**[COMPOSITION]** Wide, 16:9, three evenly spaced heads at the same scale, single row.

**[CRITICAL — add these to the negative prompt for this image]**
> tears, crying, weeping, wet eyes, trembling mouth, open mouth, downcast eyes, looking away, pleading,
> distressed, anguished

*The whole prompt hinges on that negative block. Her face here is calm. She is not upset — she is being
honest, which is a steadier thing and much harder to draw.*

*The tearful faces from Round Three are worth keeping in the folder. They are simply not her default hurt
expression; they are for the rare episode that earns them.*
