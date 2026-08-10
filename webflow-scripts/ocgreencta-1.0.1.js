/* OCGreenCta 1.0.1 — green accent for the "See Available Appointment" booking CTA.
   Oleg wants the booking button to stand out from the site's red/navy palette,
   so it gets #1e7a3c (hover #166132, white text kept). Applied site-wide via the
   Footer Code block (Site Settings → Custom Code → Footer Code).

   Targets buttons/links by their visible text ("see available appointment",
   case-insensitive, length-capped to avoid wrapping containers) rather than by
   class, so it keeps working if the button's Webflow classes change. Covers <a>,
   <button>, and <input type="submit">. Re-runs on DOMContentLoaded/load and two
   delayed passes to catch late-rendered buttons.

   v1.0.1: CSS switched to the `background` shorthand + background-image:none so
   the override also wins when the button is styled with a gradient
   (background-image paints over background-color, which kept the button
   visually red in 1.0.0).

   Companion CSS (in the same footer block):
   .oc-cta-green{background:#1e7a3c !important;background-image:none !important;border-color:#1e7a3c !important;color:#fff !important}
   .oc-cta-green:hover{background:#166132 !important;background-image:none !important;border-color:#166132 !important;color:#fff !important}
   .oc-cta-green:focus-visible{outline:3px solid rgba(30,122,60,.4) !important;outline-offset:2px}
*/
(function () {
  function tag() {
    var els = document.querySelectorAll('a,button,input[type="submit"]');
    for (var i = 0; i < els.length; i++) {
      var e = els[i];
      var t = ((e.tagName === "INPUT" ? e.value : e.textContent) || "").trim();
      if (t.length < 48 && /see\s+available\s+appointment/i.test(t)) {
        e.classList.add("oc-cta-green");
      }
    }
  }
  if (document.readyState !== "loading") tag();
  else document.addEventListener("DOMContentLoaded", tag);
  window.addEventListener("load", tag);
  setTimeout(tag, 800);
  setTimeout(tag, 2000);
})();
