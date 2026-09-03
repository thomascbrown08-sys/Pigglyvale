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

  var EXTRAS = [
    {
      slug:  "the-map-of-the-keep",
      label: "A Chart from the Kingdom",
      title: "The Map of the Keep",
      path:  "pages/the-map-of-the-keep.html"
    },
    {
      slug:  "dojo-index",
      label: "A Wing of the Kingdom",
      title: "The Dojo",
      path:  "dojo/index.html"
    },
    {
      slug:  "dojo-how",
      label: "The Dojo",
      title: "How the belts work",
      path:  "dojo/how-the-belts-work.html"
    }
  ];

  var base = window.PV_BASE || "../";
  var current = window.PV_CURRENT || "";
  var list = document.getElementById("epnav-list");
  if (!list) { return; }

  function item(href, eyebrow, title, isCurrent) {
    var li = document.createElement("li");
    li.className = "epnav-item" + (isCurrent ? " is-current" : "");

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

  EPISODES.forEach(function (ep) {
    list.appendChild(
      item(base + "episodes/" + ep.file, "Episode " + ep.number, ep.title, ep.slug === current)
    );
  });

  EXTRAS.forEach(function (x) {
    list.appendChild(
      item(base + x.path, x.label, x.title, x.slug === current)
    );
  });
})();
