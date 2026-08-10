/* OCOaiqEvents 1.0.0 — OpenAI Ads Manager conversion events for nwocflooring.com.
   Fires oaiq("measure","estimate_booked",{type:"customer_action",amount:0,currency:"USD"}) on:
   1) Calendly booking completed (calendly.event_scheduled postMessage — covers inline embeds
      and Calendly popup widgets on any page);
   2) click of an external calendly.com link — only when the page has NO Calendly embed,
      so embedded pages count real bookings instead of clicks (no double counting);
   3) successful submission of any Webflow quote/contact form (fires only after the
      .w-form-done success state is shown, not on submit attempt).
   Every call is guarded: nothing runs unless the site-wide head pixel setup script has
   defined window.oaiq (the head snippet also queues calls made before the SDK loads). */
(function () {
  var FIRED = {};
  function fire(key) {
    if (FIRED[key]) return;
    FIRED[key] = 1;
    try {
      if (typeof window.oaiq === "function") {
        window.oaiq("measure", "estimate_booked", { type: "customer_action", amount: 0, currency: "USD" });
      }
    } catch (e) {}
  }

  /* 1) Calendly embedded (inline widget or popup) — booking completed */
  window.addEventListener("message", function (e) {
    try {
      if (/^https:\/\/([a-z0-9-]+\.)?calendly\.com$/.test(e.origin) && e.data && e.data.event === "calendly.event_scheduled") {
        fire("calendly-scheduled");
      }
    } catch (err) {}
  });

  /* 2) External calendly.com links — click counts only when no embed exists on the page */
  function hasCalendlyEmbed() {
    return !!document.querySelector('.calendly-inline-widget,.calendly-overlay,iframe[src*="calendly.com"]');
  }
  document.addEventListener("click", function (e) {
    var t = e.target;
    var a = t && t.closest ? t.closest('a[href*="calendly.com"]') : null;
    if (a && !hasCalendlyEmbed()) fire("calendly-link");
  }, true);

  /* 3) Webflow forms — fire only after the success message is displayed */
  function watchForm(f) {
    if (f.__ocq) return;
    f.__ocq = 1;
    f.addEventListener("submit", function () {
      var wrap = f.closest(".w-form");
      var done = wrap ? wrap.querySelector(".w-form-done") : null;
      if (!done) return;
      var n = 0;
      var iv = setInterval(function () {
        n++;
        if (getComputedStyle(done).display !== "none") {
          clearInterval(iv);
          fire("form-" + (f.id || f.getAttribute("data-name") || "form"));
        } else if (n > 40) {
          clearInterval(iv); /* no success within 10s — treat as not submitted */
        }
      }, 250);
    });
  }
  function init() {
    var fs = document.querySelectorAll(".w-form form");
    for (var i = 0; i < fs.length; i++) {
      if (fs[i].querySelector('input[type="search"]')) continue; /* skip search forms */
      watchForm(fs[i]);
    }
  }
  if (document.readyState !== "loading") init();
  else document.addEventListener("DOMContentLoaded", init);
  window.addEventListener("load", init);
  setTimeout(init, 1500);
})();
