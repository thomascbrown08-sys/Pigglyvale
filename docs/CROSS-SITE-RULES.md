# Cross-Site Standing Rules — Carolyn Stories Project

**Version 2 · 2026-09-04 · supersedes v1**
*Changed in this version:* verified all three sites live and added a §Status block, since the previous
version had no way to tell what was actually built. Added the full link map. Corrected one rule that v1
stated correctly but that my own suggestion files had drifted from. Everything else is unchanged.

**Paste this into Project Knowledge, replacing the previous copy.** Any chat working on Pigglyvale, Keep
Your Heart, or My Toolbox should read it before making cross-site claims or links.

---

## Status, verified 2026-09-04

| Site | Live | State |
|---|---|---|
| **My Toolbox** | [link](https://thomascbrown08-sys.github.io/My_Toolbox/) | 21 patterns · 7 dynamics · 14 modalities. **All eleven suggested additions are built.** |
| **Keep Your Heart** | [link](https://thomascbrown08-sys.github.io/KeepYourHeart/) | 27 chapters, 24 written. Ch 14 Anger, Ch 16 Repair, Ch 22 Church Hurt pending. Build v2.2. |
| **Pigglyvale** | [link](https://thomascbrown08-sys.github.io/Pigglyvale/index.html) | 2 episodes complete with art · the Keep · the Dojo (5 masks, 7 belt cases) · **9 characters with approved reference sheets as of 2026-09-04.** Episode 003 unblocked. |

Each site's own file is the authority for its detail: `TODO.md` (Pigglyvale, master),
`KEEP-YOUR-HEART-TODO.md`, and `TOOLBOX-SUGGESTIONS.md`. This file carries only what does not change often.

---

## The three sites and how traffic flows

Pigglyvale → Keep Your Heart, and Pigglyvale → My Toolbox.
Keep Your Heart → My Toolbox only — **never to Pigglyvale.**
My Toolbox → **nothing.** It is the base layer and never links out.

Traffic is one-way throughout. If a chat is asked to add a link running the other direction, that is a
stop-and-ask moment, not a judgment call to make alone.

> **A drift caught on 2026-09-04, recorded so it is not repeated.** My own suggestion file proposed
> cross-links between Keep Your Heart and My Toolbox *in both directions* — "a reader landing on Ch 21
> should be able to reach *Toxic shame vs. guilt*, and the reverse." **The second half was wrong.** The
> Toolbox never links out. The rule was right in v1; the suggestion drifted from it, and the Keep Your Heart
> build correctly implemented only the outbound half. No harm done, and the lesson is that a chat proposing
> cross-site work should re-read this file rather than reason from the shape of the sites.

### Why the directions are what they are

- **The Toolbox never links out** because it has to stay usable by somebody who is not in this project at
  all — a reader bringing an informed question to a clinician. An outbound link to a devotional workbook, or
  to a talking-animal kingdom, costs it that.
- **Keep Your Heart never links to Pigglyvale** for the same reason at one remove: it should be handable to
  a counselor, and a link to a fable about pigs changes what kind of document it is.
- **Pigglyvale links to both** because it is the outermost layer and the only one that can afford to.

## The universal content rule

**Write to the pattern, never to the person.** Test: could someone who knows the author reconstruct his
history from this content? If yes, cut it. Applies most strictly in Keep Your Heart Part VI and any Toolbox
page informed by lived experience — which is most of them.

Pigglyvale's version of the same rule: all content stays generic and composite even when personally
informed, and the site never narrates the reader's progress.

---

## The link map, as actually built

Pigglyvale offers **two doors** wherever it raises a problem, and they are deliberately different:
My Toolbox is *"if you want the clinical words for it"*; Keep Your Heart is *"if you want to go further
with this."*

| Pigglyvale page | → My Toolbox | → Keep Your Heart |
|---|---|---|
| Episode 002, Toolbox block | Contingent worth ×2 | ch18 · A Life You Did Not Build |
| The Map of the Keep | Rupture and repair | ch25 · What Was Done To You |
| The Dojo front page | — | ch15 · Truth in Love |
| How the belts work | Fawning | — |
| Under the Helper | Codependency · Nowhere safe to fail | ch17 · Burdens and Loads · ch21 · Care That Was Not Care |
| Under the Weather-Keeper | Over-responsibility · Emotional labour · Hypervigilance · Parentification · Differentiation | ch17 · ch21 · ch13 · Ordered Affections |
| Under the Mind-Reader | Disorganized attachment · DARVO | ch27 · The Record That Survives · ch15 · Truth in Love |
| Under the Long Winter | Learned helplessness · Toxic shame vs. guilt | ch03 · Why You Hurt |

**Chapter renumbering is the standing hazard.** Keep Your Heart renumbered on 2026-09-04 and eleven
Pigglyvale links broke silently. Filenames change, not just labels. **Whenever a KYH chapter is inserted,
the KYH chat must hand Pigglyvale a mapping table** — the one in `KEEP-YOUR-HEART-TODO.md` was exactly
right and took ten minutes to apply. Note that `ch03` was missing from it because it was added after the
table was written; a mapping table should be generated from the live links, not from memory.

## Site-specific conventions

**My Toolbox** — 1024×572 `.jpg`, soft atmospheric oil-painting devotional style, no faces in close-up,
always a visible light source. Patterns run short and scannable; Dynamics match Patterns' register;
Modalities run warmer and unhurried. Gradient placeholder renders when art is pending — never leave a page
looking broken. Zips ship as `my_toolbox_vN.zip`, incrementing on every rebuild; prior versions are never
overwritten. Pages live in `patterns/`, `dynamics/` and `modalities/` subfolders — **a flat base URL will
404**, which is how the first attempt at cross-linking failed.

**Keep Your Heart** — 1024×572 lowercase `.jpg`. Stone-room frame: alcove-with-reed for chapter heroes,
lectern for plates, torn-paper border. Ships as `_SITE` (upload) and `_SOURCE` (keep) zips — **do not lose
the source zip**; it was reconstructed once from published HTML after a container reset. `TODO.md` is
maintained on every update and is the authoritative status record.

**Pigglyvale** — house style in `series-bible_v4.md`; structural rules in `docs/site-conventions.md`; all
art in `prompts/ART-QUEUE.md`. Left-hand nav pane on every content page (index excepted). Episodes listed
oldest-first. No local CSS, ever. **The image tool has no negative-prompt field** — every exclusion is
written as a positive fact, and naming a thing to forbid it draws it.

---

## Currently open cross-site decisions

- **Church Hurt (KYH Ch 22) and the Toolbox spiritual-abuse page are linked decisions.** The dials for one
  shape the framing of the other; KYH Ch 21 was deliberately kept general so as not to preempt it. **Not yet
  resolved.** Nine dials are written out in `KEEP-YOUR-HEART-TODO.md` and want answers before drafting.
  Whoever picks this up should have both documents in view at once, not just one site's chat.
  *Note: the Toolbox now has **Institutional betrayal**, **Coercive control** and **Testimonial injustice**
  live, which cover much of the clinical ground — so the open question may be narrower than it was.*

- **When KYH Ch 16 · Repair ships, Pigglyvale should link it.** It is the chapter Pigglyvale most needs and
  has nowhere to point: the repair beat is the premise of every episode, and the Dojo carries four prayers
  about apologising with no fuller treatment behind them. Best homes — the Episode 002 Advisor's Notes, and
  `under-the-weather-keeper.html` beside the yellow-belt drill on apologising and then stopping.

- **When KYH Ch 14 · Anger ships, the Dojo's right-hand ditch gets its first outbound link.** Lashing
  currently has nowhere to go on either companion site, while caving now has Fawning. That asymmetry is
  worth closing.

---

## Known, accepted quirks — not open questions

- **Keep Your Heart's art style changes mid-book.** A deliberate mid-stream decision, not an error. Earlier
  chapters were not redone and there is no plan to. A future chat noticing the seam is not surfacing a bug.
- **Pigglyvale's Map of the Keep was rebuilt once from a summary and then replaced by the author's real
  page.** The current page is the author's. If a chat finds a shorter version anywhere, it is the discarded
  reconstruction.
- **Episode One predates the six-slot art contract** but was brought onto it on 2026-09-02 at the author's
  request — repair illustration added, close renumbered.

## Starting a new chat on any of these three sites

Point Claude at this file first, then at that site's own TODO. If a change might affect another site, say so
explicitly in the request — do not assume the chat will infer it or go looking.

**And whichever site you are working on, the other two are probably ahead of your assumptions.** All three
moved substantially in the first four days of September 2026. Check the live site before proposing an
addition; three of the eleven Toolbox suggestions written on 2026-09-02 were built within forty-eight hours.
