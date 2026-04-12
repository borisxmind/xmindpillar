# Claude Code Prompt: x-mind Pillarsite Konsolidierung v2
# Maximum Content Uniqueness Edition
# Einsatz: Direkt in Claude Code – schrittweise nach Phasen

---

## GITHUB & PROJEKTSTRUKTUR

Das bestehende Projekt liegt auf GitHub. Die Ursprungsdaten (alte Stadtseiten)
bleiben dort **unberührt** – du legst alle neuen Dateien in einem separaten Ordner an.

**Repo-Struktur:**
```
x-mind.de/                          ← Repo-Root (bestehend, NICHT anfassen)
├── webdesign/                      ← alte Pillar-Seiten (bleiben erhalten)
├── werbeagentur/
├── seo-agentur/
├── webagentur/
├── marketing-agentur/
├── corporate-design/
├── werbefotografie/
├── drohnenfotografie/
│
└── agentur/                        ← NEU – dieser Ordner wird komplett neu angelegt
    ├── _template/
    │   └── index.html              ← Basis-Template
    ├── stadtdaten.json             ← Stadtdaten für alle 34 Städte
    ├── generate_stadtseiten.py     ← Generator-Script
    ├── generate_redirects.py       ← Redirect-Generator
    ├── audit_uniqueness.py         ← Uniqueness-Prüfscript
    ├── singen/
    │   └── index.html              ← generierte Stadtseite
    ├── konstanz/
    │   └── index.html
    └── ... (alle 34 Städte)
```

**Wichtige Regeln:**
- Alles was du erstellst landet in `/agentur/` – niemals außerhalb
- Bestehende Ordner (`/webdesign/`, `/werbeagentur/` etc.) werden **nicht verändert**
- Die `.htaccess` im Repo-Root bekommst du am Ende als separates Snippet (`redirects.htaccess`) – du schreibst sie **nicht** direkt um
- Committe nach jeder Phase mit aussagekräftiger Message:
  - `feat: add /agentur/ template (Phase 1)`
  - `feat: add stadtdaten.json with 34 cities (Phase 3)`
  - `feat: add generator scripts (Phase 2+4)`
  - `feat: generate all 34 city pages (Phase 2 run)`
  - `feat: add uniqueness audit script (Phase 5)`

---

## KONTEXT FÜR CLAUDE CODE

Du arbeitest am Projekt der Werbeagentur **x mind** (x-mind.de), Singen am Bodensee.

Die Website hat 272 HTML-Landingpages (8 Themen × 34 Städte) die Google als
"Scaled Content Abuse" wertet und abstraft.

**Ziel:** Konsolidierung auf eine starke, inhaltlich einzigartige Stadtseite pro Stadt:
```
/agentur/singen/index.html     ← alle 8 Themen vereint + maximal unique Content
/agentur/konstanz/index.html
... (alle 34 Städte)
```

Alte Themen-URLs → 301-Redirect auf neue Stadtseite.
Alte Pillar-Seiten (/webdesign/, /seo-agentur/ etc.) → bleiben erhalten.

---

## CONTENT-UNIQUENESS STRATEGIE

Jede Stadtseite muss sich von allen anderen **in mindestens 6 Dimensionen** unterscheiden.
Das Generator-Script befüllt folgende stadtspezifische Blöcke aus der JSON-Datendatei:

| Block | Unique-Anteil | Beschreibung |
|-------|--------------|--------------|
| Hero H1 + Subline | hoch | Stadtname + Region variabel |
| Wirtschafts-Absatz | hoch | 3-4 Sätze, individuell pro Stadt |
| Branchen-Fokus-Text | hoch | 2 Sätze über die dominante Branche |
| Leistungs-Intro-Satz | mittel | Stadtspezifischer Einstiegssatz pro Leistungsblock |
| Lokale Herausforderungen | hoch | Welche Marketing-Probleme hat diese Stadt konkret? |
| Geografischer Kontext | hoch | Lage, Nachbarstädte, Einzugsgebiet |
| FAQ – Frage 1 | hoch | Stadtspezifische FAQ-Frage zur lokalen Situation |
| FAQ – Frage 2 | mittel | Branchen-spezifische Frage |
| Cross-Links Nachbarstädte | hoch | Je nach Stadtlage unterschiedliche Nachbarstädte |
| Schema.org LocalBusiness | hoch | Stadtspezifische areaServed-Daten |
| CTA-Schlusstext | mittel | Stadtspezifische Formulierung |

**Ziel-Uniqueness: mind. 55–60% einzigartiger Content pro Seite.**

---

## PHASE 1 – TEMPLATE MIT UNIQUENESS-SLOTS

Erstelle `/agentur/_template/index.html`

### Alle Platzhalter (komplett):

```
# Basis-Daten
{{STADT}}                    → "Singen"
{{STADT_SLUG}}               → "singen"
{{STADT_GENITIV}}            → "Singens"
{{REGION}}                   → "Hegau & Bodensee"
{{BUNDESLAND}}               → "Baden-Württemberg"
{{LAND_LABEL}}               → "" (leer für DE) oder "(CH)" oder "(AT)"
{{EINWOHNER}}                → "47.000"
{{WAHRZEICHEN}}              → "Hohentwiel"
{{NACHBARSTAEDTE_LISTE}}     → "Konstanz, Radolfzell und Stockach"
{{EINZUGSGEBIET_KM}}         → "30"   (km Radius Einzugsgebiet)

# Wirtschaft & Branchen
{{BRANCHEN}}                 → "Metallverarbeitung, Maschinenbau, Nahrungsmittelindustrie"
{{BRANCHEN_DOMINANT}}        → "Metallverarbeitung und Maschinenbau"  (nur die 1-2 wichtigsten)
{{WIRTSCHAFT_ABSATZ}}        → 3-4 Sätze individueller Wirtschaftstext
{{BRANCHEN_FOKUS_TEXT}}      → 2 Sätze: Was bedeutet die Hauptbranche für Marketing-Bedarf?
{{LOKALE_HERAUSFORDERUNG}}   → 2 Sätze: Spezifisches Marketing-Problem dieser Stadt/Region
{{GEO_KONTEXT}}              → 1-2 Sätze: Lage, Nachbarschaft, Besonderheit

# Leistungs-Intro-Sätze (je 1 stadtspezifischer Einstiegssatz pro Leistung)
{{WEBDESIGN_INTRO}}          → z.B. "In Singen entscheiden Kunden aus Industrie und Handel..."
{{SEO_INTRO}}                → z.B. "Wer in Singen gesucht wird, konkurriert mit Konstanz..."
{{CORPORATE_INTRO}}          → z.B. "Singener Unternehmen stehen im Wettbewerb mit..."
{{MARKETING_INTRO}}          → z.B. "Der Hegau-Markt ist eng – gezieltes Marketing..."
{{WEBAGENTUR_INTRO}}         → z.B. "WordPress oder Joomla – in Singen setzen wir..."
{{FOTO_INTRO}}               → z.B. "Industriefotografie für den Wirtschaftsraum Hegau..."
{{DROHNEN_INTRO}}            → z.B. "Am Hohentwiel und im Hegau entstehen..."
{{FULLSERVICE_INTRO}}        → z.B. "Von der Imagebroschüre bis zur Google-Kampagne..."

# FAQ (2 stadtspezifische Fragen + 6 generische)
{{FAQ_LOKAL_FRAGE_1}}        → z.B. "Arbeitet ihr auch mit Industriebetrieben in Singen?"
{{FAQ_LOKAL_ANTWORT_1}}      → stadtspezifische Antwort
{{FAQ_LOKAL_FRAGE_2}}        → z.B. "Kennt ihr den Schweizer Markt?"  (für Grenzstädte)
{{FAQ_LOKAL_ANTWORT_2}}      → stadtspezifische Antwort

# Cross-Links (stadtspezifisch, 4-6 Nachbarstädte)
{{CROSSLINKS_REGION_1_TITEL}} → "Hegau & Bodensee"
{{CROSSLINKS_REGION_1_LINKS}} → HTML-Liste mit 3-4 Nachbarstadt-Links
{{CROSSLINKS_REGION_2_TITEL}} → "Weitere Städte"
{{CROSSLINKS_REGION_2_LINKS}} → HTML-Liste

# CTA & Abschluss
{{CTA_SCHLUSSTEXT}}          → stadtspezifischer Satz im Kontaktbereich
{{CTA_SUBTEXT}}              → z.B. "Für Unternehmen in Singen und dem Hegau."

# Meta & SEO
{{META_TITLE}}               → "Werbeagentur Singen | Webdesign, SEO & Marketing – x mind"
{{META_DESC}}                → individuell, max. 155 Zeichen
{{CANONICAL_URL}}            → "https://www.x-mind.de/agentur/singen/"
{{OG_TITLE}}                 → wie META_TITLE
{{OG_DESC}}                  → wie META_DESC

# Schema.org (strukturierte Daten)
{{SCHEMA_CITY}}              → "Singen"
{{SCHEMA_REGION}}            → "Baden-Württemberg"
{{SCHEMA_COUNTRY}}           → "DE" oder "CH" oder "AT"
{{SCHEMA_AREA_SERVED}}       → "Singen, Konstanz, Radolfzell, Hegau"
```

### Seitenstruktur des Templates:

```html
<!-- 1. HEAD mit allen Meta-Tags, Canonical, OG, Schema.org JSON-LD -->

<!-- 2. NAVIGATION – sticky, Logo → x-mind.de -->

<!-- 3. HERO -->
<section class="hero">
  <!-- Breadcrumb: x-mind.de › Agentur › {{STADT}} -->
  <h1>Werbeagentur {{STADT}} – Webdesign, SEO & Marketing</h1>
  <p>Ihre Full-Service-Agentur in {{REGION}} – persönlich, regional, seit 18 Jahren.
     Für Unternehmen in {{STADT}} und einem Einzugsgebiet von {{EINZUGSGEBIET_KM}} km.</p>
  <!-- CTA: Kostenlose Beratung | Referenzen ansehen -->
  <!-- Trust-Badges: ✓ Kostenlos · ✓ Unverbindlich · ✓ Persönlich vor Ort -->
</section>

<!-- 4. STATS-BAR: 100% Passion | 500+ Projekte | 18 Jahre | 100+ Kunden -->

<!-- 5. WIRTSCHAFT & STANDORT – stadtspezifischer Block -->
<section class="standort">
  <h2>x mind in {{STADT}} – Ihr lokaler Agenturpartner</h2>
  <p>{{GEO_KONTEXT}}</p>
  <p>{{WIRTSCHAFT_ABSATZ}}</p>
  <div class="branchen-box">
    <h3>Typische Branchen in {{STADT}}</h3>
    <!-- Auflistung: {{BRANCHEN}} als Tag-Chips -->
  </div>
  <p class="branchen-fokus">{{BRANCHEN_FOKUS_TEXT}}</p>
  <div class="herausforderung-box">
    <h3>Marketing in {{REGION}}: Was Unternehmen hier wirklich brauchen</h3>
    <p>{{LOKALE_HERAUSFORDERUNG}}</p>
  </div>
</section>

<!-- 6. LEISTUNGS-GRID – 8 Kacheln, je mit stadtspezifischem Intro-Satz -->
<section class="leistungen">
  <h2>Unsere Leistungen für {{STADT}} und {{REGION}}</h2>

  <!-- Kachel 1: Webdesign -->
  <div class="leistung-card">
    <h3>Webdesign & Webentwicklung</h3>
    <p class="intro-lokal">{{WEBDESIGN_INTRO}}</p>
    <p>Individuelle Websites für Handwerk, Mittelstand und regionale Unternehmen –
       mobil, schnell, suchmaschinenoptimiert.</p>
    <a href="/webdesign/">Mehr erfahren →</a>
  </div>

  <!-- Kachel 2: SEO -->
  <div class="leistung-card">
    <h3>SEO & Suchmaschinenoptimierung</h3>
    <p class="intro-lokal">{{SEO_INTRO}}</p>
    <p>Lokale und regionale Sichtbarkeit bei Google – für Ihre Branche in {{STADT}}.</p>
    <a href="/seo-agentur/">Mehr erfahren →</a>
  </div>

  <!-- Kachel 3: Corporate Design -->
  <div class="leistung-card">
    <h3>Corporate Design & Branding</h3>
    <p class="intro-lokal">{{CORPORATE_INTRO}}</p>
    <p>Logo, Farben, Typografie – ein konsistentes Erscheinungsbild, das in Erinnerung bleibt.</p>
    <a href="/corporate-design/">Mehr erfahren →</a>
  </div>

  <!-- Kachel 4: Marketing -->
  <div class="leistung-card">
    <h3>Marketing & Kampagnen</h3>
    <p class="intro-lokal">{{MARKETING_INTRO}}</p>
    <p>Print, Digital, Social – Kampagnen, die Ihre Zielgruppe in {{REGION}} erreichen.</p>
    <a href="/marketing-agentur/">Mehr erfahren →</a>
  </div>

  <!-- Kachel 5: Webagentur -->
  <div class="leistung-card">
    <h3>Webagentur & CMS-Lösungen</h3>
    <p class="intro-lokal">{{WEBAGENTUR_INTRO}}</p>
    <p>WordPress, Joomla, Elementor – Websites die Sie selbst pflegen können.</p>
    <a href="/webagentur/">Mehr erfahren →</a>
  </div>

  <!-- Kachel 6: Werbefotografie -->
  <div class="leistung-card">
    <h3>Werbefotografie</h3>
    <p class="intro-lokal">{{FOTO_INTRO}}</p>
    <p>Produkt-, Team- und Imagefotografie für Ihren professionellen Auftritt.</p>
    <a href="/werbefotografie/">Mehr erfahren →</a>
  </div>

  <!-- Kachel 7: Drohnenfotografie -->
  <div class="leistung-card">
    <h3>Drohnenfotografie</h3>
    <p class="intro-lokal">{{DROHNEN_INTRO}}</p>
    <p>Luftaufnahmen für Immobilien, Industrie und Events in {{REGION}}.</p>
    <a href="/drohnenfotografie/">Mehr erfahren →</a>
  </div>

  <!-- Kachel 8: Full-Service -->
  <div class="leistung-card">
    <h3>Werbeagentur Full-Service</h3>
    <p class="intro-lokal">{{FULLSERVICE_INTRO}}</p>
    <p>Alles aus einer Hand – Strategie, Kreation, Umsetzung, Betreuung.</p>
    <a href="/werbeagentur/">Mehr erfahren →</a>
  </div>
</section>

<!-- 7. PROZESS-SECTION: 3 Schritte (generisch, bewusst) -->

<!-- 8. TESTIMONIALS: 3 echte Zitate (statisch) -->

<!-- 9. FAQ – 2 stadtspezifisch + 6 generisch -->
<section class="faq">
  <h2>Häufige Fragen – Werbeagentur {{STADT}}</h2>

  <!-- Stadtspezifische FAQs -->
  <div class="faq-item lokal">
    <h3>{{FAQ_LOKAL_FRAGE_1}}</h3>
    <p>{{FAQ_LOKAL_ANTWORT_1}}</p>
  </div>
  <div class="faq-item lokal">
    <h3>{{FAQ_LOKAL_FRAGE_2}}</h3>
    <p>{{FAQ_LOKAL_ANTWORT_2}}</p>
  </div>

  <!-- Generische FAQs (identisch, aber trotzdem wertvoll für Nutzer) -->
  <div class="faq-item">
    <h3>Was kostet eine professionelle Website?</h3>
    <p>Einfache Business-Websites starten ab ca. 1.500 €...</p>
  </div>
  <!-- weitere 5 generische FAQs -->
</section>

<!-- 10. CROSS-LINKS zu Nachbarstädten – stadtspezifisch gruppiert -->
<section class="weitere-staedte">
  <h2>x mind auch in Ihrer Nachbarschaft</h2>
  <div class="region-gruppe">
    <h3>{{CROSSLINKS_REGION_1_TITEL}}</h3>
    {{CROSSLINKS_REGION_1_LINKS}}
  </div>
  <div class="region-gruppe">
    <h3>{{CROSSLINKS_REGION_2_TITEL}}</h3>
    {{CROSSLINKS_REGION_2_LINKS}}
  </div>
</section>

<!-- 11. KONTAKT-CTA -->
<section class="kontakt-cta">
  <h2>Ihr Projekt in {{STADT}} – reden wir Klartext.</h2>
  <p>{{CTA_SCHLUSSTEXT}}</p>
  <p class="sub">{{CTA_SUBTEXT}}</p>
</section>

<!-- 12. FOOTER -->

<!-- 13. SCHEMA.ORG JSON-LD im <head> -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "x mind Werbeagentur",
  "url": "{{CANONICAL_URL}}",
  "telephone": "+4977319398316",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Freibühlstraße 19",
    "addressLocality": "Singen",
    "postalCode": "78224",
    "addressCountry": "DE"
  },
  "areaServed": "{{SCHEMA_AREA_SERVED}}",
  "description": "{{META_DESC}}"
}
</script>
```

**Design-Vorgaben:**
- Dark navy `#0b243b`, Accent gelb `#f5c842`, Weiß
- Exakt gleicher Font-Stack wie `/webdesign/webdesign-singen/index.html`
- Fully responsive, mobile-first
- Self-contained HTML (nur Google Fonts extern)
- `.intro-lokal` Klasse: leicht anders gestylt (z.B. italic, leicht anderer Ton) damit der stadtspezifische Satz visuell als lokale Note erkennbar ist

---

## PHASE 2 – PYTHON GENERATOR-SCRIPT

Erstelle `/agentur/generate_stadtseiten.py`

```python
#!/usr/bin/env python3
"""
x-mind Stadtseiten Generator
Liest stadtdaten.json → erzeugt /agentur/{slug}/index.html für jede Stadt
"""

import json
import os
import shutil
from pathlib import Path

TEMPLATE_PATH = Path("_template/index.html")
DATA_PATH     = Path("stadtdaten.json")
OUTPUT_DIR    = Path(".")   # /agentur/ ist das Arbeitsverzeichnis

def generate_crosslinks(aktuelle_stadt_slug, alle_staedte):
    """
    Erzeugt stadtspezifische Cross-Link-HTML basierend auf
    geografischer Nähe (Regionen aus JSON).
    Gibt HTML für Region-1 und Region-2 zurück.
    """
    # Aktuelle Stadt aus Liste holen
    aktuelle = next(s for s in alle_staedte if s["slug"] == aktuelle_stadt_slug)
    aktuelle_region = aktuelle["region"]

    # Selbe Region (außer aktuelle Stadt)
    selbe_region = [
        s for s in alle_staedte
        if s["region"] == aktuelle_region and s["slug"] != aktuelle_stadt_slug
    ]

    # Andere Regionen – max. 4 Städte aus anderen Regionen
    andere = [
        s for s in alle_staedte
        if s["region"] != aktuelle_region
    ][:4]

    def mache_links(staedte_liste):
        links = ""
        for s in staedte_liste[:4]:
            label = f"Werbeagentur {s['stadt']}"
            links += f'<a href="/agentur/{s["slug"]}/">{label}</a>\n'
        return links

    region_1_titel = aktuelle_region
    region_1_links = mache_links(selbe_region)
    region_2_titel = "Weitere Städte"
    region_2_links = mache_links(andere)

    return region_1_titel, region_1_links, region_2_titel, region_2_links


def render_template(template_str, stadt_data, alle_staedte):
    """Ersetzt alle {{PLATZHALTER}} im Template durch Stadtdaten."""

    r1_titel, r1_links, r2_titel, r2_links = generate_crosslinks(
        stadt_data["slug"], alle_staedte
    )

    replacements = {
        # Basis
        "{{STADT}}":                    stadt_data["stadt"],
        "{{STADT_SLUG}}":               stadt_data["slug"],
        "{{STADT_GENITIV}}":            stadt_data["genitiv"],
        "{{REGION}}":                   stadt_data["region"],
        "{{BUNDESLAND}}":               stadt_data["bundesland"],
        "{{LAND_LABEL}}":               stadt_data.get("land_label", ""),
        "{{EINWOHNER}}":                stadt_data["einwohner"],
        "{{WAHRZEICHEN}}":              stadt_data["wahrzeichen"],
        "{{NACHBARSTAEDTE_LISTE}}":     stadt_data.get("nachbarstaedte_liste", ""),
        "{{EINZUGSGEBIET_KM}}":         str(stadt_data.get("einzugsgebiet_km", "30")),

        # Wirtschaft
        "{{BRANCHEN}}":                 stadt_data["branchen"],
        "{{BRANCHEN_DOMINANT}}":        stadt_data.get("branchen_dominant", ""),
        "{{WIRTSCHAFT_ABSATZ}}":        stadt_data["wirtschaft"],
        "{{BRANCHEN_FOKUS_TEXT}}":      stadt_data.get("branchen_fokus_text", ""),
        "{{LOKALE_HERAUSFORDERUNG}}":   stadt_data.get("lokale_herausforderung", ""),
        "{{GEO_KONTEXT}}":              stadt_data.get("geo_kontext", ""),

        # Leistungs-Intros
        "{{WEBDESIGN_INTRO}}":          stadt_data.get("webdesign_intro", ""),
        "{{SEO_INTRO}}":                stadt_data.get("seo_intro", ""),
        "{{CORPORATE_INTRO}}":          stadt_data.get("corporate_intro", ""),
        "{{MARKETING_INTRO}}":          stadt_data.get("marketing_intro", ""),
        "{{WEBAGENTUR_INTRO}}":         stadt_data.get("webagentur_intro", ""),
        "{{FOTO_INTRO}}":               stadt_data.get("foto_intro", ""),
        "{{DROHNEN_INTRO}}":            stadt_data.get("drohnen_intro", ""),
        "{{FULLSERVICE_INTRO}}":        stadt_data.get("fullservice_intro", ""),

        # FAQ lokal
        "{{FAQ_LOKAL_FRAGE_1}}":        stadt_data.get("faq_lokal_frage_1", ""),
        "{{FAQ_LOKAL_ANTWORT_1}}":      stadt_data.get("faq_lokal_antwort_1", ""),
        "{{FAQ_LOKAL_FRAGE_2}}":        stadt_data.get("faq_lokal_frage_2", ""),
        "{{FAQ_LOKAL_ANTWORT_2}}":      stadt_data.get("faq_lokal_antwort_2", ""),

        # Cross-Links
        "{{CROSSLINKS_REGION_1_TITEL}}": r1_titel,
        "{{CROSSLINKS_REGION_1_LINKS}}": r1_links,
        "{{CROSSLINKS_REGION_2_TITEL}}": r2_titel,
        "{{CROSSLINKS_REGION_2_LINKS}}": r2_links,

        # CTA
        "{{CTA_SCHLUSSTEXT}}":          stadt_data.get("cta_schlusstext", f"Rufen Sie an oder schreiben Sie uns – wir sind persönlich für Sie da."),
        "{{CTA_SUBTEXT}}":              stadt_data.get("cta_subtext", f"Für Unternehmen in {stadt_data['stadt']} und {stadt_data['region']}."),

        # Meta & SEO
        "{{META_TITLE}}":               stadt_data["meta_title"],
        "{{META_DESC}}":                stadt_data["meta_desc"],
        "{{CANONICAL_URL}}":            f"https://www.x-mind.de/agentur/{stadt_data['slug']}/",
        "{{OG_TITLE}}":                 stadt_data["meta_title"],
        "{{OG_DESC}}":                  stadt_data["meta_desc"],

        # Schema.org
        "{{SCHEMA_CITY}}":              stadt_data["stadt"],
        "{{SCHEMA_REGION}}":            stadt_data["bundesland"],
        "{{SCHEMA_COUNTRY}}":           stadt_data.get("schema_country", "DE"),
        "{{SCHEMA_AREA_SERVED}}":       stadt_data.get("schema_area_served",
                                            f"{stadt_data['stadt']}, {stadt_data['region']}"),
    }

    result = template_str
    for placeholder, value in replacements.items():
        result = result.replace(placeholder, value)

    # Warnung wenn noch Platzhalter übrig
    import re
    remaining = re.findall(r'\{\{[A-Z_]+\}\}', result)
    if remaining:
        print(f"  ⚠ Nicht ersetzte Platzhalter: {set(remaining)}")

    return result


def main():
    print("x-mind Stadtseiten Generator")
    print("=" * 40)

    template_str = TEMPLATE_PATH.read_text(encoding="utf-8")
    alle_staedte = json.loads(DATA_PATH.read_text(encoding="utf-8"))

    erfolg = 0
    fehler = 0

    for stadt in alle_staedte:
        slug = stadt["slug"]
        output_dir = OUTPUT_DIR / slug
        output_dir.mkdir(exist_ok=True)

        output_file = output_dir / "index.html"

        try:
            html = render_template(template_str, stadt, alle_staedte)
            output_file.write_text(html, encoding="utf-8")
            print(f"  ✓ {slug}/index.html")
            erfolg += 1
        except Exception as e:
            print(f"  ✗ {slug}: {e}")
            fehler += 1

    print("=" * 40)
    print(f"Fertig: {erfolg} Seiten generiert, {fehler} Fehler")


if __name__ == "__main__":
    main()
```

---

## PHASE 3 – STADTDATEN JSON (MAXIMALE UNIQUENESS)

Erstelle `/agentur/stadtdaten.json`

Jede Stadt hat **alle neuen Felder** befüllt. Hier das vollständige Format
mit allen 34 Städten:

```json
[
  {
    "stadt": "Singen",
    "slug": "singen",
    "genitiv": "Singens",
    "region": "Hegau & Bodensee",
    "bundesland": "Baden-Württemberg",
    "land_label": "",
    "schema_country": "DE",
    "einwohner": "47.000",
    "wahrzeichen": "Hohentwiel",
    "einzugsgebiet_km": "25",
    "nachbarstaedte_liste": "Konstanz, Radolfzell und Stockach",

    "branchen": "Metallverarbeitung, Maschinenbau, Nahrungsmittelindustrie",
    "branchen_dominant": "Metallverarbeitung und Maschinenbau",
    "wirtschaft": "Singen am Hohentwiel ist der wirtschaftliche Anker des Hegau – mit Industriebetrieben wie Georg Fischer und Maggi/Nestlé sowie einem wachsenden Dienstleistungssektor. Als Kreisstadt des Landkreises Konstanz hat Singen Versorgungsfunktion für das gesamte Hegau. Die Nähe zur Schweizer Grenze bringt grenzüberschreitenden Kundenverkehr und einen intensiven Wettbewerb um Fachkräfte.",
    "branchen_fokus_text": "Industriebetriebe und Maschinenbauer in Singen brauchen keine Hochglanzbroschüren – sie brauchen klare B2B-Kommunikation, technisch präzise Texte und eine Website, die bei Ausschreibungsrecherchen gefunden wird.",
    "lokale_herausforderung": "Singener Unternehmen kämpfen digital auf zwei Fronten: gegen größere Agenturen aus Konstanz und Stuttgart auf der einen Seite, und gegen günstige Schweizer Mitbewerber auf der anderen. Wer hier sichtbar bleiben will, braucht lokale SEO-Kompetenz und eine klare Positionierung.",
    "geo_kontext": "Singen liegt 40 km westlich von Konstanz und 8 km nördlich der Schweizer Grenze – ein Wirtschaftsstandort im Dreieck Deutschland, Schweiz und Vorarlberg.",

    "webdesign_intro": "Industriebetriebe und Mittelständler in Singen entscheiden online binnen Sekunden, ob ein Anbieter ernst genommen wird – Ihre Website ist das digitale Schaufenster am Hohentwiel-Ring.",
    "seo_intro": "Wer in Singen nach einem Dienstleister sucht, tippt oft von Schaffhausen oder Konstanz aus – lokales SEO muss den Einzugsbereich Hegau vollständig abdecken, nicht nur die Postleitzahl.",
    "corporate_intro": "Singener Unternehmen stehen im direkten Sichtvergleich mit Mitbewerbern aus Konstanz und der Schweiz – ein konsistentes Corporate Design ist kein Nice-to-have, sondern Vertrauenssignal.",
    "marketing_intro": "Der Hegau ist ein enger Markt, in dem sich Branchen kennen und Empfehlungen zählen – gezieltes regionales Marketing verstärkt genau diesen Effekt.",
    "webagentur_intro": "WordPress-Installationen in Singen betreuen wir seit Jahren persönlich vor Ort – ohne Ticketsystem, mit direktem Draht.",
    "foto_intro": "Industrie- und Produktfotografie für den Wirtschaftsraum Hegau: von Maschinenaufnahmen am Hohentwiel-Ring bis zu Teamfotos für den Unternehmensauftritt.",
    "drohnen_intro": "Am Hohentwiel, über den Gewerbegebieten in Bohlingen oder beim Firmengelände am Stadtrand – Drohnenaufnahmen geben Singener Unternehmen eine neue Perspektive.",
    "fullservice_intro": "Von der Imagebroschüre für die Hannover Messe bis zur lokalen Google-Kampagne – x mind betreut Singener Unternehmen seit 18 Jahren aus einer Hand.",

    "faq_lokal_frage_1": "Arbeitet ihr auch mit Industriebetrieben und B2B-Unternehmen in Singen zusammen?",
    "faq_lokal_antwort_1": "Ja – B2B und Industrie sind unsere Kernkompetenz in Singen. Wir kennen den Hohentwiel-Ring, die Zuliefererstruktur und die Anforderungen an technische Kommunikation. BGO Singen, MTS Reifenservice und weitere Singener Betriebe sind langjährige Kunden.",
    "faq_lokal_frage_2": "Könnt ihr auch Kunden in der Schweiz betreuen, die über Singen auf euch stoßen?",
    "faq_lokal_antwort_2": "Absolut. Durch unsere Grenznähe haben wir Erfahrung mit Schweizer Kunden – von der Rechnungsstellung in CHF bis zur Berücksichtigung des Schweizer Markts in SEO und Werbetexten.",

    "cta_schlusstext": "Rufen Sie an oder schreiben Sie uns – wir sind persönlich vor Ort in Singen und kennen Ihren Markt.",
    "cta_subtext": "Für Unternehmen in Singen, dem Hegau und der gesamten Bodenseeregion.",

    "schema_area_served": "Singen, Hegau, Konstanz, Radolfzell, Stockach, Bodenseeregion",
    "meta_title": "Werbeagentur Singen | Webdesign, SEO & Marketing – x mind",
    "meta_desc": "x mind – Ihre Werbeagentur direkt in Singen. Webdesign, SEO, Corporate Design & Fotografie. Seit 18 Jahren im Hegau. Jetzt kostenloses Erstgespräch."
  },
  {
    "stadt": "Konstanz",
    "slug": "konstanz",
    "genitiv": "Konstanz'",
    "region": "Bodensee",
    "bundesland": "Baden-Württemberg",
    "land_label": "",
    "schema_country": "DE",
    "einwohner": "85.000",
    "wahrzeichen": "Münster",
    "einzugsgebiet_km": "30",
    "nachbarstaedte_liste": "Radolfzell, Singen und Überlingen",

    "branchen": "Tourismus, Hochschule & Forschung, Medizintechnik, Dienstleistungen",
    "branchen_dominant": "Hochschule, Forschung und Tourismus",
    "wirtschaft": "Konstanz ist Universitätsstadt, Touristikzentrum und Wirtschaftsstandort zugleich. Die Universität Konstanz und die HTWG prägen den Fachkräftemarkt und bringen kontinuierlich junge Unternehmen hervor. Grenznahe Lage zur Schweiz erzeugt intensiven Wettbewerb und internationale Kundschaft.",
    "branchen_fokus_text": "Tourismusbetriebe und Dienstleister in Konstanz konkurrieren um eine kaufkraftstarke Kundschaft aus Deutschland und der Schweiz – professionelles Webdesign und lokales SEO entscheiden, wer bei der Online-Suche gefunden wird.",
    "lokale_herausforderung": "Konstanz hat eine hohe Agentur-Dichte – Unternehmen müssen hier sehr genau hinschauen, welche Agentur echte lokale Expertise mitbringt und wer nur auf Stadtname-Keywords optimiert.",
    "geo_kontext": "Konstanz liegt direkt an der Schweizer Grenze, umgeben vom Bodensee und dem Untersee – die einzige deutsche Stadt, die während des Zweiten Weltkriegs unzerstört blieb.",

    "webdesign_intro": "In Konstanz entscheiden Touristen und Studenten oft spontan per Smartphone – eine mobile-first Website, die in 2 Sekunden lädt, ist kein Luxus, sondern Grundvoraussetzung.",
    "seo_intro": "Für Konstanzer Unternehmen ist lokales SEO besonders komplex: Sie ranken gegen Mitbewerber aus Radolfzell, Kreuzlingen (CH) und Überlingen gleichzeitig.",
    "corporate_intro": "Konstanz ist eine Stadt mit Haltung und Geschichte – Corporate Design für lokale Unternehmen sollte diese Qualität widerspiegeln statt generisch zu wirken.",
    "marketing_intro": "Saisonales Marketing ist in Konstanz ein eigenes Handwerk – Hochsaison, Fasching, Konzilsstadtimage. Wir kennen den Rhythmus der Stadt.",
    "webagentur_intro": "CMS-Betreuung für Konstanzer Unternehmen: schnell erreichbar, kein Stunden-Tracking, direkter Ansprechpartner.",
    "foto_intro": "Bodensee-Atmosphäre, historische Altstadt, modernes Universitätsflair – Werbefotografie in Konstanz lebt von diesen Kontrasten.",
    "drohnen_intro": "Der Bodensee aus der Luft, die Altstadt von oben, Seerhein-Panoramen – Drohnenaufnahmen in Konstanz bieten spektakuläre Motive für Ihre Unternehmenskommunikation.",
    "fullservice_intro": "Von der Tourismusbroschüre bis zur universitätsnahen Employer-Branding-Kampagne – in Konstanz kennen wir die Zielgruppen.",

    "faq_lokal_frage_1": "Habt ihr Erfahrung mit Tourismus- und Gastronomiebetrieben in Konstanz?",
    "faq_lokal_antwort_1": "Ja – Gastronomie, Hotellerie und Tourismusbetriebe gehören zu unserer Kundschaft am Bodensee. Wir wissen, was saisonales Marketing in Konstanz bedeutet und wie man auf Buchungsportalen und Google gleichzeitig sichtbar bleibt.",
    "faq_lokal_frage_2": "Können wir auch Schweizer Kunden über eine Konstanzer Kampagne ansprechen?",
    "faq_lokal_antwort_2": "Absolut. Wir entwickeln Kampagnen, die grenzüberschreitend funktionieren – mit angepasster Ansprache, CHF-Preisangaben wo sinnvoll und Kenntnissen des Schweizer Konsumentenverhaltens.",

    "cta_schlusstext": "Persönlicher Termin in Konstanz oder bei uns in Singen – Sie entscheiden, wo wir uns kennenlernen.",
    "cta_subtext": "Für Unternehmen in Konstanz, der Bodenseeregion und der Grenzregion Schweiz.",

    "schema_area_served": "Konstanz, Bodensee, Radolfzell, Überlingen, Kreuzlingen, Bodenseeregion",
    "meta_title": "Werbeagentur Konstanz | Webdesign, SEO & Marketing – x mind",
    "meta_desc": "x mind – Werbeagentur für Konstanz. Webdesign, SEO & Marketing für Tourismus, Mittelstand und Dienstleister am Bodensee. Seit 18 Jahren. Jetzt anfragen."
  },
  {
    "stadt": "Radolfzell",
    "slug": "radolfzell",
    "genitiv": "Radolfzells",
    "region": "Bodensee & Hegau",
    "bundesland": "Baden-Württemberg",
    "land_label": "",
    "schema_country": "DE",
    "einwohner": "32.000",
    "wahrzeichen": "Münster Unserer Lieben Frau",
    "einzugsgebiet_km": "20",
    "nachbarstaedte_liste": "Singen, Konstanz und Stockach",
    "branchen": "Industrie, Einzelhandel, Gesundheit, Tourismus",
    "branchen_dominant": "Industrie und Einzelhandel",
    "wirtschaft": "Radolfzell am Bodensee verbindet mittelständische Industrie, lebhaften Einzelhandel und eine wachsende Gesundheitswirtschaft. Die Stadt liegt zwischen den Wirtschaftspolen Singen und Konstanz und profitiert von beiden Einzugsgebieten.",
    "branchen_fokus_text": "Einzelhändler und Dienstleister in Radolfzell konkurrieren zunehmend mit Online-Angeboten – wer lokal präsent bleibt, braucht eine starke Google-Sichtbarkeit und eine Website, die Vertrauen aufbaut.",
    "lokale_herausforderung": "Radolfzell steht im digitalen Schatten von Konstanz und Singen – Unternehmen hier profitieren davon, wenn ihr Online-Auftritt klar die lokale Kompetenz und Erreichbarkeit kommuniziert.",
    "geo_kontext": "Radolfzell liegt am Untersee zwischen Singen (15 km) und Konstanz (20 km) – mit direktem Seezugang und guter Verkehrsanbindung in alle Richtungen.",
    "webdesign_intro": "Radolfzeller Unternehmen werden bei Google oft hinter Konstanz und Singen gelistet – mit einer gezielt optimierten Website ändern wir das.",
    "seo_intro": "Lokales SEO für Radolfzell bedeutet: sowohl für 'Radolfzell' als auch für den Bodensee-Raum ranken – wir decken beide Suchintentionen ab.",
    "corporate_intro": "Ein starkes Corporate Design hilft Radolfzeller Betrieben, sich gegen größere Nachbarstädte zu behaupten – Professionalität schlägt Stadtgröße.",
    "marketing_intro": "Für Radolfzell funktionieren regionale Kampagnen, die Singen und Konstanz mitdenken – so erreicht Ihre Botschaft den gesamten Hegau.",
    "webagentur_intro": "WordPress-Wartung und CMS-Betreuung für Radolfzell: persönlich, schnell, ohne lange Wartezeiten.",
    "foto_intro": "Produktfotografie und Imageshootings in Radolfzell – mit dem Untersee als natürlichem Hintergrund für Ihre Unternehmensfotos.",
    "drohnen_intro": "Luftaufnahmen über dem Untersee, dem Hafen oder Ihrem Firmengelände in Radolfzell – eindrucksvolle Perspektiven für Ihr Marketing.",
    "fullservice_intro": "Für Radolfzeller Unternehmen bieten wir alles aus einer Hand – von der Imagebroschüre bis zur Google-Ads-Kampagne.",
    "faq_lokal_frage_1": "Betreut ihr auch kleinere Unternehmen und Einzelhändler in Radolfzell?",
    "faq_lokal_antwort_1": "Ja – gerade für kleinere und mittelständische Betriebe in Radolfzell haben wir skalierbare Pakete. Wir passen Leistung und Budget ehrlich aufeinander ab.",
    "faq_lokal_frage_2": "Kann meine Radolfzeller Website auch Kunden aus Konstanz und Singen ansprechen?",
    "faq_lokal_antwort_2": "Das ist genau unser Ansatz: Wir optimieren Ihre Website so, dass sie in Radolfzell, Konstanz und Singen gleichzeitig gefunden wird – mit einer URL, statt drei separater Stadtseiten.",
    "cta_schlusstext": "Schnelle Rückmeldung, persönliches Gespräch – für Unternehmen in Radolfzell und Umgebung.",
    "cta_subtext": "Für Unternehmen in Radolfzell, Singen, Konstanz und dem Hegau.",
    "schema_area_served": "Radolfzell, Hegau, Konstanz, Singen, Stockach, Bodenseeregion",
    "meta_title": "Werbeagentur Radolfzell | Webdesign, SEO & Marketing – x mind",
    "meta_desc": "x mind – Ihre Agentur für Webdesign, SEO und Marketing in Radolfzell am Bodensee. Regional verankert, persönlich erreichbar. Jetzt kostenloses Erstgespräch."
  },
  {
    "stadt": "Überlingen",
    "slug": "ueberlingen",
    "genitiv": "Überlingens",
    "region": "Bodenseekreis",
    "bundesland": "Baden-Württemberg",
    "land_label": "",
    "schema_country": "DE",
    "einwohner": "23.000",
    "wahrzeichen": "Münster St. Nikolaus",
    "einzugsgebiet_km": "20",
    "nachbarstaedte_liste": "Konstanz, Meersburg und Stockach",
    "branchen": "Tourismus, Gesundheit & Kur, Obstbau, Dienstleistungen",
    "branchen_dominant": "Tourismus und Gesundheitswirtschaft",
    "wirtschaft": "Überlingen ist staatlich anerkanntes Kneipp-Heilbad und Touristenmagnet am nördlichen Bodensee. Wellnesshotels, Heilpraktiker und Obstbaubetriebe prägen das Stadtbild – ergänzt durch einen lebhaften Einzelhandel in der mittelalterlichen Altstadt.",
    "branchen_fokus_text": "Tourismusbetriebe und Gesundheitsanbieter in Überlingen brauchen eine starke Online-Präsenz, die Buchungen generiert – Google-Rankings für 'Urlaub Bodensee' und 'Kur Überlingen' sind heiß umkämpft.",
    "lokale_herausforderung": "Überlinger Betriebe sind saisonal stark schwankend belastet – Marketing muss die Nebensaison aktivieren und die Hauptsaison voll ausschöpfen.",
    "geo_kontext": "Überlingen liegt am nördlichen Bodensee, 30 km westlich von Friedrichshafen und 20 km östlich von Konstanz – das Tor zum Bodenseekreis.",
    "webdesign_intro": "Touristen und Kurgäste googeln Überlingen oft ohne konkreten Betrieb im Kopf – wer dann oben steht, bekommt die Anfrage.",
    "seo_intro": "Saisonales SEO für Überlingen: Im Frühjahr auf Touristik optimieren, im Winter auf Wellness und Kurangebote – wir steuern die Schwerpunkte nach.",
    "corporate_intro": "Das Kneippheilbad-Image Überlingens ist ein Qualitätsmerkmal – Corporate Design sollte diese Positionierung konsequent widerspiegeln.",
    "marketing_intro": "Überlingen lebt von Wiederbesuchern – Marketing muss Stammgäste binden und neue Urlauber ansprechen. Zwei verschiedene Zielgruppen, eine koordinierte Strategie.",
    "webagentur_intro": "Buchungssysteme, Eventkalender, mehrsprachige Inhalte – Überlingers Tourismusbetriebe brauchen mehr als eine Standard-WordPress-Installation.",
    "foto_intro": "Bodensee-Panoramen, Kurgarten, mittelalterliche Altstadt – Werbefotografie in Überlingen hat einzigartige Motive.",
    "drohnen_intro": "Über dem Bodensee, dem Kurgarten oder der Altstadt von Überlingen entstehen Drohnenaufnahmen, die im Gedächtnis bleiben.",
    "fullservice_intro": "Tourismusmarketing, Gesundheitsbranding, lokale SEO – für Überlingen denken wir Kampagnen ganzheitlich.",
    "faq_lokal_frage_1": "Habt ihr Erfahrung mit Tourismus- und Kurhotels in Überlingen?",
    "faq_lokal_antwort_1": "Ja – Tourismusbetriebe am Bodensee gehören zu unseren Kernkunden. Wir wissen, wie Buchungsseiten aufgebaut werden müssen und wie man im Sommer-Peak sichtbar bleibt.",
    "faq_lokal_frage_2": "Können wir auch internationale Gäste ansprechen, die Überlingen noch nicht kennen?",
    "faq_lokal_antwort_2": "Absolut – wir erstellen mehrsprachige Inhalte und optimieren für internationale Suchanfragen, damit Ihre Website auch Gäste aus der Schweiz, Österreich und dem restlichen Europa erreicht.",
    "cta_schlusstext": "Sprechen Sie uns an – für Ihren Webauftritt in Überlingen und am Bodensee.",
    "cta_subtext": "Für Tourismusbetriebe, Händler und Dienstleister in Überlingen und dem Bodenseekreis.",
    "schema_area_served": "Überlingen, Bodenseekreis, Konstanz, Meersburg, Stockach",
    "meta_title": "Werbeagentur Überlingen | Webdesign, SEO & Marketing – x mind",
    "meta_desc": "x mind – Werbeagentur für Überlingen am Bodensee. Webdesign, SEO & Marketing für Tourismus, Kurbetriebe und Handel. Persönlich & regional. Jetzt anfragen."
  },
  {
    "stadt": "Stockach",
    "slug": "stockach",
    "genitiv": "Stockachs",
    "region": "Hegau",
    "bundesland": "Baden-Württemberg",
    "land_label": "",
    "schema_country": "DE",
    "einwohner": "17.000",
    "wahrzeichen": "Burg Stockach",
    "einzugsgebiet_km": "20",
    "nachbarstaedte_liste": "Singen, Radolfzell und Überlingen",
    "branchen": "Industrie, Automobilzulieferer, Handwerk, Einzelhandel",
    "branchen_dominant": "Industrie und Automobilzulieferer",
    "wirtschaft": "Stockach ist ein wichtiger Industriestandort im Hegau mit starker Automobilzulieferer-Struktur. ZF Friedrichshafen und weitere Tier-1-Zulieferer haben hier Produktionsstätten. Der Mittelstand prägt neben der Industrie auch Handel und Handwerk.",
    "branchen_fokus_text": "Automobilzulieferer in Stockach brauchen klare B2B-Kommunikation und eine Website, die bei Ausschreibungen und Lieferantenauswahl überzeugt – nicht nur bei Endkunden.",
    "lokale_herausforderung": "Stockacher Betriebe sind oft unsichtbar zwischen den dominanteren Nachbarstädten Singen und Konstanz – gezieltes lokales SEO und ein professioneller Webauftritt schaffen hier Wettbewerbsvorteile.",
    "geo_kontext": "Stockach liegt im südlichen Baden-Württemberg an der B14, zwischen Singen (25 km) und Überlingen (20 km) – ein Industrieknotenpunkt im Hegau.",
    "webdesign_intro": "B2B-Websites für Stockacher Automobilzulieferer müssen Lieferantendatenbanken, Qualitätszertifikate und technische Specs übersichtlich präsentieren.",
    "seo_intro": "Für Stockach bedeutet lokales SEO: nicht nur in Stockach ranken, sondern im gesamten Einzugsgebiet zwischen Singen, Radolfzell und Überlingen sichtbar sein.",
    "corporate_intro": "Industriebetriebe in Stockach brauchen ein Corporate Design, das Zuverlässigkeit und technische Kompetenz ausstrahlt – kein verspieltes Start-up-Look.",
    "marketing_intro": "B2B-Marketing für Stockacher Industrie: Fachmessen, Lieferantenanfragen, LinkedIn-Präsenz – wir sprechen die richtige Sprache.",
    "webagentur_intro": "WordPress-Betreuung für Stockacher Betriebe: Updates, Sicherheit, Performance – ohne dass Sie sich darum kümmern müssen.",
    "foto_intro": "Industriefotografie für Stockacher Produktionsbetriebe: Maschinenparks, Fertigungslinien, Teamfotos – professionell und branchentypisch.",
    "drohnen_intro": "Luftaufnahmen von Industriegeländen und Firmenstandorten in Stockach – für Imagefilme, Jahresberichte und Firmenwebsites.",
    "fullservice_intro": "Von der Produktbroschüre für die Automesse bis zur B2B-Landingpage – Full-Service-Agentur für Stockacher Industriebetriebe.",
    "faq_lokal_frage_1": "Könnt ihr auch Industriebetriebe und Automobilzulieferer in Stockach betreuen?",
    "faq_lokal_antwort_1": "Ja – B2B und Industrie sind eine unserer Kernkompetenzen. Wir kennen die Anforderungen von Zulieferbetrieben: Qualitätszertifikate, technische Dokumentation, nüchterne aber professionelle Kommunikation.",
    "faq_lokal_frage_2": "Wir haben kein großes Marketingbudget – lohnt sich eine Zusammenarbeit trotzdem?",
    "faq_lokal_antwort_2": "Absolut. Wir arbeiten mit Mittelständlern jeder Größe und entwickeln Pakete, die zum Budget passen. Ein professioneller Webauftritt muss nicht teuer sein – er muss nur gut sein.",
    "cta_schlusstext": "Persönliche Beratung für Ihr Unternehmen in Stockach – direkt, unkompliziert, ohne Agentur-Overhead.",
    "cta_subtext": "Für Industriebetriebe, Handwerker und Händler in Stockach und dem Hegau.",
    "schema_area_served": "Stockach, Hegau, Singen, Radolfzell, Überlingen",
    "meta_title": "Werbeagentur Stockach | Webdesign, SEO & Marketing – x mind",
    "meta_desc": "x mind – Ihre Werbeagentur für Stockach und den Hegau. Webdesign, SEO & Marketing für Industrie, Handwerk und Handel. Persönlich & regional. Jetzt anfragen."
  }
]
```

**WICHTIG:** Die restlichen 29 Städte (Tuttlingen, Friedrichshafen, Villingen-Schwenningen, Freiburg, Offenburg, Rottweil, Tübingen, Donaueschingen, Pfullendorf, Meersburg, Bad Dürrheim, Markdorf, Schiltach, Gengenbach, Hausach, Triberg, Kehl, Lahr, Oberkirch, Spaichingen, Rottenburg, Schaffhausen, St. Gallen, Zürich, Winterthur, Frauenfeld, Basel, Bregenz, Luzern) müssen mit denselben Feldern vollständig befüllt werden. Generiere für jede Stadt alle Felder mit stadtspezifischen, realistischen Inhalten – gleiche Qualität und Tiefe wie die 5 Beispielstädte oben.

---

## PHASE 4 – REDIRECT-GENERATOR

Erstelle `/agentur/generate_redirects.py`

```python
#!/usr/bin/env python3
"""Generiert .htaccess-Redirects für alle alten Themen-URLs → neue Stadtseiten"""

import json
from pathlib import Path

DATA_PATH = Path("stadtdaten.json")

THEMEN = [
    ("webdesign",          "webdesign"),
    ("werbeagentur",       "werbeagentur"),
    ("seo-agentur",        "seo-agentur"),
    ("webagentur",         "webagentur"),
    ("marketing-agentur",  "marketing-agentur"),
    ("corporate-design",   "corporate-design"),
    ("werbefotografie",    "werbefotografie"),
    ("drohnenfotografie",  "drohnenfotografie"),
]

staedte = json.loads(DATA_PATH.read_text(encoding="utf-8"))

htaccess_lines = ["# x-mind Pillarsite Redirects – automatisch generiert", "# Alte Themen-Stadtseiten → Neue Stadtseiten", ""]
doc_lines = ["x-mind Redirect-Dokumentation", "=" * 50, ""]

count = 0
for stadt in staedte:
    slug = stadt["slug"]
    ziel = f"/agentur/{slug}/"
    for ordner, prefix in THEMEN:
        quelle = f"/{ordner}/{prefix}-{slug}/"
        htaccess_lines.append(f"Redirect 301 {quelle} {ziel}")
        doc_lines.append(f"{quelle}  →  {ziel}")
        count += 1

Path("redirects.htaccess").write_text("\n".join(htaccess_lines), encoding="utf-8")
Path("redirects_dokumentation.txt").write_text("\n".join(doc_lines), encoding="utf-8")
print(f"✓ {count} Redirects generiert → redirects.htaccess")
```

---

## PHASE 5 – UNIQUENESS-AUDIT SCRIPT

Erstelle `/agentur/audit_uniqueness.py`

Dieses Script prüft nach der Generierung automatisch die Content-Uniqueness:

```python
#!/usr/bin/env python3
"""
Prüft generierte Stadtseiten auf:
1. Verbleibende {{PLATZHALTER}}
2. Doppelte <title>-Tags
3. Doppelte Meta-Descriptions
4. Doppelte H1-Tags
5. Anteil stadtspezifischer Content-Blöcke
"""

import os
import re
from pathlib import Path
from collections import Counter

AGENTUR_DIR = Path(".")
staedte_dirs = [d for d in AGENTUR_DIR.iterdir() if d.is_dir() and not d.name.startswith("_")]

titles = []
descs = []
h1s = []
fehler = []

for stadt_dir in sorted(staedte_dirs):
    index = stadt_dir / "index.html"
    if not index.exists():
        fehler.append(f"FEHLT: {stadt_dir.name}/index.html")
        continue

    html = index.read_text(encoding="utf-8")

    # Platzhalter-Check
    remaining = re.findall(r'\{\{[A-Z_]+\}\}', html)
    if remaining:
        fehler.append(f"PLATZHALTER in {stadt_dir.name}: {set(remaining)}")

    # Title
    title_match = re.search(r'<title>(.*?)</title>', html)
    titles.append(title_match.group(1) if title_match else "KEIN TITLE")

    # Meta Description
    desc_match = re.search(r'<meta name="description" content="(.*?)"', html)
    descs.append(desc_match.group(1) if desc_match else "KEINE DESC")

    # H1
    h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', html, re.DOTALL)
    h1s.append(re.sub(r'<[^>]+>', '', h1_match.group(1)).strip() if h1_match else "KEIN H1")

print("=" * 50)
print("UNIQUENESS-AUDIT BERICHT")
print("=" * 50)

# Duplikate
title_dupes = [t for t, c in Counter(titles).items() if c > 1]
desc_dupes = [d for d, c in Counter(descs).items() if c > 1]
h1_dupes = [h for h, c in Counter(h1s).items() if c > 1]

print(f"\n✓ Seiten geprüft: {len(staedte_dirs)}")
print(f"✓ Unique Titles: {len(set(titles))}/{len(titles)}")
print(f"✓ Unique Descriptions: {len(set(descs))}/{len(descs)}")
print(f"✓ Unique H1s: {len(set(h1s))}/{len(h1s)}")

if title_dupes:
    print(f"\n⚠ DOPPELTE TITLES: {title_dupes}")
if desc_dupes:
    print(f"⚠ DOPPELTE DESCRIPTIONS: {len(desc_dupes)} Stück")
if h1_dupes:
    print(f"⚠ DOPPELTE H1s: {h1_dupes}")
if fehler:
    print(f"\n✗ FEHLER:\n" + "\n".join(fehler))
else:
    print("\n✓ Keine Fehler gefunden")
```

---

## AUSFÜHRUNGSREIHENFOLGE

```bash
# Im Verzeichnis /agentur/ ausführen:

# 1. Template erstellen (Phase 1) – visuell abnehmen vor Phase 2
# 2. Stadtdaten anlegen (Phase 3)
# 3. Generator schreiben (Phase 2)
# 4. Stadtseiten generieren:
python generate_stadtseiten.py

# 5. Redirects generieren:
python generate_redirects.py

# 6. Uniqueness-Audit:
python audit_uniqueness.py

# 7. Redirects in .htaccess einfügen (ans ENDE der bestehenden .htaccess)
```

---

## WICHTIGE HINWEISE FÜR CLAUDE CODE

- Template visuell identisch zu `/webdesign/webdesign-singen/index.html` – diese Seite als Referenz nutzen
- `.intro-lokal` CSS-Klasse: leicht kursiv oder farblich akzentuiert, damit der stadtspezifische Satz erkennbar ist
- Keine externen JS/CSS-Abhängigkeiten außer Google Fonts
- Python 3.x, nur Stdlib (json, os, re, pathlib, collections)
- Canonical immer mit trailing slash
- Schema.org JSON-LD im `<head>`, nicht am Ende der Seite
- Die `.htaccess`-Redirects ans **Ende** der bestehenden Datei – nicht überschreiben
- Für die 29 restlichen Städte in Phase 3: gleiche Qualität und Tiefe wie die 5 Beispielstädte
