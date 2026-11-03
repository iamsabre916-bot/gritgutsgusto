# Grit Guts & Gusto Advisory website

Website for Grit Guts & Gusto Advisory (gritgutsgusto.com.my). It is a plain static site served by GitHub Pages.

## How it is organised

- `pages/` holds the content of each page. Edit these.
- `tools/build.py` wraps each page in the shared header and footer and writes the finished `.html` files to the repo root. Run `python3 tools/build.py` after editing anything in `pages/` or the header and footer in `build.py`.
- `assets/css/site.css` holds the styles (maroon `#5c0f1e`, gold `#b8924a`, Caladea and Lato fonts).
- `assets/img/` holds the photos, taken from the 2026 company profile.

## Content rules

English only, professional tone. Use only real facts from the company profile, trainer profile and course outlines, and only real client reviews.

## Publishing

Settings → Pages → Deploy from a branch → `main`, folder `/ (root)`. For the custom domain, add `gritgutsgusto.com.my` under Pages → Custom domain once the DNS records point to GitHub.
