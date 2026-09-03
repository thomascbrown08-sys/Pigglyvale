/* ============================================================
   PIGGLYVALE — episodes.js
   Builds the "Jump to an episode" sidebar on every episode page.

   To add an episode: add one line to EPISODES, newest last.
   Nothing else on the site needs to change.
   ============================================================ */

(function () {
  "use strict";

  var EPISODES = [
    {
      slug:   "ep-001-the-small-yeses",
      number: "One",
      title:  "The Small Yeses",
      file:   "ep-001-the-small-yeses.html"
    },
    {
      slug:   "ep-002-the-column-nobody-read",
      number: "Two",
      title:  "The Column Nobody Read",
      file:   "ep-002-the-column-nobody-read.html"
    }
  ];

  /* `level` indents the entry. `prefix` marks it current for any page whose
     PV_CURRENT starts with it, so the Dojo stays lit while you are deep in a
     mask or a drill. Exact slug matches always win over a prefix match. */
  var EXTRAS = [
    {
      slug:  "the-map-of-the-keep",
      label: "A Chart from the Kingdom",
      title: "The Map of the Keep",
      path:  "pages/the-map-of-the-keep.html",
      level: 0
    },
    {
      slug:   "dojo-index",
      label:  "A Wing of the Keep",
      title:  "The Dojo",
      path:   "dojo/index.html",
      level:  1,
      prefix: "dojo-"
    },
    {
      slug:  "dojo-how",
      label: "Before you start",
      title: "How the belts work",
      path:  "dojo/how-the-belts-work.html",
      level: 2
    }
  ];

  var base = window.PV_BASE || "../";
  var current = window.PV_CURRENT || "";
  var list = document.getElementById("epnav-list");
  if (!list) { return; }

  function item(href, eyebrow, title, isCurrent, level) {
    var li = document.createElement("li");
    li.className = "epnav-item lv-" + (level || 0) + (isCurrent ? " is-current" : "");

    var a = document.createElement("a");
    a.href = href;
    if (isCurrent) { a.setAttribute("aria-current", "page"); }

    var small = document.createElement("span");
    small.className = "epnav-number";
    small.textContent = eyebrow;

    var strong = document.createElement("span");
    strong.className = "epnav-name";
    strong.textContent = title;

    a.appendChild(small);
    a.appendChild(strong);
    li.appendChild(a);
    return li;
  }

  var exact = EPISODES.concat(EXTRAS).some(function (e) { return e.slug === current; });

  EPISODES.forEach(function (ep) {
    list.appendChild(
      item(base + "episodes/" + ep.file, "Episode " + ep.number, ep.title,
           ep.slug === current, 0)
    );
  });

  EXTRAS.forEach(function (x) {
    var isCurrent = (x.slug === current) ||
      (!exact && x.prefix && current.indexOf(x.prefix) === 0);
    list.appendChild(item(base + x.path, x.label, x.title, isCurrent, x.level));
  });
})();
