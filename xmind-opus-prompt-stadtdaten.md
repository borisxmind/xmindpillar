# Opus Prompt: x-mind Stadtdaten JSON – Vollständige Ausarbeitung
# Einsatz: In Claude Opus 4.6 – zusammen mit xmind-claude-code-prompt-v2.md hochladen

---

## DEINE AUFGABE

Du bist ein SEO- und Copywriting-Experte für regionale Werbeagenturen im deutschsprachigen Raum.

Die beigefügte Datei `xmind-claude-code-prompt-v2.md` enthält das komplette Projekt-Setup
für die Werbeagentur **x mind** aus Singen am Bodensee. Lies sie vollständig.

Deine konkrete Aufgabe: **Erstelle die vollständige `stadtdaten.json`** mit allen 34 Städten.

Die ersten 5 Städte (Singen, Konstanz, Radolfzell, Überlingen, Stockach) sind in der v2.md
bereits als Referenz-Qualität ausgearbeitet. Diese 5 übernimmst du 1:1.

**Du ergänzt die fehlenden 29 Städte** in exakt gleicher Tiefe und Qualität.

---

## DIE 29 FEHLENDEN STÄDTE

```
Tuttlingen, Friedrichshafen, Villingen-Schwenningen, Freiburg im Breisgau,
Offenburg, Rottweil, Tübingen, Donaueschingen, Pfullendorf, Meersburg,
Bad Dürrheim, Markdorf, Schiltach, Gengenbach, Hausach, Triberg,
Kehl, Lahr/Schwarzwald, Oberkirch, Spaichingen, Rottenburg am Neckar,
Schaffhausen (CH), St. Gallen (CH), Zürich (CH), Winterthur (CH),
Frauenfeld (CH), Basel (CH), Bregenz (AT), Luzern (CH)
```

---

## QUALITÄTSANFORDERUNGEN – KRITISCH

### 1. Kein generisches Füllmaterial
Jede Stadt bekommt **echte lokale Insights**. Nicht:
> ❌ "Tuttlingen ist eine mittelgroße Stadt in Baden-Württemberg mit einer vielfältigen Wirtschaft."

Sondern:
> ✅ "Tuttlingen ist die Welthauptstadt der Medizintechnik – über 400 Unternehmen der Branche, darunter Karl Storz und Aesculap, sind hier ansässig. Die hochpräzise Industrie exportiert weltweit und hat einen enormen Bedarf an professioneller B2B-Kommunikation."

### 2. Die 8 Leistungs-Intro-Sätze müssen sich wirklich unterscheiden
Nicht nur der Stadtname wechseln. Jeder Satz muss auf die **spezifische Branche, Marktsituation oder lokale Besonderheit** der Stadt eingehen.

Schlecht:
> ❌ `webdesign_intro`: "In Tuttlingen entscheiden Kunden online, ob ein Anbieter ernst genommen wird."

Gut:
> ✅ `webdesign_intro`: "Medizintechnikunternehmen in Tuttlingen werden von internationalen Einkäufern und OEM-Partnern online bewertet – eine englischsprachige, technisch präzise Website ist hier kein Luxus."

### 3. Tonalität je nach Stadttyp anpassen

| Stadttyp | Tonalität |
|----------|-----------|
| Industriestadt (Tuttlingen, VS, Stockach) | Sachlich, B2B, technisch |
| Universitätsstadt (Konstanz, Tübingen, Freiburg) | Modern, Fachkräfte, Start-up-affin |
| Tourismusstadt (Überlingen, Triberg, Meersburg, Luzern) | Emotional, saisonal, Erlebnisqualität |
| Schweizer Städte (Zürich, Basel, Schaffhausen) | International, CHF-Markt, höhere Kaufkraft |
| Kleinstadt (Hausach, Triberg, Gengenbach) | Persönlich, Handwerk, lokale Verwurzelung |
| Grenzstadt (Kehl, Singen, Schaffhausen) | Grenzüberschreitend, bilingual, zwei Märkte |

### 4. Schweizer und österreichische Städte: Besonderheiten beachten
- `land_label`: "(CH)" bzw. "(AT)"
- `schema_country`: "CH" bzw. "AT"
- FAQ-Fragen auf Schweizer/österreichischen Markt eingehen (CHF, MWST, Swissness etc.)
- `lokale_herausforderung` und `branchen_fokus_text` müssen den anderenMarkt reflektieren
- Für Zürich, Basel, St. Gallen: höheres Preisniveau, internationale Ausrichtung erwähnen

### 5. `faq_lokal_frage_1+2` – stadttypisch, nicht generisch
Die FAQ-Fragen sollen sich so lesen, als hätte ein echter Unternehmer aus dieser Stadt sie gestellt.

Gut für Zürich:
> "Wir sind ein Schweizer KMU – könnt ihr uns trotz eurem Sitz in Deutschland betreuen?"

Gut für Triberg:
> "Wir sind ein kleiner Souvenirshop – lohnt sich professionelles Webdesign für uns überhaupt?"

Gut für Freiburg:
> "Wir sprechen vor allem die Uni-Zielgruppe an – habt ihr Erfahrung mit jungen Zielgruppen?"

### 6. `einzugsgebiet_km` realistisch setzen
- Kleinstadt (< 10.000 EW): 15
- Mittelstadt (10.000–50.000): 20–25
- Großstadt (> 50.000): 30–40
- Metropole (Zürich, Freiburg, Basel): 50

---

## AUSGABE-FORMAT

Gib **nur die vollständige JSON-Datei** aus – alle 34 Städte, die 5 bereits ausgearbeiteten
(Singen, Konstanz, Radolfzell, Überlingen, Stockach) plus die 29 neuen.

Kein erklärender Text davor oder danach. Kein Markdown-Codeblock-Wrapper.
Nur valides JSON, direkt beginnend mit `[` und endend mit `]`.

Das JSON muss direkt als `stadtdaten.json` gespeichert werden können.

---

## PFLICHTFELDER PRO STADT (alle müssen befüllt sein)

```json
{
  "stadt": "",
  "slug": "",
  "genitiv": "",
  "region": "",
  "bundesland": "",
  "land_label": "",
  "schema_country": "",
  "einwohner": "",
  "wahrzeichen": "",
  "einzugsgebiet_km": "",
  "nachbarstaedte_liste": "",
  "branchen": "",
  "branchen_dominant": "",
  "wirtschaft": "",
  "branchen_fokus_text": "",
  "lokale_herausforderung": "",
  "geo_kontext": "",
  "webdesign_intro": "",
  "seo_intro": "",
  "corporate_intro": "",
  "marketing_intro": "",
  "webagentur_intro": "",
  "foto_intro": "",
  "drohnen_intro": "",
  "fullservice_intro": "",
  "faq_lokal_frage_1": "",
  "faq_lokal_antwort_1": "",
  "faq_lokal_frage_2": "",
  "faq_lokal_antwort_2": "",
  "cta_schlusstext": "",
  "cta_subtext": "",
  "schema_area_served": "",
  "meta_title": "",
  "meta_desc": ""
}
```

**meta_desc**: max. 155 Zeichen, immer mit „Jetzt anfragen" oder „Jetzt Erstgespräch" am Ende.
**meta_title**: Format immer `Werbeagentur {Stadt} | Webdesign, SEO & Marketing – x mind`

---

## SLUG-REFERENZ (exakt diese Slugs verwenden)

```
tuttlingen, friedrichshafen, villingen-schwenningen, freiburg-im-breisgau,
offenburg, rottweil, tuebingen, donaueschingen, pfullendorf, meersburg,
bad-duerrheim, markdorf, schiltach, gengenbach, hausach, triberg,
kehl, lahr-schwarzwald, oberkirch, spaichingen, rottenburg-am-neckar,
schaffhausen, st-gallen, zuerich, winterthur, frauenfeld, basel,
bregenz, luzern
```

---

## WICHTIG: NACH DER AUSGABE

Prüfe selbst bevor du ausgibst:
- Ist das JSON valide? (keine trailing commas, korrekte Anführungszeichen)
- Sind alle 34 Städte enthalten?
- Haben alle Städte exakt dieselben Felder?
- Sind alle meta_desc unter 155 Zeichen?
- Sind die Schweizer/österreichischen Städte korrekt mit land_label und schema_country?
