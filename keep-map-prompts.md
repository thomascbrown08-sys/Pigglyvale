# The Map of the Keep — image prompts

**Read this first.** The ring diagram itself is **not** an image-model job. Every label on it is
load-bearing, and diffusion models cannot set type — the style lock's own negative block already says
*"text or lettering in the image."* Asking Gemini for a labelled diagram fights that instruction and loses.
The diagram is SVG in the page: crisp at any size, readable by a screen reader, and editable when a ring
gets renamed.

So the image model does the job it is actually good at: **a textless illustration behind and beside the
diagram.** Labels stay in HTML on top.

Attach `images/_reference/carolyn-portrait.png` and `carolyn-sheet.png` to Slot 02. Reference sheets go on
every prompt, always.

---

## Slot 01 — `01-keep-aerial.png` · 16:9 · page header

> **[STYLE LOCK]** Warm storybook illustration, gouache and soft ink linework, hand-painted texture, visible
> brush edges. Sun-warmed palette: deep plum, mango gold, guava pink, herb green, buttermilk paper.
> Rounded, friendly character shapes. Soft directional light, late-afternoon. Children's picture-book
> sensibility with adult compositional care. Flat-ish depth, no heavy rendering.

**[SCENE]** A hand-painted aerial map of a small walled kingdom, drawn as an old illustrated chart. At the
centre, a warm lit kitchen hearth with smoke curling up. Around it, in widening bands: a long dining table
in a courtyard garden; a small walled inner court with four fruit trees; a great hall with an open roof; a
crowded market street of striped awnings and produce carts; and at the outermost edge an open country road
winding away between hills toward a distant ridge.

**[COMPOSITION]** Straight-down aerial, slight painterly tilt, the hearth exactly centred. Concentric bands
clearly readable as separate zones. Generous empty buttermilk-paper margin all around — the outer eighth of
the frame stays nearly empty so labels can be set over it in the page.

**[MOOD]** Inviting, orderly, safe. A map you would want to live inside. Late afternoon, long soft shadows.

> **[NEGATIVE]** photorealism, 3D render, CGI, anime or manga styling, harsh shadows, dark or grim
> atmosphere, horror, text or lettering in the image, watermarks, extra limbs, uncanny human faces.

*Also add:* labels, banners, scrolls, cartouches, compass rose with letters, numbers, signage, map keys,
legends, fortress, castle keep, military architecture, moat, arrow slits, portcullis, guards, weapons.

*(Pigglyvale is a warm kingdom, not a fortification. The market crowd is majority pig — pigs at the carts,
pigs at the awnings, a couple of pigs walking the road.)*

---

## Slot 02 — `02-carolyn-gate.png` · 4:3 · beside the Watch section

**[STYLE LOCK]** — verbatim, as above.

**[CHARACTERS]** — pasted verbatim from `series-bible.md` §2. Do not paraphrase it, ever; paraphrase is how a character drifts.

> an anthropomorphic pig woman, warm caramel-brown skin, soft pink snout, large dark expressive eyes with full lashes, floppy ears set high on her head, long dark locs falling past her shoulders with small gold cuffs banded along them, a slender gold tiara set with a single amber stone, a mango-gold dress with three-quarter sleeves under a deep-plum apron embroidered with butterflies and green vines; short, round, and warm

*Attach `images/_reference/carolyn-portrait.png` first (identity anchor), then `carolyn-sheet.png`. Tokens hold costume and colour; the sheets hold face and proportion. Neither works alone.*

> **Open question — the forearm cuffs.** The delivered image has wide gold cuffs on both forearms. The > token above does not, and Pipeline Note 5 records them as *cut from canon* because they returned in > only one roll out of eight. But `00-reference-sheets.md` says the opposite — that they are better and > now canonical. The two files disagree. Rule it one way and fix whichever file is wrong.

**[SCENE]** Princess Carolyn stands in the open doorway of a warm kitchen at dusk, one hand resting easily
on the doorframe, the other holding a covered dish out toward someone just off-frame. Her expression is
kind, level, and entirely unbothered. She is not stepping back and she is not stepping aside. Warm light
behind her, cool blue evening in front of her.

**[COMPOSITION]** Three-quarter view, Carolyn at frame left, the lit doorway behind her, the dark garden
path leading off to the right. The threshold line is visible and clearly between her and the viewer.

**[MOOD]** Generous and immovable at once. Nothing tense, nothing cold. She is glad to see them and she is
not moving.

**[NEGATIVE]** — verbatim, as above. *Also add:* tears, crying, wet eyes, trembling mouth, downcast eyes,
looking away, pleading, anger, scowling, folded arms, defensive posture, slammed door, confrontation.

*(That last block matters more here than anywhere. A boundary held well is level, not distressed and not
hostile — the model will otherwise draw "boundary" as either a sad woman or an angry one, and it is
neither.)*
