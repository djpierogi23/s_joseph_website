#!/usr/bin/env python3
"""
Generate palette-preview.html from index.html.

Adds a floating Green / Navy switch so the same page can be compared in both
palettes. Because every colour in index.html is a CSS custom property, the
navy version is a pure token override — no markup or layout changes at all.

Re-run after editing index.html:  python3 build_preview.py
"""

import re
import pathlib

SRC = pathlib.Path(__file__).parent / "index.html"
OUT = pathlib.Path(__file__).parent / "palette-preview.html"

NAVY_THEME = """
<style id="palette-navy">
/* Navy palette — token override only. Gold accent retained; sage used for
   small-cap labels on dark, matching the navy business-card comp. */
:root.navy{
  --forest:#1d2b40; --forest2:#15202f; --forest3:#2b3c52;
  --brass:#b28a4c; --brasstx:#7a5c2c; --brass2:#c69f5c;
  --ink:#1f2833; --body:#4c545d; --mut:#676e77;
  --line:#e2e5ea; --cream:#f6f6f2; --ph:#e7eaee;
  --on-dark:#f4f2ea; --on-dark-body:#cbd3dc; --on-dark-mut:#9fb0a4;
  --on-dark-sub:#b9c4d0; --on-dark-faint:#7f8d95; --on-dark-ghost:#e4ddcc;
  --edge-strong:#c3c9d1; --edge-field:#d2d7de; --edge-soft:#dde1e7;
  --dim:#bfc5cd; --ph-txt:#7d8795; --cream2:#f0f1ee; --nav-txt:#474d55;
  --tbd-bg:#f3ede1; --tbd-line:#d8c49b;
  --tbd-dark-txt:#cdbb96; --tbd-dark-txt2:#e0cfa8;
  --shadow-rgb:29,43,64;
}
/* The monogram rect is the one non-token colour (an inline SVG fill). */
:root.navy .mark rect{fill:#1d2b40;}

/* ── switcher chrome ── */
#pal-bar{position:fixed;bottom:0;left:0;right:0;z-index:9000;
  background:rgba(255,255,255,.97);border-top:1px solid #dcdfe3;
  box-shadow:0 -2px 14px rgba(0,0,0,.08);
  padding:11px 20px;display:flex;align-items:center;justify-content:center;
  gap:16px;flex-wrap:wrap;font-family:system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;}
#pal-bar .lbl{font-size:11px;letter-spacing:1.6px;text-transform:uppercase;
  color:#6b7280;font-weight:700;}
#pal-bar .grp{display:flex;gap:0;border:1px solid #d3d7dc;border-radius:4px;overflow:hidden;}
#pal-bar button{font-family:inherit;font-size:13px;font-weight:600;padding:9px 20px;
  border:none;background:#fff;color:#3f4650;cursor:pointer;display:flex;
  align-items:center;gap:8px;}
#pal-bar button+button{border-left:1px solid #d3d7dc;}
#pal-bar button:hover{background:#f3f5f7;}
#pal-bar button[aria-pressed="true"]{background:#1f2833;color:#fff;}
#pal-bar .sw{width:13px;height:13px;border-radius:50%;display:inline-block;
  border:1px solid rgba(0,0,0,.18);}
#pal-bar .note{font-size:12px;color:#6b7280;}
#pal-bar .note a{color:#1f2833;font-weight:600;}
body{padding-bottom:62px;}
@media(max-width:640px){#pal-bar .note{display:none;}}
@media print{#pal-bar{display:none;}body{padding-bottom:0;}}
</style>
"""

SWITCHER = """
<div id="pal-bar" role="group" aria-label="Palette comparison">
  <span class="lbl">Palette</span>
  <span class="grp">
    <button type="button" data-pal="green" aria-pressed="true">
      <span class="sw" style="background:#1f3a2e"></span>Green</button>
    <button type="button" data-pal="navy" aria-pressed="false">
      <span class="sw" style="background:#1d2b40"></span>Navy</button>
  </span>
  <span class="note">Comparison only &mdash; the live site is
    <a href="index.html">index.html</a></span>
</div>
<script>
(function(){
  var bar = document.getElementById('pal-bar');
  function set(p){
    document.documentElement.classList.toggle('navy', p === 'navy');
    bar.querySelectorAll('[data-pal]').forEach(function(b){
      b.setAttribute('aria-pressed', String(b.getAttribute('data-pal') === p));
    });
    try{ localStorage.setItem('sj-palette', p); }catch(e){}
  }
  bar.addEventListener('click', function(e){
    var b = e.target.closest('[data-pal]');
    if(b) set(b.getAttribute('data-pal'));
  });
  var saved = null;
  try{ saved = localStorage.getItem('sj-palette'); }catch(e){}
  if(saved) set(saved);
})();
</script>
"""

BANNER_TITLE = "Palette comparison — S Joseph Law LLC"


def main():
    html = SRC.read_text(encoding="utf-8")

    if "id=\"pal-bar\"" in html:
        raise SystemExit("index.html already contains the switcher — aborting.")

    # Distinct <title> so the tab is identifiable next to the real site.
    html = re.sub(r"<title>.*?</title>",
                  "<title>%s</title>" % BANNER_TITLE, html, count=1, flags=re.S)

    # Stop the router from rewriting the title on every route change.
    html = html.replace("document.title = r.title;", "/* title fixed in preview */")

    html = html.replace("</head>", NAVY_THEME + "</head>", 1)
    html = html.replace("</body>", SWITCHER + "</body>", 1)

    OUT.write_text(html, encoding="utf-8")
    print("wrote %s (%d bytes)" % (OUT.name, len(html)))


if __name__ == "__main__":
    main()
