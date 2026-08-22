// OC Areas slider start slide (OCAreasStart) v1.0.0
// Applied as inline <script> in the SITE-WIDE freeform footer custom code block
// (not a registered script — the registered footer block is at its 15-script limit).
//
// The "Proudly Serving Homeowners Across King & Snohomish Counties" service-areas
// slider (Section // Areas component, powered by the hosted ocareasslider script)
// always opened on its first slide, "Laminate Floor Service Areas", regardless of
// what the page is about. This makes it open on the slide matching the page:
//   floor-repair pages + /services/flooring-repair  -> "Floor Repair Service Areas"
//   home page + refinishing pages + /services/floor-refinishing
//                                                   -> "Hardwood Floor Refinishing Service Areas"
//   vinyl plank pages + /services/vinyl-plank-flooring-and-laminate-flooring
//                                                   -> "Luxury Vinyl Plank Service Areas"
//   hardwood installation pages + /services/hardwood-floor-installation
//                                                   -> "Hardwood Service Areas"
// Pages with no match keep the default order (Laminate first).
//
// Mechanism: runs synchronously at parse time (bottom of <body>) and moves the
// matching .content-box-area slide to the front of .areas-content-wrapper BEFORE
// the slider initializes — the slider waits on the deferred Swiper bundle, so the
// reorder always wins the race. The repair check runs first so Bothell pages under
// the /hardwood-floor-refinishing/ folder are classified by their page slug, not
// their folder name.
(function () {
  var p = location.pathname.replace(/\/+$/, '');
  var t = null;
  if (p.indexOf('hardwood-floor-repair-in') > -1 || p === '/services/flooring-repair') t = 'floor repair service areas';
  else if (p === '' || p === '/index' || p === '/home' || p.indexOf('hardwood-floor-refinishing-in') > -1 || p === '/services/floor-refinishing') t = 'hardwood floor refinishing service areas';
  else if (p.indexOf('vinyl-plank-flooring-installation-in') > -1 || p === '/services/vinyl-plank-flooring-and-laminate-flooring') t = 'luxury vinyl plank service areas';
  else if (p.indexOf('hardwood-floor-installation-in') > -1 || p === '/services/hardwood-floor-installation') t = 'hardwood service areas';
  if (!t) return;
  function pick() {
    var boxes = document.querySelectorAll('.areas-content-wrapper .content-box-area');
    for (var i = 0; i < boxes.length; i++) {
      var h = boxes[i].querySelector('.heading-area,h3');
      if (h && h.textContent.replace(/\s+/g, ' ').trim().toLowerCase() === t) {
        var par = boxes[i].parentNode;
        if (par && par.firstElementChild !== boxes[i]) par.insertBefore(boxes[i], par.firstElementChild);
        return true;
      }
    }
    return false;
  }
  if (!pick() && document.readyState === 'loading') document.addEventListener('DOMContentLoaded', pick);
})();
