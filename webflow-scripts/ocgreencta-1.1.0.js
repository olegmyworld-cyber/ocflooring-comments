/* OCGreenCta 1.1.0 — green accent for the "See Available Appointment" booking CTA.
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

/* v1.1.0: also recolors every BUTTON that links to /contact, site-wide
   (relative "/contact" or absolute https://www.nwocflooring.com/contact,
   trailing slash tolerated via a.pathname). Plain TEXT links to /contact are
   left alone: a link qualifies only if it (or a descendant) has a
   button/btn/cta class, or it has a filled (non-transparent) background.

   v1.0.2 additions:
   - length cap raised 48 -> 120 so hover text-swap buttons (which duplicate the
     label in markup) still match; whitespace collapsed before matching.
   - CSS now also recolors descendants and ::before/::after fill overlays, so
     link-blocks whose inner div carries the red background go green too.
   - Debug badge: open any page with ?ocdebug=1 to see a corner badge with
     tagged count and candidate button texts (for remote diagnosis).
*/
(function () {
  var info = { tagged: 0, cand: [] };
  function isBtn(e) {
    if (/button|btn|cta/i.test(e.className || "")) return true;
    var k = e.querySelectorAll("[class]");
    for (var i = 0; i < k.length && i < 10; i++) {
      var c = k[i].className;
      if (typeof c === "string" && /button|btn|cta/i.test(c)) return true;
    }
    try {
      var bg = getComputedStyle(e).backgroundColor;
      if (bg && bg !== "transparent" && bg !== "rgba(0, 0, 0, 0)") return true;
    } catch (r) {}
    return false;
  }
  function tag() {
    var els = document.querySelectorAll('a,button,input[type="submit"]');
    info.tagged = 0; info.cand = [];
    for (var i = 0; i < els.length; i++) {
      var e = els[i];
      var t = ((e.tagName === "INPUT" ? e.value : e.textContent) || "").replace(/\s+/g, " ").trim();
      if (/appointment/i.test(t) && info.cand.length < 8) info.cand.push(t.slice(0, 60));
      var byText = t.length < 120 && /see\s+available\s+appointment/i.test(t);
      var byLink = e.tagName === "A" && e.pathname && e.pathname.replace(/\/+$/, "") === "/contact" && isBtn(e);
      if (byText || byLink) {
        e.classList.add("oc-cta-green");
        info.tagged++;
      }
    }
    if (/[?&]ocdebug=1/.test(location.search)) dbg();
  }
  function dbg() {
    var d = document.getElementById("ocdbg");
    if (!d) {
      d = document.createElement("div");
      d.id = "ocdbg";
      d.style.cssText = "position:fixed;left:8px;bottom:8px;z-index:99999;background:#111;color:#0f0;font:12px/1.4 monospace;padding:8px 10px;border-radius:6px;max-width:70vw";
      document.body.appendChild(d);
    }
    d.textContent = "OCGreenCta v1.1.0 tagged=" + info.tagged + " cand=" + JSON.stringify(info.cand);
  }
  if (document.readyState !== "loading") tag();
  else document.addEventListener("DOMContentLoaded", tag);
  window.addEventListener("load", tag);
  setTimeout(tag, 800);
  setTimeout(tag, 2500);
})();
