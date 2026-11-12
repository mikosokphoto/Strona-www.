# -*- coding: utf-8 -*-
# Generuje wszystkie strony mikosokphoto.pl (PL w katalogu głównym, pozostałe języki w podfolderach).
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from content import *

OUT = sys.argv[1] if len(sys.argv) > 1 else "/home/claude/mikosokphoto.pl"
SITE = "https://mikosokphoto.pl/"
PAGES = ["index.html", "pediatria-leki.html", "kontakt.html", "polityka-prywatnosci.html", "pediatria-leki-prywatnosc.html"]
NAV_FILES = ["index.html", "pediatria-leki.html", "kontakt.html", "polityka-prywatnosci.html"]
ACTIVE = {"index.html": 0, "pediatria-leki.html": 1, "kontakt.html": 2, "polityka-prywatnosci.html": 3, "pediatria-leki-prywatnosc.html": 1}


def folder(lang):
    return "" if lang == "pl" else lang + "/"


def page(lang, fname, title, desc, body):
    t = T[lang]
    up = "" if lang == "pl" else "../"
    alts = "\n".join(
        f'  <link rel="alternate" hreflang="{l}" href="{SITE}{folder(l)}{"" if fname == "index.html" else fname}">' for l in LANGS)
    alts += f'\n  <link rel="alternate" hreflang="x-default" href="{SITE}{"" if fname == "index.html" else fname}">'
    nav = "\n".join(
        f'        <a href="{f}"{" aria-current=\"page\"" if ACTIVE[fname] == i else ""}>{t["nav"][i]}</a>'
        for i, f in enumerate(NAV_FILES))
    langs = "\n".join(
        f'        <a href="{up}{folder(l)}{fname}" hreflang="{l}" lang="{l}" title="{LANG_NAME[l]}"{" aria-current=\"true\"" if l == lang else ""}>{LANG_LABEL[l]}</a>'
        for l in LANGS)
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{SITE}{folder(lang)}{"" if fname == "index.html" else fname}">
{alts}
  <link rel="icon" href="{up}logo.svg" type="image/svg+xml">
  <link rel="stylesheet" href="{up}style.css">
</head>
<body>
  <header>
    <div class="wrap bar">
      <a class="brand" href="index.html"><img src="{up}logo.svg" alt="">MikoSokPhoto</a>
      <nav>
{nav}
      </nav>
      <div class="langs" role="navigation" aria-label="{t["lang_aria"]}">
{langs}
      </div>
    </div>
  </header>

  <main>
    <div class="wrap">
{body}
    </div>
  </main>

  <footer>
    <div class="wrap">
      © 2026 {COMPANY} · NIP {NIP} ·
      <a href="polityka-prywatnosci.html">{t["nav"][3]}</a>
    </div>
  </footer>
</body>
</html>
"""


def sections(items):
    out = []
    for i, (h, p) in enumerate(items):
        style = ' style="margin-top:0"' if i == 0 else ""
        out.append(f'        <h2{style}>{h}</h2>\n        <p>{p}</p>')
    return "\n\n".join(out)


def build(lang):
    t = T[lang]
    up = "" if lang == "pl" else "../"
    files = {}

    files["index.html"] = page(lang, "index.html", t["home_title"], t["home_desc"], f"""      <section class="hero">
        <img src="{up}logo.svg" alt="{t["logo_alt"]}">
        <h1>MikoSokPhoto</h1>
        <p>{t["home_sub"]}</p>
        <div class="buttons">
          <a class="button" href="pediatria-leki.html">Pediatria LEKI</a>
          <a class="button" href="kontakt.html">{t["nav"][2]}</a>
        </div>
      </section>""")

    L = t["labels"]
    files["kontakt.html"] = page(lang, "kontakt.html", t["contact_title"], t["contact_desc"], f"""      <h1>{t["contact_h1"]}</h1>
      <div class="card">
        <dl>
          <dt>{L[0]}</dt>
          <dd>{COMPANY}</dd>
          <dt>{L[1]}</dt>
          <dd>{STREET}<br>{CITY}, {t["country"]}</dd>
          <dt>{L[2]}</dt>
          <dd>{NIP}</dd>
          <dt>{L[3]}</dt>
          <dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd>
          <dt>{L[4]}</dt>
          <dd><a href="tel:{PHONE_HREF}">{PHONE}</a></dd>
        </dl>
      </div>""")

    files["polityka-prywatnosci.html"] = page(lang, "polityka-prywatnosci.html", t["priv_title"], t["priv_desc"], f"""      <h1>{t["priv_h1"]}</h1>
      <p>{t["priv_date"]}</p>
      <div class="card">
{sections(t["priv"])}
      </div>""")

    parts = []
    for i, (h, content) in enumerate(t["app_sections"]):
        style = ' style="margin-top:0"' if i == 0 else ""
        if content and isinstance(content[0], tuple):
            lis = "\n".join(f"          <li><strong>{a}</strong> – {b}</li>" for a, b in content)
            parts.append(f"        <h2{style}>{h}</h2>\n        <ul>\n{lis}\n        </ul>")
        else:
            ps = "\n".join(f"        <p>{p}</p>" for p in content)
            parts.append(f"        <h2{style}>{h}</h2>\n{ps}")
    files["pediatria-leki.html"] = page(lang, "pediatria-leki.html", t["app_title"], t["app_desc"], f"""      <h1>Pediatria LEKI</h1>
      <p class="lead">{t["app_lead"]}</p>

      <div class="notice">
        {t["app_notice"]}
      </div>

      <div class="card">
{chr(10).join(chr(10) + p if j else p for j, p in enumerate(parts))}
      </div>""")

    files["pediatria-leki-prywatnosc.html"] = page(lang, "pediatria-leki-prywatnosc.html", t["ap_title"], t["ap_desc"], f"""      <h1>{t["ap_h1"]}</h1>
      <p>{t["ap_version"]} <code>pl.pediatrialeki.mobile</code></p>
      <div class="card">
{sections(t["ap"])}
        <p>{t["ap_publisher"]}: <strong>{COMPANY}</strong>, {STREET}, {CITY}, NIP {NIP} · {t["ap_contact"]}: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
      </div>""")

    d = os.path.join(OUT, folder(lang))
    os.makedirs(d, exist_ok=True)
    for f, html in files.items():
        with open(os.path.join(d, f), "w", encoding="utf-8") as fh:
            fh.write(html)


for l in LANGS:
    build(l)
print("OK", OUT)
