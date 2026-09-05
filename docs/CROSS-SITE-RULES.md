# Cross-Site Standing Rules — Carolyn Stories Project

**Version 3 · 2026-09-05 · supersedes v2 (2026-09-04)**
*Changed in this version:* **a full link audit was run against both live sites — all 22 outbound links
resolve and every anchor label still matches its target's live title. Nothing broke.** Status block
refreshed (KYH is now complete at 27 of 27; the Toolbox has an eighth Dynamic; Pigglyvale has three
episodes). **All three open cross-site decisions are now closed** — Church Hurt and the spiritual-abuse
page are both built, and Ch 16 and Ch 14 have shipped and are now linked. Link map extended with Episode
003 and the three new links. New §Grief added, because all three sites now hold grief material and nobody
had checked whether it agrees with itself. Traffic rules unchanged.

**Paste this into Project Knowledge, replacing the previous copy.** Any chat working on Pigglyvale, Keep
Your Heart, or My Toolbox should read it before making cross-site claims or links.

---

## Status, verified 2026-09-04

| Site | Live | State |
|---|---|---|
| **My Toolbox** | [link](https://thomascbrown08-sys.github.io/My_Toolbox/) | 21 patterns · **8 dynamics** · 14 modalities. Spiritual abuse is built and live. |
| **Keep Your Heart** | [link](https://thomascbrown08-sys.github.io/KeepYourHeart/) | **Complete: 27 of 27 chapters written and live**, plus front matter, Nutshells, Warrants, Lament Finder, Glossary, Tracker, Judgment-Call Log and Sources. Ch 14, 16 and 22 all shipped. |
| **Pigglyvale** | [link](https://thomascbrown08-sys.github.io/Pigglyvale/index.html) | **3 episodes** (003 *Quantity Not Stated* shipped 2026-09-05, art pending) · the Keep · the Dojo (5 masks, 7 belt cases) · 9 approved reference sheets. **Episode 004 is blocked** on Bruno's sheet and the theft ruling. |

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

| Episode 003, Toolbox block | Differentiation | — |
| Episode 002, Advisor's Notes | — | ch16 · Repair *(added 2026-09-05)* |
| Under the Weather-Keeper | — | ch16 · Repair *(added 2026-09-05)* |
| How the belts work, right-hand ditch | — | ch14 · Anger *(added 2026-09-05)* |

**Chapter renumbering is the standing hazard.** Keep Your Heart renumbered on 2026-09-04 and eleven
Pigglyvale links broke silently. Filenames change, not just labels. **Whenever a KYH chapter is inserted,
the KYH chat must hand Pigglyvale a mapping table** — the one in `KEEP-YOUR-HEART-TODO.md` was exactly
right and took ten minutes to apply. Note that `ch03` was missing from it because it was added after the
table was written; a mapping table should be generated from the live links, not from memory.

> **Audit, 2026-09-05.** Every outbound link was re-checked against both live indexes: 8 to Keep Your Heart,
> 14 to My Toolbox, plus the two site roots. **All resolve, and every anchor label still matches the live
> title of its target.** The 2026-09-04 mapping-table process worked and nothing has drifted since. Worth
> repeating this audit after any KYH insertion — it takes one pass over the live index and it is the only
> way to catch a link that is *wrong* rather than *broken*, since a renumbered chapter still returns a page.

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

**Pigglyvale** — house style in `series-bible_v6.md`; structural rules in `docs/site-conventions.md`; all
art in `prompts/ART-QUEUE.md`. Left-hand nav pane on every content page (index excepted). Episodes listed
oldest-first. No local CSS, ever. **The image tool has no negative-prompt field** — every exclusion is
written as a positive fact, and naming a thing to forbid it draws it.

---

## Currently open cross-site decisions

**None.** All three items carried in v2 closed on 2026-09-05. Kept below for the record.

## Recently closed

- ~~**Church Hurt (KYH Ch 22) and the Toolbox spiritual-abuse page.**~~ **Both built and live.** Division of
  labour as settled: **My Toolbox names the mechanism; Keep Your Heart works it.** The Toolbox page is
  mechanism-only — no Scripture, no devotional register — and it is the one page on that site that closes
  with *Further reading* rather than *Look up*. Worth knowing before assuming every Toolbox page has the
  same shape.
- ~~**When KYH Ch 16 · Repair ships, Pigglyvale should link it.**~~ **Shipped and linked 2026-09-05**, in
  both of the homes this file named: the Episode 002 Advisor's Notes and `under-the-weather-keeper.html`.
- ~~**When KYH Ch 14 · Anger ships, the Dojo's right-hand ditch gets its first outbound link.**~~
  **Shipped and linked 2026-09-05**, in `how-the-belts-work.html`. Both ditches now have a door: caving has
  *Fawning* on the Toolbox, lashing has *Anger* on Keep Your Heart. The asymmetry is closed.

---

## Grief — which site owns which piece

Added 2026-09-05, because grief material accumulated independently on all three sites and nobody had
checked whether the three accounts agree. They do, and they divide cleanly, but the division was accidental
and should now be deliberate.

| | Holds | Does not |
|---|---|---|
| **My Toolbox** | The mechanisms, named and checkable: **Ambiguous loss** (grief for someone still alive), **Disenfranchised grief** (grief nobody has granted you standing to feel), **Godly grief vs. worldly grief** (sorted by what the sorrow produces, not by how heavy it is). | Comfort. Meaning. Any instruction about what to do. |
| **Keep Your Heart** | The work: **Ch 10 · Lament** — God wrote a hymnbook and made complaint the largest section in it. **Ch 09 · The Cup and the Garden** — He said out loud that it was avoidable. **Ch 18 · A Life You Did Not Build.** Plus the **Lament Finder** and the **Lament as practice** modality. | Naming clinical mechanisms in clinical language. |
| **Pigglyvale** | **Nothing yet.** | — |

**Two things follow from that table and they are easy to get backwards.**

**One: the companion sites are ahead of Pigglyvale here, not behind it.** The instinct when planning a
grief episode is that it will generate work on the other two. On this subject it will not. The mechanisms
are named and the theological work is done; what is missing is the *story*. A grief episode should be
planned as a consumer of existing material, and the two doors it offers are already built.

**Two: the one genuine gap is a Toolbox gap, and it is not about death.** There is a page for grief over
someone still living and a page for grief nobody grants you standing to feel, but there is nothing for
**grief over a life that did not happen** — the road not taken, the years spent somewhere that did not
repay them, the thing you are now too old to start. That is *not* the same as ambiguous loss and it is only
sometimes disenfranchised. If a Pigglyvale grief episode goes near lost opportunity rather than lost
people, this is the page it will want and the page that does not exist. **Propose it to the Toolbox chat
before writing the episode, not after** — the Toolbox is the base layer and it is much easier to write a
page first and point at it than to point at a page and then have to write it to spec.

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
