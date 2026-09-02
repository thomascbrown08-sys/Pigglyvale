/* ============================================================
   PIGGLYVALE — dojo.js
   Drives the practice drills: choose a response, see what it
   caused, then hear the sensei.

   Progressive enhancement. The outcomes are visible in the HTML
   with no script running, so a reader without JavaScript gets
   the whole case as a plain page. This file hides them and
   reveals them on choice.
   ============================================================ */

(function () {
  "use strict";

  function setUp(drill) {
    var choices = Array.prototype.slice.call(drill.querySelectorAll(".choice"));
    var outcomes = Array.prototype.slice.call(drill.querySelectorAll(".outcome"));
    var done = drill.querySelector(".drill-done");
    var again = drill.querySelector(".drill-again");
    var seen = {};

    if (!choices.length || !outcomes.length) { return; }

    outcomes.forEach(function (o) { o.hidden = true; });
    if (done) { done.hidden = true; }
    if (again) { again.hidden = true; }

    choices.forEach(function (btn) {
      btn.setAttribute("aria-pressed", "false");

      btn.addEventListener("click", function () {
        var id = btn.getAttribute("data-outcome");
        var panel = drill.querySelector("#" + id);
        if (!panel) { return; }

        outcomes.forEach(function (o) { o.hidden = (o !== panel); });
        choices.forEach(function (b) {
          b.setAttribute("aria-pressed", String(b === btn));
        });

        btn.classList.add("is-seen");
        seen[id] = true;

        if (again) { again.hidden = false; }
        if (done && Object.keys(seen).length === choices.length) {
          done.hidden = false;
        }

        panel.setAttribute("tabindex", "-1");
        panel.focus({ preventScroll: true });
        panel.scrollIntoView({ behavior: "smooth", block: "nearest" });
      });
    });
  }

  function init() {
    Array.prototype.slice
      .call(document.querySelectorAll(".drill"))
      .forEach(setUp);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
