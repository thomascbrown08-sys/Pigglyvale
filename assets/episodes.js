/* ============================================================
   PIGGLYVALE — episode index
   ------------------------------------------------------------
   THIS IS THE ONLY FILE YOU EDIT TO ADD AN EPISODE.
   Add one object to the top of the array below. The sidebar on
   every page and the shelf on the front page both build
   themselves from it.

   Newest episode goes FIRST in the array.
   ============================================================ */

window.PIGGLYVALE_EPISODES = [

  {
    number:  1,
    numeral: "One",
    slug:    "ep-001-the-small-yeses",
    title:   "The Small Yeses",
    blurb:   "Fair Week arrives, four promises land on the same Thursday, and the smallest one gets broken.",
    lesson:  "On saying no early, and on being rescued when you didn't ask to be.",
    hero:    "images/ep-001/01-hero.png"
  }

];

/* ------------------------------------------------------------
   Rendering. You shouldn't need to touch anything below.

   Each page sets two globals before loading this file:
     window.PV_BASE    = ""   on the front page
                       = "../" on an episode page
     window.PV_CURRENT = the slug of the episode being read
   ------------------------------------------------------------ */

(function () {
  var eps     = window.PIGGLYVALE_EPISODES || [];
  var base    = window.PV_BASE || "";
  var current = window.PV_CURRENT || "";

  function href(ep) { return base + "episodes/" + ep.slug + ".html"; }

  /* --- the sidebar --- */
  var list = document.getElementById("epnav-list");
  if (list) {
    if (!eps.length) {
      var none = document.createElement("li");
      none.className = "epnav-empty";
      none.textContent = "No episodes yet.";
      list.appendChild(none);
    }
    eps.forEach(function (ep) {
      var li = document.createElement("li");
      var a  = document.createElement("a");
      a.href = href(ep);
      a.innerHTML = '<span class="epnav-num">' + ep.number + '</span>' + ep.title;
      if (ep.slug === current) {
        a.className = "is-current";
        a.setAttribute("aria-current", "page");
      }
      li.appendChild(a);
      list.appendChild(li);
    });
  }

  /* --- the front-page shelf --- */
  var shelf = document.getElementById("plates");
  if (shelf) {
    if (!eps.length) {
      shelf.innerHTML =
        '<div class="plate is-empty"><span class="plate-number">Episode One</span>' +
        '<h3 class="plate-title">Coming shortly</h3>' +
        '<p class="plate-blurb">The kingdom is being swept.</p></div>';
      return;
    }
    eps.forEach(function (ep) {
      var a = document.createElement("a");
      a.className = "plate";
      a.href = href(ep);
      a.innerHTML =
        '<img src="' + base + ep.hero + '" alt="">' +
        '<span class="plate-number">Episode ' + ep.numeral + '</span>' +
        '<h3 class="plate-title">' + ep.title + '</h3>' +
        '<p class="plate-blurb">' + ep.blurb + '</p>' +
        '<p class="plate-lesson">' + ep.lesson + '</p>';
      shelf.appendChild(a);
    });
  }
})();
