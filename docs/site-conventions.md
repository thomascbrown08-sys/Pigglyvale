# Site conventions

Standing rules for how pages on this site are built. These are not Pigglyvale-specific — they apply to any
site made for this project family, and a new session should read them before adding a page.

---

## 1. Every content page carries a left navigation pane

**This is the default and does not need to be asked about.** Any page with substantial content — an episode,
a chart, an essay, a reference page — gets a left-hand pane giving quick access to the wider site. The
reader should never have to go back to the front page to find out what else exists.

The markup:

```html
<div class="layout">

  <aside class="epnav">
    <h2 class="epnav-title">Jump to an episode</h2>
    <ul class="epnav-list" id="epnav-list"></ul>
    <a class="epnav-home" href="../index.html">Front page</a>
  </aside>

  <main>
    ...
  </main>

</div>
```

and, immediately before `</body>`:

```html
<script>window.PV_BASE = "../"; window.PV_CURRENT = "this-page-slug";</script>
<script src="../assets/episodes.js"></script>
```

`assets/episodes.js` fills the list. Adding a page to the pane is one line in its `EPISODES` array (for
episodes) or `EXTRAS` array (for anything else). `PV_CURRENT` matching a slug in either array marks that
entry as the current page.

The pane is styled in `assets/style.css` under *episode page shell + sidebar navigation*. Above 68rem it
sits alongside the content and sticks on scroll; below that it stacks above the content, so it costs
nothing on a phone.

**The exception is the front page.** `index.html` is itself the site index, and a pane listing the same
episodes as the grid beside it would read as a duplication rather than a convenience. If that ever stops
being true — if the front page becomes something other than a list of everything — it gets a pane too.

## 2. Episodes are listed in sequence, oldest first

Not newest-first. The reverse-chronological habit comes from blogs, where readers arrive already caught up
and want what they have not seen yet. This is a serialized story and it does not work that way: episodes are
produced faster than anyone reads them, so almost every visitor is arriving behind rather than waiting on
the next one. Putting the newest at the top asks that visitor to start in the middle, or to scroll to the
bottom to find the beginning — which is friction in exchange for a benefit almost nobody here is collecting.

So new episodes go at the **end** of the run on `index.html`, above the Map of the Keep, which stays last as
a companion piece rather than an episode. The sidebar pane already runs in sequence and needs no change.

Nothing on the site is spoiled by starting at the start, and the front page should say so.

## 3. No local CSS, ever

Every page links `assets/style.css` and adds no `<style>` block and no inline styling. Restyling the site
later has to mean editing one file. A new component means a new block at the foot of the stylesheet, named
and commented.

## 4. One masthead, one footer

Masthead reads **The Chronicles of Pigglyvale** and links to `index.html`. Footer reads **Made for
Carolyn.** Page titles end with `&mdash; The Chronicles of Pigglyvale`.

## 5. Class names follow the page that had them first

Where two pages solve the same problem with different markup, the earlier page wins and the later one is
converted. The Washing-Up is the worked example: `.setting`, `p.line`, `span.who`, `<em>` for business —
those came from the Keep page and everything else was changed to match.

## 6. Paths are relative to the page, not the root

Pages in `pages/` and `episodes/` reach assets with `../assets/`, `../images/`, `../index.html`. Anything
written to sit flat beside its assets needs repointing before it goes in.
