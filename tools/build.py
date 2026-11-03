"""Build the site pages.

Each page body lives in pages/<name>.html. The first lines of each file set
the title, description and active nav item:

    <!-- title: About | Grit Guts & Gusto Advisory -->
    <!-- description: ... -->
    <!-- nav: about -->

Run from the repo root:  python3 tools/build.py
It writes <name>.html files to the repo root, wrapped in the shared header
and footer below. Edit the shared parts here, edit page content in pages/.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://gritgutsgusto.com.my"
YEAR = "2026"

NAV = [
    ("index", "Home", "index.html"),
    ("programmes", "Programmes", "programmes.html"),
    ("advisory", "Advisory", "advisory.html"),
    ("about", "About", "about.html"),
    ("providers", "For training providers", "training-providers.html"),
    ("notes", "Notes", "notes.html"),
]

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{site}/assets/img/sabrena-portrait.jpg">
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Caladea:ital,wght@0,400;0,700;1,400&family=Lato:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/site.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="index.html" aria-label="Grit Guts &amp; Gusto Advisory, home">
      <span class="brand-name">Grit Guts &amp; Gusto</span>
      <span class="brand-sub">ADVISORY</span>
    </a>
    <nav class="nav" aria-label="Main">
      <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="nav-list">Menu</button>
      <ul id="nav-list">
{nav}
        <li><a class="btn" href="contact.html"{contact_current}>Contact</a></li>
      </ul>
    </nav>
  </div>
</header>
<main id="main">
"""

FOOT = """</main>
<footer class="site-footer">
  <div class="wrap">
    <div>
      <span class="brand-name">Grit Guts &amp; Gusto</span>
      <p style="margin-top:12px">Training and advisory for leaders who have to deliver under pressure. Led by Ir. Ts. Dr. Bibi Sabrena Sakandar Khan, PMP&reg;, HRD Corp Accredited Trainer (ID 66988).</p>
    </div>
    <div>
      <h4>Pages</h4>
      <ul>
        <li><a href="programmes.html">Training programmes</a></li>
        <li><a href="advisory.html">Advisory services</a></li>
        <li><a href="about.html">About the Principal Advisor</a></li>
        <li><a href="training-providers.html">For training providers</a></li>
        <li><a href="notes.html">Notes</a></li>
        <li><a href="contact.html">Contact</a></li>
      </ul>
    </div>
    <div>
      <h4>Get in touch</h4>
      <ul>
        <li><a href="tel:+60122910834">+60 12-291 0834</a></li>
        <li><a href="mailto:sabrenakhan@gritgutsgusto.com.my">sabrenakhan@gritgutsgusto.com.my</a></li>
        <li><a href="https://www.linkedin.com/in/sabrenakhan" rel="noopener">LinkedIn: sabrenakhan</a></li>
        <li>Seremban, Negeri Sembilan, Malaysia</li>
      </ul>
    </div>
    <div class="legal">&copy; {year} Grit Guts &amp; Gusto Advisory (202603285787 / 003904056-T). Registered under the Registration of Businesses Act 1956.</div>
  </div>
</footer>
<script>
  (function () {{
    var nav = document.querySelector('.nav');
    var btn = document.querySelector('.nav-toggle');
    if (!nav || !btn) return;
    btn.addEventListener('click', function () {{
      var open = nav.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    }});
  }})();
</script>
</body>
</html>
"""


def meta(src, key):
    m = re.search(r"<!--\s*" + key + r":\s*(.*?)\s*-->", src)
    return m.group(1) if m else ""


def build():
    for page in sorted((ROOT / "pages").glob("*.html")):
        src = page.read_text(encoding="utf-8")
        name = page.stem
        active = meta(src, "nav")
        body = re.sub(r"^(\s*<!--.*?-->\s*\n)+", "", src, flags=re.S)
        nav = "\n".join(
            '        <li><a href="{href}"{cur}>{label}</a></li>'.format(
                href=href, label=label,
                cur=' aria-current="page"' if key == active else "")
            for key, label, href in NAV)
        out_name = "index.html" if name == "index" else name + ".html"
        canonical = SITE + "/" + ("" if name == "index" else out_name)
        html = HEAD.format(
            title=meta(src, "title"), description=meta(src, "description"),
            canonical=canonical, site=SITE, nav=nav,
            contact_current=' aria-current="page"' if active == "contact" else "",
        ) + body + FOOT.format(year=YEAR)
        (ROOT / out_name).write_text(html, encoding="utf-8")
        print("built", out_name)


if __name__ == "__main__":
    build()
