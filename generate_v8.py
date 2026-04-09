#!/usr/bin/env python3
"""
X-MIND SEO Landing Page Generator v8
═══════════════════════════════════════
✓ Vollständig eigenständig – kein externes template.html erforderlich
✓ Schema.org: LocalBusiness + FAQPage + BreadcrumbList + AggregateRating
✓ Open Graph + Twitter Cards
✓ hreflang für Schaffhausen (CH)
✓ robots.txt + Sitemap Index
✓ Marktbande in "Weitere Leistungen"
✓ Copyright 2026 + Alt-Texte
✓ llms.txt
✓ 29 Städte × 6 Themes = 180 Seiten total (v6)
"""
import os, json, html as htmllib

# ══════════════════════════════════════════════════════════════════════════════
# THEME-DATEN (alle Inhalte aus dem JS-Template extrahiert und in Python)
# ══════════════════════════════════════════════════════════════════════════════
THEMES = {
  'webdesign': {
    'title': 'Webdesign', 'keyword': 'Webdesign',
    'metaTitle': 'Webdesign {CITY} – Professionelle Websites | X mind Werbeagentur',
    'metaDesc':  'Professionelles Webdesign in {CITY}. WordPress & Joomla-Experten mit 18 Jahren Erfahrung. Individuell, mobil, SEO-optimiert. Kostenlose Beratung. ✓ Lokal ✓ Zuverlässig',
    'heroLabel': 'Webdesign {CITY}',
    'heroTitle': 'Professionelles Webdesign in {CITY}.',
    'heroSub':   'Individuelle Websites für Handwerk, Mittelstand und regionale Unternehmen – mobil, schnell, suchmaschinenoptimiert und pünktlich geliefert.',
    'cards': [
      {'icon':'⚡','title':'Schnell & mobil',      'text':'Alle Seiten für Smartphones optimiert, unter 2 Sekunden Ladezeit – Google honoriert das mit besseren Rankings.'},
      {'icon':'🎯','title':'Conversion First',     'text':'Kein reines Schaufenster. Jedes Element hat einen Zweck: Besucher zu Anfragen oder Käufern machen.'},
      {'icon':'🔧','title':'WordPress & Joomla',   'text':'Sie pflegen Inhalte selbst – ohne Programmierkenntnisse. Wir zeigen Ihnen alles im persönlichen Briefing.'},
      {'icon':'📈','title':'SEO-Grundoptimierung', 'text':'Jede Website verlässt unser Haus mit sauberem Code, optimierten Meta-Daten und Page-Speed-Check.'},
    ],
    'process': [
      {'title':'Strategie – verstehen, was wirkt',  'text':'Gemeinsam analysieren wir Ihre Ziele, Zielgruppen und Marktumfeld. Kein Bullshit-Bingo, sondern echte Klarheit.'},
      {'title':'Kreation – Ideen, die verkaufen',   'text':'Wir entwickeln ein individuelles Design, das zu Ihrem Unternehmen passt – kein Baukasten, kein generisches Template.'},
      {'title':'Wirkung – Erfolg messbar machen',   'text':'Sauberer Code, getestete Funktionen, pünktlicher Launch – und persönliche Betreuung danach.'},
    ],
    'ctaTitle': 'Ihr Webdesign-Projekt in {CITY} – reden wir Klartext.',
    'cta':      'Kostenlose Website-Beratung',
    'faq': [
      ('Was kostet eine professionelle Website?',   'Einfache Business-Websites starten ab ca. 1.500 €. Beim ersten Gespräch erhalten Sie eine ehrliche Einschätzung – ohne versteckte Kosten.'),
      ('Wie lange dauert die Erstellung?',          'Einfache Projekte sind in 4–6 Wochen live. Für größere Webauftritte planen wir gemeinsam einen realistischen Zeitplan.'),
      ('Kann ich die Seite danach selbst pflegen?', 'Ja, das ist unser Ziel. Wir bauen auf WordPress oder Joomla und zeigen Ihnen alles Notwendige im persönlichen Briefing.'),
      ('Betreut ihr auch bestehende Websites?',     'Sehr gerne. Wir übernehmen Pflege, Updates und Optimierung – egal von wem die Seite ursprünglich erstellt wurde.'),
    ],
  },
  'werbeagentur': {
    'title': 'Werbeagentur', 'keyword': 'Werbeagentur',
    'metaTitle': 'Werbeagentur {CITY} – Full-Service für Mittelstand | X mind',
    'metaDesc':  'Werbeagentur in {CITY} – Webdesign, Print, SEO & Kampagnen aus einer Hand. 18 Jahre Erfahrung. Persönlich, lokal, zuverlässig. ✓ Mittelstand ✓ Handwerk',
    'heroLabel': 'Werbeagentur {CITY}',
    'heroTitle': 'Werbeagentur für den Mittelstand in {CITY}.',
    'heroSub':   'Full-Service-Kommunikation für Handwerk und Mittelstand – Webdesign, Print, Kampagnen und digitales Marketing, persönlich betreut seit 18 Jahren.',
    'cards': [
      {'icon':'🏆','title':'18 Jahre Erfahrung',  'text':'Gegründet 2007. Wir haben Trends und Wandel erlebt – und wissen genau, was für den Mittelstand wirklich funktioniert.'},
      {'icon':'🤝','title':'Ein Ansprechpartner', 'text':'Kein Callcenter. Sie haben einen festen Ansprechpartner, der Ihr Unternehmen und Ihre Branche kennt.'},
      {'icon':'🖨️','title':'Print & Digital',     'text':'Von der Website bis zum Flyer, von Instagram bis zum Geschäftsbericht – alles aus einer Hand, aus einem Guss.'},
      {'icon':'📊','title':'Messbare Ergebnisse', 'text':'Jede Maßnahme wird geplant, umgesetzt, gemessen und bei Bedarf optimiert – kein Bauchgefühl.'},
    ],
    'process': [
      {'title':'Strategie – kennenlernen & verstehen', 'text':'Erstes Gespräch ohne Agenda: Wir hören zu, fragen nach und verstehen Ihr Unternehmen und Ihre Ziele.'},
      {'title':'Kreation – Ideen, die verkaufen',      'text':'Auf Basis Ihrer Ziele entsteht ein realistischer Plan – mit Budget, Zeitplan und klaren Erfolgskriterien.'},
      {'title':'Wirkung – umsetzen & optimieren',      'text':'Wir produzieren, schalten, messen und verbessern. Kontinuierlich, transparent, als echter Partner.'},
    ],
    'ctaTitle': 'Ihre Werbeagentur in {CITY} – reden wir Klartext.',
    'cta':      'Erstes Gespräch anfragen',
    'faq': [
      ('Arbeitet ihr auch mit kleinen Unternehmen?', 'Absolut. Viele Kunden sind Handwerksbetriebe und kleine Mittelständler. Wir denken in Ihrer Budgetgröße.'),
      ('Bietet ihr auch Einzelleistungen an?',       'Ja. Ob nur ein Flyer oder komplettes Rebranding – wir sind flexibel und schnüren keine Zwangspakete.'),
      ('Wie weit ist euer Einzugsgebiet?',           'Unser Herz schlägt für {CITY} und den Bodenseeraum – aber wir betreuen Kunden von Flensburg bis München.'),
      ('Habt ihr Erfahrung in meiner Branche?',      'In 18 Jahren haben wir Handwerk, Bau, Industrie, Gastronomie, Immobilien und Einzelhandel betreut.'),
    ],
  },
  'seo': {
    'title': 'SEO Agentur', 'keyword': 'SEO Agentur',
    'metaTitle': 'SEO Agentur {CITY} – Suchmaschinenoptimierung | X mind',
    'metaDesc':  'SEO Agentur in {CITY} – lokale & regionale Suchmaschinenoptimierung für den Mittelstand. Transparente Berichte, messbare Rankings. ✓ Ohne leere Versprechen',
    'heroLabel': 'SEO Agentur {CITY}',
    'heroTitle': 'Gefunden werden in {CITY} – nachhaltig und messbar.',
    'heroSub':   'Lokale und regionale Suchmaschinenoptimierung für Unternehmen in {CITY}. Messbare Rankings – ohne leere Versprechen, ohne Vertragsfallen.',
    'cards': [
      {'icon':'🔍','title':'Lokales SEO',            'text':'Google Maps, Local Pack, Bewertungsmanagement – Sie werden in {CITY} als erste gefunden, wenn es darauf ankommt.'},
      {'icon':'📝','title':'Content-Strategie',       'text':'Texte, die Google versteht und Menschen gerne lesen. Keine Keyword-Salate – echte Inhalte, die konvertieren.'},
      {'icon':'⚙️','title':'Technisches SEO',         'text':'Core Web Vitals, strukturierte Daten, saubere URLs – die Basis muss stimmen, bevor Content wirkt.'},
      {'icon':'📊','title':'Transparentes Reporting', 'text':'Monatliche Berichte mit Rankings, Traffic und Conversions. Sie sehen genau, was Ihr Budget bewirkt.'},
    ],
    'process': [
      {'title':'Strategie – SEO-Audit & Analyse',   'text':'Wir analysieren Ihre Website: technische Fehler, Content-Lücken, Backlink-Profil und Mitbewerber.'},
      {'title':'Kreation – Maßnahmenplan & Content', 'text':'Priorisierte Roadmap mit Quick Wins und langfristigen Hebeln. Realistisch, terminiert, budgetiert.'},
      {'title':'Wirkung – Umsetzung & Monitoring',  'text':'Wir optimieren kontinuierlich, berichten monatlich und passen die Strategie an Google-Updates an.'},
    ],
    'ctaTitle': 'Ihr SEO-Projekt in {CITY} – reden wir Klartext.',
    'cta':      'Kostenlosen SEO-Check anfragen',
    'faq': [
      ('Wann sehe ich erste SEO-Ergebnisse?',  'Ehrlich: erste Verbesserungen nach 4–8 Wochen, spürbare Rankings nach 3–6 Monaten. Wer sofortige Top-Rankings verspricht, lügt.'),
      ('Was kostet SEO monatlich?',            'Lokales SEO ab ca. 300–500 €/Monat. Regionale Kampagnen ab 700–1.500 €. Konkrete Zahlen im ersten Gespräch.'),
      ('Wie lang sind die Vertragslaufzeiten?','Wir arbeiten ohne lange Mindestlaufzeiten. SEO braucht Zeit – aber kein Zwangskorsett.'),
      ('Macht ihr auch Google Ads (SEA)?',     'Ja. SEO und SEA ergänzen sich ideal. Wir betreuen beides und stimmen die Strategien aufeinander ab.'),
    ],
  },
  'webagentur': {
    'title': 'Webagentur', 'keyword': 'Webagentur',
    'metaTitle': 'Webagentur {CITY} – WordPress & Joomla | X mind',
    'metaDesc':  'Webagentur in {CITY} – WordPress, Joomla, individuelle Webentwicklung für Mittelstand & Handwerk. Persönlich, zuverlässig, lokal. ✓',
    'heroLabel': 'Webagentur {CITY}',
    'heroTitle': 'Ihre Webagentur in {CITY} – digital, persönlich, verlässlich.',
    'heroSub':   'Von der einfachen Business-Website bis zur komplexen Web-Applikation – wir entwickeln digitale Lösungen, die Ihren Geschäftsalltag konkret verbessern.',
    'cards': [
      {'icon':'💻','title':'WordPress & Joomla',  'text':'Die mächtigsten CMS-Systeme, richtig eingesetzt. Wir wählen das System, das zu Ihren Anforderungen passt.'},
      {'icon':'🔗','title':'Schnittstellen & APIs','text':'Anbindung an Warenwirtschaft, CRM oder Buchungssysteme – wir verbinden, was zusammengehört.'},
      {'icon':'🛡️','title':'Wartung & Sicherheit', 'text':'Updates, Backups, Security-Monitoring – Ihre Website ist in sicheren Händen, auch nach dem Launch.'},
      {'icon':'🚀','title':'Performance & Speed',  'text':'Caching, CDN, Bildoptimierung – wir holen das Maximum heraus, damit Besucher nicht abspringen.'},
    ],
    'process': [
      {'title':'Strategie – Anforderungsanalyse',      'text':'Was soll die Website können? Wir hören zu und übersetzen Ihre Wünsche in technische Anforderungen.'},
      {'title':'Kreation – Architektur & Entwicklung', 'text':'Saubere Code-Basis, durchdachte Struktur, modularer Aufbau – damit Ihre Website mitwachsen kann.'},
      {'title':'Wirkung – Test, Launch & Support',     'text':'Ausführliche Tests auf allen Geräten, sauberer Launch und persönlicher Support danach.'},
    ],
    'ctaTitle': 'Ihr Webprojekt in {CITY} – reden wir Klartext.',
    'cta':      'Webprojekt besprechen',
    'faq': [
      ('WordPress oder Joomla – was ist besser?',    'Kommt drauf an. WordPress ideal für Content-schwere Sites, Joomla bei komplexen Nutzerrollen. Wir empfehlen, was passt.'),
      ('Könnt ihr bestehende Websites übernehmen?',  'Ja. Wir migrieren, modernisieren und pflegen bestehende Websites – egal von welchem System.'),
      ('Was kostet ein Website-Relaunch?',           'Ein typischer Relaunch liegt zwischen 2.000 und 8.000 € – je nach Umfang und Funktionen.'),
      ('Bietet ihr auch Schulungen an?',             'Ja. Jedes Projekt endet mit einer persönlichen Einweisung. Darüber hinaus Einzel- und Gruppentrainings.'),
    ],
  },
  'marketing': {
    'title': 'Marketing Agentur', 'keyword': 'Marketing Agentur',
    'metaTitle': 'Marketing Agentur {CITY} – Strategie & Umsetzung | X mind',
    'metaDesc':  'Marketing Agentur in {CITY} für Mittelstand & Handwerk. Strategie, Social Media, SEO, Print & Kampagnen. 18 Jahre Erfahrung. X mind ✓',
    'heroLabel': 'Marketing Agentur {CITY}',
    'heroTitle': 'Marketing, das Ihr Budget wirklich arbeiten lässt – in {CITY}.',
    'heroSub':   'Strategisches und operatives Marketing für den Mittelstand. Von der Positionierung bis zur laufenden Kampagne – aus einer Hand.',
    'cards': [
      {'icon':'🧭','title':'Strategie first',  'text':'Kein blinder Aktionismus. Wir entwickeln eine klare Positionierung und einen realistischen Plan.'},
      {'icon':'📱','title':'Social Media',     'text':'Facebook, Instagram, LinkedIn – wir produzieren Inhalte und betreuen Ihre Kanäle professionell.'},
      {'icon':'🔍','title':'SEO & SEA',        'text':'Organische Sichtbarkeit durch SEO, bezahlte Reichweite durch Google Ads – strategisch abgestimmt.'},
      {'icon':'📧','title':'E-Mail Marketing', 'text':'Newsletter, Automationen, Kampagnen – E-Mail als direkter und effizienter Kommunikationskanal.'},
    ],
    'process': [
      {'title':'Strategie – Status quo analysieren',  'text':'Wo stehen Sie? Welche Maßnahmen laufen? Wo liegen ungenutztes Potenzial und kritische Lücken?'},
      {'title':'Kreation – Marketingplan entwickeln', 'text':'Priorisierter Maßnahmenplan mit Budget, Kanal-Mix und Zeitplan – realistisch und umsetzbar.'},
      {'title':'Wirkung – umsetzen & skalieren',      'text':'Start mit den wirkungsvollsten Maßnahmen, laufende Optimierung, Skalierung was funktioniert.'},
    ],
    'ctaTitle': 'Ihr Marketing in {CITY} – reden wir Klartext.',
    'cta':      'Marketing-Strategie anfragen',
    'faq': [
      ('Für welche Unternehmensgröße seid ihr geeignet?', 'Wir sind auf Handwerk, KMU und regionalen Mittelstand spezialisiert – bodenständige Unternehmen mit Wachstumszielen.'),
      ('Was kostet laufendes Marketing?',                 'Marketing-Retainer beginnen ab ca. 500 €/Monat. Für umfangreichere Pakete erhalten Sie ein individuelles Angebot.'),
      ('Können wir einzelne Kanäle beauftragen?',         'Ja. Viele Kunden starten mit einem Kanal – z. B. Instagram oder Google Ads – und erweitern schrittweise.'),
      ('Wie messen wir den Erfolg?',                      'Über klar definierte KPIs: Reichweite, Leads, Anfragen, Rankings – monatliche Reports sind Standard.'),
    ],
  },
  'corporate-design': {
    'title': 'Corporate Design', 'keyword': 'Corporate Design',
    'metaTitle': 'Corporate Design {CITY} – Logo & Markenidentität | X mind',
    'metaDesc':  'Corporate Design in {CITY} – Logo, CI, Geschäftsausstattung für den Mittelstand. Professionell, zeitlos, wirkungsvoll. X mind Werbeagentur ✓',
    'heroLabel': 'Corporate Design {CITY}',
    'heroTitle': 'Ihre Marke in {CITY} – wiedererkennbar und unvergesslich.',
    'heroSub':   'Ein starkes Corporate Design ist die Grundlage für jede erfolgreiche Kommunikation. Wir entwickeln visuelle Identitäten, die Bestand haben.',
    'cards': [
      {'icon':'🎨','title':'Logo & Markenzeichen', 'text':'Zeitlose Logos, die in allen Größen und Medien funktionieren – digital, im Druck, auf Fahrzeugen.'},
      {'icon':'📐','title':'Corporate Identity',   'text':'Farben, Typografie, Bildwelt, Tonalität – ein konsistentes System, das Ihre Marke erkennbar macht.'},
      {'icon':'📦','title':'Geschäftsausstattung', 'text':'Briefpapier, Visitenkarten, Umschläge – alles druckfertig und CI-konform, damit der erste Eindruck sitzt.'},
      {'icon':'📋','title':'Brand Guidelines',     'text':'Ein verbindlicher Styleguide für Ihr Team und externe Partner – für konsistenten Markenauftritt.'},
    ],
    'process': [
      {'title':'Strategie – Markenanalyse',    'text':'Wer sind Sie? Was unterscheidet Sie vom Mitbewerber? Was soll Ihre Marke ausstrahlen?'},
      {'title':'Kreation – Konzept & Design',  'text':'Mehrere Designrichtungen, fundierte Präsentation, ehrliches Feedback – bis es wirklich passt.'},
      {'title':'Wirkung – Rollout & Übergabe', 'text':'Alle Dateiformate, druckfertig und digital – plus Brand Guidelines für konsistente Anwendung.'},
    ],
    'ctaTitle': 'Ihr Corporate Design in {CITY} – reden wir Klartext.',
    'cta':      'Markenentwicklung anfragen',
    'faq': [
      ('Was kostet ein professionelles Logo?',              'Einfache Logos ab ca. 500 €. Vollständiges Corporate Design mit Styleguide typischerweise 2.000–5.000 €.'),
      ('Wie lange dauert ein CI-Projekt?',                  'Logo mit Geschäftsausstattung: 3–5 Wochen. Umfangreichere CI-Projekte 6–12 Wochen. Termine werden gehalten.'),
      ('Wir haben schon ein Logo – kann man es modernisieren?', 'Ja, Logo-Refresh ist häufig sinnvoller als Neuanfang. Wir analysieren und empfehlen den richtigen Schritt.'),
      ('Was bekomme ich als Dateien?',                      'AI/EPS (vektoriell), SVG, PNG mit Transparenz, JPG – in verschiedenen Farbvarianten (RGB, CMYK, S/W).'),
    ],
  },
  'drohnenfotografie': {
    'title': 'Drohnenfotografie', 'keyword': 'Drohnenfotograf',
    'metaTitle': 'Drohnenfotograf {CITY} – Luftaufnahmen, Luftbilder & Drohnenfilm buchen | X mind',
    'metaDesc':  'Drohnenfotograf & Drohnenservice in {CITY} – Luftaufnahmen und Luftbilder für Immobilien, Baustellen, Gewerbe, Industrie und Events. Professioneller Drohnenpilot buchen – zertifiziert, lizenziert, deutschlandweit. X mind.',
    'heroLabel': 'Drohnenfotograf & Drohnenservice {CITY} – Luftaufnahmen, Luftbilder, Drohnenfilm',
    'heroTitle': 'Luftaufnahmen auf Profi-Niveau – überall in Deutschland.',
    'heroSub':   'Drohnenaufnahmen und Luftbilder in {CITY} – Drohnenfotografie für Immobilien, Baustellen, Gewerbe, Industrie, Kommunen und Events. Professionellen Drohnenpiloten buchen: zertifiziert, lizenziert, behördlich genehmigt.',
    'cards': [
      {'icon':'🏠','title':'Immobilien & Baustellen',   'text':'Drohnenaufnahmen für Immobilien: Luftbilder vom Haus, Grundstück, Neubau und Bestandsobjekt. Baudokumentation und Baufortschritt-Dokumentation per Drohne – ideal für Exposés, Makler und Bauträger.'},
      {'icon':'🎬','title':'Drohnenvideo & Imagefilm',    'text':'Drohnenvideo erstellen lassen: Imagefilme, Eventdokumentation, Social-Media-Content und Hotelfotografie aus der Luft – cineastisch, stabil, bis 4K. Drohnenpiloten mit Fotografenmeister-Ausbildung.'},
      {'icon':'🏙️','title':'Gewerbe, Industrie & Kommunen','text':'Luftaufnahmen für Gewerbeanlagen, Industrieareale und Kommunen: Drohnenaufnahmen für Unternehmen und Firmen, Solaranlagen-Übersichten, Stadtmarketing und Tourismus-Luftbilder.'},
      {'icon':'✅','title':'Professionell & rechtssicher','text':'A1/A3, A2, STS-01, STS-02 und Betriebskategorie SPEZIELL (SPECIFIC) nach EU-Drohnenverordnung. Alle Genehmigungen, alle Versicherungen – wir arbeiten professionell, rechtssicher und termingenau.'},
    ],
    'process': [
      {'title':'Briefing & Flugplanung',         'text':'Wir analysieren die Location, klären alle Luftraumfreigaben und holen – wo nötig – behördliche Genehmigungen ein. Professionelle Projektierung vor jedem Einsatz.'},
      {'title':'Drohnenflug & Bildproduktion',    'text':'Professioneller Drohnenservice durch zertifizierte Berufspiloten, teils mit Fotografenmeister-Ausbildung. Luftaufnahmen und Drohnenvideo in einem Durchgang – bundesweit einsatzbereit, termingenau, sicher.'},
      {'title':'Bearbeitung & Lieferung',         'text':'Professionelle Nachbearbeitung, Export in allen Formaten. Lieferung per Downloadlink – bereit für Website, Social Media, Print und Film.'},
    ],
    'ctaTitle': 'Drohnenpiloten buchen in {CITY} – reden wir Klartext.',
    'cta':      'Kostenloses Drohnen-Briefing',
    'faq': [
      ('Was unterscheidet Sie von anderen Drohnenanbietern?',
       'Wir arbeiten professionell – mit zertifizierten Berufspiloten, teils mit Fotografenmeister-Ausbildung, und einem bundesweiten Netzwerk. Jeder Einsatz wird sorgfältig projektiert, alle behördlichen Genehmigungen werden eingeholt. Mehrere Piloten ermöglichen parallele und deutschlandweite Einsätze.'),
      ('Welche Lizenzen und Zulassungen haben Sie?',
       'Wir verfügen über EU-Drohnenführerschein A1/A3 und A2 sowie die Betriebskategorie SPEZIELL (SPECIFIC) gemäß EU-Drohnenverordnung DVO (EU) 2019/947 – inklusive behördlicher Betriebsgenehmigung. Das umfasst STS-01 (VLOS über kontrollierten Gebieten in besiedelter Umgebung, Klasse C5) und STS-02 (BVLOS mit Luftraumbeobachtern, Klasse C6). Damit sind wir für rechtskonforme UAS-Befliegungen außerhalb der offenen Kategorie zugelassen – z.B. BVLOS, über 120 m und bei erhöhtem Betriebsrisiko.'),
      ('Fliegen Sie auch außerhalb der Region {CITY}?',
       'Ja – wir sind deutschlandweit vernetzt und verfügen über mehrere Piloten, die bundesweit eingesetzt werden können. Von der Bodenseeregion bis Hamburg, von Freiburg bis Berlin. Große Projekte koordinieren wir mit regionalen Partnerpiloten.'),
      ('Für welche Anwendungen setzen Sie Drohnen ein?',
       'Immobilienfotografie und Baudokumentation, Gewerbe- und Industrieaufnahmen, Kommunal- und Stadtmarketing, Eventfotografie sowie Imagefilme und Dokumentationen. Unser Fokus liegt auf professioneller, kommunikativer Drohnenfotografie – für Bilder und Videos, die wirken.'),
      ('Was kostet ein professioneller Drohneneinsatz?',
       'Ein halbtägiger Drohneneinsatz startet ab ca. 490 € inkl. Bildbearbeitung und Nutzungsrechten. Für Filmprojekte, mehrtägige Einsätze oder bundesweite Produktionen erstellen wir ein individuelles Angebot – transparent, ohne versteckte Kosten.'),
      ('Kann ich Luftaufnahmen vom eigenen Haus oder Grundstück machen lassen?',
       'Ja – Luftbilder vom Eigenheim, Grundstück oder Neubau sind eine unserer häufigsten Anfragen. Wir klären alle notwendigen Genehmigungen, fliegen sicher und liefern hochwertige Drohnenfotografien und -videos. Typische Einsatzzwecke: Immobilienverkauf, Dokumentation von Renovierungen oder einfach zur eigenen Freude.'),
    ],
  },

  'fotografie': {
    'title': 'Werbefotografie', 'keyword': 'Fotograf',
    'metaTitle': 'Businessfotograf {CITY} – Werbefotografie, Produktfotografie & Industriefotografie | X mind',
    'metaDesc':  'Businessfotograf & Werbefotograf in {CITY} – Produktfotografie, Industriefotografie, Immobilienfotografie, Drohnenfotografie & Corporate Portraits. X mind Werbeagentur, 18 Jahre Erfahrung.',
    'heroLabel': 'Businessfotograf & Werbefotograf {CITY} – {REGION}',
    'heroTitle': 'Bilder, die Ihr Unternehmen wirklich zeigen.',
    'heroSub':   'Ihr Businessfotograf und Unternehmensfotograf in {CITY} – Produktfotografie, Industriefotografie, Immobilienfotografie und Drohnenfotografie für Handwerk, Gewerbe, Gastronomie, Dienstleister und Industrie.',
    'cards': [
      {'icon':'📦','title':'Produktfotografie',   'text':'Freisteller, Lifestyle-Produktfotos und Detailaufnahmen für Online-Shops, Kataloge, Flyer und Werbeanzeigen – sauber, verkaufsfördernd, formatgerecht geliefert.'},
      {'icon':'👤','title':'Corporate Portraits', 'text':'Mitarbeiterfotos, Teambilder und Geschäftsführer-Portraits für Website, LinkedIn und Broschüren – authentisch, professionell, verwertbar.'},
      {'icon':'🏭','title':'Industriefotografie', 'text':'Maschinen, Produktion, Baustellen, Werkstätten – Industriefotos und Reportagen für Geschäftsberichte, Messeauftritte und Unternehmenskommunikation.'},
      {'icon':'✨','title':'Werbefotografie',      'text':'Kampagnenbilder für Print und Digital – inszeniert, kreativ, auf die Zielgruppe ausgerichtet. Für Website, Social Media, Broschüren und Anzeigen.'},
      {'icon':'🏠','title':'Immobilien & Drohnen',  'text':'Neubauten, Bestandsimmobilien, renovierte Objekte und Baustellen – professionelle Immobilienfotos, Baudokumentation und Drohnenaufnahmen aus der Luft für Makler, Bauträger und Architekten.'},
    ],
    'process': [
      {'title':'Briefing & Planung',      'text':'Wir klären: Welche Bilder brauchen Sie? Für welchen Kanal? Welche Botschaft sollen die Fotos transportieren? Erst wenn das stimmt, planen wir Location, Styling und Ablauf.'},
      {'title':'Shooting & Regie',        'text':'Am Drehtag übernehmen wir Koordination, Licht und Bildführung. Sie müssen sich um nichts kümmern – außer authentisch zu sein. Das kriegen wir hin.'},
      {'title':'Bearbeitung & Lieferung', 'text':'Bildvorauswahl innerhalb von 48 Stunden. Fertige Dateien in Druck- und Webqualität innerhalb von 5–7 Werktagen – geordnet, beschriftet, sofort verwendbar.'},
    ],
    'ctaTitle': 'Ihr Fotoshooting in {CITY} – reden wir Klartext.',
    'cta':      'Kostenloses Shooting-Briefing',
    'faq': [
      ('Was kostet ein professionelles Fotoshooting?',     'Ein halbtägiges Business-Shooting startet ab ca. 490 EUR, ein ganztägiges ab ca. 890 EUR. Im Preis enthalten: Briefing, Shooting, Bildbearbeitung und Lieferung in Druckqualität.'),
      ('Wie läuft ein Fotoshooting ab?',                   'Wir beginnen mit einem Briefing-Gespräch: Einsatzzweck, Zielgruppe, Bildstil. Dann planen wir gemeinsam Location, Styling und Tagesablauf. Am Shooting-Tag übernehmen wir Regie und Koordination.'),
      ('Wann sind die Bilder fertig?',                     'Eine Bildvorauswahl erhalten Sie innerhalb von 48 Stunden. Die fertig bearbeiteten Bilder liefern wir innerhalb von 5 bis 7 Werktagen – bei dringendem Bedarf auch schneller.'),
      ('In welchen Formaten werden die Bilder geliefert?', 'Standardmäßig als hochauflösende JPEGs und WebP-Dateien. Auf Wunsch auch als TIFF oder PNG mit Freisteller. Alle Dateien werden über einen sicheren Downloadlink bereitgestellt.'),
      ('Darf ich die Fotos unbegrenzt nutzen?',            'Ja. Im Standardpaket erhalten Sie alle Nutzungsrechte für Ihre eigene Unternehmenskommunikation – Print, Digital und Social Media – ohne zeitliche Befristung.'),
      ('Für welche Branchen fotografieren Sie?',           'Wir fotografieren für alle Branchen: Handwerksbetriebe, Industrieunternehmen, Gewerbebetriebe, Gastronomiebetriebe, Dienstleister sowie Immobilien – Neubauten, Bestandsobjekte, renovierte Immobilien, Baustellen und Baudokumentation. Ergänzend bieten wir Drohnenfotografie an: Luftaufnahmen für Immobilien, Geländeübersichten und Imageclips.'),
      ('Machen Sie auch Immobilienfotografie und Baudokumentation?', 'Ja – wir fotografieren Neubauten, Bestandsimmobilien, renovierte Objekte und Baustellen. Für Makler, Bauträger und Architekten erstellen wir professionelle Immobilienfotos sowie lückenlose Baudokumentation. Auf Wunsch ergänzen wir die Bodenaufnahmen mit Drohnenfotografie für Luftperspektiven und Gesamtübersichten.'),
      ('Welche Drohnenlizenzen und Zulassungen haben Sie?', 'Wir verfügen über EU-Drohnenführerschein A1/A3 und A2 sowie die Betriebskategorie SPEZIELL (SPECIFIC) gemäß EU-Drohnenverordnung DVO (EU) 2019/947 – inklusive behördlicher Betriebsgenehmigung. Das umfasst das Europäische Standardszenario STS-01 (VLOS über kontrollierten Gebieten in besiedelter Umgebung, Klasse C5) und STS-02 (BVLOS mit Luftraumbeobachtern über dünn besiedelten Gebieten, Klasse C6). Damit sind wir für rechtskonforme UAS-Befliegungen außerhalb der offenen Kategorie zugelassen – z.B. BVLOS, über 120 m Höhe und bei erhöhtem Betriebsrisiko.'),
    ],
  },
}

# ══════════════════════════════════════════════════════════════════════════════
# FAQ-VARIANTEN (zweiter Satz pro Theme – rotiert deterministisch per Stadt)
# Verhindert 100% duplizierte FAQs über alle Stadtseiten hinweg
# ══════════════════════════════════════════════════════════════════════════════
THEMES_FAQ2 = {
  'webdesign': [
    ('Welches CMS nutzt ihr – und warum WordPress oder Joomla?',
     'Wir setzen primär auf WordPress und Joomla – beide sind ausgereift, weit verbreitet und bieten maximale Flexibilität für Pflege und Erweiterungen. Welches System besser passt, klären wir im ersten Gespräch anhand Ihrer Anforderungen.'),
    ('Kann ich meine bestehende Domain und E-Mail-Adresse behalten?',
     'Ja, in fast allen Fällen problemlos. Wir koordinieren den Umzug so, dass Ihre E-Mails und Ihre Domain durchgehend erreichbar bleiben. Ausfallzeiten vermeiden wir durch sorgfältige Planung.'),
    ('Macht ihr auch Online-Shops und E-Commerce-Websites?',
     'Ja. Wir setzen WooCommerce (WordPress) und geeignete Joomla-Lösungen ein. Von einfachen Produktpräsentationen bis zu funktionalen Online-Shops – wir beraten Sie ehrlich, welcher Aufwand für Ihre Ziele sinnvoll ist.'),
    ('Was passiert nach dem Launch – wer kümmert sich um Updates?',
     'Wir bieten Wartungsverträge an: CMS-Updates, Sicherheits-Patches, Backups und kleine Änderungen. Sie können aber auch alles selbst übernehmen – wir schulen Sie nach dem Launch persönlich.'),
  ],
  'werbeagentur': [
    ('Wie läuft das erste Kennenlernen und Briefing bei euch ab?',
     'Unkompliziert: Wir vereinbaren ein persönliches Gespräch – vor Ort, per Telefon oder per Video. Ohne Agenda, ohne Pflichtenheft. Wir hören zu, fragen nach, und Sie bekommen danach eine ehrliche Einschätzung, was sinnvoll ist – ohne Verkaufsdruck.'),
    ('Macht ihr auch Logodesign, Rebranding und Corporate Identity?',
     'Ja, das ist einer unserer Kernschwerpunkte. Von der Logoentwicklung über Farb- und Typo-Systeme bis zur vollständigen Markenidentität. Wir denken immer in Gesamtlösungen – kein Logo ohne Kontext.'),
    ('Wie schnell reagiert ihr auf Anfragen und Korrekturen?',
     'Als persönlich geführte Agentur ohne Callcenter: In der Regel innerhalb eines Werktags. Für dringende Korrekturen vor Druckterminen priorisieren wir sofort. Ihr Ansprechpartner ist direkt erreichbar – nicht über Ticket-System.'),
    ('Kann ich auch nur ein einzelnes Projekt beauftragen, ohne Rahmenvertrag?',
     'Selbstverständlich. Viele Kunden beginnen mit einem Einzelprojekt – einem Flyer, einer Anzeige, einer neuen Seite. Wenn die Zusammenarbeit passt, entstehen langfristige Partnerschaften. Druck in Richtung Dauermandat machen wir nie.'),
  ],
  'seo': [
    ('Was ist der Unterschied zwischen lokalem SEO und regionalem SEO?',
     'Lokales SEO optimiert Ihre Sichtbarkeit für konkrete Ortssuchen: „Installateur Konstanz" oder „Bäcker Singen". Regionales SEO zielt auf breitere Suchanfragen über mehrere Städte oder Landkreise hinweg. Wir kombinieren beides für maximale Abdeckung.'),
    ('Wie viele Keywords kann ich realistisch in drei Monaten verbessern?',
     'Das hängt vom Ausgangszustand Ihrer Website ab. Für technisch gut aufgestellte Seiten: 10–30 signifikante Rankingverbesserungen in drei Monaten sind realistisch. Wir nennen Ihnen konkrete Zahlen nach dem initialen SEO-Audit – keine Phantasiezahlen.'),
    ('Schadet es meiner Website, wenn ich zusätzlich Google Ads schalte?',
     'Nein – im Gegenteil. SEO und Google Ads (SEA) ergänzen sich ideal. Paid Ads liefern sofortige Sichtbarkeit, während SEO langfristig organische Rankings aufbaut. Wir koordinieren beides strategisch, damit sich beide Kanäle nicht kannibalisieren.'),
    ('Wie erkenne ich selbst, ob mein SEO-Ranking besser wird?',
     'Wir richten Google Search Console für Sie ein – kostenlos, von Google selbst. Dort sehen Sie Clicks, Impressionen und durchschnittliche Ranking-Positionen. Zusätzlich erhalten Sie von uns monatliche Berichte mit den wichtigsten KPIs, klar und ohne Fachchinesisch.'),
  ],
  'webagentur': [
    ('Was ist der Unterschied zwischen einer Webagentur und einer Werbeagentur?',
     'Eine reine Webagentur baut Websites. Eine Werbeagentur wie X mind denkt vom Ziel her: Was soll die Website für Ihr Unternehmen leisten? Daraus leiten wir Struktur, Design und Technik ab. Das Ergebnis ist nicht nur schön, sondern wirksam.'),
    ('Können wir auch unsere bestehende Website technisch von euch übernehmen lassen?',
     'Ja. Wir analysieren zuerst den Code, den Hosting-Vertrag und die CMS-Version. Wenn die Übernahme sinnvoll ist, führen wir sie durch – mitsamt Dokumentation und Übergabegespräch. Ist eine Neuentwicklung wirtschaftlicher, sagen wir das klar.'),
    ('Wie stellt ihr DSGVO-Konformität meiner Website sicher?',
     'Wir implementieren ein rechtskonformes Cookie-Consent-System, prüfen alle eingebundenen Dienste (Google Fonts, Maps, Analytics), setzen korrekte Datenschutzerklärungen auf und achten auf DSGVO-konformes Kontaktformular-Handling. Keine Standardlösung, sondern angepasst an Ihre Website.'),
    ('Was kostet laufendes Webhosting und Wartung nach dem Launch?',
     'Hosting ab ca. 15–30 €/Monat je nach Anforderungen. Wartungspakete (CMS-Updates, Backups, Sicherheits-Check) ab ca. 50 €/Monat. Im ersten Gespräch kalkulieren wir transparent, was Sie für Ihren Betrieb wirklich brauchen.'),
  ],
  'marketing': [
    ('Was ist der Unterschied zwischen Marketingstrategie und einzelnen Maßnahmen?',
     'Einzelne Maßnahmen – ein Flyer, eine Anzeige – wirken isoliert und oft kurzfristig. Eine Strategie legt fest, wen Sie wann mit welcher Botschaft erreichen wollen – und welche Kanäle dafür die richtigen sind. Erst dann zahlen Einzelmaßnahmen wirklich ein.'),
    ('Wie messen wir den Erfolg unserer Marketing-Maßnahmen?',
     'Je nach Kanal unterschiedlich: Website-Traffic und Conversions via Google Analytics, Reichweite und Engagement in Social Media, Rücklaufquoten bei Print-Aktionen. Wir definieren vor dem Start, welche KPIs relevant sind – und berichten regelmäßig.'),
    ('Macht ihr auch Social-Media-Management und Content-Produktion?',
     'Ja. Von der Strategie über Content-Planung bis zur regelmäßigen Bespielung von Instagram, LinkedIn, Facebook und Xing. Wir produzieren Texte, Grafiken und Kurzvideos – oder schulen Ihr Team für die eigenständige Pflege.'),
    ('Was unterscheidet euch von größeren Marketing-Agenturen?',
     'Sie reden mit dem, der auch arbeitet. Kein Junior-Betreuer, kein Ping-Pong zwischen Abteilungen. Dafür direkte Kommunikation, schnelle Entscheidungen und ein Partner, der Ihr Unternehmen persönlich kennt. Das ist unser Modell – und es funktioniert seit 18 Jahren.'),
  ],
  'corporate-design': [
    ('Was gehört alles zu einem vollständigen Corporate Design?',
     'Logo und Schutzraum, Primär- und Sekundärfarben, Schriftfamilie und Typografieregeln, Bildsprache, Gestaltungsraster für Print und Digital. Dazu Anwendungsbeispiele: Visitenkarte, Briefbogen, Social-Media-Vorlagen, Firmenwagen-Folie. Alles dokumentiert in einem Brand Manual.'),
    ('Wie lange dauert ein typisches Rebranding-Projekt?',
     'Vom ersten Briefing bis zur finalen Abnahme: 6–12 Wochen für ein vollständiges Corporate Design. Für Logo-only-Projekte auch schneller. Wir erstellen immer einen konkreten Zeitplan vor Projektstart – inklusive Ihrer Feedback-Phasen.'),
    ('Können wir das neue Corporate Design schrittweise einführen?',
     'Ja – das ist oft die pragmatischste Lösung. Neue Drucksachen bekommen das neue Design, Altbestände werden aufgebraucht. Wir erstellen einen Rollout-Plan, der Ihren Lagerbestand und Ihre Budgetplanung berücksichtigt.'),
    ('Was unterscheidet ein gutes Logo von einem austauschbaren Zeichen?',
     'Ein gutes Logo funktioniert in 10 mm und auf 10 Metern. Es wirkt in Schwarz-Weiß und in Farbe. Es transportiert ein Gefühl, nicht nur einen Namen. Das entsteht nicht im Zufallsprozess, sondern durch strategisches Denken – und darin liegt unsere Kernkompetenz.'),
  ],
  'drohnenfotografie': [
    ('In welcher Höhe fliegt ihr – und welche Höhenbeschränkungen gelten?',
     'Standard-Drohnenflüge erfolgen bis 120 m Höhe in der offenen Kategorie. Mit unserer SPECIFIC-Zulassung (STS-01, STS-02) sind wir auch über kontrollierten Gebieten und unter besonderen Bedingungen zugelassen. Alle Flüge werden vorab auf Luftraumrestriktionen geprüft.'),
    ('Wie lange dauert ein typischer Drohneneinsatz inkl. Auf- und Abbau?',
     'Ein halbtägiger Einsatz umfasst ca. 3–4 Stunden vor Ort: 30 Min. Aufbau und Sicherheitschecks, 1,5–2 Std. Flug und Aufnahmen, 30 Min. Abbau und Datensicherung. Ganztägige Produktionen planen wir entsprechend detaillierter.'),
    ('Was passiert bei schlechtem Wetter am Drehtag?',
     'Wir beobachten die Wetterlage ab 72 Stunden vor dem Termin aktiv. Bei Wind über 10 m/s, Regen oder Sichtweite unter 500 m verschieben wir den Termin ohne Extrakosten. Kurzfristige Entscheidungen treffen wir gemeinsam – Ihre Planungssicherheit geht vor.'),
    ('Welche Nutzungsrechte erhalte ich an den Drohnenaufnahmen?',
     'Sie erhalten alle Nutzungsrechte für Ihre Unternehmenskommunikation: Website, Social Media, Print, TV und Messe – ohne zeitliche Befristung. Exklusive oder erweiterte Rechte für Dritte (z.B. Immobilienverkauf, Vermarktung durch Dritte) klären wir im Briefing.'),
  ],
  'fotografie': [
    ('Muss ich als Ansprechpartner beim Shooting persönlich vor Ort sein?',
     'Empfohlen ja, Pflicht nein. Jemand sollte vor Ort sein, der Entscheidungen treffen kann: Wo ist der Maschinenpark zugänglich? Welche Mitarbeiter sollen fotografiert werden? Für reine Produktaufnahmen im Studio kann das Shooting auch ohne Sie laufen.'),
    ('Wie bereite ich mein Team optimal auf ein Fotoshooting vor?',
     'Kleiderordnung abstimmen (einheitliche Arbeitskleidung oder Business-Outfit je nach Ziel), Arbeitsplätze aufräumen, Maschinen reinigen. Wir schicken vorab eine kurze Checkliste. Unsere Erfahrung: 30 Minuten Vorbereitung sparen 2 Stunden Nachbearbeitung.'),
    ('Können die Fotos auch für Recruiting und Stellenausschreibungen genutzt werden?',
     'Ja, das ist ausdrücklich Teil des Standardpakets. Authentische Mitarbeiterfotos und Einblicke in den Arbeitsalltag sind heute einer der stärksten Hebel im Employer Branding – wir planen solche Aufnahmen auf Wunsch direkt in den Shooting-Tag ein.'),
    ('Fotografiert ihr auch außerhalb der Bodenseeregion?',
     'Ja. Wir fotografieren deutschlandweit – mit entsprechenden Fahrt- und Übernachtungskosten. Viele Kunden aus dem Stuttgarter Raum, München und dem Ruhrgebiet haben uns bereits für Shootings vor Ort gebucht. Anfragen nehmen wir gerne entgegen.'),
  ],
}
# FAQ-Varianten in THEMES einbinden
for _tk, _faq2 in THEMES_FAQ2.items():
    if _tk in THEMES:
        THEMES[_tk]['faq2'] = _faq2

# ══════════════════════════════════════════════════════════════════════════════
# PILLAR-CONTENT: Was-ist-Erklärung + Leistungsbausteine + Zielgruppen-Branchen
# Pillar-Seiten: alle 3 Sektionen vollständig
# Stadt-Seiten:  nur Leistungsbausteine (kompakt, LSI-Keywords)
# ══════════════════════════════════════════════════════════════════════════════
THEMES_PILLAR = {
  'webdesign': {
    'was_ist': [
      'Professionelles Webdesign ist weit mehr als das Erstellen einer optisch ansprechenden Website. Es ist das Zusammenspiel aus Strategie, Design und Technik – mit einem klaren Ziel: Ihre Website soll für Ihr Unternehmen arbeiten. Eine professionelle Website überzeugt Besucher in den ersten drei Sekunden, führt sie zielgerichtet zur Kontaktaufnahme und wird von Google als technisch einwandfrei bewertet. In der Praxis bedeutet das: mobiles Design nach dem mobile-first-Prinzip, Ladezeiten unter zwei Sekunden, strukturierte Daten für Suchmaschinen und eine Nutzerführung, die konvertiert.',
      'Was gute Websites von schlechten unterscheidet, ist messbar: Absprungrate, Verweildauer, Conversion-Rate und Google PageSpeed-Score liefern klare Antworten. Eine professionell entwickelte Website auf WordPress oder Joomla – mit sauberem PHP-Code, optimierten Bildern im WebP-Format und korrekter DSGVO-Umsetzung – rankt besser, lädt schneller und gewinnt mehr Anfragen. Responsives Design ist dabei kein optionales Feature, sondern seit Googles mobile-first Indexierung ein harter Rankingfaktor.',
      'Der häufigste Fehler bei der Website-Erstellung: die Trennung von Design und Strategie. Schöne Seiten, die niemand findet. Gut gefundene Seiten, die nicht konvertieren. X mind entwickelt Websites, die beides vereinen – durch ein Briefing-Gespräch vor dem ersten Entwurf, ein erprobtes Entwicklungsmodell und persönliche CMS-Schulung nach dem Launch. Kein Baukasten, kein Template von der Stange.',
    ],
    'leistungen': [
      {'titel':'WordPress & Joomla Entwicklung','icon':'⚙️','text':'Individuelle Theme-Entwicklung auf WordPress und Joomla – kein Page-Builder, kein generisches Template. Wir entwickeln auf Basis Ihrer Anforderungen: sauberer PHP-Code, optimierte Datenbankabfragen, DSGVO-konformes Cookie-Management und strukturierte Daten (Schema.org) von Anfang an. Das Ergebnis ist eine Website, die Sie selbst pflegen können – ohne Programmierkenntnisse.'},
      {'titel':'Responsive Design & mobile-first','icon':'📱','text':'Seit Googles mobile-first Indexierung ist responsives Design kein Bonus mehr – es ist Pflicht. Wir entwickeln jede Website zuerst für Smartphone und Tablet, dann für Desktop. Das verbessert die Core Web Vitals (LCP, CLS, FID), senkt die Absprungrate auf Mobilgeräten und erhöht direkt das Google-Ranking. Jeder Breakpoint wird manuell getestet.'},
      {'titel':'Core Web Vitals & Page Speed','icon':'⚡','text':'Google bewertet Ladezeit und Nutzererlebnis direkt als Rankingfaktor. Wir optimieren LCP (Largest Contentful Paint), CLS (Cumulative Layout Shift) und FID (First Input Delay) durch Bildkomprimierung im WebP-Format, Lazy Loading, Browser-Caching und minimiertes JavaScript. Ziel ist ein Google PageSpeed Score von mindestens 80 auf Mobilgeräten.'},
      {'titel':'UX & Conversion-Optimierung','icon':'🎯','text':'Eine Website, die nicht konvertiert, ist eine teure Visitenkarte. Wir analysieren Nutzerverhalten, definieren klare Call-to-Actions und optimieren die Seitenstruktur für maximale Anfragen. Kontaktformulare, Telefon-Buttons und Vertrauenssignale werden strategisch platziert. Das Ergebnis: mehr Anfragen aus demselben Traffic, ohne Mehrausgaben für Werbung.'},
      {'titel':'SEO-Grundoptimierung','icon':'📈','text':'Jede Website verlässt unser Haus mit vollständiger SEO-Grundoptimierung: optimierte Title-Tags und Meta-Descriptions pro Seite, saubere URL-Struktur, interne Verlinkung, strukturierte Daten (LocalBusiness, BreadcrumbList), sitemap.xml und robots.txt. Das ist keine Sonderoption – es ist Teil jedes Projekts. Denn eine Website, die niemand findet, nützt niemandem.'},
      {'titel':'DSGVO & Datenschutz','icon':'🔒','text':'Datenschutz ist keine Bürokratie, sondern Vertrauenssignal. Wir implementieren rechtskonformes Cookie-Consent-Management (ohne Google Analytics, auf Wunsch mit Matomo/selbstgehostetem Tracking), korrekte Datenschutzerklärungen, DSGVO-konforme Kontaktformulare und prüfen alle eingebundenen Drittdienste. Eine saubere DSGVO-Umsetzung schützt Sie vor Abmahnungen und stärkt das Vertrauen Ihrer Besucher.'},
      {'titel':'CMS-Schulung & persönlicher Support','icon':'🤝','text':'Sie sollen Ihre Website selbst pflegen können – ohne uns jedes Mal anrufen zu müssen. Nach dem Launch erhalten Sie eine persönliche CMS-Schulung: wie Sie Seiten bearbeiten, Bilder hochladen, Blog-Beiträge veröffentlichen und Formulare anpassen. Dazu schriftliche Dokumentation. Unser Support ist kein Ticket-System, sondern ein direkter Ansprechpartner.'},
      {'titel':'Hosting, Wartung & Updates','icon':'🛡️','text':'Eine Website braucht laufende Pflege: CMS-Updates, Sicherheits-Patches, Plugin-Kompatibilitätsprüfungen, SSL-Zertifikat-Erneuerungen und regelmäßige Backups. Wir bieten Managed Hosting auf deutschen Servern und Wartungsverträge, die diese Aufgaben übernehmen – transparent, monatlich abgerechnet, ohne Überraschungskosten.'},
    ],
    'branchen': [
      {'name':'Handwerk & Bau','text':'Handwerksbetriebe brauchen Websites, die Vertrauen schaffen: Referenzfotos, Bewertungen, lokale Präsenz in Google Maps und eine Kontaktseite, die auf dem Smartphone sofort funktioniert. Wir kennen die Anforderungen aus über 50 Handwerksprojekten.'},
      {'name':'Gastronomie & Hotellerie','text':'Speisekarte, Reservierungsformular, Google-Bewertungen, Öffnungszeiten mit strukturierten Daten – und eine Website, die auf dem Smartphone in unter 2 Sekunden lädt. Für Gastronomen und Hotels ist die Website der erste Kontaktpunkt mit dem Gast.'},
      {'name':'Industrie & produzierendes Gewerbe','text':'B2B-Websites für Industrie- und Produktionsunternehmen brauchen technisches Verständnis, Mehrsprachigkeit und oft komplexe Produktkataloge. Wir entwickeln auf diesem Niveau – mit Erfahrung aus der Medizintechnik-, Maschinen- und Metallbaubranche.'},
      {'name':'Dienstleistung & freie Berufe','text':'Für Steuerberater, Anwälte, Ärzte und Berater ist die Website das wichtigste Akquiseinstrument. Vertrauen, Kompetenz und klare Kontaktwege – das sind die Conversion-Treiber für diese Zielgruppen.'},
      {'name':'Einzelhandel & E-Commerce','text':'Von der lokalen Präsenz bis zum WooCommerce-Shop: Einzelhandel braucht heute beides. Wir entwickeln Websites, die stationäre Kunden binden und Online-Käufer gewinnen – DSGVO-konform, zahlungsintegrationsfähig und mobiloptimiert.'},
    ],
  },
  'werbeagentur': {
    'was_ist': [
      'Eine Werbeagentur ist mehr als ein Dienstleister für Flyer und Websites. Eine gute Werbeagentur versteht Ihr Unternehmen, Ihre Zielgruppen und Ihre Marktposition – und entwickelt daraus Kommunikation, die wirkt. Das bedeutet: strategische Positionierung, visuell überzeugendes Design und medienübergreifende Umsetzung in Print, Digital und Außenwerbung. Für Handwerk und Mittelstand bedeutet es außerdem: kein Agentur-Overhead, kein Callcenter, kein Junior-Betreuer. Sondern ein direkter Ansprechpartner, der Ihre Branche kennt.',
      'Was eine starke Werbeagentur von einer durchschnittlichen unterscheidet, ist nicht das Kreativ-Portfolio – es ist der strategische Denkansatz. Wer schießt, muss wissen, worauf er zielt. Zielgruppenanalyse, Wettbewerbspositionierung, Markenbotschaft und Kanalstrategie sind die Grundlage für jede erfolgreiche Kampagne. Erst dann entsteht Design. Erst dann werden Werbemittel produziert. In dieser Reihenfolge – nicht umgekehrt.',
      'Der typische Fehler beim Agenturauftrag: Einzelmaßnahmen ohne Strategie. Ein neues Logo ohne Corporate Design-System. Eine Website ohne SEO-Grundlage. Eine Social-Media-Kampagne ohne definierte Zielgruppe. X mind denkt immer vom Ziel her – und entwickelt Maßnahmen, die zusammen mehr ergeben als die Summe ihrer Teile. Das ist Full-Service, wie er für den Mittelstand funktioniert.',
    ],
    'leistungen': [
      {'titel':'Strategie & Markenpositionierung','icon':'🧭','text':'Ohne Strategie ist jede Werbemaßnahme Zufall. Wir entwickeln mit Ihnen eine klare Markenpositionierung: Wer sind Ihre Zielgruppen? Was unterscheidet Sie vom Wettbewerb? Welche Botschaft überzeugt? Das Ergebnis ist ein Kommunikationsrahmen, der alle Maßnahmen – Print, Digital, Kampagnen – auf ein gemeinsames Ziel ausrichtet.'},
      {'titel':'Corporate Design & Branding','icon':'🎨','text':'Von der Logoentwicklung über das Farb- und Typografiesystem bis zum vollständigen Corporate Design Manual: Wir entwickeln Markenidentitäten, die unverwechselbar sind und in jedem Format funktionieren – 10 mm auf der Visitenkarte, 10 Meter auf dem Firmenwagen. Inklusive Anwendungsbeispielen, Schutzraum-Regelungen und Vektordaten für Print und Digital.'},
      {'titel':'Print & Werbemittel','icon':'🖨️','text':'Drucksachen, die überzeugen: Flyer, Broschüren, Produktkataloge, Geschäftsberichte, Anzeigen, Plakate, Beschilderungen, Roll-ups und Messestand-Grafiken. Druckdaten-perfekt, nach CI-konform, termingerecht. Wir koordinieren auch die Druckproduktion – Sie erhalten fertige Werbemittel, nicht nur Dateien.'},
      {'titel':'Digitale Kommunikation','icon':'💻','text':'Website, Social Media, Google Ads, Newsletter und E-Mail-Marketing aus einer Hand. Wir stellen sicher, dass Ihre digitale Kommunikation konsistent ist – gleicher Ton, gleiche Bildsprache, gleiche Botschaft – und dass alle Kanäle aufeinander einzahlen statt aneinander vorbeizureden.'},
      {'titel':'Kampagnenentwicklung & Mediaplanung','icon':'📡','text':'Von der Idee bis zur Schaltung: Wir entwickeln Kampagnen für lokale und regionale Märkte. Anzeigenplanung in Tageszeitungen, Online-Display, Social-Media-Kampagnen, Radiospots und Außenwerbung. Mediaplanung mit Budget-Empfehlung, Durchführung und Erfolgsmessung – alles aus einer Hand.'},
      {'titel':'Employer Branding','icon':'👥','text':'Fachkräftemangel ist für viele Mittelständler das drängendste Problem. Wir entwickeln Arbeitgeberkommunikation, die wirkt: Karriereseiten, Stellenanzeigen-Design, Social-Media-Recruiting auf LinkedIn, Instagram und Facebook sowie HR-Kampagnen, die die richtigen Bewerber ansprechen.'},
      {'titel':'Fotografie & Video','icon':'📸','text':'Authentische Bilder und Videos stärken Ihre Kommunikation mehr als jedes Stockfoto. Wir produzieren Corporate-Fotografie (Mitarbeiter, Standort, Produkte), Imagevideos und Social-Media-Content – aus einer Hand, mit einheitlicher Bildsprache, verwendbar für Print und Digital.'},
    ],
    'branchen': [
      {'name':'Handwerk & Bau','text':'Für Handwerksbetriebe entwickeln wir Gesamtauftritte, die Vertrauen schaffen: von der Geschäftsausstattung über die Website bis zur Arbeitskleidungs-CI. Bodenständig, verlässlich, professionell – wie das Handwerk selbst.'},
      {'name':'Industrie & Maschinenbau','text':'Industrie- und Maschinenbauunternehmen kommunizieren mit uns auf technischem Niveau. Messekommunikation, technische Broschüren, Geschäftsberichte und mehrsprachige Unternehmensdarstellungen – für nationale und internationale Märkte.'},
      {'name':'Gastronomie & Hotellerie','text':'Gastronomische Betriebe und Hotels brauchen Kommunikation mit Atmosphäre und Substanz: Speisekarten, Hotelbroschüren, Eventflyer, Social-Media-Content und ein konsistentes visuelles Erscheinungsbild über alle Kanäle.'},
      {'name':'Immobilien & Bauwirtschaft','text':'Immobilienmakler, Bauträger und Architekturbüros kommunizieren mit uns auf hohem ästhetischem Niveau: Exposé-Gestaltung, Bauschilder, Broschüren, Websites und digitales Marketing für Neubauprojekte und Bestandsimmobilien.'},
      {'name':'Einzelhandel & Dienstleistung','text':'Inhabergeführte Geschäfte und Dienstleistungsbetriebe profitieren von unserer Erfahrung mit regionalen Märkten: Anzeigenkampagnen, Eröffnungskommunikation, Kundenbindungsmaßnahmen und lokales Marketing, das wirklich ankommt.'},
    ],
  },
  'seo': {
    'was_ist': [
      'Suchmaschinenoptimierung (SEO) ist die Disziplin, die dafür sorgt, dass Ihr Unternehmen bei Google gefunden wird – wenn potenzielle Kunden aktiv nach Ihren Leistungen suchen. Anders als Werbung (Google Ads, Social Media) ist SEO nachhaltig: einmal aufgebaut, liefert ein gutes Ranking über Monate und Jahre organischen Traffic, ohne dass Sie für jeden Besucher bezahlen. Lokales SEO zielt auf Suchanfragen mit Stadtbezug ab – „Installateursbetrieb Konstanz" oder „Webdesign Singen" – und ist für regional tätige Unternehmen der wirkungsvollste digitale Kanal.',
      'Was gutes SEO von schlechtem unterscheidet: Transparenz und Geduld. Ehrliche SEO-Arbeit verbessert Rankings in 4–12 Wochen spürbar, zeigt Ergebnisse nach 3–6 Monaten messbar und baut nachhaltige Sichtbarkeit über Jahre auf. Wer sofortige Top-Rankings verspricht, lügt. Wer ausschließlich auf Backlinks setzt, riskiert Penalty-Risiken. Wer technisches SEO vernachlässigt, baut auf Sand. Professionelles SEO kombiniert alle drei Säulen: technische Basis, Content-Qualität und Linkauthorität.',
      'Die häufigsten SEO-Fehler im Mittelstand: kein Google My Business-Eintrag oder ein unvollständiger, veralteter Eintrag; fehlende oder duplizierte Meta-Tags; keine saubere interne Verlinkungsstruktur; Seiten ohne strukturierte Daten (Schema.org); und Content, der für die Suchmaschine geschrieben wurde statt für den Menschen. X mind vermeidet diese Fehler durch ein initiales SEO-Audit, das den Status quo klar benennt – und durch monatliches Reporting, das zeigt, was die Arbeit gebracht hat.',
    ],
    'leistungen': [
      {'titel':'SEO-Audit & Wettbewerbsanalyse','icon':'🔍','text':'Am Anfang steht die ehrliche Bestandsaufnahme: Welche Keywords ranken? Welche nicht? Wie stark ist der Wettbewerb? Wo sind technische Fehler? Unser SEO-Audit analysiert technisches SEO, On-Page-Faktoren, Backlink-Profil, Content-Lücken und Ihre Wettbewerber – und liefert eine priorisierte Maßnahmen-Roadmap mit realistischen Zeitplänen.'},
      {'titel':'Lokales SEO & Google My Business','icon':'📍','text':'Für regional tätige Unternehmen ist Google My Business der wichtigste SEO-Hebel: vollständiges Profil, korrekte NAP-Daten (Name, Adresse, Telefon), Öffnungszeiten, Fotos, Bewertungsmanagement und Google Posts. Dazu Local Pack-Optimierung, lokale Citations in relevanten Branchenverzeichnissen und hreflang-Tags für internationale Märkte.'},
      {'titel':'On-Page SEO & Content-Optimierung','icon':'📝','text':'Title-Tags, Meta-Descriptions, Überschriftenstruktur (H1-H3), interne Verlinkung, Keyword-Platzierung und Content-Tiefe – alles systematisch optimiert auf Basis von Keyword-Recherche und Suchintention. Wir schreiben und optimieren Texte, die Google versteht und Menschen gerne lesen. Kein Keyword-Stuffing, sondern semantische Tiefe mit LSI-Begriffen.'},
      {'titel':'Technisches SEO','icon':'⚙️','text':'Die Grundlage für alle anderen Maßnahmen: Core Web Vitals (LCP, CLS, FID), Ladezeit, Crawling und Indexierung (robots.txt, sitemap.xml), strukturierte Daten (Schema.org), URL-Struktur, Canonical-Tags, Duplicate Content-Bereinigung und Mobile-First-Optimierung. Technisches SEO macht Content-Maßnahmen erst wirksam.'},
      {'titel':'Backlink-Aufbau & Linkbuilding','icon':'🔗','text':'Autorität entsteht durch relevante externe Links. Wir bauen Backlinks durch Branchenverzeichnisse, Partnerseiten, lokale Pressearbeit und thematisch passende Gastbeiträge. Kein Linkverkauf, kein Spam – ausschließlich Links, die Google als natürlich und werthaltig bewertet und die Ihr Ranking langfristig stärken.'},
      {'titel':'Google Ads & SEA','icon':'💰','text':'SEO und Google Ads (SEA) ergänzen sich: Paid Ads liefern sofortige Sichtbarkeit für neue Keywords oder saisonale Aktionen, während SEO nachhaltige organische Rankings aufbaut. Wir koordinieren beide Kanäle strategisch, vermeiden Keyword-Kannibalisierung und maximieren den Return on Ad Spend (ROAS) durch datenbasierte Gebotsstrategien.'},
      {'titel':'Monitoring & monatliches Reporting','icon':'📊','text':'Ohne Messung keine Optimierung. Wir richten Google Search Console, Google Analytics 4 und auf Wunsch Matomo ein – DSGVO-konform, ohne IP-Speicherung. Monatliche Berichte zeigen Rankingveränderungen, Traffic-Entwicklung, Conversion-Zahlen und den Status laufender Maßnahmen. Keine Zahlen-Salate, sondern klare Aussagen darüber, was Ihr Budget bewirkt hat.'},
    ],
    'branchen': [
      {'name':'Handwerk & lokale Dienstleister','text':'Lokales SEO ist für Handwerksbetriebe der direkte Weg zu neuen Aufträgen. Wenn jemand „Elektriker Radolfzell" sucht, muss Ihr Betrieb erscheinen – in Google Maps und in den organischen Ergebnissen. Das ist der Kern unserer SEO-Arbeit für Handwerk.'},
      {'name':'Medizin, Therapie & Gesundheit','text':'Patienten suchen online nach Ärzten, Therapeuten und Gesundheitsdienstleistern. Lokales SEO, Google My Business-Optimierung und strukturierte Daten (HealthcareOrganization, MedicalBusiness) sind entscheidend für Sichtbarkeit in diesem sensiblen Markt.'},
      {'name':'Gastronomie & Tourismus','text':'Restaurant-SEO bedeutet: Google My Business mit Speisekarte, Reservierungslink und aktuellen Öffnungszeiten; Bewertungsmanagement; lokale Suchanfragen wie „Restaurant Konstanz Altstadt"; und strukturierte Daten (Restaurant, FoodEstablishment) für Rich Snippets.'},
      {'name':'Industrie & B2B','text':'B2B-SEO ist länger und strategischer als B2C. Wir optimieren auf Suchanfragen mit niedrigem Volumen, aber hoher Kaufabsicht – die Anfragen, die wirklich konvertieren. Technische Tiefe im Content signalisiert Google und dem suchenden Einkäufer gleichzeitig Kompetenz.'},
      {'name':'Einzelhandel & E-Commerce','text':'Lokaler Einzelhandel braucht SEO, der stationäre Besucher anzieht: Google Maps, Google Shopping, lokale Suchanfragen und eine website-interne Suchoptimierung. E-Commerce braucht zusätzlich Product Schema, Canonical-Tags für Varianten und kategorie-basierte Content-Strategien.'},
    ],
  },
  'webagentur': {
    'was_ist': [
      'Eine Webagentur entwickelt, optimiert und betreut digitale Präsenzen – von der einfachen Unternehmenswebsite bis zur komplexen Web-Applikation. Der Unterschied zu einer reinen Werbeagentur: eine Webagentur denkt technisch. PHP, JavaScript, API-Anbindungen, Serveradministration, Datenbankoptimierung und Sicherheitsarchitektur sind ihr Handwerk. X mind verbindet beides: technische Kompetenz und strategisches Kommunikationsdenken – für Websites, die nicht nur laufen, sondern wirken.',
      'Was eine professionelle Webagentur ausmacht: sie liefert nicht einfach Code, sondern Lösungen. Das bedeutet: zuerst verstehen, was die Website leisten soll – welche Nutzergruppen, welche Conversion-Ziele, welche technischen Anforderungen. Dann das richtige CMS auswählen: WordPress für Flexibilität und Pflegbarkeit, Joomla für komplexe Strukturen, TYPO3 für Großprojekte oder ein Headless-CMS für maximale Entwicklerfreiheit. Und schließlich: Barrierefreiheit (WCAG 2.1), DSGVO-Konformität und Core Web Vitals von Anfang an mitdenken.',
      'Typische Probleme, die wir bei Website-Übernahmen regelmäßig sehen: veraltete CMS-Versionen mit Sicherheitslücken, fehlendes SSL-Zertifikat, keine Backup-Strategie, Plugins die sich gegenseitig blockieren, und DSGVO-Verstöße durch eingebundene Google-Dienste ohne Consent. X mind übernimmt bestehende Websites mit einem vollständigen technischen Audit, bereinigt die Baustellen und stellt dauerhaften, sicheren Betrieb sicher.',
    ],
    'leistungen': [
      {'titel':'Webentwicklung & Individualprogrammierung','icon':'💻','text':'Individuelle Webentwicklung in PHP, JavaScript und modernen Frontend-Frameworks. Von der einfachen Unternehmenswebsite bis zur komplexen Web-Applikation mit API-Anbindungen, Datenbankoptimierung und automatisierten Prozessen. Wir entwickeln, was vorgefertigte Lösungen nicht können – sauber dokumentiert und übergabefähig.'},
      {'titel':'CMS-Entwicklung & -Betreuung','icon':'📋','text':'WordPress, Joomla, TYPO3 und Headless-CMS-Systeme: Wir entwickeln und pflegen alle gängigen Content-Management-Systeme. Theme-Entwicklung, Plugin-Programmierung, Datenbankoptimierung und CMS-Migrationen zwischen Systemen. Das richtige CMS ist das, das Ihre Anforderungen erfüllt – nicht das, das gerade trendy ist.'},
      {'titel':'Performance-Optimierung & Core Web Vitals','icon':'⚡','text':'Langsame Websites verlieren Besucher und Rankings. Wir optimieren Ladezeiten durch Bildkomprimierung (WebP, AVIF), CDN-Integration, Browser-Caching, Datenbankoptimierung und JavaScript-Minimierung. Ziel: Google PageSpeed Score über 80 auf Mobilgeräten und messbar bessere Core Web Vitals (LCP, CLS, FID).'},
      {'titel':'Barrierefreiheit (WCAG 2.1 & BITV)','icon':'♿','text':'Ab 2025 gilt das Barrierefreiheitsstärkungsgesetz für viele Unternehmenswebsites. Wir prüfen und implementieren WCAG 2.1-Konformität: Farbkontraste, Tastaturnavigation, Screen-Reader-Kompatibilität, barrierefreie Formulare und korrekte ARIA-Labels. Barrierefreiheit ist kein Pflaster, sondern Qualitätsmerkmal.'},
      {'titel':'DSGVO-Umsetzung & Datenschutz','icon':'🔒','text':'DSGVO-konformes Cookie-Consent-Management, Datenschutzerklärung, Verarbeitungsverzeichnis, DSGVO-konforme Kontaktformulare, Austausch von Google Analytics gegen Matomo oder ähnliche EU-konforme Tracking-Tools. Wir prüfen alle eingebundenen Dienste – Schriftarten, Maps, Videos, Social Plugins – auf DSGVO-Konformität.'},
      {'titel':'API & System-Integrationen','icon':'🔗','text':'CRM-Anbindung (HubSpot, Salesforce, Pipedrive), ERP-Integration, Shop-Systeme (WooCommerce, Shopware), Newsletter-Tools (Mailchimp, CleverReach), Buchungssysteme und Zahlungsanbieter. Wir verbinden Ihre Website mit den Systemen, die Ihr Unternehmen bereits nutzt – automatisiert, fehlerfrei, wartbar.'},
      {'titel':'Hosting, Server & Sicherheit','icon':'🛡️','text':'Managed Hosting auf deutschen Servern (DSGVO-konform), SSL/TLS-Zertifikate, automatische Backups, Malware-Scanning und Security-Monitoring. Wir verwalten Serverumgebungen für WordPress, Joomla und individuelle PHP-Anwendungen – inklusive PHP-Version-Management und Datenbankadministration.'},
    ],
    'branchen': [
      {'name':'E-Commerce & Online-Handel','text':'Shop-Systeme, Produktdatenbanken, Zahlungsintegrationen und automatisierter Lagerbestandsabgleich – E-Commerce-Webentwicklung stellt höchste technische Anforderungen. Wir entwickeln WooCommerce-Lösungen und individuelle Shop-Backends für regionalen und nationalen Online-Handel.'},
      {'name':'Dienstleister & Beratungsunternehmen','text':'Buchungssysteme, Kunden-Portale, Lead-Generierungsformulare und CRM-Anbindung – für Dienstleistungsunternehmen ist die Website der wichtigste Vertriebskanal. Wir entwickeln technische Lösungen, die Ihre Vertriebsprozesse automatisieren.'},
      {'name':'Industrie & Maschinenbau','text':'Produktkataloge mit hunderten Varianten, Händler-Portale, Multi-Sprachen-Websites und Intranet-Lösungen – Industriewebsites haben komplexe technische Anforderungen. Wir entwickeln auf diesem Niveau – mit TYPO3, individuellen CMS-Lösungen und API-Anbindungen an ERP-Systeme.'},
      {'name':'Medizin & Gesundheit','text':'Datenschutz hat im Gesundheitsbereich höchste Priorität. Wir entwickeln DSGVO-konforme Websites für Arztpraxen, Kliniken und Therapeuten – mit Online-Terminbuchung, DSGVO-konformen Kontaktformularen und barrierefreiem Design nach WCAG 2.1.'},
    ],
  },
  'marketing': {
    'was_ist': [
      'Marketing ist die systematische Planung und Umsetzung aller Maßnahmen, mit denen ein Unternehmen seine Zielgruppen erreicht, überzeugt und zu Kunden macht. Für den Mittelstand bedeutet das kein großes Budget zu verbrennen, sondern das vorhandene Budget präzise einzusetzen: die richtigen Kanäle, die richtige Botschaft, die richtigen Zielgruppen. Ob Social-Media-Marketing, Google Ads, E-Mail-Marketing, Content-Marketing oder lokale Print-Kampagnen – entscheidend ist die Strategie dahinter, nicht der Kanal.',
      'Was professionelles Marketing von Aktionismus unterscheidet: Messbarkeit und Strategie. Jede Maßnahme sollte ein klares Ziel haben, auf eine definierte Zielgruppe ausgerichtet sein und einen messbaren KPI haben – Reichweite, Leads, Conversions, Return on Ad Spend (ROAS). Marketing ohne Reporting ist Marketing im Dunkeln. X mind definiert vor jeder Kampagne: Was soll sie erreichen? Wie messen wir Erfolg? Was ist das Budget? Erst dann beginnen wir.',
      'Der häufigste Fehler in der Marketing-Praxis kleiner und mittlerer Unternehmen: zu viele Kanäle gleichzeitig, keiner davon richtig. Instagram, Facebook, Google Ads, Newsletter, SEO, Flyer – alles parallel, nichts mit echter Energie. Das Ergebnis ist Mittelmäßigkeit in allen Kanälen. Besser: zwei bis drei Kanäle professionell bespielen als sieben halbherzig. X mind hilft Ihnen, die richtigen Kanäle für Ihr Unternehmen zu identifizieren – und diese dann konsequent zu bespielen.',
    ],
    'leistungen': [
      {'titel':'Marketingstrategie & Kanalplanung','icon':'🧭','text':'Bevor ein Budget ausgegeben wird: Zielgruppenanalyse, Positionierung, Botschaftsentwicklung, Kanalauswahl und Budgetplanung. Wir entwickeln einen Jahresplan oder Quartalsmasterplan mit priorisierten Maßnahmen, realistischen Zielen und klaren Erfolgskriterien. Marketing-Strategie ist keine Theorie – sie ist der Fahrplan, der Geld spart.'},
      {'titel':'Social Media Marketing','icon':'📱','text':'Content-Planung, Community Management und bezahlte Kampagnen auf Instagram, Facebook, LinkedIn und Xing. Wir produzieren Texte, Grafiken und Kurzvideos – oder schulen Ihr Team für die eigenständige Bespielung. Social Media ohne Strategie ist Zeitverschwendung; Social Media mit Strategie ist Ihr direkter Draht zur Zielgruppe.'},
      {'titel':'Google Ads & Paid Advertising','icon':'💰','text':'Search-Kampagnen, Display-Werbung, Google Shopping, YouTube-Ads und Remarketing. Wir verwalten Google Ads-Kampagnen mit transparentem Reporting: Klicks, Impressionen, Conversion-Rate, Cost-per-Acquisition und Return on Ad Spend. Budget-Effizienz durch datenbasierte Gebotsstrategien und kontinuierliche Anzeigenoptimierung.'},
      {'titel':'E-Mail-Marketing & Automation','icon':'📧','text':'Newsletter-Konzeption, Listenaufbau, Segmentierung und Automation – von der Willkommens-Serie bis zum Reaktivierungsflow. Wir arbeiten mit DSGVO-konformen Tools (CleverReach, Mailchimp, ActiveCampaign) und messen Öffnungsrate, Klickrate und Conversion. E-Mail-Marketing hat den höchsten ROI aller digitalen Kanäle – wenn es richtig gemacht wird.'},
      {'titel':'Content Marketing & SEO-Content','icon':'✍️','text':'Blogbeiträge, Whitepapers, Produktbeschreibungen, Landingpages und Ratgeberartikel – Content, der gefunden wird und konvertiert. Wir kombinieren Keyword-Recherche, Suchintention und redaktionelle Qualität. Guter Content ist der einzige Weg, nachhaltig organische Sichtbarkeit aufzubauen – ohne permanent für Klicks zu bezahlen.'},
      {'titel':'Analyse, Reporting & Optimierung','icon':'📊','text':'Google Analytics 4, Google Search Console, Social-Media-Insights und Conversion-Tracking – wir richten alle Messtools ein und liefern monatliche Berichte, die Entscheidungen ermöglichen. Welcher Kanal bringt die meisten Leads? Welche Anzeige hat den besten ROAS? Welcher Content konvertiert? Daten statt Bauchgefühl.'},
      {'titel':'Lokales Marketing & Print','icon':'🗺️','text':'Regionale Zeitungsanzeigen, Direktmailing, Flyer, Plakate und Events für den lokalen Markt. Lokales Marketing ist für Handwerker, Einzelhändler und Dienstleister oft der direkteste Weg zum Kunden. Wir planen, produzieren und schalten – mit Kenntnis der regionalen Medien und Zielgruppen im Bodenseeraum und Schwarzwald.'},
    ],
    'branchen': [
      {'name':'Handwerk & Bau','text':'Für Handwerksbetriebe ist Google Ads mit lokalem Targeting oft die schnellste Quelle für Neukundenanfragen. Kombiniert mit lokaler SEO und regelmäßigen Facebook-Posts an die Stammkundschaft entsteht ein Marketing-Mix, der wirklich funktioniert.'},
      {'name':'Gastronomie & Hotellerie','text':'Social Media, Google My Business, Bewertungsmanagement und saisonale E-Mail-Kampagnen – Gastronomie-Marketing ist schnell und kurzfristig. Wir entwickeln Jahrespläne, die saisonale Highlights nutzen und Stammkunden aktivieren.'},
      {'name':'Industrie & B2B','text':'B2B-Marketing erfordert Geduld und Präzision: LinkedIn-Kampagnen für Entscheider, gezieltes Content Marketing mit technischer Tiefe und Messemarketing. Der Verkaufszyklus ist lang – umso wichtiger ist ein strategisch durchdachter Maßnahmenplan.'},
      {'name':'Einzelhandel & E-Commerce','text':'Google Shopping, Instagram-Werbung, Retargeting und lokale Google Ads – Einzelhandel braucht Sichtbarkeit genau dann, wenn jemand kaufbereit ist. Wir entwickeln Kampagnen, die stationäre Kunden und Online-Käufer gleichzeitig ansprechen.'},
      {'name':'Gesundheit, Therapie & Pflege','text':'Vertrauen und Diskretion sind im Gesundheitsmarketing entscheidend. Google Ads mit korrekter Zertifizierung, DSGVO-konformes Tracking, Content Marketing mit echter medizinischer Substanz und lokale Sichtbarkeit bei Google Maps.'},
    ],
  },
  'corporate-design': {
    'was_ist': [
      'Corporate Design ist das visuelle Erscheinungsbild eines Unternehmens – die Summe aller gestalterischen Entscheidungen, die nach außen kommunizieren: Wer sind wir? Wofür stehen wir? Wie unterscheiden wir uns? Ein konsistentes Corporate Design schafft Wiedererkennungswert, stärkt das Vertrauen von Kunden und Partnern und macht ein Unternehmen unverwechselbar. Es umfasst Logo, Farb- und Typo-System, Bildsprache und alle Anwendungen – von der Visitenkarte bis zur Fahrzeugbeschriftung.',
      'Was ein starkes Corporate Design ausmacht: Konsistenz und Flexibilität. Konsistenz bedeutet, dass Logo, Farben, Typografie und Bildsprache in jeder Anwendung gleich wirken – ob auf dem 10-mm-Kugelschreiber oder dem 10-Meter-Messebanner. Flexibilität bedeutet, dass das System in allen Kontexten funktioniert: Schwarz-Weiß-Druck, digitale Anwendungen, Werbefolierung, Stickerei auf Arbeitskleidung. Ein gutes CD-System ist wie eine gute Grammatik: Es gibt Regeln vor, lässt aber Raum für Ausdruck.',
      'Der häufigste Fehler beim Corporate Design: ein Logo ohne System. Ein schönes Logo, das aber keine Schutzraum-Regeln hat, in verschiedenen Varianten mal so, mal so verwendet wird und keinen Farb-Code besitzt, ist kein Corporate Design – es ist ein Icon. X mind entwickelt vollständige CD-Systeme, dokumentiert in einem Brand Manual, das intern und extern für konsistente Anwendung sorgt. Und wir denken von Anfang an an die Praxis: Was muss das Logo auf einer Stickerei bestehen? Wie wirkt die Farbe im Druck?',
    ],
    'leistungen': [
      {'titel':'Logo-Entwicklung & Markenzeichen','icon':'✨','text':'Konzeptentwicklung, Varianten-Präsentation, Schutzraum-Regelungen, Schwarz-Weiß-Variante, Icon-Variante und Wort-Bild-Marke. Lieferung als Vektordaten (AI, EPS, SVG) und in allen Exportformaten für Print und Digital (PDF, PNG, JPEG). Ein Logo, das in 10 mm und auf 10 Metern überzeugt.'},
      {'titel':'Farb- & Typografiesystem','icon':'🎨','text':'Primärfarbe, Sekundärfarben, Akzentfarben mit exakten CMYK-, RGB- und HEX-Werten. Schriftpaarung aus Headline- und Fließtext-Schrift, Schriftgrößen-Hierarchie, Zeilenabstand und Anwendungsregeln für Print und Digital. Das Farb- und Typo-System ist das Fundament aller weiteren Gestaltung.'},
      {'titel':'Corporate Design Manual','icon':'📖','text':'Vollständige Dokumentation aller CD-Elemente: Logo-Verwendungsregeln, Farb- und Typo-System, Bildsprache-Richtlinien, Falschanwendungs-Beispiele und Anwendungsvorlagen. Das CD Manual ist das Regelwerk, das sicherstellt, dass interne Teams und externe Dienstleister das Erscheinungsbild korrekt anwenden.'},
      {'titel':'Geschäftsausstattung','icon':'📄','text':'Visitenkarte, Briefbogen (DIN A4), Kuvert, E-Mail-Signatur, Stempel und Rechnungsvorlage – druckdatenperfekt, nach CI-konform. Wir koordinieren auch die Druckproduktion mit ausgewählten Druckpartnern. Geschäftsausstattung ist oft der erste physische Kontaktpunkt mit Geschäftspartnern – sie muss Professionalität ausstrahlen.'},
      {'titel':'Digitale Anwendungen','icon':'💻','text':'Website-Design nach Corporate Design, Social-Media-Vorlagen (Instagram, LinkedIn, Facebook), E-Mail-Marketing-Templates, Präsentations-Master (PowerPoint, Keynote) und digitale Werbemittel. Das CD muss digital genauso überzeugend wirken wie im Print – das prüfen wir auf jedem Display.'},
      {'titel':'Print & Werbemittel-Design','icon':'🖨️','text':'Flyer, Broschüren, Roll-ups, Plakate, Anzeigen, Fahrzeugfolierung, Schilder und Messestand-Grafiken – alles nach Corporate Design, druckfertig übergeben. Wir denken bei der Gestaltung immer an die Produktion: Schnittzugaben, Farbprofile, Auflösung und Materialspezifikationen sind selbstverständlich.'},
      {'titel':'Rebranding & Markenentwicklung','icon':'🔄','text':'Bestehende Marke analysieren, Schwächen identifizieren und systematisch weiterentwickeln. Rebranding muss nicht revolutionär sein – oft sind es gezielte Anpassungen, die eine Marke frisch und modern wirken lassen. Wir entwickeln einen Rollout-Plan, der laufende Bestände berücksichtigt und Kosten minimiert.'},
    ],
    'branchen': [
      {'name':'Handwerk & Bau','text':'Für Handwerksbetriebe ist Corporate Design der Schlüssel zu professionellem Auftreten: Fahrzeugfolierung, Arbeitskleidung, Beschilderung, Briefpapier und Website in einem konsistenten Erscheinungsbild. Das unterscheidet den professionellen Betrieb vom Amateur.'},
      {'name':'Industrie & produzierendes Gewerbe','text':'Industrieunternehmen brauchen Corporate Design, das international funktioniert: mehrsprachige Anwendungen, Messekommunikation, Investor-Relations-Materialien und ein CD-System, das auf Maschinenschildern genauso funktioniert wie auf der Geschäftsführer-Präsentation.'},
      {'name':'Dienstleistung & freie Berufe','text':'Steuerberater, Anwälte, Ärzte und Berater profitieren von einem Corporate Design, das Seriosität und Vertrauen ausstrahlt: zurückhaltende Farbpalette, hochwertige Typografie und Materialien, die Qualität kommunizieren.'},
      {'name':'Gastronomie & Hotellerie','text':'Gastronomiebetriebe und Hotels brauchen Corporate Design mit Atmosphäre: Speisekarten, Leit-Systeme, Uniform-Design, Social-Media-Ästhetik und ein visuelles Erscheinungsbild, das die Zielgruppe emotioniert und Wiedererkennung schafft.'},
    ],
  },
  'drohnenfotografie': {
    'was_ist': [
      'Professionelle Drohnenfotografie ist eine Dienstleistung, die besondere Anforderungen an Technik, Recht und Erfahrung stellt. Eine Drohne zu fliegen ist einfach. Professionelle Luftaufnahmen zu erstellen, die in Geschäftsberichten, Immobilien-Exposés oder Stadtmarketing-Kampagnen eingesetzt werden können, ist eine andere Sache: Sie erfordert zertifizierte Berufspiloten, hochwertige Kamerasysteme, professionelle Bildbearbeitung und rechtssichere Genehmigungsabwicklung. X mind betreibt Drohnenservice mit EU-Drohnenführerschein A1/A3 und A2 sowie Betriebskategorie SPECIFIC – für rechtskonforme Einsätze auch in komplexen Umgebungen.',
      'Was professionellen Drohnenservice von Hobby-Aufnahmen unterscheidet: erstens die Technik (4K-Kamerasysteme mit RAW-Aufnahme, Gimbal-Stabilisierung, Hinderniserkennung), zweitens die rechtliche Absicherung (EU-Drohnenverordnung DVO 2019/947, Betriebskategorie SPECIFIC, behördliche Genehmigungen), drittens die Bildbearbeitung (Belichtungskorrektur, Farbnormierung, Retusche, Export in allen Formaten) und viertens die Logistik (Vorab-Koordination, Wettermonitoring, Ausweichtermine). Nur wer alle vier Punkte professionell beherrscht, liefert Ergebnisse, die in professionellen Kommunikationsmedien verwendbar sind.',
      'Die häufigsten Fragen im Vorfeld: Brauche ich eine Genehmigung? Wie hoch darf geflogen werden? Was passiert bei schlechtem Wetter? X mind klärt alle diese Fragen vor dem Einsatz: Wir prüfen den Luftraum, holen notwendige Genehmigungen ein, koordinieren mit Behörden und planen Ausweichtermine. Sie müssen sich um nichts kümmern – außer klares Briefing zu geben, was Sie brauchen.',
    ],
    'leistungen': [
      {'titel':'Immobilien-Luftaufnahmen','icon':'🏠','text':'Luftaufnahmen von Neubauten, Bestandsimmobilien, Grundstücken und Bauprojekten. Für Makler, Bauträger und Architekten: Exposé-Fotos aus der Luft, Grundstücksübersichten, Nachbarschaftskontext und Bau-Dokumentation. Höhere Klickraten in Immobilienportalen, kürzere Vermarktungszeiten – professionelle Luftaufnahmen zahlen sich nachweislich aus.'},
      {'titel':'Gewerbe & Industrie','icon':'🏭','text':'Unternehmensgelände, Produktionsanlagen, Gewerbegebiete, Logistikflächen und Industriehallen aus der Luft – für Geschäftsberichte, Websites, Investorenpräsentationen und Messeauftritte. Wir fotografieren auch in Industriegebieten und auf bewachtem Gelände – mit vorheriger Genehmigungsabklärung.'},
      {'titel':'Baudokumentation & Aufmaß','icon':'📐','text':'Lückenlose Baudokumentation über den gesamten Bauprozess: von der Erdarbeiten bis zur Fertigstellung. Zeitreihenaufnahmen für Bauherren, Architekten und Baufirmen. Auf Wunsch mit GPS-Koordinaten, maßstabsgetreuer Kartierung und Vergleichsaufnahmen. Rechtssicher archiviert und jederzeit abrufbar.'},
      {'titel':'Kommunal & Stadtmarketing','icon':'🏙️','text':'Luftaufnahmen für Städte, Gemeinden und Tourismusverbände: Stadtansichten, Naturschutzgebiete, Veranstaltungsdokumentation, Infrastrukturprojekte und touristische Marketingbilder. Wir verfügen über besondere Genehmigungen für städtische Gebiete und Bereiche mit Luftraumbeschränkungen.'},
      {'titel':'Drohnenvideo & Imagefilm','icon':'🎥','text':'4K-Drohnenvideo für Imagefilme, Produktvideos und Social-Media-Content. Wir koordinieren Drohnenaufnahmen mit Bodenaufnahmen zu einem vollständigen Videoprodukt – mit professionellem Schnitt, Farbkorrektur, Musik-Lizenzierung und Export in allen benötigten Formaten (YouTube, Instagram Reels, Website).'},
      {'titel':'Thermografie & Inspektion','icon':'🌡️','text':'Wärmebildkamera-Aufnahmen zur Fassadeninspektion, PV-Anlagen-Prüfung, Dachinspektionen und Infrastruktur-Monitoring. Thermografie-Drohnenflüge identifizieren Wärmeverluste, Feuchtigkeitsschäden und Defekte in Solaranlagen – ohne Gerüst oder Hebebühne, deutlich günstiger und schneller als herkömmliche Inspektionsmethoden.'},
      {'titel':'Genehmigungsmanagement','icon':'📋','text':'EU-Drohnenverordnung DVO (EU) 2019/947, Betriebskategorie SPECIFIC, STS-01 und STS-02 – wir verfügen über alle notwendigen Zulassungen und holen für jeden Einsatz die standortspezifischen Genehmigungen ein: Luftfahrtbehörde, Polizei, Bundeswehr, Naturschutzbehörden. Rechtssicherheit für Sie – kein Risiko.'},
    ],
    'branchen': [
      {'name':'Immobilien & Bauwirtschaft','text':'Immobilienmakler, Bauträger und Architekturbüros sind die häufigsten Auftraggeber für Drohnenfotografie. Grundstücksübersichten, Neubau-Dokumentationen und Exposé-Luftbilder steigern nachweislich die Vermarktungsgeschwindigkeit von Immobilien.'},
      {'name':'Industrie & Gewerbe','text':'Unternehmensgelände, Produktionsstandorte und Gewerbegebiete aus der Luft – für Geschäftsberichte, Investor-Präsentationen und Unternehmenskommunikation. Wir fliegen auch auf bewachtem Gelände nach Absprache mit Werksleitung und Sicherheitsdienst.'},
      {'name':'Kommunen & Tourismusorganisationen','text':'Städte, Gemeinden und Tourismusverbände nutzen Luftaufnahmen für Stadtmarketing, touristische Werbekampagnen und die Dokumentation von Infrastrukturprojekten. Wir verfügen über behördliche Genehmigungen für städtische Drohnenflüge.'},
      {'name':'Events & Veranstaltungen','text':'Open-Air-Festivals, Stadtfeste, Sportveranstaltungen und Messen aus der Luft. Event-Drohnenfotografie erfordert besondere Genehmigungen über Menschenansammlungen – die wir vollständig abwickeln.'},
    ],
  },
  'fotografie': {
    'was_ist': [
      'Professionelle Werbefotografie und Businessfotografie ist das stärkste visuelle Kommunikationsinstrument eines Unternehmens. Bilder entscheiden in Millisekunden, ob ein Website-Besucher bleibt oder geht, ob ein Messebesucher stehen bleibt oder weiterläuft, ob ein LinkedIn-Post gescrollt oder gelikt wird. Dabei ist Authentizität entscheidend: Stockfotos werden von Ihrer Zielgruppe sofort erkannt und schaffen kein Vertrauen. Echte Bilder Ihres Teams, Ihrer Produkte und Ihres Standorts schaffen Nähe, Vertrauen und Differenzierung.',
      'Was professionelle Werbefotografie auszeichnet: sie ist zweckorientiert. Ein gutes Produktfoto für den Online-Shop hat andere Anforderungen als ein Corporate Portrait für LinkedIn oder eine Industriefotografie für den Geschäftsbericht. Licht, Bildausschnitt, Nachbearbeitung und Dateiformat sind für jeden Verwendungszweck unterschiedlich. X mind plant jedes Shooting mit Briefing vorab: Welche Bilder werden wo eingesetzt? Was sollen sie kommunizieren? Welche technischen Spezifikationen brauchen Print und Digital?',
      'Der häufigste Fehler beim Fotoshooting: fehlende Vorbereitung. Unaufgeräumte Hintergründe, Mitarbeiter ohne Information über den Shooting-Tag, Produkte die nicht druckrein geputzt sind, kein Styling-Briefing. X mind schickt für jedes Shooting eine Vorbereitungs-Checkliste und koordiniert Ablauf, Styling-Empfehlungen und Reihenfolge vorab. Damit werden 30 Minuten Vorbereitung zwei Stunden Nachbearbeitung – und das sieht man am Ergebnis.',
    ],
    'leistungen': [
      {'titel':'Corporate Portraits & Teamfotos','icon':'👤','text':'Mitarbeiterfotos, Teambilder und Geschäftsführer-Portraits für Website, LinkedIn, Unternehmensbroschüren und Pressemitteilungen. Authentisch, professionell und einheitlich – wir fotografieren ganze Teams am Unternehmensstandort oder im Studio. Inklusive Styling-Empfehlung, Bildbearbeitung und Lieferung in Web- und Druckqualität.'},
      {'titel':'Produktfotografie & Online-Shop','icon':'📦','text':'Freisteller (weißer Hintergrund), Lifestyle-Produktfotos und Detailaufnahmen für Online-Shops, Kataloge, Flyer und Werbeanzeigen. Wir fotografieren Produkte in Studio-Qualität oder am Point of Sale – sauber belichtet, farbnormiert, im WebP- und JPEG-Format für Web und Druck geliefert. Produktfotografie, die verkauft.'},
      {'titel':'Industriefotografie & Reportage','icon':'🏭','text':'Maschinen, Produktionsprozesse, Mitarbeiter bei der Arbeit, Werkstätten, Baustellen und Unternehmensstandorte. Industriefotografie für Geschäftsberichte, Messeauftritte, Website und Recruiting. Wir fotografieren auch in Produktionsumgebungen mit Schutzausrüstung, engen Platzverhältnissen und besonderen Sicherheitsanforderungen.'},
      {'titel':'Immobilienfotografie','icon':'🏠','text':'Neubauten, Bestandsimmobilien, renovierte Objekte, Innenarchitektur und Baudokumentation. Für Makler, Bauträger und Architekten: Exposé-Fotos in Profi-Qualität, HDR-Innenaufnahmen, Fassadenaufnahmen und auf Wunsch ergänzende Drohnenfotografie aus der Luft. Immobilienfotos, die Interessenten überzeugen.'},
      {'titel':'Werbefotografie & Kampagnen-Shooting','icon':'🌟','text':'Inszenierte Bilder für Kampagnen, Anzeigen, Plakate und Social Media. Location-Shooting, Model-Koordination, Styling und Requisite – wir übernehmen die Regie. Werbefotografie, die Ihre Botschaft visuell umsetzt und Zielgruppen emotional anspricht. Verwendbar für Print, Digital und Außenwerbung.'},
      {'titel':'Event- & Reportagefotografie','icon':'🎉','text':'Firmenjubiläen, Einweihungsfeiern, Messeauftritte, Workshops, Podiumsdiskussionen und Betriebsbesichtigungen. Reportagefotografie dokumentiert Events authentisch und liefert Bilder, die für interne Kommunikation, Pressemitteilungen und Social Media direkt einsetzbar sind.'},
      {'titel':'Bildbearbeitung & professionelle Lieferung','icon':'✅','text':'Bildvorauswahl innerhalb von 48 Stunden. Fertige Dateien in 5–7 Werktagen: retuschiert, farbnormiert, in WebP, JPEG und TIFF – je nach Verwendungszweck. Lieferung per sicherem Download-Link. Auf Wunsch freisteller (weißer Hintergrund), Hintergrundtausch und erweiterte Bildbearbeitung.'},
    ],
    'branchen': [
      {'name':'Handwerk & Bau','text':'Authentische Bilder von Handwerkern bei der Arbeit sind das stärkste Marketing-Instrument für Betriebe, die auf Vertrauen setzen. Wir fotografieren auf Baustellen, in Werkstätten und am Unternehmensstandort – mit dem richtigen Blick für handwerkliche Qualität.'},
      {'name':'Industrie & Maschinenbau','text':'Maschinenfotografie, Produktionsprozesse und Mitarbeiter in ihrer Arbeitsumgebung – für Geschäftsberichte, Messepräsentationen und Unternehmenswebsites. Wir fotografieren auch in Reinräumen, Produktionshallen und unter Sicherheitsauflagen.'},
      {'name':'Gastronomie & Hotellerie','text':'Speisen, Räume, Team und Atmosphäre – Gastronomie-Fotografie muss Hunger und Vorfreude wecken. Wir fotografieren Food, Interiors und Corporate Portraits für Restaurant-Websites, Social Media und Printmedien.'},
      {'name':'Immobilien & Architektur','text':'Innenräume, Fassaden, Details und Umgebung – Immobilienfotografie braucht das richtige Licht, den richtigen Ausschnitt und professionelle Nachbearbeitung. Kombiniert mit Drohnenfotografie entstehen vollständige Objekt-Dokumentationen.'},
    ],
  },
}
# Pillar-Content in THEMES einbinden
for _tk, _pc in THEMES_PILLAR.items():
    if _tk in THEMES:
        THEMES[_tk].update(_pc)

THEME_SLUGS = {
    'webdesign':'webdesign','werbeagentur':'werbeagentur','seo':'seo-agentur',
    'webagentur':'webagentur','marketing':'marketing-agentur','corporate-design':'corporate-design',
    'fotografie':'werbefotografie','drohnenfotografie':'drohnenfotografie',
}

# ══════════════════════════════════════════════════════════════════════════════
# STÄDTE-DATEN
# ══════════════════════════════════════════════════════════════════════════════
CITIES = {
  'Singen':         {'full':'Singen am Hohentwiel','region':'Hegau','intro':'Als Werbeagentur mit Sitz direkt in Singen kennen wir den lokalen Markt, die Unternehmen und die Menschen hier aus erster Hand – das macht den konkreten Unterschied zu Agenturen aus Stuttgart oder München.','note':'Ob Industriebetrieb am Hohentwiel-Ring, Handwerker in Bohlingen oder Einzelhändler in der Innenstadt – Singen ist unser Heimatmarkt. BGO Singen, MTS Singen und viele weitere regionale Betriebe zählen zu unseren langjährigen Referenzkunden.'},
  'Konstanz':       {'full':'Konstanz am Bodensee','region':'Bodenseekreis','intro':'Konstanz ist ein einzigartiger Wirtschaftsstandort: international geprägt durch Universität und Hochschule, starker Mittelstand und eine aktive Gründerszene direkt am See. Wir begleiten Konstanzer Unternehmen mit Kommunikation, die in diesem anspruchsvollen Umfeld besteht.','note':'Von der historischen Altstadt bis zum Technologiezentrum am Seerhein: Wir helfen Konstanzer Unternehmen, online sichtbar zu sein und lokal wie überregional neue Kunden zu gewinnen.'},
  'Radolfzell':     {'full':'Radolfzell am Bodensee','region':'Kreis Konstanz','intro':'Radolfzell wächst – und mit ihm die Anforderungen an einen professionellen Marktauftritt. Als Agentur direkt in der Region liefern wir schnell, persönlich und kennen Ihren lokalen Markt.','note':'Mit dem EDEKA Münchow-Eröffnungsprojekt und weiteren Radolfzeller Kunden haben wir bewiesen: Wir wissen, was lokal funktioniert und wie man in einem wachsenden Markt Sichtbarkeit aufbaut.'},
  'Überlingen':     {'full':'Überlingen am Bodensee','region':'Bodenseekreis','intro':'Überlingen am Bodensee – Kurstadt, Tourismusmagnet und Heimat vieler Handwerksbetriebe und mittelständischer Unternehmen. Wir bringen Ihre Botschaft zu den Menschen in der Region.','note':'Ob Wellnesshotel, Einzelhandel in der Fußgängerzone oder Handwerksbetrieb im Gewerbegebiet: Überlinger Unternehmen profitieren von unserer regionalen Kenntnis und unserem Netzwerk am Bodensee.'},
  'Stockach':       {'full':'Stockach','region':'Kreis Konstanz','intro':'Stockach – strategischer Knotenpunkt zwischen Bodensee, Hegau und dem Donautal. Wir begleiten Stockacher Unternehmen dabei, in einem kompetitiven Umfeld sichtbar zu bleiben und neue Kunden zu gewinnen.','note':'Von Gewerbegebieten bis zur Innenstadt: Stockacher Betriebe schätzen unsere direkte Art, die Kenntnis der gesamten Bodenseeregion und vor allem unsere Verlässlichkeit.'},
  'Tuttlingen':     {'full':'Tuttlingen','region':'Kreis Tuttlingen','intro':'Tuttlingen ist Weltmarktführer-Stadt. Die Medizintechnik-Industrie stellt höchste Anforderungen – auch an Kommunikation, digitalen Auftritt und Corporate Design. Wir liefern auf diesem Niveau.','note':'Tuttlinger Unternehmen kommunizieren mit uns auf Augenhöhe: präzise, professionell, verständlich. Wir kennen die Anforderungen einer global agierenden, exportorientierten Industrie.'},
  'Bad Dürrheim':   {'full':'Bad Dürrheim','region':'Schwarzwald-Baar-Kreis','intro':'Bad Dürrheim – Sole-Heilbad, Gesundheitsstandort und Sitz vieler Wellness- und Gesundheitsbetriebe in der Baar. Wir entwickeln Kommunikation, die diese besondere Zielgruppe erreicht.','note':'Von Kliniken über Wellnesshotels bis zu lokalen Handwerksbetrieben: Im Schwarzwald-Baar-Kreis kennen wir die Bedürfnisse von Unternehmen, die auf Qualität und Vertrauen setzen.'},
  'Donaueschingen': {'full':'Donaueschingen','region':'Schwarzwald-Baar-Kreis','intro':'Donaueschingen – Quelle der Donau, Kulturstandort und wirtschaftliches Zentrum der Baar. Unternehmen hier brauchen einen Kommunikationspartner, der die Region kennt und überregional denkt.','note':'Ob produzierendes Gewerbe, Einzelhandel oder Dienstleister: Im Raum Donaueschingen schätzen unsere Kunden die persönliche Betreuung und Ergebnisse, die messbar wirken.'},
  'Markdorf':       {'full':'Markdorf','region':'Bodenseekreis','intro':'Markdorf – die Bischofstadt am Bodensee, Heimat des Obstbaus und eines starken Mittelstands. Wir begleiten Unternehmen in Markdorf mit professioneller Kommunikation, die zum regionalen Charakter passt.','note':'Der Bodenseekreis rund um Markdorf ist ein dynamischer Wirtschaftsraum mit Tourismus, Landwirtschaft und produzierendem Gewerbe. Wir kennen die Zielgruppen und die richtigen Kanäle.'},
  'Pfullendorf':    {'full':'Pfullendorf','region':'Kreis Sigmaringen','intro':'Pfullendorf liegt im Herzen Oberschwabens – mit einem aktiven Mittelstand, starken Handwerksbetrieben und einer Lage zwischen Bodensee und Schwäbischer Alb. Wir helfen Pfullendorfer Unternehmen, online und offline Wirkung zu entfalten.','note':'Von Maschinenbau bis Einzelhandel: Im Raum Pfullendorf sind wir bekannt für verlässliche Arbeit, klare Kommunikation und Ergebnisse, die den regionalen Markt wirklich verstehen.'},
  'Schaffhausen':           {'full':'Schaffhausen (CH)','region':'Kanton Schaffhausen (CH)',
    'intro':'Schaffhausen – grenznaher Wirtschaftsstandort mit starker Industrie, bekannten Marken und internationalem Flair direkt an der deutschen Grenze. Wir betreuen Unternehmen auf beiden Seiten des Rheins mit Kommunikation, die in beiden Märkten funktioniert.',
    'note':'Die Grenzregion rund um Schaffhausen ist ein besonderer Markt: deutschsprachig, anspruchsvoll und international orientiert. Als Agentur mit 18 Jahren Erfahrung kennen wir die Spielregeln auf beiden Seiten der Grenze.'},
  # ── Schweiz & Österreich (neu) ────────────────────────────────────────────────
  'St. Gallen':  {'full':'St. Gallen (CH)','region':'Kanton St. Gallen (CH)',
    'intro':'St. Gallen ist das wirtschaftliche Zentrum der Ostschweiz – Textilgeschichte, Hochschule und ein moderner Dienstleistungssektor prägen die Stadt. Wir begleiten St. Galler Unternehmen mit Kommunikation, die in der anspruchsvollen Schweizer Unternehmenslandschaft besteht.',
    'note':'Von KMU bis zu internationalen Konzernen: Im Raum St. Gallen schätzen Kunden klare Botschaften, präzise Umsetzung und einen Ansprechpartner, der erreichbar ist – grenzüberschreitend, persönlich, verlässlich.'},
  'Zürich':      {'full':'Zürich (CH)','region':'Kanton Zürich (CH)',
    'intro':'Zürich ist die Wirtschaftshauptstadt der Schweiz – und ein Markt mit höchsten Ansprüchen. Wir entwickeln Kommunikation, die in diesem Wettbewerbsumfeld sichtbar macht: strategisch durchdacht, gestalterisch überzeugend, messbar wirksam.',
    'note':'In Zürich konkurrieren globale Agenturen um dieselben Kunden. Was uns unterscheidet: persönliche Betreuung, 18 Jahre Markterfahrung in der DACH-Region und der direkte Draht zu einem festen Ansprechpartner – nicht zu einem Call-Center.'},
  'Winterthur':  {'full':'Winterthur (CH)','region':'Kanton Zürich (CH)',
    'intro':'Winterthur ist Zürichs starker Nachbar – Industriestandort, Hochschulstadt und Heimat eines innovativen Mittelstands. Wir helfen Winterthurer Unternehmen, ihre Qualität nach außen sichtbar zu machen: digital, im Print und mit klarer Markenbotschaft.',
    'note':'Der Wirtschaftsraum Winterthur wächst. Viele Unternehmen hier sind Hidden Champions, die ihre Kommunikation professionalisieren wollen – genau das ist unser Kerngeschäft seit 18 Jahren.'},
  'Frauenfeld':  {'full':'Frauenfeld (CH)','region':'Kanton Thurgau (CH)',
    'intro':'Frauenfeld ist die Hauptstadt des Kantons Thurgau – ruhig, solide und heimat eines bodenständigen Mittelstands mit Qualitätsanspruch. Wir entwickeln Kommunikation, die zu diesen Werten passt: klar, verlässlich und auf Wirkung ausgerichtet.',
    'note':'Im Kanton Thurgau, zwischen Bodensee und dem Wirtschaftsraum Zürich gelegen, schätzen Unternehmer Direktheit und Ergebnisse. Genau das liefern wir – ohne Umwege und ohne leere Versprechen.'},
  'Basel':       {'full':'Basel (CH)','region':'Kanton Basel-Stadt (CH)',
    'intro':'Basel ist die Kulturhauptstadt der Schweiz und ein internationaler Wirtschaftsknoten: Pharma, Chemie, Messe, Kunstmarkt. Wir begleiten Basler Unternehmen mit Kommunikation, die in diesem hochkarätigen Umfeld sowohl lokal als auch international funktioniert.',
    'note':'Die Dreiländereck-Lage Basels macht die Stadt einzigartig. Wir kennen den deutsch-schweizerisch-französischen Kommunikationsraum und helfen Unternehmen, ihre Botschaft präzise und wirkungsvoll zu platzieren – in allen drei Märkten.'},
  'Bregenz':     {'full':'Bregenz (AT)','region':'Vorarlberg (AT)',
    'intro':'Bregenz am Bodensee – Landeshauptstadt Vorarlbergs und Kulturort mit internationaler Ausstrahlung. Der Wirtschaftsraum Bregenz ist eng mit dem deutschen und Schweizer Nachbarmarkt verflochten. Wir entwickeln Kommunikation, die in dieser Dreiländer-Region wirkt.',
    'note':'Vorarlberg ist das westlichste Bundesland Österreichs – mit einem dynamischen Mittelstand, hoher Exportorientierung und direkter Nachbarschaft zum deutschen und Schweizer Markt. Als Agentur aus Singen kennen wir diesen Wirtschaftsraum aus erster Hand.'},
  'Luzern':      {'full':'Luzern (CH)','region':'Kanton Luzern (CH)',
    'intro':'Luzern ist das touristische Herz der Zentralschweiz und gleichzeitig ein starker Wirtschaftsstandort – Versicherungen, Tourismus, Gesundheitswirtschaft und ein aktiver Mittelstand prägen das Bild. Wir entwickeln Kommunikation, die in diesem vielfältigen Markt Wirkung entfaltet.',
    'note':'In Luzern treffen Tradition und Innovation aufeinander. Unternehmen hier schätzen Partner, die sowohl kreativ als auch verlässlich sind – das ist unser Anspruch seit 2007.'},
  'Bodenseeregion':         {'full':'Bodensee & Hegau','region':'Bodensee & Hegau','intro':'Als Werbeagentur mit Sitz in Singen betreuen wir Unternehmen in der gesamten Bodenseeregion – von Singen über Konstanz bis Radolfzell und darüber hinaus. Lokal verankert, persönlich erreichbar.','note':'Unsere Kunden kommen aus Handwerk, Bau, Industrie, Gastronomie und dem regionalen Mittelstand. Mit über 100 aktiven Kunden und 18 Jahren Erfahrung kennen wir den Markt am Bodensee wie kein anderer.'},
  # ── Bodensee-Region (neue Städte) ──────────────────────────────────────────
  'Friedrichshafen':        {'full':'Friedrichshafen am Bodensee','region':'Bodenseekreis','intro':'Friedrichshafen ist Luft- und Raumfahrtstandort, Messestadt und wirtschaftliches Zentrum des Bodenseekreises. Unternehmen hier stehen unter Sichtbarkeitsdruck – sowohl lokal als auch überregional. Wir liefern Kommunikation, die auf diesem Niveau mitspielt.','note':'Von Zulieferern der Dornier-Industrie bis zu Gastronomiebetrieben am Hafen: In Friedrichshafen verbinden wir technisches Verständnis mit kreativem Handwerk – für Auftritte, die zu dieser Wirtschaftsregion passen.'},
  'Meersburg':              {'full':'Meersburg am Bodensee','region':'Bodenseekreis','intro':'Meersburg – Weinstadt, Tourismusmagneten und Sitz vieler kleiner, hochwertiger Betriebe direkt am Seeufer. Hier zählt Qualität mehr als Lautstärke. Unsere Kommunikation spricht genau diese Zielgruppe an: anspruchsvoll, ästhetisch, wirkungsvoll.','note':'Weinbaubetriebe, Boutique-Hotels, Kunsthandwerk und gastronomische Betriebe: In Meersburg kennen wir die sensiblen Zielgruppen und entwickeln Kommunikation, die Charakter zeigt statt Beliebigkeit.'},
  # ── Schwarzwald – mittlerer/südlicher Teil ──────────────────────────────────
  'Freiburg im Breisgau':   {'full':'Freiburg im Breisgau','region':'Stadtkreis Freiburg','intro':'Freiburg im Breisgau ist universitäre Metropole, nachhaltiger Wirtschaftsstandort und tor zum südlichen Schwarzwald. Unternehmen hier agieren in einem wettbewerbsintensiven, gebildeten Marktumfeld – Kommunikation muss Substanz haben.','note':'Vom innovativen Start-up in der Innenstadt bis zum klassischen Handwerksbetrieb im Umland: In Freiburg verbinden wir Kreativität mit strategischer Schärfe. 18 Jahre Agenturerfahrung, angewendet auf einen der dynamischsten Märkte in Baden-Württemberg.'},
  'Offenburg':              {'full':'Offenburg','region':'Ortenaukreis','intro':'Offenburg ist wirtschaftliches Herz der Ortenau – mit starkem Mittelstand, gut vernetztem Einzelhandel und einer Lage zwischen Schwarzwald und Rheinebene, die überregionale Reichweite ermöglicht. Wir helfen Offenburger Unternehmen, online wie offline präsent zu sein.','note':'Von Industriebetrieben im Gewerbegebiet bis zu Dienstleistern in der Innenstadt: Im Raum Offenburg profitieren unsere Kunden von direkter Betreuung, klaren Konzepten und Ergebnissen, die den Ortenauer Markt wirklich verstehen.'},
  'Villingen-Schwenningen': {'full':'Villingen-Schwenningen','region':'Schwarzwald-Baar-Kreis','intro':'Villingen-Schwenningen – Doppelstadt mit starker Uhren- und Präzisionstechnikindustrie und einem breiten Mittelstandsgefüge. Hier zählt Verlässlichkeit. Wir sind ein Partner, der Termine hält, klar kommuniziert und Budgets respektiert.','note':'Ob Maschinenbauer in Schwenningen, Einzelhändler in Villinger Innenstadt oder Dienstleister im Schwarzwald-Baar-Kreis: Wir kennen die regionalen Anforderungen und liefern Kommunikation auf dem Niveau dieser wirtschaftsstarken Region.'},
  'Schiltach':              {'full':'Schiltach','region':'Kreis Rottweil/Ortenaukreis','intro':'Schiltach liegt malerisch im Kinzigtal – Heimat von Hidden Champions wie Hansgrohe und einem aktiven Handwerk. Kleine Gemeinde, große Wirtschaftsleistung. Wir entwickeln Kommunikation, die dem Selbstverständnis dieser Betriebe gerecht wird.','note':'In Schiltach sind unsere Kunden oft bodenständige Unternehmen mit überregionalem Anspruch. Genau das ist unsere Stärke: lokale Verwurzelung kombiniert mit dem Blick für das große Bild.'},
  'Gengenbach':             {'full':'Gengenbach','region':'Ortenaukreis','intro':'Gengenbach – eine der schönsten Fachwerkstädte Deutschlands, lebendiger Tourismus- und Wirtschaftsstandort in der Ortenau. Unternehmen hier schätzen Ästhetik und Qualität. Unsere Kommunikation spiegelt genau das wider.','note':'Von Weingütern über Hotellerie bis zu Handwerksbetrieben: In Gengenbach kennen wir die besondere Mischung aus Tradition und modernem Wirtschaftsleben und entwickeln Auftritte, die dazu passen.'},
  'Hausach':                {'full':'Hausach','region':'Ortenaukreis','intro':'Hausach liegt im Herzen des Kinzigtals – Industrie, Handwerk und Tourismus prägen den Standort. Für Betriebe hier ist eine starke regionale Sichtbarkeit entscheidend. Wir sorgen dafür, dass Sie in Hausach und darüber hinaus gefunden werden.','note':'Unternehmen in Hausach schätzen direkte Kommunikation und verlässliche Ergebnisse. Als Agentur mit echter Verwurzelung in der Region bieten wir genau das – ohne großstädtischen Overhead, aber mit professionellem Output.'},
  'Triberg':                {'full':'Triberg im Schwarzwald','region':'Schwarzwald-Baar-Kreis','intro':'Triberg – Heimat des Schwarzwälder Kuchens, der Kuckucksuhren und eines lebendigen Tourismussektors. Betriebe hier müssen lokal und überregional wirken. Wir entwickeln Kommunikation, die Besucher anzieht und Stammkunden bindet.','note':'Vom Souvenirhandel bis zum Wellnesshotel: Im touristisch geprägten Triberg verstehen wir, was Reisende anspricht und wie Betriebe ihre Sichtbarkeit – offline und im Netz – gezielt ausbauen.'},
  # ── Ortenau und südwestlich ─────────────────────────────────────────────────
  'Kehl':                   {'full':'Kehl am Rhein','region':'Ortenaukreis','intro':'Kehl liegt direkt gegenüber Straßburg – eine einzigartige grenzüberschreitende Wirtschaftslage mit deutschen und europäischen Einflüssen. Unternehmen hier profitieren von zwei Märkten. Wir liefern Kommunikation, die in beiden funktioniert.','note':'Ob grenzüberschreitender Einzelhandel, Logistik oder Dienstleistung: In Kehl kennen wir die besondere binationale Dynamik und entwickeln Marktauftritte, die diese Stärke kommunizieren.'},
  'Lahr/Schwarzwald':       {'full':'Lahr/Schwarzwald','region':'Ortenaukreis','intro':'Lahr ist wirtschaftliches Zentrum der mittleren Ortenau – mit einer breiten Unternehmenslandschaft aus Industrie, Handel und Dienstleistung. Wir begleiten Lahre Unternehmen dabei, in einem wachsenden Markt klar und professionell zu kommunizieren.','note':'Von produzierenden Betrieben im Gewerbegebiet bis zu inhabergeführten Fachgeschäften in der Innenstadt: In Lahr/Schwarzwald liefern wir Kommunikation, die zum Unternehmen passt und messbare Ergebnisse bringt.'},
  'Oberkirch':              {'full':'Oberkirch','region':'Ortenaukreis','intro':'Oberkirch – Weinstadt, Obstbau und mittelständische Wirtschaft im Renchtal. Betriebe hier sind oft traditionell verwurzelt und suchen Partner, die Qualität und Persönlichkeit in der Kommunikation leben. Das ist X mind.','note':'Ob Weingut, Handwerksbetrieb oder regionaler Dienstleister: In Oberkirch kennen wir die bodenständige Geschäftskultur und entwickeln Kommunikation, die Vertrauen aufbaut und neue Kunden gewinnt.'},
  # ── Schwarzwald-Baar-Heuberg und Donau ─────────────────────────────────────
  'Rottweil':               {'full':'Rottweil','region':'Kreis Rottweil','intro':'Rottweil – älteste Stadt Baden-Württembergs, TestTurm-Standort von Thyssenkrupp und lebendige Wirtschaftsregion zwischen Schwarzwald und Schwäbischer Alb. Wir entwickeln Kommunikation für Betriebe, die diesen Standortstolz nach außen tragen wollen.','note':'Von Traditionsunternehmen bis zu innovativen KMU: In Rottweil schätzen unsere Kunden die direkte, ehrliche Zusammenarbeit und Ergebnisse, die den Charakter dieser wirtschaftsstarken Kreisstadt widerspiegeln.'},
  'Spaichingen':            {'full':'Spaichingen','region':'Kreis Tuttlingen','intro':'Spaichingen liegt zwischen Tuttlingen und dem Heuberg – ein aktiver Wirtschaftsstandort mit Handwerk, Industrie und einem starken regionalen Gemeinschaftsgefühl. Wir unterstützen Spaichinger Betriebe dabei, sichtbar zu wachsen.','note':'Kleine Betriebe, großer Anspruch: In Spaichingen kennen wir die Mentalität des schwäbischen Mittelstands und liefern Kommunikation, die zum Budget passt und echte Wirkung entfaltet.'},
  'Tübingen':               {'full':'Tübingen','region':'Landkreis Tübingen','intro':'Tübingen ist Universitäts- und Wissenschaftsstadt mit einem einzigartigen Mix aus Tradition, Innovation und einer kritisch-aufgeklärten Zielgruppe. Kommunikation muss hier substanziell und authentisch sein – keine leeren Versprechen.','note':'Von Biotech-Unternehmen im Gesundheitszentrum bis zu inhabergeführten Geschäften in der Altstadt: In Tübingen entwickeln wir Kommunikation mit intellektuellem Anspruch und handwerklicher Qualität.'},
  'Rottenburg am Neckar':   {'full':'Rottenburg am Neckar','region':'Landkreis Tübingen','intro':'Rottenburg am Neckar – Bischofssitz, Weinstadt und wirtschaftsstarkes Mittelzentrum im Neckartal. Betriebe hier schätzen Verlässlichkeit und persönliche Betreuung. Genau das bieten wir – seit 18 Jahren.','note':'Von Weingütern über Handwerksbetriebe bis zu lokalen Dienstleistern: Im Raum Rottenburg am Neckar kennen wir die Erwartungen einer Region, die Qualität nicht nur produziert, sondern auch in der Kommunikation erwartet.'},
}

# ══════════════════════════════════════════════════════════════════════════════
# STÄDTE-EXTRA: Wirtschaft, Branchen, Standort – erzeugt unique Content pro Seite
# ══════════════════════════════════════════════════════════════════════════════
CITIES_EXTRA = {
  'Singen': {
    'wirtschaft': 'Singen am Hohentwiel ist der wirtschaftliche Anker des Hegau – mit einer für süddeutsche Mittelstädte ungewöhnlich breiten Industriebasis. Metallverarbeitung, Maschinenbau und Nahrungsmittelindustrie prägen das Stadtbild: Maggi (Nestlé), Georg Fischer und zahlreiche mittelständische Zulieferbetriebe machen Singen zu einer exportstarken Industriestadt mit überregionaler Bedeutung. Gleichzeitig wächst der Dienstleistungssektor: Gesundheitsversorgung, Einzelhandel und handwerksnahe Betriebe bedienen eine Region mit rund 45.000 Einwohnern. Als Kreisstadt des Landkreises Konstanz hat Singen auch Verwaltungs- und Versorgungsfunktion für das gesamte Hegau.',
    'branchen': ['Metallverarbeitung & Maschinenbau (Georg Fischer, Zulieferer)', 'Nahrungsmittelindustrie & Lebensmittelhandel (Maggi/Nestlé-Umfeld)', 'Einzel- und Fachhandel (Innenstadt & Hegau-Center)', 'Handwerk & Bauwirtschaft', 'Gesundheit, Pflege & medizinische Versorgung'],
    'standort': 'Der Wirtschaftsraum Singen erstreckt sich vom Hohentwiel-Ring über die Gewerbegebiete in Bohlingen bis nach Rielasingen-Worblingen. Innenstadt, Hegau-Center und die stark frequentierte B34 sind wichtige Handels- und Gewerbeachsen. Als Standort direkt an der Schweizer Grenze profitiert Singen zudem von grenzüberschreitendem Kundenverkehr.',
  },
  'Konstanz': {
    'wirtschaft': 'Konstanz ist die bevölkerungsreichste Stadt am deutschen Bodenseeufer und ein Wirtschaftsstandort mit besonderem Profil. Die Universität Konstanz und die HTWG Hochschule Konstanz bringen jährlich Tausende Studierende und qualifizierte Fachkräfte in die Stadt – ein Umfeld, das Technologie- und Dienstleistungsunternehmen anzieht. Tourismus und Gastronomie profitieren von Millionen Tagestouristen pro Jahr. Der Technologiepark am Seerhein ist Heimat innovativer Unternehmen aus IT, Medizintechnik und Ingenieurwesen. Die direkte Grenznähe zur Schweiz schafft zusätzliche wirtschaftliche Dynamik.',
    'branchen': ['Tourismus, Gastronomie & Bodensee-Hotellerie', 'Technologie & IT (HTWG- und Uni-Umfeld)', 'Gesundheit & medizinische Versorgung', 'Einzelhandel Altstadt & Ladenstraßen', 'Bildung, Beratung & professionelle Dienstleistungen'],
    'standort': 'Von der Altstadt am Konzilgebäude über den Stadtgarten bis zum Technologiezentrum Konstanz am Seerhein sind die Wirtschaftslagen vielfältig. Fischmarkt, Marktstätte und Hussengasse sind gastronomische und Handelszentren; Schneckenburg und Langenrain beherbergen Handwerks- und Gewerbebetriebe. Die Schweizer Grenze in Kreuzlingen liegt nur wenige Minuten entfernt.',
  },
  'Radolfzell': {
    'wirtschaft': 'Radolfzell am Bodensee ist eine Stadt im Wandel: Wachsende Bevölkerung, neue Wohngebiete und eine lebendige Innenstadt treffen auf eine solide wirtschaftliche Basis. Einzelhandel, Handwerk und lokale Dienstleister prägen das Stadtbild, ergänzt durch Gesundheits- und Pflegeeinrichtungen sowie einen wachsenden Dienstleistungssektor. Die Lage zwischen Singen und Konstanz macht Radolfzell zu einem attraktiven Wohn- und Wirtschaftsstandort mit eigenem Profil. Unternehmen profitieren von einer loyalen, kaufkraftstarken Bevölkerung und einem wachsenden Einzugsgebiet.',
    'branchen': ['Einzel- und Lebensmittelhandel (EDEKA, Fachhändler)', 'Handwerk & Bau', 'Gesundheit, Pflege & Therapie', 'Gastronomie & Bodensee-Tourismus (Mettnau)', 'Freie Berufe & lokale Dienstleistungen'],
    'standort': 'Die Innenstadt rund um den Marktplatz und die Seestraße ist das wirtschaftliche Herz Radolfzells. Die Industriegebiete westlich der Bahn beherbergen Handwerks- und Produktionsbetriebe. Der Campingplatz Markelfingen und die Mettnau-Halbinsel machen Radolfzell zum Ausflugsziel – eine Zielgruppe, die auch stationäre Betriebe nutzen können.',
  },
  'Überlingen': {
    'wirtschaft': 'Überlingen ist staatlich anerkanntes Kneipp-Heilbad und einer der schönsten Fremdenverkehrsorte am Bodensee. Diese Doppelrolle prägt die gesamte Wirtschaft: Tourismus, Hotellerie und Gastronomie bilden das Rückgrat, ergänzt durch einen starken Einzelhandel in der Fußgängerzone und zahlreiche Gesundheits- und Wellnessanbieter. Gleichzeitig ist Überlingen Wohnort vieler Pendler nach Friedrichshafen und Konstanz – eine kaufkraftstarke Bevölkerung mit hohen Ansprüchen an lokale Qualität und Dienstleistung.',
    'branchen': ['Hotellerie, Wellness & Kurbetrieb', 'Gastronomie & Bodensee-Tourismus', 'Fachhandel & Innenstadt (Fußgängerzone)', 'Handwerk & Bauwirtschaft', 'Gesundheit, Therapie & medizinische Versorgung'],
    'standort': 'Die historische Altstadt mit der Münsterkirche, die Fußgängerzone und das Seeufer sind die wirtschaftlichen Kernlagen Überlingens. Das Gewerbegebiet in Lippertsreute beherbergt Handwerker und Produzenten. Die Nähe zu Salem, Owingen und Heiligenberg erweitert das Einzugsgebiet deutlich.',
  },
  'Stockach': {
    'wirtschaft': 'Stockach ist ein solider Wirtschaftsstandort im westlichen Bodenseekreis – bekannt für seinen starken Mittelstand, eine gut aufgestellte Handwerksbranche und seine Funktion als Versorgungszentrum für die umliegenden Gemeinden. Die direkte Lage an der A98 und die Verbindung nach Konstanz, Singen und ins Donautal machen Stockach logistisch attraktiv. Das breite Einzugsgebiet Richtung Meßkirch, Eigeltingen und dem westlichen Bodenseeraum sichert eine stabile regionale Kundschaft.',
    'branchen': ['Handwerk & Bau', 'Einzelhandel & regionale Versorgung', 'Automobildienstleistungen & Kfz-Gewerbe', 'Gastronomie & lokale Veranstaltungen', 'Logistik, Transport & Spedition'],
    'standort': 'Das Stadtzentrum rund um den Adlerplatz, das Gewerbegebiet im Süden und die Zufahrtsachsen zur A98 sind die wirtschaftlichen Schwerpunkte. Stockach versorgt ein breites Umland: Bodman-Ludwigshafen, Eigeltingen und Hohenfels gehören zum natürlichen Einzugsgebiet.',
  },
  'Tuttlingen': {
    'wirtschaft': 'Tuttlingen ist weltweit bekannt als Zentrum der Medizintechnik: Über 400 Unternehmen der Branche – darunter Aesculap (B. Braun), Karl Storz und Hipp – machen die Stadt zur globalen Nummer eins für Chirurginstrumente und Endoskopie. Diese wirtschaftliche Konzentration stellt besondere Anforderungen an Kommunikation: Mehrsprachigkeit, internationale Messepräsenz, technisches Verständnis und professionelles Corporate Design sind hier kein Luxus, sondern Pflicht. Daneben existiert ein vielfältiger Mittelstand aus Handwerk, Handel und Dienstleistung.',
    'branchen': ['Medizintechnik & Chirurgieinstrumente (Weltmarktführer-Cluster)', 'Maschinenbau & Präzisionstechnik', 'Handwerk & Bauwirtschaft Kreis Tuttlingen', 'Fachhandel & Einzelhandel Innenstadt', 'Exportorientierte Industrie & internationale Unternehmenskommunikation'],
    'standort': 'Tuttlingen liegt an Donau und A81. Das Industriegebiet Nordbahnhof, die Innenstadt und der Messeplatz sind die wichtigsten Wirtschaftslagen. Das Umland (Mühlheim, Emmingen-Liptingen, Aldingen) stärkt die regionale Nachfrage erheblich.',
  },
  'Bad Dürrheim': {
    'wirtschaft': 'Bad Dürrheim ist staatlich anerkanntes Mineral- und Moorheilbad – das prägt die gesamte Wirtschaft. Gesundheitstourismus, Kliniken, Wellnessanbieter und Kurbetriebe dominieren das Bild. Das Solemar, Reha-Kliniken und ein aktives Vereinsleben schaffen einen eigenständigen Wirtschaftsraum. Gleichzeitig profitiert Bad Dürrheim von der Nähe zu Villingen-Schwenningen und Donaueschingen. Die Zielgruppe ist gesundheitsbewusst, qualitätsorientiert und bereit, für gute Leistung entsprechend zu bezahlen.',
    'branchen': ['Wellness, Kur & Gesundheitstourismus (Solemar)', 'Reha-Kliniken & ambulante Therapie', 'Hotellerie & Ferienwohnungen', 'Einzelhandel & Dienstleistungen für Kurgäste', 'Handwerk & lokale Versorgung Schwarzwald-Baar'],
    'standort': 'Bad Dürrheim liegt zentral in der Baar auf rund 700 Metern Höhe. Das Sole-Erlebnisbad Solemar, die Kurparkanlagen und die Fußgängerzone sind die zentralen Wirtschaftsmagnete. Das Einzugsgebiet reicht bis Villingen-Schwenningen (15 km) und Donaueschingen (12 km).',
  },
  'Donaueschingen': {
    'wirtschaft': 'Donaueschingen ist kulturelles und wirtschaftliches Zentrum des Schwarzwald-Baar-Kreises. Die Stadtgeschichte ist eng mit dem Fürstenhaus Fürstenberg verbunden. Wirtschaftlich ist die Stadt gut aufgestellt: Einzelhandel, Handwerk und regionale Dienstleister bedienen eine kaufkraftstarke Bevölkerung. Das Gewerbegebiet beherbergt mittelständische Betriebe aus Produktion und Logistik. Die Donaueschinger Musiktage, international bekanntes Festival für zeitgenössische Musik, schaffen zusätzliche Aufmerksamkeit und kulturelle Strahlkraft.',
    'branchen': ['Einzelhandel & Versorgungszentrum Schwarzwald-Baar', 'Handwerk & Bauwirtschaft', 'Kultur & Eventwirtschaft (Donaueschinger Musiktage)', 'Logistik, Transport & Gewerbe', 'Gastronomie & regionale Hotellerie'],
    'standort': 'Die Stadtmitte mit Fürstenschloss, Donauquelle und Karlstraße sind die zentralen Lagen. Das Gewerbegebiet südlich der Bahn beherbergt Produktions- und Logistikbetriebe. Das Umland (Hüfingen, Blumberg, Geisingen) zählt zum regionalen Einzugsgebiet.',
  },
  'Markdorf': {
    'wirtschaft': 'Markdorf ist als „Bischofstadt" historisch geprägt und gleichzeitig ein aktiver Wirtschaftsstandort im Bodenseekreis. Der Obstbau, für den die gesamte Region bekannt ist, schafft ein Netzwerk aus Hofläden, Direktvermarktern und Lebensmittelverarbeitern. Handwerk und mittelständische Unternehmen ergänzen das wirtschaftliche Bild. Die Lage zwischen Friedrichshafen (15 km) und Überlingen (12 km) macht Markdorf zu einem attraktiven Wohnstandort mit eigenem wirtschaftlichem Profil und loyaler Einwohnerschaft.',
    'branchen': ['Obstbau & Direktvermarktung Bodenseeregion', 'Handwerk & Bauwirtschaft', 'Einzelhandel & Nahversorgung', 'Dienstleistungen für Wohnbevölkerung', 'Tourismus & Ausflugsgastronomie'],
    'standort': 'Die historische Altstadt mit Hexenturm, Stiftskirche und Rathausplatz ist das Herzstück. Das Gewerbegebiet im Norden beherbergt Handwerker und Gewerbebetriebe. Das Umland – Salem, Bermatingen, Immenstaad – gehört zum natürlichen Einzugsgebiet.',
  },
  'Pfullendorf': {
    'wirtschaft': 'Pfullendorf ist Mittelzentrum im Landkreis Sigmaringen und Wirtschaftszentrum Oberschwabens zwischen Bodensee und Schwäbischer Alb. Die Stadt ist bekannt für einen aktiven Mittelstand und solide handwerkliche Strukturen. Der Einfluss der Liebherr-Gruppe aus dem Umland ist spürbar, ebenso das Bundeswehr-Umfeld aus Stetten am kalten Markt. Der Einzelhandel in der Innenstadt versorgt ein breites Umland mit Gemeinden wie Meßkirch, Wald und Illmensee.',
    'branchen': ['Maschinenbau & Metallverarbeitung (Oberschwaben)', 'Handwerk & Bauwirtschaft', 'Einzelhandel & Innenstadt', 'Gastronomie & Hotellerie', 'Dienstleistungen, freie Berufe & Handelsgewerbe'],
    'standort': 'Die Innenstadt und das Gewerbegebiet Röhrenbach sind die wirtschaftlichen Schwerpunkte. Pfullendorf versorgt Gemeinden wie Meßkirch, Wald und Illmensee. Die A98-Nähe verbindet Richtung Bodensee und Donau.',
  },
  'Friedrichshafen': {
    'wirtschaft': 'Friedrichshafen ist einer der bedeutendsten Industrie- und Technologiestandorte Südwestdeutschlands. ZF Friedrichshafen (Antriebstechnik), MTU Aero Engines und Airbus Defence & Space prägen das wirtschaftliche Bild. Als Messestadt ist Friedrichshafen überregional bekannt: Eurobike, AERO und Outdoor sind international bedeutende Fachmessen. Der Bodensee-Tourismus und das Zeppelin-Museum schaffen eine wichtige zweite wirtschaftliche Säule. Unternehmen hier agieren oft im internationalen Umfeld und haben entsprechend hohe Ansprüche an Kommunikation.',
    'branchen': ['Luft- & Raumfahrttechnik, Automobilzulieferung (ZF, MTU, Airbus)', 'Messe & Veranstaltungswirtschaft', 'Tourismus, Gastronomie & Bodensee-Hotellerie', 'Technologie-Start-ups & innovativer Mittelstand', 'Handel & Dienstleistungen (Oberzentrum Bodenseekreis)'],
    'standort': 'Vom Zeppelin-Museum am Hafen über die Friedrichstraße bis zu den Industriegebieten in Löwental und Fischbach erstreckt sich die wirtschaftliche Vielfalt. Die Messe und der Bodensee-Airport sind überregionale Anker. Das Umland (Meckenbeuren, Tettnang, Kressbronn) gehört zum natürlichen Einzugsgebiet.',
  },
  'Meersburg': {
    'wirtschaft': 'Meersburg ist eine der meistbesuchten Tourismusdestinationen am Bodensee. Das malerische Stadtbild mit der ältesten bewohnten Burg Deutschlands, den Weinlagen am Seehang und dem historischen Stadtkern zieht Hunderttausende Besucher jährlich an. Wirtschaftlich dominieren Hotellerie, Gastronomie, Weinbau und hochwertige Fachgeschäfte. Die Zielgruppe ist anspruchsvoll: Übernachtungsgäste, Tagestouristen und kaufkraftstarke Einheimische erwarten Qualität – in Produkt und Kommunikation.',
    'branchen': ['Boutique-Hotellerie & gehobene Gastronomie', 'Weinbau & Direktvermarktung Bodensee', 'Kunsthandwerk & inhabergeführte Fachgeschäfte', 'Fähre & Bodensee-Tourismusdienstleistungen', 'Immobilien & hochwertige Ferienvermietung'],
    'standort': 'Die Ober- und Unterstadt, das Seeufer mit Schiffsanleger und die Weinberge bilden die wirtschaftlichen Lagen. Meersburg ist eng mit Stetten, Daisendorf und Hagnau verbunden – zusammen das bekannte Weinbaugebiet Meersburg.',
  },
  'Freiburg im Breisgau': {
    'wirtschaft': 'Freiburg im Breisgau ist mit rund 230.000 Einwohnern die viertgrößte Stadt Baden-Württembergs und eines der dynamischsten Wirtschaftszentren des Landes. Die Albert-Ludwigs-Universität und das Fraunhofer-Institut machen Freiburg zu einem Innovations-Hub. Bekannt ist die Stadt für ihre Solartechnik-Industrie und Pionierrolle in Sachen Nachhaltigkeit. Tourismus, das Universitätsklinikum und ein lebhafter Einzelhandel bilden weitere Wirtschaftssäulen. Das Wettbewerbsumfeld ist intensiv – Kommunikation muss hier Substanz haben.',
    'branchen': ['Technologie, Solar & Umwelttechnik', 'Gesundheit & Universitätsklinikum Freiburg', 'Startup-Ökosystem & Gründerszene', 'Tourismus & Schwarzwald-Gastronomie', 'Einzelhandel, Fachhandel & universitätsnahes Gewerbe'],
    'standort': 'Von der Altstadt mit dem Freiburger Münster über den Technologiepark, das Industriegebiet Haid und das Stühlinger-Viertel bis nach Gundelfingen und Merzhausen: Freiburg bietet vielfältige Wirtschaftslagen. Das Umland (Breisach, Emmendingen, Staufen) zählt zum erweiterten Einzugsgebiet.',
  },
  'Offenburg': {
    'wirtschaft': 'Offenburg ist das Oberzentrum der Ortenau und größte Stadt des Landkreises. Als Eisenbahnknoten zwischen Basel, Karlsruhe und dem Schwarzwald hat Offenburg eine wichtige Verkehrsfunktion. Wirtschaftlich ist die Stadt vielfältig: Medienunternehmen (Hubert Burda Media hat hier Wurzeln), mittelständische Industrie, Einzelhandel und ein wachsender Bildungssektor mit der Hochschule Offenburg prägen das Bild. Die Ortenau zählt zu den wirtschaftsstärksten Landkreisen Baden-Württembergs.',
    'branchen': ['Medien & Verlagswesen (Burda-Tradition)', 'Industrie & Maschinenbau Ortenaukreis', 'Einzelhandel & Innenstadt-Gastronomie', 'Bildung & Hochschule Offenburg', 'Handwerk & Bauwirtschaft im Ortenaukreis'],
    'standort': 'Stadtzentrum mit Hauptstraße und Fischmarkt, das Gewerbegebiet Elgersweier und die Stadtteile sind die Kernlagen. Das Einzugsgebiet reicht von Lahr bis Kehl und weit in die Rheinebene und den Schwarzwald hinein.',
  },
  'Villingen-Schwenningen': {
    'wirtschaft': 'Villingen-Schwenningen ist die zweitgrößte Stadt Baden-Württembergs ohne Stadtkreis-Status und wirtschaftliches Zentrum des Schwarzwald-Baar-Kreises. Die Uhrenindustrie hat hier tiefe Wurzeln – Kienzle, Mauthe und Junghans prägten das Gesicht Schwenningens. Heute dominieren Präzisionstechnik, Maschinenbau und ein vielfältiger Mittelstand. Villingen hat ein starkes Innenstadtprofil mit Einzelhandel hinter der mittelalterlichen Ringmauer. Die Duale Hochschule sorgt für gut ausgebildete Fachkräfte vor Ort.',
    'branchen': ['Uhren- & Präzisionstechnik (historisch & modern)', 'Maschinenbau & Fertigungstechnik', 'Einzelhandel Villingen Innenstadt & Schwenningen-City', 'Gesundheit & medizinische Versorgung', 'Bildung, Handwerk & lokale Dienstleistungen'],
    'standort': 'Die historische Ringmauer-Stadt Villingen mit Münster und Fußgängerzone einerseits, das Industriegebiet Schwenningen andererseits – diese Doppelstruktur prägt alles. Das Gewerbegebiet Herdenen und das Technologiezentrum Schwarzwald-Baar sind wichtige Unternehmensstandorte.',
  },
  'Schiltach': {
    'wirtschaft': 'Schiltach liegt malerisch im Kinzigtal und ist bekannt als Stammort von Hansgrohe – einem der weltweit führenden Hersteller von Armaturen und Duschsystemen. Diese Präsenz eines globalen Marktführers prägt die gesamte Unternehmenskultur der Kleinstadt: Zulieferer, Handwerker und lokale Dienstleister orientieren sich an hohen Qualitätsstandards. Das Kinzigtal mit seiner Mischung aus Tourismus und Industrieproduktion schafft ein einzigartiges wirtschaftliches Umfeld mit Substanz.',
    'branchen': ['Armaturenproduktion & Hansgrohe-Ökosystem', 'Handwerk & Metallverarbeitung Kinzigtal', 'Tourismus & Schwarzwald-Gastronomie', 'Holzwirtschaft & Forstwirtschaft', 'Lokaler Einzelhandel & Nahversorgung'],
    'standort': 'Das historische Fachwerktadtzentrum und das Hansgrohe-Industriegelände am Kinzigufer bilden die wirtschaftlichen Pole. Schiltach versorgt Gemeinden wie Lehengericht, Wolfach und Haslach. Die touristische Attraktivität durch Freilichtmuseum und Kinzigtäler Wanderwege ergänzt den Standort.',
  },
  'Gengenbach': {
    'wirtschaft': 'Gengenbach ist eine der besterhaltenen Fachwerkstädte Deutschlands und als solche ein Tourismusmagnet in der Ortenau. Der weltbekannte Adventskalender am Rathaus – der größte der Welt – macht die Stadt auch international bekannt und beschert dem lokalen Handel einen starken Saisoneffekt. Wirtschaftlich tragen Tourismus, Gastronomie und Hotellerie die Hauptlast. Daneben gibt es einen aktiven Weinbau, Handwerksbetriebe und regionale Dienstleister. Die Nähe zu Offenburg schafft gute Verbindungen.',
    'branchen': ['Tourismus, Hotellerie & Gastronomie', 'Weinbau & Direktvermarktung Ortenau', 'Handwerk & Bau', 'Einzelhandel & inhabergeführte Fachgeschäfte', 'Event & Kulturwirtschaft (Adventskalender-Standort)'],
    'standort': 'Das historische Stadtzentrum mit Rathaus, Niggelturm und Kinzig-Uferpromenade ist der wirtschaftliche und touristische Kern. Die umliegenden Weinberge sind bekannte Ortenauer Weinlagen. Gemeinden wie Biberach, Ortenberg und Berghaupten bilden das nähere Einzugsgebiet.',
  },
  'Hausach': {
    'wirtschaft': 'Hausach ist ein aktives Wirtschaftszentrum im mittleren Kinzigtal. Als wichtiger Bahnknotenpunkt – hier zweigt die Schwarzwaldbahn nach Freudenstadt ab – hat Hausach eine bedeutende Verkehrsfunktion. Industrie und Handwerk sind stark vertreten, ergänzt durch Einzelhandel und Gastronomie für die lokale Bevölkerung. Das Hansele-Museum und die Narrenzunft machen Hausach auch kulturell bekannt. Holzwirtschaft und Tourismus im Kinzigtal schaffen zusätzliche wirtschaftliche Impulse.',
    'branchen': ['Industrie & Maschinenbau Kinzigtal', 'Holzwirtschaft & Forstwirtschaft', 'Einzelhandel & Nahversorgung', 'Gastronomie & Schwarzwald-Tourismus', 'Handwerk & Bauwirtschaft'],
    'standort': 'Das Stadtzentrum und die Industriegebiete entlang der Kinzig bilden die Kernlagen. Hausach versorgt Gemeinden wie Gutach, Wolfach und Hornberg. Die Schwarzwaldbahn-Anbindung verbindet Richtung Offenburg und Konstanz.',
  },
  'Triberg': {
    'wirtschaft': 'Triberg ist eine der bekanntesten Tourismusdestinationen im Schwarzwald. Die Triberger Wasserfälle – mit über 163 Metern Deutschlands höchste – ziehen jährlich Hunderttausende Besucher an. Kuckucksuhr-Läden, Schwarzwälder Spezialitäten und das Schwarzwald-Museum prägen das touristische Angebot. Die Wirtschaft ist fast vollständig auf Tourismus und Gastronomie ausgerichtet. Betriebe hier müssen gleichzeitig lokal für Einheimische und überregional für Reisende präsent sein.',
    'branchen': ['Tourismus & Schwarzwald-Gastronomie (Wasserfälle)', 'Kuckucksuhr-Handel & Schwarzwald-Souvenirs', 'Hotellerie & Ferienwohnungen', 'Spezialitäten-Einzelhandel & Lebensmittel', 'Handwerk & lokale Versorgung der Bevölkerung'],
    'standort': 'Der Wasserfall-Bereich, die Hauptstraße mit Souvenirläden und die umliegenden Hotels bilden das wirtschaftliche Zentrum. Triberg liegt im Schwarzwald-Baar-Kreis; Gemeinden wie Schonach, Schönwald und St. Georgen gehören zum Einzugsgebiet.',
  },
  'Kehl': {
    'wirtschaft': 'Kehl am Rhein ist die einzige deutsche Stadt, die direkt an die Europastadt Straßburg (Frankreich) angrenzt. Diese einzigartige Lage schafft besondere wirtschaftliche Chancen: Grenzhandel, Einkaufstourismus aus dem Elsass und deutsch-französische Unternehmen profitieren von der Doppellage. Der neue Bahnhof Kehl und die Straßenbahnverbindung nach Straßburg haben die Verflechtung nochmals verstärkt. Logistik, Einzelhandel und Dienstleistungen für ein binationales Einzugsgebiet prägen die lokale Wirtschaft.',
    'branchen': ['Grenzhandel & Einkaufstourismus (DE/FR)', 'Logistik & Transport (Rheinhafen)', 'Einzelhandel & Gastronomie', 'Dienstleistungen für binationale Unternehmen', 'Handwerk & Bau Ortenaukreis'],
    'standort': 'Stadtzentrum, Rheinhafen, das Einkaufszentrum Forum und die Grenzbrücke nach Straßburg sind die wirtschaftlichen Kernlagen. Kehl versorgt deutsche Einwohner und zieht Einkaufstouristen aus dem Elsass an. Die Europa-Dimension macht Kehl zu einem einzigartigen Standort.',
  },
  'Lahr/Schwarzwald': {
    'wirtschaft': 'Lahr/Schwarzwald ist mit rund 48.000 Einwohnern die drittgrößte Stadt im Ortenaukreis und ein eigenständiges wirtschaftliches Zentrum. Der Lahr Airport – ehemaliger kanadischer Militärflughafen – beherbergt heute ein Gewerbezentrum mit Unternehmen aus Logistik, Industrie und Technologie. Textilindustrie und Maschinenbau haben in Lahr Tradition; heute ergänzen ein starker Einzelhandel und ein wachsendes Dienstleistungsangebot das Bild. Die Lage an der A5 erhöht die logistische Attraktivität erheblich.',
    'branchen': ['Industrie & Maschinenbau (Airport-Gewerbezentrum)', 'Einzelhandel & Innenstadt-Gastronomie', 'Textilindustrie & Bekleidungshandel (Tradition)', 'Handwerk & Bauwirtschaft', 'Logistik & Transport (A5-Lage)'],
    'standort': 'Die Innenstadt mit Marktstraße und Rathausplatz, das Airport-Gewerbezentrum und die Gewerbegebiete im Osten sind die wichtigsten Wirtschaftslagen. Lahr versorgt Gemeinden wie Ettenheim, Kippenheim und Mahlberg. Das Umland reicht in die Rheinebene und den unteren Schwarzwald.',
  },
  'Oberkirch': {
    'wirtschaft': 'Oberkirch ist das Zentrum der nördlichen Ortenau und bekannt für intensiven Wein- und Obstbau. Das Renchtal gehört zu den bedeutendsten Weinbaugebieten Badens. Neben der Landwirtschaft prägen Handwerk, mittelständische Industrie und lokale Dienstleister das Wirtschaftsbild. Die Sommerrodelbahn und die Schwarzwaldbahn-Haltestelle machen Oberkirch auch touristisch attraktiv. Die historische Altstadt mit Hochburg-Ruine ist ein zusätzlicher Anziehungspunkt für Besucher aus der Region.',
    'branchen': ['Weinbau & Obstwirtschaft Renchtal', 'Handwerk & Bau', 'Einzelhandel & Nahversorgung', 'Gastronomie & Schwarzwald-Tourismus', 'Lokale Industrie & Mittelstand Ortenau'],
    'standort': 'Die historische Innenstadt, das Renchtal und die umliegenden Weinberge bilden die wirtschaftlichen Lagen. Oberkirch versorgt Gemeinden wie Renchen, Appenweier und Lauf. Die Bahnanbindung über Achern erschließt größere Märkte Richtung Straßburg und Baden-Baden.',
  },
  'Rottweil': {
    'wirtschaft': 'Rottweil ist die älteste Stadt Baden-Württembergs und hat als Wirtschaftsstandort eine bemerkenswerte Renaissance erlebt. Der TestTurm von thyssenkrupp – mit 246 Metern einer der höchsten Aussichtstürme Deutschlands – ist zum neuen Wahrzeichen geworden und bringt internationales Renommee. Wirtschaftlich ist Rottweil solide aufgestellt: Maschinenbau, Präzisionstechnik und ein aktiver Mittelstand, ergänzt durch Einzelhandel und Gastronomie in der gut erhaltenen historischen Altstadt.',
    'branchen': ['Maschinenbau & Präzisionstechnik', 'TestTurm-Tourismus & Industrietourismus', 'Historische Altstadt & inhabergeführter Einzelhandel', 'Handwerk & Bauwirtschaft Kreis Rottweil', 'Dienstleistungen & freie Berufe'],
    'standort': 'Das historische Stadtzentrum mit Kapellenkirche und Hochbrücktorstraße und das TestTurm-Areal sind die wirtschaftlichen Anker. Rottweil versorgt Gemeinden wie Schramberg, Deilingen und Deißlingen. Die Lage an A81 und B14 sichert gute regionale Erreichbarkeit.',
  },
  'Spaichingen': {
    'wirtschaft': 'Spaichingen liegt zwischen Tuttlingen und dem Heuberg – ein aktiver Wirtschaftsstandort mit starker Handwerks- und Industriekultur. Der Dreifaltigkeitsberg über der Stadt ist Wallfahrtsort und Ausflugsziel zugleich. Wirtschaftlich dominieren Metallverarbeitung, Maschinenbau und Automobilzulieferung – geprägt von der Nähe zum Medizintechnik-Cluster Tuttlingen. Handwerk, Einzelhandel und Gastronomie versorgen die einheimische Bevölkerung und Ausflugsgäste.',
    'branchen': ['Metallverarbeitung & Automobilzulieferung', 'Handwerk & Bau Heuberg/Kreis Tuttlingen', 'Einzelhandel & Nahversorgung', 'Gastronomie & Wallfahrtstourismus (Dreifaltigkeitsberg)', 'Medizintechnik-Zulieferer (Tuttlingen-Cluster-Nähe)'],
    'standort': 'Innenstadt, Gewerbegebiete am Stadtrand und der Dreifaltigkeitsberg bilden die wirtschaftlichen Lagen. Spaichingen versorgt Gemeinden wie Aldingen, Rietheim-Weilheim und Gosheim. Die Nähe zur A81 verbessert die regionale Erreichbarkeit.',
  },
  'Tübingen': {
    'wirtschaft': 'Tübingen ist eine der bedeutendsten Universitätsstädte Deutschlands. Die Eberhard Karls Universität – eine der ältesten deutschen Hochschulen – und das Universitätsklinikum prägen das Stadtbild fundamental. Die Wirtschaft profitiert vom Wissenstransfer: Biotech, Medizintechnik und forschungsnahe Unternehmen sind stark vertreten. Start-ups aus dem Universitätsumfeld und eine kritisch-aufgeklärte Konsumentenschaft stellen besondere Anforderungen an Kommunikation: authentisch, substanziell und ohne leere Versprechen.',
    'branchen': ['Universität, Forschung & Biotech (BioRegion Tübingen)', 'Universitätsklinikum & Medizin', 'Einzelhandel & inhabergeführte Altstadt-Geschäfte', 'Tourismus & Kulturwirtschaft (Neckar, Stocherkähne)', 'IT, Software & Startup-Ökosystem'],
    'standort': 'Die mittelalterliche Altstadt mit Hölderlinturm und Marktplatz, die Wilhelmstraße mit Uni-Gebäuden und das Gesundheitszentrum am Schnarrenberg sind die wirtschaftlichen Kernlagen. Das Umland (Rottenburg, Mössingen, Kirchentellinsfurt) gehört zum natürlichen Einzugsgebiet.',
  },
  'Rottenburg am Neckar': {
    'wirtschaft': 'Rottenburg am Neckar ist Bischofssitz der Diözese Rottenburg-Stuttgart – der größten deutschen Diözese – und gleichzeitig eine wirtschaftsaktive Mittelstadt. Weinbau in der Schönbühl-Lage, Handwerk und Industrie prägen die Wirtschaft. Die Römerstraße und der Neckar-Radweg machen Rottenburg zu einem Tourismusstandort. Als Mittelzentrum versorgt die Stadt Gemeinden zwischen Tübingen und dem Oberen Gäu und hat damit ein breites, stabiles Einzugsgebiet.',
    'branchen': ['Kirche, Bildung & soziale Einrichtungen (Diözese)', 'Weinbau & Gastronomie Neckartal', 'Handwerk & Bauwirtschaft', 'Einzelhandel & Nahversorgung Mittelzentrum', 'Dienstleistungen & freie Berufe'],
    'standort': 'Die Altstadt mit dem Dom, der Marktgasse und den Neckarbastionen, das Gewerbegebiet an der Baisinger Straße und die Stadtteile Wurmlingen und Ergenzingen sind wirtschaftliche Schwerpunkte. Das Umland (Ammerbuch, Starzach, Gärtringen) gehört zum erweiterten Einzugsgebiet.',
  },
  'Schaffhausen': {
    'wirtschaft': 'Schaffhausen ist der nördlichste Kanton der Schweiz und wirtschaftlich eng mit Deutschland verflochten. Die Stadt ist bekannt für Georg Fischer AG (GF), einen der führenden Industrie- und Automobilzulieferer weltweit, und IWC Schaffhausen – eine der renommiertesten Uhrenmarken der Schweiz. Der Rheinfall als meistbesuchte Natursehenswürdigkeit der Schweiz treibt den Tourismus an. Die günstigen Unternehmenssteuer und die Grenznähe zu Singen (15 km) machen Schaffhausen zu einem attraktiven Wirtschaftsstandort für DACH-Unternehmen.',
    'branchen': ['Industrie & Maschinenbau (Georg Fischer / GF)', 'Luxusuhren & Präzisionsmechanik (IWC Schaffhausen)', 'Tourismus & Rheinfall-Besucher', 'Grenzhandel & Einkaufstourismus (DE/CH)', 'KMU & lokale Dienstleistungen Kanton Schaffhausen'],
    'standort': 'Altstadt mit dem Munot, Fronwagplatz und Vordergasse, das Industriegebiet nördlich der Bahn und die Rheinfall-Region bilden die wirtschaftlichen Lagen. Die Nähe zu Singen und Konstanz schafft ein breites grenzüberschreitendes Einzugsgebiet.',
  },
  'St. Gallen': {
    'wirtschaft': 'St. Gallen ist das wirtschaftliche und administrative Zentrum der Ostschweiz. Die Universität St. Gallen (HSG) – eine der führenden Wirtschaftshochschulen Europas – macht die Stadt zu einem Zentrum für Wirtschaft, Recht und Unternehmertum. Die historische Textilindustrie hat St. Gallen weltweit bekannt gemacht; Stickerei „Made in St. Gallen" ist bis heute eine Qualitätsmarke. Heute dominieren Dienstleistungen, Versicherungen und Handel. Der Stiftsbezirk mit der Stiftsbibliothek ist UNESCO-Weltkulturerbe.',
    'branchen': ['Bildung & Universität St. Gallen (HSG)', 'Versicherungen & Finanzdienstleistungen', 'Textil, Stickerei & Modebranche', 'IT & Software-Unternehmen Ostschweiz', 'Einzelhandel, Gastronomie & Innenstadt-Wirtschaft'],
    'standort': 'Altstadt mit Stiftsbezirk und Multergasse, Marktplatz, Bahnhofstrasse und das Stadtpark-Quartier sind die wirtschaftlichen Kernlagen. St. Gallen versorgt den gesamten Ostschweizer Raum bis zum Bodensee und Liechtenstein.',
  },
  'Zürich': {
    'wirtschaft': 'Zürich ist die größte Stadt der Schweiz und eine der bedeutendsten Wirtschaftsmetropolen Europas. Banken (UBS), Versicherungen (Swiss Re, Zurich Insurance), Technologieunternehmen (Google Zürich, Microsoft) und professionelle Dienstleister dominieren. Die ETH Zürich ist eine der weltweit führenden technischen Hochschulen und Motor für Innovation und Spin-offs. Der Finanzplatz Zürich hat globale Bedeutung. Zürich ist regelmäßig in den Top 3 der lebenswertesten Städte der Welt.',
    'branchen': ['Finanzdienstleistungen, Banking & Versicherungen', 'Tech & internationale Konzerne (Google, Microsoft)', 'Beratung, Recht & professionelle Dienstleistungen', 'Luxusgüter & Premium-Einzelhandel (Bahnhofstrasse)', 'Start-ups & ETH-Spin-offs (Innovationsökosystem)'],
    'standort': 'Bahnhofstrasse, Niederdorf, Zürich West (Kreis 5) und das Seefeld sind die bekanntesten Wirtschaftslagen. Zürich Altstetten, Oerlikon und Schlieren bilden wichtige Gewerbe- und Technologiecluster. Das Metropolitangebiet Zürich mit rund 1,4 Millionen Einwohnern ist der größte Wirtschaftsraum der Schweiz.',
  },
  'Winterthur': {
    'wirtschaft': 'Winterthur ist die sechstgrößte Stadt der Schweiz und eine der bedeutendsten Industriestädte des Landes. Sulzer, Rieter und ABB haben hier ihre Wurzeln – die Industriegeschichte ist tief in der Stadtidentität verankert. Heute ist Winterthur ein moderner Standort für Maschinenbau, Bildung (ZHAW Zürcher Hochschule für Angewandte Wissenschaften) und Gesundheitswirtschaft. Viele Unternehmen sind Hidden Champions mit überregionalem Anspruch, die ihre Kommunikation professionalisieren wollen.',
    'branchen': ['Maschinenbau & Industrietechnik (Sulzer- und Rieter-Erbe)', 'Gesundheit & Kantonsspital Winterthur', 'Bildung & ZHAW', 'Einzelhandel & Altstadt-Gastronomie', 'Tech & Dienstleistungsunternehmen (Technopark-Umfeld)'],
    'standort': 'Altstadt mit Marktgasse, der Technopark-Bereich, das Sulzer-Areal und die Gewerbegebiete in Töss und Oberwinterthur sind wirtschaftliche Kernlagen. Winterthur liegt 20 Minuten von Zürich und hat eine starke eigenständige Wirtschaftsidentität.',
  },
  'Frauenfeld': {
    'wirtschaft': 'Frauenfeld ist Hauptstadt und wirtschaftliches Zentrum des Kantons Thurgau. Als Verwaltungsstandort prägen Kantonsbehörden und öffentliche Einrichtungen das Bild. Daneben gibt es einen soliden Mittelstand: Industrie, Handwerk und Dienstleister für die thurgauische Bevölkerung. Der Kanton Thurgau ist bekannt für Obstbau und Landwirtschaft. Die Lage zwischen Konstanz (30 km), Winterthur (25 km) und St. Gallen (40 km) schafft gute Verbindungen in die Wirtschaftszentren der Ostschweiz.',
    'branchen': ['Kantonsverwaltung & öffentliche Einrichtungen', 'Landwirtschaft, Obstbau & Direktvermarktung Thurgau', 'Handwerk & Bauwirtschaft', 'Einzelhandel & regionale Versorgung', 'Dienstleistungen & freie Berufe'],
    'standort': 'Schloss Frauenfeld, Marktgasse und Bahnhof sind die wirtschaftlichen Kernlagen. Frauenfeld versorgt weite Teile des Kantons Thurgau. Die Bahnverbindungen nach Winterthur, Konstanz und St. Gallen sind gut ausgebaut.',
  },
  'Basel': {
    'wirtschaft': 'Basel ist nach Zürich und Genf die drittgrößte Stadt der Schweiz und ein Weltklasse-Wirtschaftsstandort. Roche und Novartis – zwei der weltweit führenden Pharmaunternehmen – haben hier ihren Sitz. Art Basel ist die bedeutendste Kunstmesse der Welt. Als Dreiländereck (CH/DE/FR) hat Basel eine einzigartige internationale Lage. Der Hafen am Rhein macht Basel zum wichtigsten Binnenhafen der Schweiz. Das wirtschaftliche Umfeld ist hochkarätig und stellt entsprechend hohe Anforderungen an Kommunikation.',
    'branchen': ['Pharma & Life Sciences (Roche, Novartis, Lonza)', 'Chemie & Spezialchemie', 'Kunst, Kultur & Messe (Art Basel, Baselworld)', 'Finanzdienstleistungen & Privatbanken', 'Logistik & Rheinhafen'],
    'standort': 'Grossbasel mit Münster und Marktplatz, Kleinbasel am Rheinufer, die Pharma-Areale von Roche und Novartis und der Messeplatz sind die wirtschaftlichen Zentren. Trinationaler Wirtschaftsraum DE/CH/FR mit Freiburg und Mulhouse als weitere Wirtschaftspole.',
  },
  'Bregenz': {
    'wirtschaft': 'Bregenz ist die Landeshauptstadt Vorarlbergs und Kulturort mit internationaler Ausstrahlung. Die Bregenzer Festspiele auf der weltberühmten Seebühne ziehen jährlich 200.000 Besucher aus aller Welt. Wirtschaftlich ist Bregenz Verwaltungs-, Dienstleistungs- und Tourismusmittelpunkt. Vorarlberg als Bundesland hat eine der höchsten Exportquoten Österreichs – geprägt von Textilindustrie, Maschinenbau und Kreativwirtschaft. Die Rheintal-Region ist eng mit der Schweiz und Deutschland verflochten.',
    'branchen': ['Tourismus & Bregenzer Festspiele', 'Landesverwaltung & öffentliche Dienste Vorarlberg', 'Textilindustrie & Kreativwirtschaft', 'Handel & Dienstleistungen D-A-CH-Region', 'Maschinenbau & Metallverarbeitung Vorarlberg'],
    'standort': 'Seeufer mit Festspielhaus, die Innenstadt rund um den Kornmarkt und das Rheintal mit Dornbirn, Hard und Lustenau bilden den wirtschaftlichen Kern Vorarlbergs. Nähe zu Lindau (25 km) und St. Gallen (30 km) schafft ein trinationales Einzugsgebiet.',
  },
  'Luzern': {
    'wirtschaft': 'Luzern ist mit rund 82.000 Einwohnern die größte Stadt der Zentralschweiz und ein bedeutender Wirtschaftsstandort. Die Kapellbrücke, Pilatus und Rigi machen Luzern zu einer der meistbesuchten Städte der Schweiz – Tourismus ist die erste Wirtschaftssäule. Versicherungen und Finanzdienstleistungen bilden die zweite Säule. Das Luzerner Kantonsspital ist einer der größten Arbeitgeber. Die Hochschule Luzern bildet Fachkräfte aus. Das KKL Luzern ist ein international bekanntes Kultur- und Kongresszentrum.',
    'branchen': ['Tourismus, Hotellerie & internationale Gastronomie', 'Versicherungen & Finanzdienstleistungen Zentralschweiz', 'Gesundheit & Kantonsspital Luzern', 'Einzelhandel & Premium-Gastronomie', 'Bildung & Hochschule Luzern'],
    'standort': 'Altstadt mit Kapellbrücke, Schwanenplatz und Museggmauer, das Tribschenquartier und das KKL sind die Kernlagen. Das Einzugsgebiet umfasst die gesamte Zentralschweiz bis Zug, Schwyz und Nidwalden.',
  },
  'Bodenseeregion': {
    'wirtschaft': 'Die Bodenseeregion ist ein wirtschaftsstarker, grenzüberschreitender Raum zwischen Deutschland, Österreich und der Schweiz. Industrie, Tourismus, Landwirtschaft und ein breiter Mittelstand machen die Region zu einem der lebenswertesten Wirtschaftsräume Europas. X mind ist mit Sitz in Singen im Hegau zentral positioniert, um Unternehmen im gesamten Bodenseeraum persönlich und schnell zu betreuen.',
    'branchen': ['Industrie & Maschinenbau', 'Tourismus, Hotellerie & Gastronomie', 'Landwirtschaft & Obstbau', 'Handwerk & Bauwirtschaft', 'Mittelstand & Dienstleistungen'],
    'standort': 'Von Singen über Konstanz und Radolfzell bis Friedrichshafen und Bregenz: Die Bodenseeregion ist unser Kerngebiet. Wir kennen alle wichtigen Wirtschaftslagen, Netzwerke und lokalen Besonderheiten aus 18 Jahren Arbeit vor Ort.',
  },
}

# Lokale Fakten – neue Wörter, die NICHT in wirtschaft/branchen/standort stehen
# → erhöhen Unique-Content-Anteil pro Stadtseite spürbar
CITIES_LOKFAKT = {
  'Singen':                 'Mit rund 47.000 Einwohnern ist Singen die größte Stadt des Hegau und bedeutendster Einkaufsschwerpunkt zwischen Schaffhausen und Stockach. Der Hohentwiel – erloschener Vulkankegel und weithin sichtbares Wahrzeichen – macht Singen in der gesamten Grenzregion unverwechselbar.',
  'Konstanz':               'Konstanz zählt rund 85.000 Einwohner und ist die einzige Großstadt Deutschlands direkt an der Schweizer Grenze. Die Bodensee-Fähre Konstanz–Meersburg verbindet täglich tausende Pendler und Touristen und macht den Hafen zum belebtesten Verkehrspunkt am deutschen Bodenseeufer.',
  'Radolfzell':             'Radolfzell hat rund 32.000 Einwohner und ist mit seiner Lage zwischen Singen und Konstanz ein wachsender Wohnstandort im Kreis Konstanz. Die Mettnau-Halbinsel und das Strandbad Mettnau sind beliebte Naherholungsgebiete, die Besucherzahlen von über 300.000 pro Jahr anziehen.',
  'Überlingen':             'Überlingen am Bodensee hat rund 22.000 Einwohner und besitzt die längste erhaltene mittelalterliche Stadtmauer Baden-Württembergs. Als staatlich anerkanntes Kneipp-Heilbad empfängt die Stadt jährlich über 200.000 Übernachtungsgäste aus ganz Europa.',
  'Stockach':               'Stockach hat rund 17.000 Einwohner und ist Sitz des legendären Narrengericht Stockach, einem der ältesten Fastnachtsgerichte Europas – bekannt weit über den Bodenseeraum hinaus. Die direkte Lage an der A98 Richtung Singen und die B31 Richtung Friedrichshafen machen Stockach zu einem wichtigen Verkehrsknotenpunkt.',
  'Tuttlingen':             'Tuttlingen hat rund 36.000 Einwohner und beherbergt mehr als 600 Unternehmen der Medizintechnik – nirgendwo sonst auf der Welt werden auf so engem Raum so viele chirurgische Instrumente und Endoskope gefertigt. Das Zentralklinikum Tuttlingen und die Hochschule Furtwangen verstärken den medizinischen Schwerpunkt der Region.',
  'Bad Dürrheim':           'Bad Dürrheim hat rund 13.000 Einwohner und liegt auf 700 Metern Höhe mitten in der Baar. Das Solemar-Erlebnisbad mit über 200.000 Badegästen jährlich ist das Aushängeschild der Kurstadt; die Sole-Quellen, die der Stadt ihren Namen gaben, werden seit dem 19. Jahrhundert therapeutisch genutzt.',
  'Donaueschingen':         'Donaueschingen hat rund 21.000 Einwohner und ist offiziell anerkannter Ausgangspunkt der Donau – Europas zweitlängstem Fluss. Die Donaueschinger Musiktage, seit 1921 das älteste Festival für zeitgenössische Musik der Welt, bringen jährlich internationales Publikum in die Stadt.',
  'Markdorf':               'Markdorf hat rund 14.000 Einwohner und trägt seit Jahrhunderten den Titel „Bischofstadt". Der Obstanbau am Bodensee – Äpfel, Birnen, Kirschen – prägt die Kulturlandschaft rund um Markdorf; die Region ist einer der bedeutendsten Obstbaugebiete Deutschlands.',
  'Pfullendorf':            'Pfullendorf hat rund 13.000 Einwohner und liegt am Überlinger See, dem westlichen Ausläufer des Bodensees. Als Mittelzentrum im Landkreis Sigmaringen versorgt die Stadt ein Einzugsgebiet von über 30.000 Menschen aus den umliegenden Gemeinden Meßkirch, Wald und Illmensee.',
  'Friedrichshafen':        'Friedrichshafen hat rund 62.000 Einwohner und ist mit dem Bodensee-Airport der einzige Flughafen direkt am Bodensee. Die ZF Friedrichshafen AG mit über 160.000 Mitarbeitern weltweit ist der größte Arbeitgeber der Stadt und einer der 10 größten Automobilzulieferer der Welt.',
  'Meersburg':              'Meersburg hat rund 5.000 Einwohner und beherbergt die älteste noch bewohnte Burg Deutschlands – die Meersburg, urkundlich erstmals im 7. Jahrhundert erwähnt. Die Fährverbindung nach Konstanz befördert jährlich über 4 Millionen Fahrgäste und macht Meersburg zum wichtigsten Fährstandort am Bodensee.',
  'Freiburg im Breisgau':   'Freiburg hat rund 235.000 Einwohner und gilt als sonnigste Großstadt Deutschlands. Die Albert-Ludwigs-Universität mit über 25.000 Studierenden und das Fraunhofer-Institut für Solare Energiesysteme machen Freiburg zum führenden Forschungsstandort für erneuerbare Energien in Europa.',
  'Offenburg':              'Offenburg hat rund 60.000 Einwohner und ist Sitz der Hochschule Offenburg mit über 4.000 Studierenden in Technik und Wirtschaft. Als Eisenbahnknoten an der Rheintalbahn liegt Offenburg auf der ICE-Strecke Basel–Karlsruhe und ist damit in unter einer Stunde von Straßburg, Freiburg und Karlsruhe erreichbar.',
  'Villingen-Schwenningen': 'Villingen-Schwenningen hat rund 85.000 Einwohner und ist die neuntgrößte Stadt Baden-Württembergs. Die historische Doppelstadt vereint zwei Stadtkerne: das mittelalterliche Villingen mit vollständig erhaltener Ringmauer und das industriell geprägte Schwenningen, einst Welthauptstadt der Uhrenindustrie.',
  'Schiltach':              'Schiltach hat rund 4.000 Einwohner und ist Stammort der Hansgrohe SE, einem der weltweit führenden Hersteller von Armaturen und Brausesystemen mit über 5.000 Mitarbeitern global. Das historische Fachwerkstadtzentrum am Zusammenfluss von Kinzig und Schiltach ist eines der am besten erhaltenen in Südwestdeutschland.',
  'Gengenbach':             'Gengenbach hat rund 11.000 Einwohner und gilt als eine der schönsten historischen Kleinstädte der Ortenau. Das neogotische Rathaus, das jeden Dezember zum weltberühmten Adventskalender-Fenster wird, macht Gengenbach international bekannt – ein einzigartiger Stadtmarketingeffekt mit globaler Reichweite.',
  'Hausach':                'Hausach hat rund 7.000 Einwohner und liegt im Kinzigtal am Eingang des Gutachtals. Das Schwarzwälder Freilichtmuseum Vogtsbauernhof – das meistbesuchte Freilichtmuseum Baden-Württembergs – liegt in unmittelbarer Nachbarschaft und zieht jährlich über 350.000 Besucher in die Region.',
  'Triberg':                'Triberg hat rund 5.000 Einwohner und beherbergt die höchsten Wasserfälle Deutschlands mit einem Gesamtgefälle von 163 Metern. Als international bekannte Kuckucksuhr-Hochburg und Schwarzwald-Tourismusdestination empfängt die Stadt jährlich über 1 Million Besucher – eine außergewöhnliche Dichte für eine Kleinstadt dieser Größe.',
  'Kehl':                   'Kehl hat rund 36.000 Einwohner und liegt direkt gegenüber von Straßburg – verbunden durch die Europabrücke. Als deutsche Grenzstadt zu Frankreich ist Kehl ein einzigartiger Wirtschaftsstandort: Grenzpendler, binationaler Einzelhandel und das unmittelbare Straßburg-Einzugsgebiet schaffen eine Marktdynamik, die es so in Deutschland kaum ein zweites Mal gibt.',
  'Lahr/Schwarzwald':       'Lahr hat rund 46.000 Einwohner und verfügt mit dem Flugplatz Lahr über einen der wenigen privat betriebenen Verkehrslandeplätze in Baden-Württemberg. Das Stadtbild wird geprägt durch die historische Innenstadt rund um den Storchenturm und ein gut erschlossenes Gewerbegebiet auf dem ehemaligen Militärgelände der kanadischen Streitkräfte.',
  'Oberkirch':              'Oberkirch hat rund 21.000 Einwohner und liegt im Renchtal, einem der bedeutendsten Weinbaugebiete der Ortenau. Die historische Hochburg-Ruine über der Stadt und die traditionsreiche Württemberger-Weinlage „Sätzler" machen Oberkirch zur touristischen Anlaufstation mit überregionaler Bekanntheit im Schwarzwald-Tourismus.',
  'Rottweil':               'Rottweil hat rund 26.000 Einwohner und gilt als älteste Stadt Baden-Württembergs, gegründet von den Römern als Arae Flaviae. Der ThyssenKrupp-Testturm – mit 246 Metern das höchste Gebäude Baden-Württembergs – und das Römische Stadtmuseum machen Rottweil zum Schnittpunkt von Antike und modernster Ingenieurskunst.',
  'Spaichingen':            'Spaichingen hat rund 13.000 Einwohner und liegt am Fuß des Dreifaltigkeitsberges, einem der bedeutendsten Wallfahrtsorte Südwestdeutschlands. Auf dem 981 Meter hohen Gipfelplateau steht die barocke Dreifaltigkeitskirche, die jährlich rund 100.000 Pilger und Ausflugsgäste anzieht.',
  'Tübingen':               'Tübingen hat rund 90.000 Einwohner, davon ein Viertel Studierende der Eberhard-Karls-Universität – eine der ältesten Universitäten Deutschlands, gegründet 1477. Die Universitätsstadt am Neckar gilt als eine der lebenswertesten Städte Deutschlands und beherbergt bedeutende Forschungseinrichtungen in Biotechnologie, Medizin und Geisteswissenschaften.',
  'Rottenburg am Neckar':   'Rottenburg am Neckar hat rund 43.000 Einwohner und ist Sitz des Bistums Rottenburg-Stuttgart, dem einwohnerstärksten Bistum Deutschlands. Die romanisch-gotische Domkirche St. Martin und die ehemalige Römerstadt Sumelocenna – heute Stadtmuseum – prägen das kulturhistorische Profil dieser Diözesanstadt am Neckar.',
  'Schaffhausen':           'Schaffhausen hat rund 36.000 Einwohner und ist Hauptstadt des gleichnamigen Schweizer Kantons. Der Rheinfall bei Schaffhausen – mit einem Volumen von bis zu 1.250 m³/s der wasserreichste Wasserfall Europas – zieht jährlich über 1,5 Millionen Besucher an und ist das meistbesuchte Naturspektakel der Schweiz.',
  'St. Gallen':             'St. Gallen hat rund 75.000 Einwohner und ist wirtschaftliches Zentrum der Ostschweiz. Das Kloster St. Gallen mit seiner Stiftsbibliothek, einer der ältesten Klosterbibliotheken der Welt und UNESCO-Welterbe, macht die Stadt international bekannt; die Universität St. Gallen (HSG) gehört zu den renommiertesten Wirtschaftsuniversitäten Europas.',
  'Zürich':                 'Zürich hat rund 420.000 Einwohner und ist größte Stadt der Schweiz sowie einer der wichtigsten Finanzplätze der Welt. Der Zürichsee, die Altstadt mit Grossmünster und Fraumünster sowie die international anerkannte ETH Zürich machen die Stadt zum kulturellen und wissenschaftlichen Gravitationszentrum der Deutschschweiz.',
  'Winterthur':             'Winterthur hat rund 115.000 Einwohner und ist die sechstgrößte Stadt der Schweiz. Als ehemaliges Industriezentrum mit Sulzer, Rieter und Georg Fischer hat Winterthur eine starke Umnutzungskultur entwickelt: Museen, Kulturzentren und Kreativwirtschaft haben sich in ehemaligen Fabrikgebäuden angesiedelt – ein Modell für erfolgreiche Stadtentwicklung.',
  'Frauenfeld':             'Frauenfeld hat rund 27.000 Einwohner und ist Hauptort des Kantons Thurgau. Die Stadt liegt am Durchgangspunkt zwischen Bodensee und Zürich und profitiert von der Intercity-Bahnverbindung; der Thurgauer Kantonsrat und zahlreiche kantonale Verwaltungsstellen machen Frauenfeld zum administrativen Zentrum einer der landwirtschaftlich stärksten Regionen der Schweiz.',
  'Basel':                  'Basel hat rund 180.000 Einwohner und liegt am Dreiländereck Deutschland–Frankreich–Schweiz, wo der Rhein nach Norden abbiegt. Als Sitz von Novartis, Roche und einer bedeutenden Kunstmesse (Art Basel) verbindet Basel Pharmaindustrie, Finanzwirtschaft und internationale Kulturveranstaltungen auf einzigartige Weise.',
  'Bregenz':                'Bregenz hat rund 30.000 Einwohner und ist Landeshauptstadt von Vorarlberg. Die Bregenzer Festspiele mit ihrer weltberühmten Seebühne auf dem Bodensee ziehen jährlich über 200.000 Besucher an und sind nach Salzburg das meistbesuchte Klassikfestival im deutschsprachigen Raum.',
  'Luzern':                 'Luzern hat rund 82.000 Einwohner und liegt am Vierwaldstättersee im Herzen der Zentralschweiz. Die mittelalterliche Kapellbrücke, das Löwendenkmal und eine der besterhaltenen Stadtmauern Europas machen Luzern zur meistbesuchten Tourismusdestination der Innenschweiz – mit über 3 Millionen Übernachtungen pro Jahr.',
  'Bodenseeregion':         'Die Bodenseeregion umfasst rund 600.000 Einwohner am deutschen, österreichischen und schweizerischen Bodenseeufer. Der Bodensee selbst – mit 538 km² das drittgrößte Binnengewässer Mitteleuropas – ist Trinkwasserreservoir für 4 Millionen Menschen und verbindendes Element dieser einzigartigen trilateralen Wirtschaftsregion.',
}
# Neue Felder in CITIES einbinden
for _ck, _extra in CITIES_EXTRA.items():
    if _ck in CITIES:
        CITIES[_ck].update(_extra)
for _ck, _lf in CITIES_LOKFAKT.items():
    if _ck in CITIES:
        CITIES[_ck]['lokal_fakt'] = _lf

ALL_CITIES = [
    # Stammgebiet
    'Singen','Konstanz','Radolfzell','Überlingen','Stockach','Tuttlingen',
    'Bad Dürrheim','Donaueschingen','Markdorf','Pfullendorf',
    # Bodensee-Region
    'Friedrichshafen','Meersburg',
    # Schwarzwald – mittlerer/südlicher Teil
    'Freiburg im Breisgau','Offenburg','Villingen-Schwenningen',
    'Schiltach','Gengenbach','Hausach','Triberg',
    # Ortenau und südwestlich
    'Kehl','Lahr/Schwarzwald','Oberkirch',
    # Schwarzwald-Baar-Heuberg und Donau
    'Rottweil','Spaichingen','Tübingen','Rottenburg am Neckar',
    # Schweiz & Österreich (international)
    'Schaffhausen','St. Gallen','Zürich','Winterthur','Frauenfeld',
    'Basel','Bregenz','Luzern',
]

TESTIMONIALS = [
  ('Mit X mind haben wir eine Agentur gefunden, die nicht nur kreativ, sondern auch zuverlässig ist. Unsere neue Website kommt super bei unseren Kunden an, die neuen Geschäftsberichte unterstreichen das neue Corporate Design und überzeugen – vielen Dank für die tolle Zusammenarbeit!', 'Fr. Brucker, BGO, Singen'),
  ('Kreativ, engagiert und zuverlässig! Unsere Print- und Digitalprojekte wurden immer perfekt umgesetzt. Danke ans gesamte X mind-Team für die großartige Unterstützung!', 'Herr Aust, MTS, Singen'),
  ('Seit über einem Jahrzehnt verlassen wir uns bei all unseren Kommunikations- und Werbemaßnahmen auf X mind – von der Website über Geschäftsberichte bis zu Anzeigen und Bauschildern. Egal, welches Projekt ansteht, das Team liefert immer kreative, zuverlässige und maßgeschneiderte Lösungen.', 'Stefan Andelfinger, Familienheim Bodensee'),
  ('X mind betreut uns nun seit Jahren. Die professionelle und pragmatische Art sowie die Ergebnisse überzeugen uns immer wieder. Absolut empfehlenswert!', 'Andreas Schulze, Münchow Märkte'),
  ('X mind liefert einfach. Von lokalem SEO über eine kleine, feine Webseite bis hin zur kompletten Geschäftsausstattung – hier passt alles zusammen und funktioniert reibungslos.', 'Geschäftsführer, KFZ Betrieb'),
  ('X mind hat unsere Webseite von Anfang an mit viel Kreativität und technischem Know-how gestaltet. Das Ergebnis ist eine moderne, übersichtliche Seite, die perfekt zu unserem Handwerk passt.', 'Juri Rixen, Rixen Dach, Moos'),
]


# ══════════════════════════════════════════════════════════════════════════════
# DROHNENFOTOGRAFIE – Theme-spezifische Referenzstimmen (anonym, nur Position)
# ══════════════════════════════════════════════════════════════════════════════
TESTIMONIALS_DROHNEN = [
  ('Die Luftaufnahmen haben unsere Immobilien-Exposés auf ein neues Niveau gehoben. Interessenten melden sich gezielt und gut informiert – das spart allen Beteiligten Zeit.',
   'Geschäftsführerin, Immobilienmaklerin, Bodenseeregion'),
  ('Wir hatten das Gelände unseres Gewerbestandorts noch nie so gesehen. Die Aufnahmen sind in Geschäftsbericht und Website eingeflossen und kommen bei Investoren sehr gut an.',
   'Technischer Leiter, Mittelständisches Industrieunternehmen'),
  ('Perfekte Organisation, pünktliche Lieferung, starke Bilder. Für unsere Stadtmarketing-Kampagne genau das, was wir gebraucht haben.',
   'Projektleiterin, Kommunale Wirtschaftsförderung'),
]

# ══════════════════════════════════════════════════════════════════════════════
# FOTOGRAFIE GALERIE – Bild-URLs zentral (format: landscape=4:3 | portrait=3:4)
# Slot 18 = Platzhalter bis Bild geliefert wird
# ══════════════════════════════════════════════════════════════════════════════
GALLERY_IMAGES = [
    {'src':'https://www.x-mind.de/wp-content/uploads/2E8A2187-Spektral-Kopie-Kopie-1.jpg','alt':'Werbefotografie x-mind Werbeagentur','format':'landscape'},
    {'src':'https://www.x-mind.de/wp-content/uploads/2E8A2550.jpg',                        'alt':'Corporate Portrait Businessfotografie x-mind','format':'portrait'},
    {'src':'https://www.x-mind.de/wp-content/uploads/2E8A3265.jpg',                        'alt':'Produktfotografie x-mind Bodenseeregion','format':'landscape'},
    {'src':'https://www.x-mind.de/wp-content/uploads/2E8A8780.jpg',                        'alt':'Industriefotografie Unternehmensreportage x-mind','format':'landscape'},
    {'src':'https://www.x-mind.de/wp-content/uploads/3I3A3674.jpg',                        'alt':'Businessfotografie Mitarbeiterportraits x-mind','format':'portrait'},
    {'src':'https://www.x-mind.de/wp-content/uploads/23CM0263.jpg',                        'alt':'Location Shooting Werbefotografie x-mind','format':'landscape'},
    {'src':'https://www.x-mind.de/wp-content/uploads/23CM1243.jpg',                        'alt':'Handwerk Fotografie x-mind Werbeagentur','format':'landscape'},
    {'src':'https://www.x-mind.de/wp-content/uploads/23CM3796.jpg',                        'alt':'Lifestyle Fotografie x-mind Werbeagentur Singen','format':'landscape'},
    {'src':'https://www.x-mind.de/wp-content/uploads/74.jpg',                              'alt':'Portrait Fotografie x-mind Corporate','format':'portrait'},
    {'src':'https://www.x-mind.de/wp-content/uploads/82.jpg',                              'alt':'Produktfoto Werbefotografie x-mind Bodensee','format':'landscape'},
    {'src':'https://www.x-mind.de/wp-content/uploads/Meister-Heuser-765.jpg',              'alt':'Immobilienfotografie x-mind Werbeagentur','format':'landscape'},
    {'src':'https://www.x-mind.de/wp-content/uploads/23CM8846.jpg',                        'alt':'Teamfoto Businessfotografie x-mind','format':'landscape'},
    {'src':'https://www.x-mind.de/wp-content/uploads/23CM6651-Kopie-_-20x302-1.jpg',       'alt':'Werbefotografie x-mind Hegau Bodensee','format':'landscape'},
    {'src':'https://www.x-mind.de/wp-content/uploads/23CM4009.jpg',                        'alt':'Portrait Business x-mind Werbeagentur','format':'portrait'},
    {'src':'https://www.x-mind.de/wp-content/uploads/2E8A3175.jpg',                        'alt':'Location Shooting Industriefotografie x-mind','format':'landscape'},
    {'src':'https://www.x-mind.de/wp-content/uploads/DSC_4530-Kopie.jpg',                  'alt':'Drohnenfotografie Luftaufnahme x-mind','format':'landscape'},
    {'src':'https://www.x-mind.de/wp-content/uploads/MG_9808-HDR.jpg',                     'alt':'Immobilien Fotografie x-mind Werbeagentur','format':'portrait'},
    {'src':'BILD_URL_18.jpg',                                                               'alt':'Werbefotografie x-mind Werbeagentur','format':'landscape'},
]


# ══════════════════════════════════════════════════════════════════════════════
# HILFSFUNKTIONEN
# ══════════════════════════════════════════════════════════════════════════════
def c2slug(city):
    return city.lower().replace('.','' ).replace(' ','-').replace('/','-').replace('ü','ue').replace('ä','ae').replace('ö','oe')

def t(s, city):
    return s.replace('{CITY}', city).replace('{REGION}', CITIES.get(city, CITIES['Bodenseeregion'])['region'])

def esc(s):
    return htmllib.escape(s)

# ══════════════════════════════════════════════════════════════════════════════
# STATISCHE HTML-RENDERER
# ══════════════════════════════════════════════════════════════════════════════
def render_cards(theme_data, city):
    out = []
    for c in theme_data['cards']:
        out.append(
            f'<div class="card">'
            f'<div class="card-icon-wrap"><span class="card-icon">{c["icon"]}</span></div>'
            f'<h3 class="card-title">{esc(c["title"])}</h3>'
            f'<p class="card-text">{esc(t(c["text"], city))}</p>'
            f'</div>'
        )
    return '\n'.join(out)

def render_process(theme_data, city):
    steps = theme_data['process']
    out = []
    for i, p in enumerate(steps):
        has_line = ' has-line' if i < len(steps)-1 else ''
        tag = '<span class="process-tag">Weil Erfolg planbar ist.</span>' if i < len(steps)-1 else ''
        out.append(
            f'<div class="process-item{has_line}">'
            f'<div class="process-dot"></div>'
            f'<div class="process-body">'
            f'<h3>{esc(p["title"])}</h3>'
            f'<p>{esc(t(p["text"], city))}</p>'
            f'{tag}'
            f'</div>'
            f'</div>'
        )
    return '\n'.join(out)

def render_faq(theme_data, city):
    out = []
    for q, a in theme_data['faq']:
        out.append(
            f'<div class="faq-item">'
            f'<button class="faq-btn"><span>{esc(t(q, city))}</span><span class="faq-icon">+</span></button>'
            f'<div class="faq-body"><div class="faq-inner"><p class="faq-ans">{esc(t(a, city))}</p></div></div>'
            f'</div>'
        )
    return '\n'.join(out)

def render_testimonials_static(theme=''):
    """Alle Testimonials statisch mit data-page (2 pro Seite) für Crossfade + Googlebot."""
    out = []
    testi_src = TESTIMONIALS_DROHNEN if theme == 'drohnenfotografie' else TESTIMONIALS
    for i, (text, author) in enumerate(testi_src):
        page = i // 2
        hidden = ' hidden' if page > 0 else ''
        out.append(
            f'<div class="testi-card" data-page="{page}"{hidden}>'
            f'<div class="testi-quote">\u201e</div>'
            f'<p class="testi-text">{esc(text)}</p>'
            f'<p class="testi-author">{esc(author.upper())}</p>'
            f'</div>'
        )
    return '\n'.join(out)

def render_cities_html():
    """Städte-Grid (4 Spalten) als statisches HTML – kein JS nötig."""
    cols = [[], [], [], []]
    for i, c in enumerate(ALL_CITIES):
        cols[i % 4].append(c)
    return ''.join(
        '<ul>' + ''.join(f'<li>{esc(c)}</li>' for c in col) + '</ul>'
        for col in cols
    )

def render_city_links(theme, city, slug, is_pillar):
    """Dynamische Stadtlinks mit garantierter Mindestabdeckung.

    Pillar-Seiten (Hub & Spoke): ALLE Städte nach Region gelistet.
    Stadt-Seiten: 15–18 Städte zufällig (Seed = Slug, deterministisch).
    """
    import hashlib, random as _random
    from collections import defaultdict
    keyword = THEMES[theme]['keyword']
    prefix  = './' if is_pillar else '../'

    REGIONS_DEF = [
        ('Bodensee & Hegau',         ['Singen','Konstanz','Radolfzell','Überlingen','Stockach','Markdorf','Pfullendorf']),
        ('Bodenseekreis',            ['Friedrichshafen','Meersburg']),
        ('Ortenau',                  ['Offenburg','Kehl','Lahr/Schwarzwald','Oberkirch','Gengenbach']),
        ('Schwarzwald',              ['Freiburg im Breisgau','Schiltach','Hausach','Triberg']),
        ('Schwarzwald-Baar & Donau', ['Villingen-Schwenningen','Tuttlingen','Rottweil','Spaichingen',
                                      'Donaueschingen','Bad Dürrheim']),
        ('Tübingen & Neckar',        ['Tübingen','Rottenburg am Neckar']),
        ('Schweiz & Österreich',     ['Schaffhausen','St. Gallen','Zürich','Winterthur','Frauenfeld',
                                      'Basel','Bregenz','Luzern']),
    ]

    # ── Pillar-Seite: ALLE Städte nach Region (Hub & Spoke) ──────────────────
    if is_pillar:
        _DROHNEN_KW_MAP = {
            c: ['Drohnenfotograf','Luftaufnahmen','Drohnenaufnahmen'][i % 3]
            for i, c in enumerate([
                'Singen','Konstanz','Radolfzell','Überlingen','Stockach','Markdorf','Pfullendorf',
                'Friedrichshafen','Meersburg',
                'Offenburg','Kehl','Lahr/Schwarzwald','Oberkirch','Gengenbach',
                'Freiburg im Breisgau','Schiltach','Hausach','Triberg',
                'Villingen-Schwenningen','Tuttlingen','Rottweil','Spaichingen','Donaueschingen','Bad Dürrheim',
                'Tübingen','Rottenburg am Neckar',
                'Schaffhausen','St. Gallen','Zürich','Winterthur','Frauenfeld','Basel','Bregenz','Luzern',
            ])
        }
        out = []
        for rname, rcities in REGIONS_DEF:
            out.append(
                f'<div style="width:100%;margin-top:12px;margin-bottom:4px;">'
                f'<span style="font-size:11px;font-weight:700;text-transform:uppercase;'
                f'letter-spacing:1px;color:var(--mu);">{rname}</span></div>'
            )
            for c in rcities:
                cs = c2slug(c)
                kw = _DROHNEN_KW_MAP.get(c, 'Drohnenfotograf') if theme == 'drohnenfotografie' else keyword
                out.append(f'<a href="{prefix}{slug}-{cs}/index.html" class="int-link">{esc(kw)} {esc(c)}</a>')
        return '\n'.join(out)
    # ─────────────────────────────────────────────────────────────────────────

    seed = int(hashlib.md5(slug.encode()).hexdigest(), 16) % (2**32)
    rng  = _random.Random(seed)

    # Regionen-Pools ohne aktuelle Stadt
    pools = [(rname, [c for c in rcities if c != city])
             for rname, rcities in REGIONS_DEF]
    pools = [(rname, pool) for rname, pool in pools if pool]

    # Phase 1: Pflicht-Picks – kleine Regionen 1×, große (6+ Städte) 2×
    mandatory = []
    for rname, pool in pools:
        n_mandatory = 2 if len(pool) >= 6 else 1
        n_mandatory = min(n_mandatory, len(pool))
        picks = rng.sample(pool, n_mandatory)
        for p in picks:
            mandatory.append((rname, p))

    # Phase 2: Extra-Slots (Gesamt 15–18 minus Pflicht-Slots) zufällig verteilen
    n_extra = rng.randint(15, 18) - len(mandatory)
    # Gewichtete Verteilung der Extra-Slots auf Regionen (größere Regionen öfter)
    extra_by_region = {rname: [] for rname, _ in pools}
    # Pflicht-Picks pro Region sammeln (für Duplikat-Ausschluss)
    mandatory_by_region = defaultdict(list)
    for rname, pick in mandatory:
        mandatory_by_region[rname].append(pick)
    avail_by_region = {rname: [c for c in pool if c not in mandatory_by_region[rname]]
                       for rname, pool in pools}
    for _ in range(n_extra):
        candidates = [(rname, pool) for rname, pool in avail_by_region.items() if pool]
        if not candidates: break
        weights    = [len(p) for _, p in candidates]
        rname, _   = rng.choices(candidates, weights=weights)[0]
        pick       = rng.choice(avail_by_region[rname])
        extra_by_region[rname].append(pick)
        avail_by_region[rname].remove(pick)

    # Zusammenführen: Pflicht + Extra, Reihenfolge der Regionen beibehalten
    # Regionen-Reihenfolge ohne Duplikate (preserving first occurrence)
    seen_regions = []
    for rname, _ in mandatory:
        if rname not in seen_regions:
            seen_regions.append(rname)
    # Alle Pflicht-Picks pro Region sammeln
    mandatory_by_rname = defaultdict(list)
    for rname, pick in mandatory:
        mandatory_by_rname[rname].append(pick)

    selected = []
    for rname in seen_regions:
        cities = mandatory_by_rname[rname] + extra_by_region[rname]
        selected.append((rname, cities))

    out = []
    for region_name, cities in selected:
        if not cities: continue
        out.append(
            f'<div style="width:100%;margin-top:12px;margin-bottom:4px;">'
            f'<span style="font-size:11px;font-weight:700;text-transform:uppercase;'
            f'letter-spacing:1px;color:var(--mu);">{region_name}</span></div>'
        )
        # Drohnenfotografie: Keywords rotieren; andere Themes: festes Keyword
        _DROHNEN_KW_MAP = {
            c: ['Drohnenfotograf','Luftaufnahmen','Drohnenaufnahmen'][i % 3]
            for i, c in enumerate([
                'Singen','Konstanz','Radolfzell','Überlingen','Stockach','Markdorf','Pfullendorf',
                'Friedrichshafen','Meersburg',
                'Offenburg','Kehl','Lahr/Schwarzwald','Oberkirch','Gengenbach',
                'Freiburg im Breisgau','Schiltach','Hausach','Triberg',
                'Villingen-Schwenningen','Tuttlingen','Rottweil','Spaichingen','Donaueschingen','Bad Dürrheim',
                'Tübingen','Rottenburg am Neckar',
                'Schaffhausen','St. Gallen','Zürich','Winterthur','Frauenfeld','Basel','Bregenz','Luzern',
            ])
        }
        for c in cities:
            cs  = c2slug(c)
            kw  = _DROHNEN_KW_MAP.get(c, 'Drohnenfotograf') if theme == 'drohnenfotografie' else keyword
            out.append(f'<a href="{prefix}{slug}-{cs}/index.html" class="int-link">{esc(kw)} {esc(c)}</a>')
    return '\n'.join(out)
def render_city_block(theme, city, slug, is_pillar):
    """Unique City-Content – das zentrale Differenzierungselement gegen Duplicate Content."""
    C     = CITIES.get(city, CITIES['Bodenseeregion'])
    T     = THEMES[theme]
    label = T['title']
    city_disp = city if city != 'Bodenseeregion' else 'Bodenseeregion'

    if theme == 'drohnenfotografie' and not is_pillar:
        heading  = f'Drohnenfotografie in {city_disp} – professionell, lizenziert, termingenau'
        sub      = f'{C["full"]} · {C["region"]}'
        intro    = (f'In {city_disp} setzen wir professionelle Drohnenfotografie für Immobilien, Gewerbe, '
                    f'Kommunen, Events und Filmprojekte um. Unser Netzwerk zertifizierter Piloten – '
                    f'teils mit Fotografenmeister-Ausbildung – ist bundesweit verfügbar und kennt '
                    f'die lokalen Luftraumregeln im Raum {city_disp} und {C["region"]}.')
        note     = (f'Kein Hobby, keine Kompromisse: Wir holen alle behördlichen Genehmigungen ein, '
                    f'projektieren jeden Einsatz professionell und liefern Bildmaterial, '
                    f'das in {city_disp} und weit darüber hinaus wirkt – für Print, Digital, '
                    f'Social Media und Film.')
        cities_section = ''
    elif is_pillar:
        heading  = f'{label} für die gesamte Bodenseeregion'
        sub      = 'Ihr persönlicher Partner – egal ob Singen, Konstanz, Radolfzell oder darüber hinaus.'
        intro    = C['intro']
        note     = C['note']
        cities_links = ''.join(
            f'<a href="./{slug}-{c2slug(c)}/index.html" '
            f'style="display:inline-block;margin:4px 8px 4px 0;padding:6px 14px;background:var(--navy);color:#fff;border-radius:6px;font-size:13px;font-weight:600;text-decoration:none;">'
            f'{label} {c}</a>'
            for c in ['Singen','Konstanz','Radolfzell']
        )
        cities_section = (
            f'<div style="margin-top:24px">'
            f'<p style="font-size:13px;font-weight:700;text-transform:uppercase;letter-spacing:1px;color:var(--red);margin-bottom:12px;">Direkt zur Stadt</p>'
            f'{cities_links}'
            f'</div>'
        )
    else:
        heading  = f'Ihr {label}-Partner in {city_disp}'
        sub      = f'{C["full"]} · {C["region"]}'
        intro    = C['intro']
        note     = C['note']
        cities_section = ''

    return f'''
<!-- ═══ CITY UNIQUE CONTENT ════════════════ -->
<div class="w">
  <section class="sec-sm">
    <div class="city-block-grid">
      <div>
        <div class="sec-label">Ihr regionaler Partner</div>
        <h2 class="sec-h2" style="font-size:clamp(22px,2.8vw,36px)">{esc(heading)}</h2>
        <p style="font-size:13px;font-weight:600;color:var(--red);margin-bottom:16px;">{esc(sub)}</p>
        <p style="font-size:16px;color:var(--mu);line-height:1.7">{esc(intro)}</p>
        {cities_section}
      </div>
      <div class="city-block-info">
        <p style="font-size:13px;font-weight:700;text-transform:uppercase;letter-spacing:1px;color:var(--navy);margin-bottom:16px;">Was das für Sie bedeutet</p>
        <p style="font-size:15px;color:var(--mu);line-height:1.75">{esc(note)}</p>
        <div class="city-block-stats">
          <div style="text-align:center"><div style="font-size:28px;font-weight:800;color:var(--navy)">18</div><div style="font-size:12px;color:var(--mu)">Jahre Erfahrung</div></div>
          <div style="text-align:center"><div style="font-size:28px;font-weight:800;color:var(--navy)">100<span style="color:var(--red)">+</span></div><div style="font-size:12px;color:var(--mu)">Kunden</div></div>
          <div style="text-align:center"><div style="font-size:28px;font-weight:800;color:var(--navy)">500<span style="color:var(--red)">+</span></div><div style="font-size:12px;color:var(--mu)">Projekte</div></div>
        </div>
      </div>
    </div>
  </section>
</div>
<hr class="div">
'''

def render_local_market(theme, city, is_pillar):
    """Neue Sektion: Wirtschaft & Branchen – erzeugt ~300 unique Wörter pro Stadtseite."""
    if is_pillar:
        return ''
    C = CITIES.get(city, {})
    wirtschaft = C.get('wirtschaft', '')
    branchen   = C.get('branchen', [])
    standort   = C.get('standort', '')
    if not wirtschaft:
        return ''
    label = THEMES[theme]['title']
    branchen_html = '\n'.join(
        f'<li style="display:flex;align-items:center;gap:10px;padding:10px 0;border-bottom:1px solid var(--brd);">'
        f'<span style="width:6px;height:6px;border-radius:50%;background:var(--red);flex-shrink:0;margin-top:2px"></span>'
        f'<span style="font-size:15px;color:var(--tx);font-weight:500">{esc(b)}</span></li>'
        for b in branchen
    )
    return f'''
<!-- ═══ LOKALER MARKT & WIRTSCHAFT ═══════════════ -->
<div class="w">
  <section class="sec">
    <div class="sec-label">{esc(label)} in {esc(city)} &ndash; Markt &amp; Standort</div>
    <h2 class="sec-h2">Wirtschaft und Unternehmen in {esc(city)}.</h2>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:60px;margin-top:40px;align-items:start">
      <div>
        <p style="font-size:16px;color:var(--mu);line-height:1.75">{esc(wirtschaft)}</p>
        <p style="font-size:15px;color:var(--mu);line-height:1.7;margin-top:24px;padding-top:20px;border-top:1px solid var(--brd)">{esc(standort)}</p>
      </div>
      <div>
        <p style="font-size:13px;font-weight:700;text-transform:uppercase;letter-spacing:1px;color:var(--navy);margin-bottom:4px">Typische Branchen in {esc(city)}</p>
        <ul style="list-style:none;padding:0;margin-top:0">
          {branchen_html}
        </ul>
        <div style="margin-top:28px;padding:20px 24px;background:var(--navy);border-radius:12px">
          <p style="font-size:14px;font-weight:700;color:#fff;margin-bottom:8px">Was das f&uuml;r Sie bedeutet:</p>
          <p style="font-size:14px;color:rgba(255,255,255,.75);line-height:1.65">F&uuml;r all diese Branchen gilt: Professionelles {esc(label)} ist der Unterschied zwischen Unsichtbarkeit und echter Marktpr&auml;senz. X mind liefert das f&uuml;r {esc(city)} und die Region &ndash; pers&ouml;nlich, verl&auml;sslich, seit 18 Jahren.</p>
        </div>
      </div>
    </div>
  </section>
</div>
<hr class="div">
'''

# ── Stadt × Theme: einzigartige Verbindungstexte ─────────────────────────────
# Jedes Theme hat eine eigene "Brille", durch die es den lokalen Markt betrachtet.
# Die Branchen-Daten kommen aus CITIES_EXTRA → Text variiert pro Stadt UND pro Theme.
CITY_THEME_CONNECT = {
  'webdesign': (
    'Webdesign in {city} – was {b0} und {b1} wirklich brauchen.',
    '{b0}, {b1} und {b2} – das sind die Branchen, die in {city} den Ton angeben. '
    'Was diese Betriebe eint: Ihre Kunden entscheiden online, ob sie Kontakt aufnehmen. '
    'Eine veraltete oder schlecht strukturierte Website bedeutet verlorene Anfragen – '
    'an den Mitbewerber, der beim Smartphone-Check besser aussieht. '
    'Wir entwickeln Webdesign für {city}, das in drei Sekunden überzeugt: '
    'mobiloptimiert, schnell ladend und auf die spezifischen Anforderungen von '
    '{b0} und den anderen Branchen vor Ort ausgerichtet. '
    'Kein generisches Template – eine Website, die Ihre Branche kennt.'
  ),
  'werbeagentur': (
    'Werbeagentur {city}: Full-Service für {b0}, {b1} und lokalen Mittelstand.',
    'Der Wirtschaftsraum {city} ist vielfältig: {b0}, {b1} und {b2} stehen nebeneinander '
    'und kämpfen teils um dieselben Kunden, teils um ganz unterschiedliche Zielgruppen. '
    'Was alle verbindet: Kommunikation, die nicht funktioniert, kostet Marktanteile. '
    'Als Werbeagentur mit 18 Jahren Erfahrung kennen wir diese Branchen. '
    'Wir entwickeln keine generischen Kampagnen, sondern Kommunikation, '
    'die im Wettbewerbsumfeld von {city} und der Region wirkt – '
    'für Print, Digital, Social Media und Außenwerbung, aus einer Hand.'
  ),
  'seo': (
    'SEO in {city}: Sichtbarkeit für {b0} und {b1}.',
    'In {city} googeln potenzielle Kunden täglich nach {b0}, {b1} und {b2}. '
    'Wer bei diesen Suchanfragen nicht in den Top 3 auftaucht, wird schlicht nicht gefunden – '
    'egal wie gut das Angebot wirklich ist. '
    'Lokales SEO für {city} bedeutet: zielgerichtete Keyword-Optimierung '
    'für den regionalen Markt, Google Business Profile, lokale Backlinks und '
    'technisch einwandfreie Seiten. '
    'Wir analysieren, welche Suchanfragen in {city} für Ihr Unternehmen relevant sind – '
    'und sorgen dafür, dass Sie genau dort gefunden werden.'
  ),
  'webagentur': (
    'Webagentur {city}: Technische Lösungen für {b0} und {b1}.',
    '{b0} in {city} hat andere technische Anforderungen als {b1} oder {b2}. '
    'Produktkataloge, Buchungssysteme, Mitgliederportale, Schnittstellen zur Warenwirtschaft – '
    'je nach Branche sind die Anforderungen grundverschieden. '
    'Als Webagentur mit tiefer CMS-Kompetenz (WordPress, Joomla) entwickeln wir '
    'exakt das, was Ihr Betrieb in {city} wirklich braucht: '
    'keine Einheitslösung, sondern eine technische Grundlage, '
    'die mit Ihrem Unternehmen wächst und sich in Ihre bestehende IT integriert.'
  ),
  'marketing': (
    'Marketing in {city}: Strategien für {b0}, {b1} und regionalen Mittelstand.',
    'Der Marketingmix für {b0} in {city} funktioniert anders als für {b1} oder {b2}. '
    'Kanalwahl, Budgetverteilung, Timing und Botschaft müssen zur Branche passen – '
    'und zum Wettbewerbsumfeld in {city}. '
    'Wir entwickeln Marketingstrategien, die realistisch, messbar und umsetzbar sind: '
    'kein blinder Aktionismus, sondern ein Maßnahmenplan, der für Ihre Branche '
    'in {city} konkret funktioniert. '
    'Von Social Media über SEO bis zu Printmaßnahmen – alles aufeinander abgestimmt.'
  ),
  'corporate-design': (
    'Corporate Design in {city}: Markenidentität für {b0} und {b1}.',
    'In {city} stehen {b0}, {b1} und {b2} im täglichen Wettbewerb. '
    'Was die stärksten Anbieter unterscheidet: Sie werden wiedererkannt. '
    'Ein starkes Corporate Design – Logo, Farben, Typografie, Bildsprache – '
    'schafft Vertrauen, bevor das erste Gespräch stattfindet. '
    'Für Handwerksbetriebe in {city} bedeutet das: der Pritschenwagen, '
    'die Visitenkarte und die Website sehen aus wie aus einem Guss. '
    'Für Dienstleister: ein Auftritt, der Kompetenz sofort signalisiert. '
    'Wir entwickeln Markenidentitäten, die in {city} und über die Region hinaus funktionieren.'
  ),
  'drohnenfotografie': (
    'Drohnenaufnahmen in {city}: Luftbilder für {b0} und {b1}.',
    'Der Wirtschaftsraum {city} bietet vielfältige Einsatzmöglichkeiten für professionelle Drohnenfotografie: '
    '{b0} braucht Luftbilder für Exposés, Baudokumentation und Vermarktung. '
    '{b1} nutzt Drohnenaufnahmen für Imagefilme und Messepräsentationen. '
    '{b2} setzt auf Luftperspektiven für Standortmarketing und Kommunikation. '
    'Unsere zertifizierten Piloten kennen die lokalen Luftraumregeln im Raum {city}, '
    'holen alle Genehmigungen ein und liefern Bildmaterial in Studioqualität – '
    'für Print, Digital, Social Media und Film.'
  ),
  'fotografie': (
    'Werbefotografie in {city}: Bilder für {b0}, {b1} und mehr.',
    'Ob Produktfotografie für {b0}, Industriereportage für {b1} oder '
    'Corporate Portraits für {b2} in {city} – '
    'jede Branche braucht Bilder, die ihre Stärken authentisch zeigen. '
    'Stockfotos wirken, wie sie sind: generisch. '
    'Wir fotografieren Ihr Unternehmen in {city}, so wie es wirklich ist – '
    'mit dem Anspruch, dass jedes Bild Vertrauen schafft, bevor das erste Gespräch stattfindet. '
    'Produktfotos, Teambilder, Maschinen, Räume, Events: '
    'alles aus einer Hand, lieferbar in Druck- und Webqualität.'
  ),
}

def render_city_theme_connect(theme, city, is_pillar):
    """Stadt × Theme: einzigartiger Content durch Branchen-Framing + stadtspezifischer Lokalfakt."""
    if is_pillar:
        return ''
    C = CITIES.get(city, {})
    branchen   = C.get('branchen', [])
    lokal_fakt = C.get('lokal_fakt', '')
    if not branchen or theme not in CITY_THEME_CONNECT:
        return ''

    def clean_b(s):
        return s.split('(')[0].strip().rstrip('&').strip()

    b = [clean_b(br) for br in branchen]
    b0 = b[0] if len(b) > 0 else ''
    b1 = b[1] if len(b) > 1 else b0
    b2 = b[2] if len(b) > 2 else b1

    heading_tpl, body_tpl = CITY_THEME_CONNECT[theme]
    heading = heading_tpl.format(city=city, b0=b0, b1=b1, b2=b2)
    body    = body_tpl.format(city=city, b0=b0, b1=b1, b2=b2)
    keyword = THEMES[theme]['keyword']

    fakt_html = (
        f'<p style="font-size:15px;color:var(--mu);line-height:1.75;margin-top:20px;'
        f'padding-top:20px;border-top:1px solid var(--brd)">'
        f'<strong style="color:var(--navy)">{esc(city)} im Überblick:</strong> {esc(lokal_fakt)}</p>'
    ) if lokal_fakt else ''

    return f'''
<!-- ═══ STADT × THEME CONNECT ═══════════════════ -->
<div style="padding:64px 0;background:var(--bg)">
  <div class="w">
    <div class="sec-label">{esc(keyword)} &amp; {esc(city)}</div>
    <h2 class="sec-h2" style="font-size:clamp(22px,2.8vw,38px)">{esc(heading)}</h2>
    <p style="font-size:16px;color:var(--mu);line-height:1.8;max-width:860px;margin-top:20px">{esc(body)}</p>
    {fakt_html}
  </div>
</div>
<hr class="div">
'''


def get_faq_for_city(theme, city):
    """Alle FAQ-Fragen kombinieren (faq + faq2) – bis zu 8 Einträge für FAQPage-Schema."""
    T    = THEMES[theme]
    faq1 = T['faq']
    faq2 = T.get('faq2', [])
    combined = faq1 + [q for q in faq2 if q not in faq1]
    return combined[:8]

def render_pillar_main(theme):
    """Pillar-Seiten: Was-ist + Leistungsbausteine + Branchen (~900 unique Wörter, LSI-reich)."""
    T = THEMES[theme]
    was_ist   = T.get('was_ist', [])
    leistungen = T.get('leistungen', [])
    branchen  = T.get('branchen', [])
    label     = T.get('title', theme.title())
    if not was_ist and not leistungen:
        return ''
    parts = []
    # --- Was ist … ---
    if was_ist:
        parts.append(f'<div style="padding:80px 0;background:var(--wh)">')
        parts.append(f'<div class="w">')
        parts.append(f'<h2>Was ist {esc(label)}?</h2>')
        for p in was_ist:
            parts.append(f'<p style="margin:18px 0;font-size:17px;line-height:1.75;color:var(--mu);max-width:820px">{esc(p)}</p>')
        parts.append(f'</div></div>')
        parts.append('<hr class="div">')
    # --- Leistungsbausteine Grid ---
    if leistungen:
        parts.append('<div style="padding:80px 0;background:var(--bg)">')
        parts.append('<div class="w">')
        parts.append(f'<h2>{esc(label)} – Unsere Leistungsbausteine</h2>')
        parts.append('<p style="margin:12px 0 36px;font-size:17px;color:var(--mu)">Von der Strategie bis zur Umsetzung: Ein vollständiges Leistungsspektrum aus einer Hand.</p>')
        parts.append('<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:24px;margin-top:32px">')
        for item in leistungen:
            icon  = esc(item.get('icon', '●'))
            titel = esc(item.get('titel', ''))
            text  = esc(item.get('text', ''))
            parts.append(
                f'<div style="background:var(--wh);border-radius:12px;padding:28px;box-shadow:0 2px 12px rgba(0,0,0,.07)">'
                f'<div style="font-size:32px;margin-bottom:12px">{icon}</div>'
                f'<h3 style="font-size:17px;margin-bottom:8px">{titel}</h3>'
                f'<p style="font-size:15px;line-height:1.65;color:var(--mu)">{text}</p>'
                f'</div>'
            )
        parts.append('</div></div></div>')
        parts.append('<hr class="div">')
    # --- Branchen ---
    if branchen:
        parts.append('<div style="padding:80px 0;background:var(--wh)">')
        parts.append('<div class="w">')
        parts.append(f'<h2>{esc(label)} für Ihre Branche</h2>')
        parts.append('<p style="margin:12px 0 36px;font-size:17px;color:var(--mu)">Branchenspezifische Lösungen – wir kennen Ihre Anforderungen und sprechen Ihre Sprache.</p>')
        parts.append('<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:20px;margin-top:28px">')
        for b in branchen:
            name = esc(b.get('name', ''))
            text = esc(b.get('text', ''))
            parts.append(
                f'<div style="border-left:4px solid var(--ac);padding:20px 24px;background:var(--bg);border-radius:0 10px 10px 0">'
                f'<h3 style="font-size:16px;margin-bottom:8px">{name}</h3>'
                f'<p style="font-size:15px;line-height:1.6;color:var(--mu)">{text}</p>'
                f'</div>'
            )
        parts.append('</div></div></div>')
        parts.append('<hr class="div">')
    return '\n'.join(parts)


def render_leistungsbausteine(theme, city):
    """Stadt-Seiten: kompakte Leistungsbausteine (4 Items, 2×2-Grid, LSI-Keywords)."""
    T = THEMES[theme]
    leistungen = T.get('leistungen', [])
    if not leistungen:
        return ''
    import hashlib
    # Deterministisch 4 aus allen Items wählen (city-abhängig für Variation)
    seed = int(hashlib.md5(f'{theme}|{city}|lb'.encode()).hexdigest(), 16)
    all_items = leistungen[:]
    # Rotate list by seed so different cities get different first-4
    offset = seed % max(1, len(all_items))
    rotated = all_items[offset:] + all_items[:offset]
    items = rotated[:4]
    label = T.get('title', theme.title())
    parts = []
    parts.append('<div style="padding:64px 0;background:var(--bg)">')
    parts.append('<div class="w">')
    parts.append(f'<h2>{esc(label)} in {esc(city)} – Leistungsüberblick</h2>')
    parts.append('<p style="margin:10px 0 28px;font-size:16px;color:var(--mu)">Was wir für Ihr Unternehmen konkret leisten – von Strategie bis Umsetzung.</p>')
    parts.append('<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:20px">')
    for item in items:
        icon  = esc(item.get('icon', '●'))
        titel = esc(item.get('titel', ''))
        text  = esc(item.get('text', ''))
        parts.append(
            f'<div style="background:var(--wh);border-radius:10px;padding:22px;box-shadow:0 2px 10px rgba(0,0,0,.06)">'
            f'<div style="font-size:28px;margin-bottom:10px">{icon}</div>'
            f'<h3 style="font-size:16px;margin-bottom:6px">{titel}</h3>'
            f'<p style="font-size:14px;line-height:1.6;color:var(--mu)">{text}</p>'
            f'</div>'
        )
    parts.append('</div></div></div>')
    parts.append('<hr class="div">')
    return '\n'.join(parts)


def render_theme_links(current_theme, slug_map, is_pillar, slug=''):
    """3–5 zufällig gewählte Themes + immer Marktbande – deterministisch per Slug-Seed."""
    import hashlib, random as _random
    prefix = '../' if is_pillar else '../../'

    seed = int(hashlib.md5((slug + '_themes').encode()).hexdigest(), 16) % (2**32)
    rng  = _random.Random(seed)

    # fotografie + drohnenfotografie werden immer fix hinzugefügt → aus Zufalls-Pool ausschließen
    other_themes = [(k, T) for k, T in THEMES.items()
                    if k != current_theme and k not in ('fotografie','drohnenfotografie')]
    n_pick       = rng.randint(3, len(other_themes))  # 3–5 Themes
    chosen       = rng.sample(other_themes, n_pick)
    # Sortierung nach Original-Reihenfolge beibehalten
    order = list(THEMES.keys())
    chosen.sort(key=lambda x: order.index(x[0]))

    out = ['<a href="https://www.marktbande.de" class="int-link" target="_blank" rel="noopener">Marktbande – Online-Marketing</a>']
    for k, T in chosen:
        ts = slug_map.get(k, k)
        out.append(f'<a href="{prefix}{ts}/index.html" class="int-link">{esc(T["title"])}</a>')
    # Werbefotografie immer anzeigen (außer auf Fotografie-Seiten selbst)
    if current_theme != 'fotografie':
        out.append(f'<a href="{prefix}werbefotografie/index.html" class="int-link">Werbefotografie</a>')
    # Drohnenfotografie immer als Extra-Link
    out.append(f'<a href="{prefix}drohnenfotografie/index.html" class="int-link">Drohnenfotografie</a>')
    return '\n'.join(out)

# ══════════════════════════════════════════════════════════════════════════════
# SCHEMA.ORG + OG
# ══════════════════════════════════════════════════════════════════════════════
def build_schema(theme, city, slug, canonical, is_pillar):
    label = THEMES[theme]['title']
    faq_items = THEMES[theme]['faq']
    city_name = city if city != 'Bodenseeregion' else 'Bodenseeregion'
    C_data    = CITIES.get(city_name, CITIES['Bodenseeregion'])
    region_name = C_data.get('region', 'Bodensee & Hegau')

    # areaServed: immer Singen (Firmensitz) + die angezeigte Stadt + deren Region
    area_served = [{"@type":"City","name":"Singen (Hohentwiel)"}]
    if city_name not in ('Bodenseeregion', 'Singen'):
        area_served.append({"@type":"City","name": city_name})
    area_served.append({"@type":"AdministrativeArea","name": region_name})

    local_biz = {
        "@context":"https://schema.org","@type":["LocalBusiness","ProfessionalService"],
        "name":"X mind Werbeagentur","alternateName":"x-mind",
        "description":f"Professionelle Werbeagentur in Singen – {label} für Handwerk und Mittelstand in {city_name} und der Bodenseeregion. Gegründet 2007, über 100 Kunden, 18 Jahre Erfahrung.",
        "url":"https://www.x-mind.de","telephone":"+49-7731-9398316","email":"info@x-mind.de",
        "foundingDate":"2007",
        "logo":"https://www.x-mind.de/wp-content/uploads/2025/06/xmind_Logo_2025.png",
        "image":"https://www.x-mind.de/wp-content/uploads/2025/06/xmind_Logo_2025.png",
        "address":{"@type":"PostalAddress","streetAddress":"Freibühlstraße 19",
                   "addressLocality":"Singen (Hohentwiel)","postalCode":"78224",
                   "addressRegion":"Baden-Württemberg","addressCountry":"DE"},
        "geo":{"@type":"GeoCoordinates","latitude":47.7592,"longitude":8.8407},
        "aggregateRating":{"@type":"AggregateRating","ratingValue":"4.9","reviewCount":"47","bestRating":"5","worstRating":"1"},
        "openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],"opens":"08:00","closes":"17:00"}],
        "sameAs":["https://www.facebook.com/xmind.marketing/","https://www.linkedin.com/company/x-mind-cross-media-active-marketing/","https://www.instagram.com/xmind.werbeagentur/"],
        "areaServed": area_served,
    }

    faq_schema = {
        "@context":"https://schema.org","@type":"FAQPage",
        "mainEntity":[{"@type":"Question","name":t(q,city),"acceptedAnswer":{"@type":"Answer","text":t(a,city)}} for q,a in faq_items]
    }

    if is_pillar:
        crumb_items = [
            {"@type":"ListItem","position":1,"name":"x-mind Werbeagentur","item":"https://www.x-mind.de"},
            {"@type":"ListItem","position":2,"name":label,"item":canonical},
        ]
    else:
        crumb_items = [
            {"@type":"ListItem","position":1,"name":"x-mind Werbeagentur","item":"https://www.x-mind.de"},
            {"@type":"ListItem","position":2,"name":label,"item":f"https://www.x-mind.de/{slug}/"},
            {"@type":"ListItem","position":3,"name":f"{label} {city_name}","item":canonical},
        ]
    breadcrumb = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":crumb_items}

    return '\n'.join(
        f'<script type="application/ld+json">\n{json.dumps(s, ensure_ascii=False, indent=2)}\n</script>'
        for s in [local_biz, faq_schema, breadcrumb]
    )

def build_og(theme, city, canonical, is_pillar):
    label = THEMES[theme]['title']
    city_d = city if city != 'Bodenseeregion' else 'Bodenseeregion'
    og_title = f"{label} {city_d} – Professionell & Regional | X mind" if not is_pillar else f"{label} Bodenseeregion | X mind Werbeagentur Singen"
    og_desc  = f"X mind: {label} für Handwerk & Mittelstand in {city_d}. 18 Jahre Erfahrung, über 100 Kunden. Kostenlose Beratung. ✓ Lokal ✓ Persönlich ✓ Verlässlich"
    img = "https://www.x-mind.de/wp-content/uploads/2025/06/xmind_Logo_2025.png"
    return (
        f'<meta property="og:type" content="website">\n'
        f'<meta property="og:url" content="{canonical}">\n'
        f'<meta property="og:title" content="{esc(og_title)}">\n'
        f'<meta property="og:description" content="{esc(og_desc)}">\n'
        f'<meta property="og:image" content="{img}">\n'
        f'<meta property="og:locale" content="de_DE">\n'
        f'<meta property="og:site_name" content="X mind Werbeagentur">\n'
        f'<meta name="twitter:card" content="summary_large_image">\n'
        f'<meta name="twitter:title" content="{esc(og_title)}">\n'
        f'<meta name="twitter:description" content="{esc(og_desc)}">\n'
        f'<meta name="twitter:image" content="{img}">'
    )

def build_hreflang(canonical, is_schaffhausen):
    if not is_schaffhausen:
        return ''
    # DE + CH hreflang für Schaffhausen
    de_url = canonical
    ch_url = canonical  # gleiche URL, aber als de-CH deklariert
    return (
        f'<link rel="alternate" hreflang="de-DE" href="{de_url}">\n'
        f'<link rel="alternate" hreflang="de-CH" href="{ch_url}">\n'
        f'<link rel="alternate" hreflang="x-default" href="{de_url}">'
    )

# ══════════════════════════════════════════════════════════════════════════════
# GALERIE-BILDER – zentral pflegbar, gilt für alle Fotografie-Stadtseiten
# format: "landscape" = 4:3  |  "portrait" = 3:4
# ══════════════════════════════════════════════════════════════════════════════
GALLERY_IMAGES = [
    {"src":"https://www.x-mind.de/wp-content/uploads/2E8A2187-Spektral-Kopie-Kopie-1.jpg","format":"landscape","alt":"Werbefotografie – X mind Werbeagentur"},
    {"src":"https://www.x-mind.de/wp-content/uploads/2E8A2550.jpg",                       "format":"portrait", "alt":"Corporate Portrait – X mind Businessfotografie"},
    {"src":"https://www.x-mind.de/wp-content/uploads/2E8A3265.jpg",                       "format":"landscape","alt":"Produktfotografie – X mind Werbeagentur"},
    {"src":"https://www.x-mind.de/wp-content/uploads/2E8A8780.jpg",                       "format":"landscape","alt":"Industriefotografie – x-mind Bodenseeregion"},
    {"src":"https://www.x-mind.de/wp-content/uploads/3I3A3674.jpg",                       "format":"portrait", "alt":"Businessfotografie – Mitarbeiterportrait x-mind"},
    {"src":"https://www.x-mind.de/wp-content/uploads/23CM0263.jpg",                       "format":"landscape","alt":"Location Shooting – Werbefotografie x-mind"},
    {"src":"https://www.x-mind.de/wp-content/uploads/23CM1243.jpg",                       "format":"landscape","alt":"Handwerk Fotografie – x-mind Werbeagentur Singen"},
    {"src":"https://www.x-mind.de/wp-content/uploads/23CM3796.jpg",                       "format":"landscape","alt":"Lifestyle Fotografie – x-mind Werbeagentur"},
    {"src":"https://www.x-mind.de/wp-content/uploads/74.jpg",                             "format":"portrait", "alt":"Portrait Business – x-mind Corporate"},
    {"src":"https://www.x-mind.de/wp-content/uploads/82.jpg",                             "format":"landscape","alt":"Produktfoto – Werbefotografie x-mind Bodensee"},
    {"src":"https://www.x-mind.de/wp-content/uploads/Meister-Heuser-765.jpg",             "format":"landscape","alt":"Immobilienfotografie – x-mind Werbeagentur"},
    {"src":"https://www.x-mind.de/wp-content/uploads/23CM8846.jpg",                       "format":"landscape","alt":"Teamfoto – Businessfotografie x-mind"},
    {"src":"https://www.x-mind.de/wp-content/uploads/23CM6651-Kopie-_-20x302-1.jpg",      "format":"landscape","alt":"Werbefotografie – x-mind Hegau Bodensee"},
    {"src":"https://www.x-mind.de/wp-content/uploads/23CM4009.jpg",                       "format":"portrait", "alt":"Portrait Businessfotografie – x-mind Werbeagentur"},
    {"src":"https://www.x-mind.de/wp-content/uploads/2E8A3175.jpg",                       "format":"landscape","alt":"Location Shooting – Industriefotografie x-mind"},
    {"src":"https://www.x-mind.de/wp-content/uploads/DSC_4530-Kopie.jpg",                 "format":"landscape","alt":"Drohnenfotografie – Luftaufnahme x-mind"},
    {"src":"https://www.x-mind.de/wp-content/uploads/MG_9808-HDR.jpg",                    "format":"landscape","alt":"Immobilien Fotografie – x-mind Werbeagentur"},
    {"src":"https://www.x-mind.de/wp-content/uploads/MG_9728-HDR.jpg",                    "format":"landscape","alt":"Baudokumentation – Immobilienfotografie x-mind"},
    {"src":"https://www.x-mind.de/wp-content/uploads/MG_9659-2-HDR.jpg",                  "format":"landscape","alt":"Immobilienfotografie – x-mind Bodenseeregion"},
    {"src":"https://www.x-mind.de/wp-content/uploads/MG_9256.jpg",                        "format":"landscape","alt":"Werbefotografie – Unternehmensfotos x-mind"},
    {"src":"https://www.x-mind.de/wp-content/uploads/MG_7895-2.jpg",                      "format":"portrait", "alt":"Corporate Portrait – Businessfotografie x-mind"},
    {"src":"https://www.x-mind.de/wp-content/uploads/MG_7349.jpg",                        "format":"landscape","alt":"Produktfotografie – x-mind Werbeagentur Hegau"},
    {"src":"https://www.x-mind.de/wp-content/uploads/2025/09/MG_6282.jpg",                "format":"landscape","alt":"Location Shooting – Werbefotografie Bodenseeregion"},
    {"src":"https://www.x-mind.de/wp-content/uploads/2025/09/MG_5208-HDR.jpg",            "format":"landscape","alt":"Baudokumentation Baustelle – x-mind Werbeagentur"},
    {"src":"https://www.x-mind.de/wp-content/uploads/2025/09/MG_5127-HDR.jpg",            "format":"landscape","alt":"Immobilienfotografie Neubau – x-mind"},
    {"src":"https://www.x-mind.de/wp-content/uploads/2025/09/MG_4738-HDR.jpg",            "format":"landscape","alt":"Industriefotografie – x-mind Bodensee Hegau"},
    {"src":"https://www.x-mind.de/wp-content/uploads/DJI_20250807190235_0026_Z.webp",      "format":"landscape","alt":"Drohnenfotografie Luftaufnahme – x-mind Werbeagentur"},
    {"src":"https://www.x-mind.de/wp-content/uploads/2025/09/MG_3853-HDR.jpg",            "format":"landscape","alt":"Immobilien Luftbild – Drohnenfotografie x-mind"},
    {"src":"https://www.x-mind.de/wp-content/uploads/2025/09/MG_1274.jpg",                "format":"portrait", "alt":"Businessfotografie Portrait – x-mind"},
    {"src":"https://www.x-mind.de/wp-content/uploads/2025/09/MG_1130.jpg",                "format":"landscape","alt":"Werbefotografie Handwerk – x-mind Werbeagentur"},
    {"src":"https://www.x-mind.de/wp-content/uploads/2E8A7747-copy-scaled.webp",           "format":"portrait", "alt":"Corporate Fotografie – x-mind Businessfotograf"},
    {"src":"https://www.x-mind.de/wp-content/uploads/2E8A8759.webp",                       "format":"landscape","alt":"Werbefotografie Produkt – x-mind Werbeagentur Singen"},
]

OUTDIR   = '/home/boris/CLAUDE CODE/xmind-seo-v8'
BASE_URL = 'https://www.x-mind.de'
TODAY    = '2026-03-11'

# ════════════════════
# EINGEBETTETES LOGO
# ════════════════════
LOGO_B64 = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAPUAAAA7CAMAAACUjTyTAAABC1BMVEX///8IPFDnSSAIPFAIPFDnSSAIPFAIPFDnSSAIPFAIPFDnSSAIPFAIPFDnSSAIPFAIPFDnSSAIPFAIPFAIPFDnSSAIPFAIPFAIPFAIPFDnSSAIPFDnSSDnSSAIPFAIPFDnSSAIPFAIPFAIPFDnSSAIPFDnSSAIPFDnSSAIPFAIPFAIPFDnSSAIPFDnSSAIPFAIPFAIPFDnSSAIPFDnSSAIPFAIPFDnSSAIPFAIPFAIPFAIPFDnSSAIPFAIPFDnSSAIPFAIPFAIPFAIPFDnSSDnSSAIPFDnSSAIPFAIPFAIPFDnSSAIPFAIPFAIPFDnSSAIPFDnSSAIPFDnSSAIPFDnSSDnSSAIPFDnSSBunVVUAAAAV3RSTlMAEBAfICAuMDA9QEBKTFBXWGBkZnBwcXR8foCIiJCSlJecnaCgpqaorLC4urrAwMHEyMjKzM/Q0NPW2Nzc3eDg4uTn6Ojq6+zt7/Dw8vP19vf3+Pj5/f5shUI3AAAFxElEQVRo3t2ae2PaNhDAZUJYwC0jlLAU0iUzWVpoMmoKZOTBcHm0pWRN3ID5/p9kPGy9z8hsZob7D+vQ3U+W7nSSEYqSxHRdD7H7lCsaenPtyRnkSt3TqO2HC/1mOpNv6dD6d1zJIX2KBRjmd2NPoRYu9LlrJh0+NbrAUP2YTJUalnBf9YFn5q8NUMeePGvjE5nqnX/zfyeF0EeXokaH5GUeiJpHuLGHNkWtb4Aa1bG5uhjKnkL3xRMy+mgT1PvkZR/ximcTb35fhp62vrmmzjdCjU5wQHuKARFGaAlB0ktL17HNUKPeFHijdXgWhCD759fTPwrhDS9HDSVtstTu0A4IR40uJrKkHfvsF923n1qetE+8sZicoV2kliZtEtu/x3aTWpa0a/hRGu0o9f4PPlynfTYvu0ItJu3+hqqO/5WaKjMumVFQrzrihml1Z73aVsOIs0356s1gbtBq/Z5wld0Sn+j85D6Ji4+wgYY1nPUytBrlpL8vr6pNy1740sKqMmo2aZMZ31dkzrRsh4htJkjT2y90y21m/qy5/NUlWparcEUembRSwqQNOMtupJJ4P6A1nU4RpCZ77nnSvhwHqzq0CuPSnK6iLZuSA76lSqjbpIu2SH21fDJcDB1vwGlpclfKD7ymM3gBUce+k6StT4NVHXu3jijdxdR6bUtaNO/NKlE7M5SOxMBQNs2TXYmmYxcBaipqT/HO/IdSKJP65DhfZl5ln2UtHa0dhDoOGHjYE1yRDfJCfgOoqQwdsOpoApaGCW0ob3FXrCJ1qgUY6AjQz4Cm85gHqKmkHajqyEOWnI7p+Isa9Z/g/09ZT7LPsKkHgJo6xQkUyqiV1C1nU6lsGU9Iar7dGplU6vjjaA1qV6zqcSr1smhSXTwwEW2PnlmjxttcLles3vP4OfBsMEjV8YoYwkOf4QP3IINDrL0e9eAXWcIwaE+ohTAs4vHIdFZQ6wy1YtWBbY2omKp1ufBFTUN7HeqGJo1Z9MrOEO0mMwfyI19qKmnP5FBtf4Jf6zEY120mx1DYytQt1uYpbqC2ciR9fuDT2dCXmiRt5arjJV64nCXqlb5nm8qBqQcaNNRFyauuCk6+sP2o6ZWtWGCeivaX8oEYSnD5vRuUWth+Fr2WCn7UAIdoJoYf9RE1wRXP/SveLOZtJR49O/f8f8oBqW/FjZG3VBv40QgcIjbRCNQxOmMrVlteSraEFrzOmkJ59hiM2hDN3vA9ZOAhYiaHSE2KDvXK2nPNROAbLQlNVjDquMJgY2u/ynfNI4ha5zYpSvGsKXrryrE0uDN/UqO2JGbLfA8mtNL4Zc9T9/i9mUruaoPUKTh+VAJRtyVmS3xb22eImLnAeXMy5qlVLnpgag2mLgWivlKhtsCVxs283IriYzq5+DfUaKPUPn6w+4ocUGgeBqk/toVavt7wocLkhIrlvd2mjvWpooNM9tVJO2rU0LrOyLzBt1qLwE32aCvPkKJCvU40Ixf019x+vLYl1DdrZK46F78OlKuQqFCbPhs55hiAeIOj9vidUGmvOFyICrXhs2mfbx5swRtSVuNlTKLbioOkqFAnPWufpG4aYvVBvjUqyI7H9W2gRvheKS971WKlSRZxX1qA3W0F9UfqagWOZcSbO2nkonaohW2gTpI7BkE7K54gHQGlpVrSjgw1dVrIndOhn23htJD6bPIAOkSrbQM1dT7ZYU7qTm3xZBh/AS5UWLpK0o4ONapSNx9lnLZfDyS3ALpPNa2StCNEzVw9PN6bpVKp0hpJb3x6PheYJI/DSTtC1OIXAvSl+ZDypuBbVCok7ShRs2GLu0y3iDdUepJi1Vbe6kaKmr3bYb8gaBBvLleEafFDtGhTo8S9A3wtcoW9Sa88/C6sStoRo57lqb+Fr1KqGvWPHDoseAKmJqxR0H3v7Nei/urbTxO6O5H3gEO58YlmHlWXyTsL3+7tiCQN88Zqt9tWs5oXduX/ANG3CsTFMKMzAAAAAElFTkSuQmCC'

# ═══════════════════
# EINGEBETTETES CSS
# ═══════════════════
CSS_BLOCK = '<style>\n/* ═══════════════════════════════════════════\n   X-MIND BRAND TOKENS (pixel-exact from site)\n   Navy    #0c2d3f\n   Red     #e04922\n   Gray-bg #f3f4f6\n   White   #ffffff\n   Text    #1a1a1a\n   Muted   #6b7280\n   ═══════════════════════════════════════════ */\n:root{\n  --navy: #0c2d3f;\n  --red:  #e04922;\n  --bg:   #f3f4f6;\n  --wh:   #ffffff;\n  --tx:   #1a1a1a;\n  --mu:   #6b7280;\n  --brd:  #e5e7eb;\n  --max:  1200px;\n  --f:    \'DM Sans\', sans-serif;\n}\n*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}\nhtml{scroll-behavior:smooth}\nbody{background:var(--wh);color:var(--tx);font-family:var(--f);font-size:16px;line-height:1.6;-webkit-font-smoothing:antialiased}\nimg{max-width:100%;display:block}\na{color:inherit;text-decoration:none}\n.w{max-width:var(--max);margin:0 auto;padding:0 48px}\n@media(max-width:768px){.w{padding:0 20px}}\n\n/* ─── NAV ──────────────────────────────── */\n.nav-outer{\n  position:sticky;top:0;z-index:200;\n  padding:12px 24px;\n  background:rgba(255,255,255,.88);\n  backdrop-filter:blur(14px);\n  -webkit-backdrop-filter:blur(14px);\n  transition:padding .3s ease,box-shadow .3s;\n}\n.nav-outer.scrolled{padding:8px 24px;box-shadow:0 2px 20px rgba(0,0,0,.08)}\n.nav-outer.scrolled .nav-pill{box-shadow:none;border-color:transparent}\n.nav-pill{\n  max-width:960px;margin:0 auto;\n  background:var(--wh);\n  border:1px solid var(--brd);\n  border-radius:100px;\n  padding:10px 14px 10px 24px;\n  display:flex;align-items:center;justify-content:space-between;gap:16px;\n  box-shadow:0 2px 16px rgba(0,0,0,.07);\n}\nimg.nav-logo{height:15px}\n.nav-center{display:flex;align-items:center;gap:8px;font-size:15px;font-weight:600;color:var(--tx)}\n.nav-dot{width:9px;height:9px;border-radius:50%;background:var(--red);animation:pulse 2s ease infinite;flex-shrink:0}\n@keyframes pulse{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.5;transform:scale(1.4)}}\n.nav-links{display:flex;align-items:center;gap:2px;list-style:none}\n.nav-links a{font-size:14px;font-weight:500;color:var(--mu);padding:7px 13px;border-radius:100px;transition:background .15s,color .15s;white-space:nowrap}\n.nav-links a:hover{background:var(--bg);color:var(--navy)}\n.nav-right{display:flex;align-items:center;gap:10px}\n.nav-hallo{background:var(--red);color:var(--wh);font-weight:700;font-size:14px;padding:10px 22px;border-radius:100px;transition:background .2s;white-space:nowrap}\n.nav-tel{font-size:14px;font-weight:600;color:var(--navy);white-space:nowrap;transition:color .2s}\n.nav-tel:hover{color:var(--red)}\n.nav-hallo:hover{background:#c93e1c}\n.nav-burger{display:none;flex-direction:column;justify-content:center;gap:5px;width:40px;height:40px;background:none;border:none;cursor:pointer;padding:6px;border-radius:8px;transition:background .15s}\n.nav-burger:hover{background:var(--bg)}\n.nav-burger span{display:block;width:22px;height:2px;background:var(--navy);border-radius:2px;transform-origin:center;transition:transform .3s ease,opacity .2s,width .3s}\n.nav-burger.open span:nth-child(1){transform:translateY(7px) rotate(45deg)}\n.nav-burger.open span:nth-child(2){opacity:0;width:0}\n.nav-burger.open span:nth-child(3){transform:translateY(-7px) rotate(-45deg)}\n.mobile-menu{display:none;position:fixed;inset:0;z-index:190;background:rgba(12,45,63,.45);backdrop-filter:blur(4px);opacity:0;transition:opacity .3s;pointer-events:none}\n.mobile-menu.open{opacity:1;pointer-events:auto}\n.mobile-drawer{position:absolute;top:0;right:0;bottom:0;width:min(300px,85vw);background:var(--wh);transform:translateX(100%);transition:transform .35s cubic-bezier(.22,1,.36,1);padding:80px 32px 40px;display:flex;flex-direction:column;gap:8px;box-shadow:-8px 0 32px rgba(0,0,0,.12)}\n.mobile-menu.open .mobile-drawer{transform:translateX(0)}\n.mobile-drawer a{font-size:17px;font-weight:600;color:var(--navy);padding:14px 0;border-bottom:1px solid var(--brd);display:block;transition:color .15s}\n.mobile-drawer a:last-child{border-bottom:none}\n.mobile-drawer a:hover{color:var(--red)}\n.mobile-drawer .mob-cta{margin-top:24px;background:var(--red);color:var(--wh);text-align:center;border-radius:100px;padding:15px 24px;border-bottom:none}\n.mobile-drawer .mob-cta:hover{background:#c93e1c;color:var(--wh)}\n@media(max-width:768px){.nav-links{display:none}.nav-tel{display:none}.nav-hallo{display:none}.nav-burger{display:flex}.mobile-menu{display:block}}\n\n/* ─── HERO ─────────────────────────────── */\n.hero{padding:72px 0 80px;text-align:center}\n.hero-label{font-size:14px;font-weight:500;color:var(--mu);margin-bottom:20px;letter-spacing:.3px}\n.hero h1{font-size:clamp(36px,5.5vw,68px);font-weight:800;color:var(--navy);line-height:1.06;letter-spacing:-1.5px;max-width:900px;margin:0 auto 22px}\n.hero-sub{font-size:18px;color:var(--mu);max-width:620px;margin:0 auto 40px;line-height:1.65;font-weight:400}\n.hero-actions{display:flex;align-items:center;justify-content:center;gap:14px;flex-wrap:wrap;margin-bottom:16px}\n.btn-red{display:inline-flex;align-items:center;background:var(--red);color:var(--wh);font-weight:700;font-size:15px;padding:14px 30px;border-radius:100px;border:none;cursor:pointer;transition:background .2s,transform .2s}\n.btn-red:hover{background:#c93e1c;transform:translateY(-1px)}\n.btn-ghost{display:inline-flex;align-items:center;background:transparent;color:var(--navy);font-weight:600;font-size:15px;padding:12px 26px;border-radius:100px;border:2px solid var(--brd);transition:border-color .2s}\n.btn-ghost:hover{border-color:var(--navy)}\n.hero-note{font-size:13px;color:var(--mu);text-align:center}\n\n/* ─── STATS ────────────────────────────── */\n.stats-bar{background:var(--bg);border-top:1px solid var(--brd);border-bottom:1px solid var(--brd);padding:0}\n.stats-inner{display:grid;grid-template-columns:repeat(4,1fr);divide-x:1px solid var(--brd)}\n.stat{padding:32px 24px;text-align:center;border-right:1px solid var(--brd)}\n.stat:last-child{border-right:none}\n.stat-n{font-size:42px;font-weight:800;color:var(--navy);line-height:1;letter-spacing:-1.5px}\n.stat-n em{color:var(--red);font-style:normal}\n.stat-l{font-size:13px;color:var(--mu);margin-top:6px;font-weight:500}\n\n/* ─── SECTION CHROME ────────────────────── */\n.sec{padding:80px 0}\n.sec-sm{padding:56px 0}\n.sec-label{font-size:13px;font-weight:700;text-transform:uppercase;letter-spacing:1.5px;color:var(--red);margin-bottom:12px;display:flex;align-items:center;gap:8px}\n.sec-label::before{content:\'\';display:block;width:18px;height:2px;background:var(--red)}\n.sec-h2{font-size:clamp(28px,3.8vw,48px);font-weight:800;color:var(--navy);letter-spacing:-1px;line-height:1.08;margin-bottom:16px}\n.sec-p{font-size:17px;color:var(--mu);max-width:580px;line-height:1.7}\nhr.div{border:none;border-top:1px solid var(--brd)}\n\n/* ─── CARDS ─────────────────────────────── */\n.cards-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:20px;margin-top:52px}\n.card{background:var(--bg);border-radius:16px;padding:32px 24px}\n.card-icon-wrap{width:52px;height:52px;border-radius:50%;background:var(--red);display:flex;align-items:center;justify-content:center;margin-bottom:20px}\n.card-icon{font-size:22px;line-height:1}\n.card-title{font-size:18px;font-weight:700;color:var(--navy);margin-bottom:10px}\n.card-text{font-size:14px;color:var(--mu);line-height:1.65}\n\n/* ─── PROCESS ───────────────────────────── */\n.process-wrap{display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:start;margin-top:0}\n.process-left h2{font-size:clamp(28px,3.5vw,44px);font-weight:800;color:var(--navy);letter-spacing:-1px;line-height:1.1;margin-bottom:12px}\n.process-left p{font-size:16px;color:var(--mu);line-height:1.65}\n.process-list{display:flex;flex-direction:column;gap:0;margin-top:8px}\n.process-item{display:flex;gap:20px;padding-bottom:36px;position:relative}\n.process-item.has-line::after{content:\'\';position:absolute;left:14px;top:28px;width:1.5px;height:calc(100% - 8px);background:var(--brd)}\n.process-dot{width:28px;height:28px;border-radius:50%;border:2px solid var(--red);background:var(--wh);flex-shrink:0;position:relative;z-index:1;margin-top:3px}\n.process-body h3{font-size:18px;font-weight:700;color:var(--navy);margin-bottom:8px}\n.process-body p{font-size:15px;color:var(--mu);line-height:1.65;margin-bottom:8px}\n.process-tag{font-size:13px;color:var(--mu);font-style:italic}\n\n/* ─── TESTIMONIALS ──────────────────────── */\n.testi-sec{background:var(--wh);padding:80px 0}\n.testi-inner{display:grid;grid-template-columns:300px 1fr;gap:60px;align-items:start}\n.testi-left h2{font-size:clamp(32px,4vw,52px);font-weight:800;color:var(--navy);letter-spacing:-1.5px;line-height:1.05;margin-bottom:16px}\n.testi-stars{display:flex;gap:4px;margin-bottom:12px}\n.star{color:var(--red);font-size:22px}\n.testi-left p{font-size:14px;color:var(--mu);line-height:1.5;margin-bottom:32px}\n.testi-arrows{display:flex;gap:10px}\n.arrow-btn{width:44px;height:44px;border-radius:50%;background:var(--red);border:none;cursor:pointer;display:flex;align-items:center;justify-content:center;color:var(--wh);font-size:18px;font-weight:700;transition:background .2s,transform .15s}\n.arrow-btn:hover{background:#c93e1c;transform:scale(1.08)}\n.testi-grid{display:grid;grid-template-columns:1fr 1fr;gap:16px;transition:opacity .4s ease,transform .4s ease}\n.testi-grid.fading{opacity:0;transform:translateY(12px)}\n.testi-card{background:var(--navy);border-radius:16px;padding:32px 28px;transition:transform .25s ease,box-shadow .25s}\n.testi-card:hover{transform:translateY(-4px);box-shadow:0 12px 32px rgba(12,45,63,.25)}\n.testi-quote{font-size:40px;font-weight:900;color:var(--red);line-height:1;margin-bottom:14px;font-family:Georgia,serif}\n.testi-text{font-size:15px;color:rgba(255,255,255,.85);line-height:1.7;font-style:italic;margin-bottom:20px}\n.testi-author{font-size:12px;font-weight:700;letter-spacing:1.5px;color:rgba(255,255,255,.55);text-transform:uppercase}\n.slide-dots{display:flex;gap:6px;margin-top:12px;justify-content:center}\n.dot{width:8px;height:8px;border-radius:50%;background:var(--brd);cursor:pointer;transition:background .2s}\n.dot-active{background:var(--red)}\n\n/* ─── CITIES CTA BAND ───────────────────── */\n.cities-band{\n  background:var(--navy);\n  border-radius:20px;\n  margin:0 48px;\n  padding:52px 56px;\n}\n.cities-inner{\n  display:grid;\n  grid-template-columns:360px 1fr;\n  gap:64px;\n  align-items:center;\n}\n.cities-left h2{\n  font-size:clamp(26px,3.2vw,42px);\n  font-weight:800;color:var(--wh);\n  letter-spacing:-1px;line-height:1.1;\n  margin-bottom:14px;\n}\n.cities-left p{font-size:15px;color:rgba(255,255,255,.6);line-height:1.65}\n.cities-cols{\n  display:grid;\n  grid-template-columns:repeat(4,1fr);\n  gap:0;\n  border-left:1px solid rgba(255,255,255,.12);\n  padding-left:40px;\n}\n.cities-cols ul{list-style:none;padding:0}\n.cities-cols li{\n  font-size:13px;\n  color:rgba(255,255,255,.6);\n  padding:6px 0;\n  border-bottom:1px solid rgba(255,255,255,.07);\n  line-height:1.4;\n}\n.cities-cols li:last-child{border-bottom:none}\n\n/* ─── CTA BOX ───────────────────────────── */\n.cta-box-wrap{background:var(--bg);border-top:1px solid var(--brd);padding:80px 0}\n.cta-box{display:flex;align-items:center;justify-content:space-between;gap:40px;flex-wrap:wrap}\n.cta-box h2{font-size:clamp(26px,3.5vw,44px);font-weight:800;color:var(--navy);letter-spacing:-1px;line-height:1.1;max-width:560px}\n.cta-box p{font-size:16px;color:var(--mu);margin-top:10px}\n.cta-contact{display:flex;flex-direction:column;gap:14px;align-items:flex-start}\n.cta-tel{font-size:32px;font-weight:800;color:var(--navy);letter-spacing:-1px}\n.cta-tel:hover{color:var(--red)}\n.cta-btns{display:flex;align-items:center;gap:10px;flex-wrap:wrap}\n.btn-outline-navy{display:inline-flex;align-items:center;background:transparent;color:var(--navy);font-weight:700;font-size:15px;padding:14px 26px;border-radius:100px;border:2px solid var(--navy);transition:all .2s;white-space:nowrap}\n.btn-outline-navy:hover{background:var(--navy);color:var(--wh)}\n\n/* ─── FAQ ───────────────────────────────── */\n.faq-list{margin-top:40px;display:flex;flex-direction:column;gap:8px}\n.faq-item{border:1.5px solid var(--brd);border-radius:12px;overflow:hidden;transition:border-color .25s,box-shadow .25s}\n.faq-item.open{border-color:var(--red);box-shadow:0 4px 20px rgba(224,73,34,.08)}\n.faq-btn{width:100%;display:flex;justify-content:space-between;align-items:center;padding:20px 24px;background:none;border:none;cursor:pointer;font-size:16px;font-weight:600;color:var(--navy);text-align:left;gap:16px;font-family:var(--f);transition:color .2s}\n.faq-btn:hover{color:var(--red)}\n.faq-icon{width:30px;height:30px;border-radius:50%;background:var(--bg);font-size:20px;display:flex;align-items:center;justify-content:center;flex-shrink:0;line-height:1;transition:background .25s,color .25s,transform .35s cubic-bezier(.22,1,.36,1)}\n.faq-item.open .faq-icon{background:var(--red);color:var(--wh);transform:rotate(45deg)}\n.faq-body{display:grid;grid-template-rows:0fr;transition:grid-template-rows .35s cubic-bezier(.22,1,.36,1)}\n.faq-item.open .faq-body{grid-template-rows:1fr}\n.faq-inner{overflow:hidden}\n.faq-ans{padding:0 24px 20px;font-size:15px;color:var(--mu);line-height:1.7}\n\n/* ─── INTERNAL LINKS ────────────────────── */\n.int-links-sec{padding:56px 0;background:var(--bg);border-top:1px solid var(--brd)}\n.int-links-grid{display:grid;grid-template-columns:2fr 1fr;gap:60px;align-items:start}\n.int-links-group h3{font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:1.5px;color:var(--mu);margin-bottom:16px}\n.int-links-wrap{display:flex;flex-wrap:wrap;gap:8px;align-items:flex-start}\n.int-link{background:var(--wh);border:1.5px solid var(--brd);color:var(--navy);padding:6px 14px;border-radius:100px;font-size:13px;font-weight:500;transition:all .2s;white-space:nowrap}\n.int-link:hover{border-color:var(--red);color:var(--red);background:var(--wh)}\n\n/* ─── FOOTER ────────────────────────────── */\nfooter{background:var(--navy);padding:0}\n.footer-top{display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:40px;padding:56px 0 40px}\n.footer-col h4{font-size:13px;font-weight:700;text-transform:uppercase;letter-spacing:1.5px;color:rgba(255,255,255,.5);margin-bottom:16px}\n.footer-col a,.footer-col p{display:block;font-size:14px;color:rgba(255,255,255,.65);margin-bottom:8px;transition:color .2s}\n.footer-col a:hover{color:var(--wh)}\nimg.footer-logo{height:13px;filter:brightness(0) invert(1) opacity(.85);margin-bottom:14px}\n.footer-bottom{border-top:1px solid rgba(255,255,255,.1);padding:20px 0;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px}\n.footer-copy{font-size:13px;color:rgba(255,255,255,.4)}\n.footer-legal{display:flex;gap:20px}\n.footer-legal a{font-size:13px;color:rgba(255,255,255,.4);transition:color .2s}\n.footer-legal a:hover{color:rgba(255,255,255,.8)}\n\n/* ─── CITY BLOCK ────────────────────────── */\n.city-block-grid{display:grid;grid-template-columns:1fr 1fr;gap:60px;align-items:start}\n.city-block-info{background:var(--bg);border-radius:16px;padding:32px;border:1px solid var(--brd)}\n.city-block-stats{margin-top:24px;padding-top:20px;border-top:1px solid var(--brd);display:flex;gap:24px;flex-wrap:wrap}\n@media(max-width:768px){.city-block-grid{grid-template-columns:1fr;gap:32px}.city-block-info{padding:24px}}\n\n/* ─── FOTO GALLERY ──────────────────────── */\n.gallery-grid{columns:3;column-gap:8px;margin-top:48px}\n.gallery-item{position:relative;overflow:hidden;border-radius:8px;background:var(--brd);cursor:pointer;break-inside:avoid;margin-bottom:8px;display:block}\n.gallery-item[data-format="landscape"]{aspect-ratio:4/3}\n.gallery-item[data-format="portrait"]{aspect-ratio:3/4}\n.gallery-item img{width:100%;height:100%;object-fit:cover;transition:transform .4s ease;display:block}\n.gallery-item:hover img{transform:scale(1.06)}\n.gallery-item::after{content:\'\';position:absolute;inset:0;background:rgba(12,45,63,.45);opacity:0;transition:opacity .3s;border-radius:8px}\n.gallery-item:hover::after{opacity:1}\n.gallery-item-icon{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-size:24px;opacity:0;transition:opacity .3s;z-index:2;pointer-events:none}\n.gallery-item:hover .gallery-item-icon{opacity:1}\n.gallery-placeholder{width:100%;height:100%;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px;color:var(--mu);font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.5px;text-align:center;padding:8px}\n.gallery-item[data-format="landscape"] .gallery-placeholder{background:linear-gradient(135deg,#e5e7eb 0%,#d1d5db 100%)}\n.gallery-item[data-format="portrait"] .gallery-placeholder{background:linear-gradient(160deg,#d1d5db 0%,#c4c9d0 100%)}\n.gallery-placeholder span{font-size:22px;opacity:.35}\n.lightbox{display:none;position:fixed;inset:0;z-index:1000;background:rgba(0,0,0,.92);align-items:center;justify-content:center;padding:20px}\n.lightbox.open{display:flex}\n.lightbox-inner{position:relative;max-width:1000px;width:100%;max-height:90vh}\n.lightbox-inner img{width:100%;height:auto;max-height:80vh;object-fit:contain;border-radius:8px}\n.lightbox-close{position:absolute;top:-44px;right:0;background:none;border:none;color:#fff;font-size:32px;cursor:pointer;line-height:1;padding:8px}\n.lightbox-nav{position:fixed;top:50%;transform:translateY(-50%);background:rgba(255,255,255,.2);border:none;color:#fff;font-size:32px;cursor:pointer;width:56px;height:56px;border-radius:50%;display:flex;align-items:center;justify-content:center;transition:background .2s;z-index:1001}\n.lightbox-nav:hover{background:rgba(255,255,255,.3)}\n.lightbox-prev{left:12px}.lightbox-next{right:12px}\n.lightbox-caption{color:rgba(255,255,255,.65);font-size:13px;margin-top:12px;text-align:center}\n@media(max-width:700px){.gallery-grid{columns:2}}\n@media(max-width:420px){.gallery-grid{columns:1}}\n.lightbox-counter{color:rgba(255,255,255,.5);font-size:12px;margin-top:8px;text-align:center}\n.leistungs-grid{display:grid;grid-template-columns:1fr 1fr 1fr;gap:32px;margin-top:32px}\n@media(max-width:900px){.leistungs-grid{grid-template-columns:1fr}}\n\n/* ─── RESPONSIVE ─────────────────────────── */\n@media(max-width:1000px){\n  .cards-grid{grid-template-columns:repeat(2,1fr)}\n  .process-wrap{grid-template-columns:1fr}\n  .testi-inner{grid-template-columns:1fr}\n  .testi-grid{grid-template-columns:1fr}\n  .cities-band{margin:0 20px;padding:36px 28px}\n  .cities-inner{grid-template-columns:1fr}\n  .cities-cols{grid-template-columns:repeat(2,1fr);border-left:none;padding-left:0;border-top:1px solid rgba(255,255,255,.12);padding-top:28px}\n  .footer-top{grid-template-columns:1fr 1fr}\n  .int-links-grid{grid-template-columns:1fr}\n  .cta-box{flex-direction:column}\n}\n@media(max-width:640px){\n  .cards-grid{grid-template-columns:1fr}\n  .nav-center span{display:none}\n  .stats-inner{grid-template-columns:repeat(2,1fr)}\n  .stat:nth-child(2){border-right:none}\n  .stat:nth-child(3){border-right:1px solid var(--brd)}\n  .footer-top{grid-template-columns:1fr}\n  .cities-cols{grid-template-columns:1fr 1fr}\n}\n\n/* ─── PROGRESS BAR ──────────────────────── */\n#progress-bar{position:fixed;top:0;left:0;height:3px;width:0%;background:var(--red);z-index:300;transition:width .1s linear;border-radius:0 2px 2px 0}\n\n/* ─── SCROLL REVEAL ─────────────────────── */\n[data-reveal]{opacity:0;transform:translateY(28px);transition:opacity .65s cubic-bezier(.22,1,.36,1),transform .65s cubic-bezier(.22,1,.36,1)}\n[data-reveal].revealed{opacity:1;transform:none}\n[data-reveal-group]>*{opacity:0;transform:translateY(20px);transition:opacity .5s cubic-bezier(.22,1,.36,1),transform .5s cubic-bezier(.22,1,.36,1)}\n[data-reveal-group].revealed>*:nth-child(1){transition-delay:.05s}\n[data-reveal-group].revealed>*:nth-child(2){transition-delay:.15s}\n[data-reveal-group].revealed>*:nth-child(3){transition-delay:.25s}\n[data-reveal-group].revealed>*:nth-child(4){transition-delay:.35s}\n[data-reveal-group].revealed>*{opacity:1;transform:none}\n</style>'



# ═══════════════════
# EFFECTS JS
# ═══════════════════
EFFECTS_JS = r"""/* effects.js – X mind Werbeagentur
   Progress Bar · Nav Shrink · Hamburger · Scroll Reveal · Counter · Testimonials · FAQ
   ──────────────────────────────────────────────────────────────────── */

/* 1. PROGRESS BAR */
(function(){
  var bar=document.getElementById('progress-bar');
  if(!bar)return;
  window.addEventListener('scroll',function(){
    var s=window.scrollY,t=document.documentElement.scrollHeight-window.innerHeight;
    bar.style.width=(t>0?s/t*100:0)+'%';
  },{passive:true});
})();

/* 2. NAV SHRINK */
(function(){
  var nav=document.getElementById('nav');
  if(!nav)return;
  window.addEventListener('scroll',function(){
    nav.classList.toggle('scrolled',window.scrollY>60);
  },{passive:true});
})();

/* 3. HAMBURGER */
(function(){
  var burger=document.getElementById('burger');
  var menu=document.getElementById('mobile-menu');
  if(!burger||!menu)return;
  function open(){menu.classList.add('open');burger.classList.add('open');burger.setAttribute('aria-expanded','true');document.body.style.overflow='hidden';}
  function close(){menu.classList.remove('open');burger.classList.remove('open');burger.setAttribute('aria-expanded','false');document.body.style.overflow='';}
  burger.addEventListener('click',function(){menu.classList.contains('open')?close():open();});
  menu.addEventListener('click',function(e){if(!e.target.closest('.mobile-drawer'))close();});
  menu.querySelectorAll('a').forEach(function(a){a.addEventListener('click',close);});
  document.addEventListener('keydown',function(e){if(e.key==='Escape')close();});
})();

/* 4. SCROLL REVEAL */
(function(){
  var els=document.querySelectorAll('[data-reveal]');
  var grps=document.querySelectorAll('[data-reveal-group]');
  if(!('IntersectionObserver' in window)){
    els.forEach(function(e){e.classList.add('revealed');});
    grps.forEach(function(e){e.classList.add('revealed');});
    return;
  }
  var io=new IntersectionObserver(function(entries){
    entries.forEach(function(en){
      if(en.isIntersecting){en.target.classList.add('revealed');io.unobserve(en.target);}
    });
  },{threshold:0.1,rootMargin:'0px 0px -40px 0px'});
  els.forEach(function(e){io.observe(e);});
  grps.forEach(function(e){io.observe(e);});
})();

/* 5. STATS COUNTER */
(function(){
  var els=document.querySelectorAll('[data-count]');
  if(!els.length)return;
  function animate(el){
    var target=parseFloat(el.dataset.count);
    var suffix=el.dataset.suffix||'';
    var dur=1400,start=performance.now();
    (function tick(now){
      var p=Math.min((now-start)/dur,1),ease=1-Math.pow(1-p,4);
      el.textContent=Math.round(ease*target)+suffix;
      if(p<1)requestAnimationFrame(tick);
    })(start);
  }
  var io=new IntersectionObserver(function(entries){
    entries.forEach(function(en){if(en.isIntersecting){animate(en.target);io.unobserve(en.target);}});
  },{threshold:0.5});
  els.forEach(function(e){io.observe(e);});
})();

/* 6. TESTIMONIALS – Crossfade Grid */
(function(){
  var grid=document.getElementById('testi-grid');
  var dotsWrap=document.getElementById('slide-dots');
  if(!grid||!dotsWrap)return;
  var cards=grid.querySelectorAll('.testi-card');
  var pages=Math.ceil(cards.length/2);
  if(pages<2)return;
  var current=0,animating=false,autoTimer;
  for(var i=0;i<pages;i++){
    (function(idx){
      var d=document.createElement('button');
      d.className='dot'+(idx===0?' dot-active':'');
      d.setAttribute('aria-label','Seite '+(idx+1));
      d.addEventListener('click',function(){goTo(idx);resetAuto();});
      dotsWrap.appendChild(d);
    })(i);
  }
  function goTo(page){
    if(animating||page===current)return;
    animating=true;
    grid.classList.add('fading');
    setTimeout(function(){
      cards.forEach(function(c){
        parseInt(c.dataset.page)===page?c.removeAttribute('hidden'):c.setAttribute('hidden','');
      });
      current=page;
      dotsWrap.querySelectorAll('.dot').forEach(function(d,i){d.classList.toggle('dot-active',i===current);});
      grid.classList.remove('fading');
      animating=false;
    },380);
  }
  function startAuto(){autoTimer=setInterval(function(){goTo((current+1)%pages);},4500);}
  function resetAuto(){clearInterval(autoTimer);startAuto();}
  var pv=document.getElementById('slide-prev'),nx=document.getElementById('slide-next');
  if(pv)pv.addEventListener('click',function(){goTo((current-1+pages)%pages);resetAuto();});
  if(nx)nx.addEventListener('click',function(){goTo((current+1)%pages);resetAuto();});
  var tx=0;
  grid.addEventListener('touchstart',function(e){tx=e.touches[0].clientX;},{passive:true});
  grid.addEventListener('touchend',function(e){
    var dx=e.changedTouches[0].clientX-tx;
    if(Math.abs(dx)>40){goTo(dx<0?(current+1)%pages:(current-1+pages)%pages);resetAuto();}
  },{passive:true});
  startAuto();
})();

/* 7. FAQ ACCORDION */
(function(){
  document.querySelectorAll('.faq-btn').forEach(function(btn){
    btn.addEventListener('click',function(){
      var item=btn.closest('.faq-item');
      var isOpen=item.classList.contains('open');
      document.querySelectorAll('.faq-item.open').forEach(function(o){o.classList.remove('open');});
      if(!isOpen)item.classList.add('open');
    });
  });
})();
"""

# ══════════════════════════════════════════════════════════════════════════════
# SCHEMA.ORG + OG + HREFLANG
# ══════════════════════════════════════════════════════════════════════════════
def build_schema(theme, city, slug, canonical, is_pillar):
    T    = THEMES[theme]
    label = T['title']
    city_name = city if city != 'Bodenseeregion' else 'Bodenseeregion'
    local_biz = {
        "@context":"https://schema.org","@type":["LocalBusiness","ProfessionalService"],
        "name":"X mind Werbeagentur","alternateName":"x-mind",
        "description":f"Professionelle Werbeagentur in Singen \u2013 {label} f\u00fcr Handwerk und Mittelstand in der Bodenseeregion. Gegr\u00fcndet 2007, \u00fcber 100 Kunden, 18 Jahre Erfahrung.",
        "url":BASE_URL,"telephone":"+49-7731-9398316","email":"info@x-mind.de",
        "foundingDate":"2007",
        "logo":"https://www.x-mind.de/wp-content/uploads/2025/06/xmind_Logo_2025.png",
        "image":"https://www.x-mind.de/wp-content/uploads/2025/06/xmind_Logo_2025.png",
        "address":{"@type":"PostalAddress","streetAddress":"Freib\u00fchlstra\u00dfe 19",
                   "addressLocality":"Singen (Hohentwiel)","postalCode":"78224",
                   "addressRegion":"Baden-W\u00fcrttemberg","addressCountry":"DE"},
        "geo":{"@type":"GeoCoordinates","latitude":47.7592,"longitude":8.8407},
        "aggregateRating":{"@type":"AggregateRating","ratingValue":"4.9","reviewCount":"47","bestRating":"5","worstRating":"1"},
        "openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],"opens":"08:00","closes":"17:00"}],
        "sameAs":["https://www.facebook.com/xmind.marketing/","https://www.linkedin.com/company/x-mind-cross-media-active-marketing/","https://www.instagram.com/xmind.werbeagentur/"],
        "areaServed":[{"@type":"City","name":"Singen"},{"@type":"City","name":"Konstanz"},{"@type":"City","name":"Radolfzell"},{"@type":"City","name":"\u00dcberlingen"},{"@type":"State","name":"Baden-W\u00fcrttemberg"}],
    }
    faq_schema = {
        "@context":"https://schema.org","@type":"FAQPage",
        "mainEntity":[{"@type":"Question","name":t(q,city_name),"acceptedAnswer":{"@type":"Answer","text":t(a,city_name)}} for q,a in get_faq_for_city(theme,city_name)]
    }
    if is_pillar:
        breadcrumb = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
            {"@type":"ListItem","position":1,"name":"x-mind Werbeagentur","item":BASE_URL},
            {"@type":"ListItem","position":2,"name":label,"item":canonical},
        ]}
    else:
        breadcrumb = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
            {"@type":"ListItem","position":1,"name":"x-mind Werbeagentur","item":BASE_URL},
            {"@type":"ListItem","position":2,"name":label,"item":f"{BASE_URL}/{slug}/"},
            {"@type":"ListItem","position":3,"name":f"{label} {city_name}","item":canonical},
        ]}
    return (
        f'<script type="application/ld+json">\n{json.dumps(local_biz,ensure_ascii=False,indent=2)}\n</script>\n'
        f'<script type="application/ld+json">\n{json.dumps(faq_schema,ensure_ascii=False,indent=2)}\n</script>\n'
        f'<script type="application/ld+json">\n{json.dumps(breadcrumb,ensure_ascii=False,indent=2)}\n</script>'
    )

def build_og(theme, city, canonical, is_pillar):
    T = THEMES[theme]; label = T['title']
    title = f'{label} {city} | X mind Werbeagentur Singen'
    desc  = f'X mind: {label} f\u00fcr Handwerk & Mittelstand in {city}. 18 Jahre Erfahrung, \u00fcber 100 Kunden. ✓ Lokal ✓ Pers\u00f6nlich ✓ Verl\u00e4sslich'
    img   = 'https://www.x-mind.de/wp-content/uploads/2025/06/xmind_Logo_2025.png'
    return (f'<meta property="og:type" content="website">\n'
            f'<meta property="og:url" content="{canonical}">\n'
            f'<meta property="og:title" content="{esc(title)}">\n'
            f'<meta property="og:description" content="{esc(desc)}">\n'
            f'<meta property="og:image" content="{img}">\n'
            f'<meta property="og:locale" content="de_DE">\n'
            f'<meta property="og:site_name" content="X mind Werbeagentur">\n'
            f'<meta name="twitter:card" content="summary_large_image">\n'
            f'<meta name="twitter:title" content="{esc(title)}">\n'
            f'<meta name="twitter:description" content="{esc(desc)}">\n'
            f'<meta name="twitter:image" content="{img}">')

def build_hreflang(canonical, is_ch, is_at=False):
    if is_at:
        return (f'<link rel="alternate" hreflang="de-DE" href="{canonical}">\n'
                f'<link rel="alternate" hreflang="de-AT" href="{canonical}">\n'
                f'<link rel="alternate" hreflang="x-default" href="{canonical}">')
    if is_ch:
        return (f'<link rel="alternate" hreflang="de-DE" href="{canonical}">\n'
                f'<link rel="alternate" hreflang="de-CH" href="{canonical}">\n'
                f'<link rel="alternate" hreflang="x-default" href="{canonical}">')
    return ''

# ══════════════════════════════════════════════════════════════════════════════
# HAUPT-PAGE-GENERATOR (v6 – eigenst\u00e4ndig, kein template.html)
# ══════════════════════════════════════════════════════════════════════════════
def generate_page(theme, city, out_path, canonical, is_pillar):
    slug      = THEME_SLUGS[theme]
    T         = THEMES[theme]
    C         = CITIES.get(city, CITIES['Bodenseeregion'])
    city_disp = city if city != 'Bodenseeregion' else 'Bodenseeregion'
    is_schaff = city in ('Schaffhausen','St. Gallen','Zürich','Winterthur','Frauenfeld','Basel','Luzern','Frauenfeld')
    is_at     = city in ('Bregenz',)

    meta_title = t(T['metaTitle'], city_disp)
    meta_desc  = t(T['metaDesc'],  city_disp)
    hero_label = t(T['heroLabel'], city_disp)
    hero_title = t(T['heroTitle'], city_disp)
    hero_sub   = t(T['heroSub'],   city_disp)
    hero_cta   = t(T['cta'],       city_disp)
    cta_title  = t(T['ctaTitle'],  city_disp)

    # ── Drohnenfotografie-Theme: Mini-Galerie 3 Bilder ────────────────────────
    GALLERY_DROHNEN = [
        {'src':'https://www.x-mind.de/wp-content/uploads/23CM6651-Kopie-_-20x302-1.jpg',
         'alt':'Drohnenfotografie – Luftaufnahme X mind Werbeagentur', 'format':'landscape'},
        {'src':'https://www.x-mind.de/wp-content/uploads/DJI_20250807190235_0026_Z.webp',
         'alt':'Drohnenaufnahme aus der Luft – X mind Werbeagentur', 'format':'landscape'},
        {'src':'https://www.x-mind.de/wp-content/uploads/2E8A7747-copy-scaled.webp',
         'alt':'Luftbild Drohnenfotografie – X mind', 'format':'portrait'},
    ]

    if theme == 'fotografie':
        def _make_item(i, img, city):
            fmt = img['format']
            src_url = img['src']
            alt = img['alt']
            cap = f'Werbefotografie {city}'
            inner = (f'<img src="{src_url}" alt="{alt} {city}" loading="lazy">'
                     if not src_url.startswith('BILD_URL')
                     else f'<div class="gallery-placeholder"><span>&#128247;</span>Foto {i+1}</div>')
            return (f'<div class="gallery-item" data-format="{fmt}" data-index="{i}" data-caption="{cap}">'
                    + inner + '<div class="gallery-item-icon">&#128269;</div></div>')
        _items_html = '\n'.join(_make_item(i, img, city_disp) for i, img in enumerate(GALLERY_IMAGES))
        _imgs_js = '[' + ','.join(
            '{src:"' + img['src'] + '",alt:"' + img['alt'] + ' ' + city_disp.replace('"','') + '",format:"' + img['format'] + '"}'
            for img in GALLERY_IMAGES
        ) + ']'
        _foto_gallery = (
            '<hr class="div">'
            '<div style="background:var(--bg);border-top:1px solid var(--brd);padding:80px 0" id="galerie">'
            '<div class="w">'
            '<div class="sec-label">Einblicke in unsere Arbeit</div>'
            f'<h2 class="sec-h2">Ausgew&auml;hlte Aufnahmen aus {esc(city_disp)} und der Region.</h2>'
            f'<p class="sec-p">Handwerk, Gastronomie, Industrie, Gewerbe, Dienstleistung und Immobilien &ndash; '
            f'professionelle Werbefotografie von X mind in {esc(city_disp)} und der Bodenseeregion.</p>'
            f'<div class="gallery-grid" id="gallery-grid">{_items_html}</div>'
            '<div style="margin-top:40px;text-align:center;padding-top:32px;border-top:1px solid var(--brd)">'
            '<p style="font-size:14px;color:var(--mu);margin-bottom:16px">'
            'Mehr Einblicke &ndash; alle Fotoprojekte aus der Region:</p>'
            '<a href="https://www.x-mind.de/fotografie/" class="btn-red">'
            '&#128247;&nbsp;Unser Fotografie-Portfolio ansehen</a>'
            '</div></div></div>'
            '<div class="lightbox" id="lightbox" role="dialog" aria-label="Bildvorschau">'
            '<button class="lightbox-close" id="lb-close" aria-label="Schlie&szlig;en">&times;</button>'
            '<button class="lightbox-nav lightbox-prev" id="lb-prev" aria-label="Zur&uuml;ck">&#8249;</button>'
            '<div class="lightbox-inner">'
            '<img id="lb-img" src="" alt="">'
            '<div class="lightbox-counter" id="lb-counter"></div>'
            '</div>'
            '<button class="lightbox-nav lightbox-next" id="lb-next" aria-label="Weiter">&#8250;</button>'
            '</div>'
        )
        _foto_js = (
            f'<script>\nconst GALLERY_IMAGES={_imgs_js};\n'
            'var _lbIdx=0;\n'
            'function _openLb(i){\n'
            '  _lbIdx=i;\n'
            '  var img=GALLERY_IMAGES[i];if(!img)return;\n'
            '  var el=document.getElementById("lb-img");\n'
            '  el.src=img.src||"";\n'
            '  el.alt=img.alt||"";\n'
            '  var ctr=document.getElementById("lb-counter");\n'
            '  if(ctr)ctr.textContent=(i+1)+" / "+GALLERY_IMAGES.length;\n'
            '  document.getElementById("lightbox").classList.add("open");\n'
            '  document.body.style.overflow="hidden";\n'
            '}\n'
            'function _closeLb(){\n'
            '  document.getElementById("lightbox").classList.remove("open");\n'
            '  var el=document.getElementById("lb-img");if(el)el.src="";\n'
            '  document.body.style.overflow="";\n'
            '}\n'
            'function _lbN(){_openLb((_lbIdx+1)%GALLERY_IMAGES.length);}\n'
            'function _lbP(){_openLb((_lbIdx-1+GALLERY_IMAGES.length)%GALLERY_IMAGES.length);}\n'
            'document.addEventListener("DOMContentLoaded",function(){\n'
            '  document.querySelectorAll(".gallery-item").forEach(function(el,i){\n'
            '    el.style.cursor="pointer";\n'
            '    el.addEventListener("click",function(e){e.stopPropagation();_openLb(i);});\n'
            '  });\n'
            '  var c=document.getElementById("lb-close");\n'
            '  if(c)c.addEventListener("click",function(e){e.stopPropagation();_closeLb();});\n'
            '  var n=document.getElementById("lb-next");\n'
            '  if(n)n.addEventListener("click",function(e){e.stopPropagation();_lbN();});\n'
            '  var p=document.getElementById("lb-prev");\n'
            '  if(p)p.addEventListener("click",function(e){e.stopPropagation();_lbP();});\n'
            '  var lb=document.getElementById("lightbox");\n'
            '  if(lb){\n'
            '    lb.addEventListener("click",function(e){\n'
            '      if(e.target===lb)_closeLb();\n'
            '    });\n'
            '    var _tx=0;\n'
            '    lb.addEventListener("touchstart",function(e){_tx=e.touches[0].clientX;},{passive:true});\n'
            '    lb.addEventListener("touchend",function(e){\n'
            '      var dx=e.changedTouches[0].clientX-_tx;\n'
            '      if(Math.abs(dx)>40){if(dx<0)_lbN();else _lbP();}\n'
            '    },{passive:true});\n'
            '  }\n'
            '  document.addEventListener("keydown",function(e){\n'
            '    var lb=document.getElementById("lightbox");\n'
            '    if(!lb||!lb.classList.contains("open"))return;\n'
            '    if(e.key==="Escape")_closeLb();\n'
            '    if(e.key==="ArrowRight")_lbN();\n'
            '    if(e.key==="ArrowLeft")_lbP();\n'
            '  });\n'
            '});\n</script>'
        )
    elif theme == 'drohnenfotografie':
        _foto_gallery = ''
        _foto_js = ''
    else:
        _foto_gallery = ''
        _foto_js = ''


    # Relative Tiefe: Pillar = 1 Ebene tief, City = 2 Ebenen tief
    root     = '../'    if is_pillar else '../../'   # zurück zur Domain-Root
    up_one   = ''       if is_pillar else '../'       # eine Ebene hoch (zum Theme-Verzeichnis)

    if is_pillar:
        crumb = (f'<div class="breadcrumb" style="padding:12px 0 4px;font-size:13px;color:var(--mu)">'
                 f'<a href="{BASE_URL}" style="color:var(--mu);text-decoration:none;">&larr; Zur\u00fcck zur X mind Startseite</a></div>')
    else:
        crumb = (f'<div class="breadcrumb" style="padding:12px 0 4px;font-size:13px;color:var(--mu)">'
                 f'<a href="{BASE_URL}" style="color:var(--mu);text-decoration:none;">x-mind.de</a>'
                 f' &rsaquo; <a href="../index.html" style="color:var(--mu);text-decoration:none;">{esc(T["title"])}</a>'
                 f' &rsaquo; {esc(city_disp)}</div>')

    js_block = ''  # Alle Interaktionslogik ist in assets/effects.js ausgelagert

    html = f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="{esc(meta_desc)}">
<link rel="canonical" href="{canonical}">
{build_hreflang(canonical, is_schaff, is_at)}
<!-- Open Graph + Twitter -->
{build_og(theme, city_disp, canonical, is_pillar)}
<!-- Schema.org -->
{build_schema(theme, city_disp, slug, canonical, is_pillar)}
<!-- Fonts (Bunny Fonts – DSGVO-konform, EU-CDN, kein Google-Tracking) -->
<link rel="preconnect" href="https://fonts.bunny.net">
<link href="https://fonts.bunny.net/css2?family=dm-sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;0,9..40,800;1,9..40,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}assets/style.css">
<script src="{root}assets/effects.js" defer></script>
<title>{esc(meta_title)}</title>
<!-- Matomo -->
<script>
  var _paq = window._paq = window._paq || [];
  _paq.push([\'trackPageView\']);
  _paq.push([\'enableLinkTracking\']);
  (function() {{
    var u="https://xmtrack.de/";
    _paq.push([\'setTrackerUrl\', u+\'matomo.php\']);
    _paq.push([\'setSiteId\', \'2\']);
    var d=document, g=d.createElement(\'script\'), s=d.getElementsByTagName(\'script\')[0];
    g.async=true; g.src=u+\'matomo.js\'; s.parentNode.insertBefore(g,s);
  }})();
</script>
<!-- End Matomo Code -->
</head>
<body>
<div id="progress-bar"></div>
<!-- NAV -->
<div class="nav-outer" id="nav">
  <nav class="nav-pill" role="navigation">
    <a href="{BASE_URL}"><img src="{LOGO_B64}" alt="x mind Werbeagentur" class="nav-logo"></a>
    <ul class="nav-links">
      <li><a href="#leistungen">Leistungen</a></li>
      <li><a href="#so-arbeiten-wir">Vorgehen</a></li>
      <li><a href="#referenzen">Referenzen</a></li>
      <li><a href="#faq">FAQ</a></li>
      <li><a href="#kontakt">Kontakt</a></li>
    </ul>
    <div class="nav-right">
      <a href="tel:+4977319398316" class="nav-tel">07731 9398316</a>
      <a href="#kontakt" class="nav-hallo">Sag Hallo</a>
      <button class="nav-burger" id="burger" aria-label="Men\u00fc \u00f6ffnen" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>
    </div>
  </nav>
</div>
<!-- MOBILE DRAWER -->
<div class="mobile-menu" id="mobile-menu" role="dialog" aria-label="Navigation">
  <div class="mobile-drawer">
    <a href="#leistungen">Leistungen</a>
    <a href="#so-arbeiten-wir">Vorgehen</a>
    <a href="#referenzen">Referenzen</a>
    <a href="#faq">FAQ</a>
    <a href="tel:+4977319398316">07731 9398316</a>
    <a href="#kontakt" class="mob-cta">Sag Hallo \u2192</a>
  </div>
</div>
<!-- HERO -->
<div class="w">
  <section class="hero">
    {crumb}
    <p class="hero-label" id="hero-label" data-reveal>{esc(hero_label)}</p>
    <h1 id="hero-title" data-reveal style="transition-delay:.08s">{esc(hero_title)}</h1>
    <p class="hero-sub" id="hero-sub" data-reveal style="transition-delay:.16s">{esc(hero_sub)}</p>
    <div class="hero-actions">
      <a href="{BASE_URL}/kontakt" class="btn-red" id="hero-cta">{esc(hero_cta)}</a>
      <a href="{BASE_URL}/projekte" class="btn-ghost">Referenzprojekte ansehen</a>
    </div>
    <p class="hero-note">\u2713 Kostenlos &nbsp;\u00b7&nbsp; \u2713 Unverbindlich &nbsp;\u00b7&nbsp; \u2713 Pers\u00f6nlich in Ihrer Region</p>
  </section>
</div>
<!-- STATS -->
<div class="stats-bar">
  <div class="w">
    <div class="stats-inner" data-reveal-group>
      <div class="stat"><div class="stat-n"><span data-count="100" data-suffix="%">100%</span></div><div class="stat-l">Passion</div></div>
      <div class="stat"><div class="stat-n"><span data-count="500" data-suffix="+">500+</span></div><div class="stat-l">Projekte</div></div>
      <div class="stat"><div class="stat-n"><span data-count="18" data-suffix="">18</span></div><div class="stat-l">Jahre Erfahrung</div></div>
      <div class="stat"><div class="stat-n"><span data-count="100" data-suffix="+">100+</span></div><div class="stat-l">Zufriedene Kunden</div></div>
    </div>
  </div>
</div>
<!-- CARDS -->
<div class="w">
  <section class="sec">
    <div class="sec-label">Was wir tun</div>
    <h2 class="sec-h2">Echt. Stark. Verl\u00e4sslich.</h2>
    <p class="sec-p">Kreative Ideen, die im Alltag funktionieren \u2013 schnell, flexibel und l\u00f6sungsorientiert. Wir liefern keine leeren Versprechen, sondern greifbare Ergebnisse.</p>
    <div class="cards-grid" id="cards-grid" data-reveal-group>{render_cards(T, city_disp)}</div>
{('<div class="w"><section style="padding:40px 0 0"><div class="sec-label">Businessfotografie &middot; Produktfotografie &middot; Industriefotografie</div><h2 class="sec-h2" style="font-size:clamp(24px,3vw,38px)">Fotos f&uuml;r Website, Social Media, Print und Broschüren.</h2><div class="leistungs-grid"><div><p style="font-size:14px;font-weight:700;color:var(--navy);margin-bottom:8px">Businessfotografie &amp; Unternehmensfotografie</p><p style="font-size:14px;color:var(--mu);line-height:1.7">Mitarbeiterfotos, Teambilder und Gesch&auml;ftsf&uuml;hrer-Portraits f&uuml;r Website, LinkedIn und Broschüren &ndash; authentisch, professionell, verwertbar.</p></div><div><p style="font-size:14px;font-weight:700;color:var(--navy);margin-bottom:8px">Produktfotografie &amp; Online-Shop</p><p style="font-size:14px;color:var(--mu);line-height:1.7">Freisteller, Lifestyle-Produktfotos und Detailaufnahmen f&uuml;r Online-Shops, Kataloge und Werbeanzeigen &ndash; sauber, verkaufsf&ouml;rdernd, formatgerecht.</p></div><div><p style="font-size:14px;font-weight:700;color:var(--navy);margin-bottom:8px">Industriefotografie &amp; Reportage</p><p style="font-size:14px;color:var(--mu);line-height:1.7">Maschinen, Produktion, Baustellen, Werkst&auml;tten &ndash; Industriefotos f&uuml;r Gesch&auml;ftsberichte, Messeauftritte und Ihre Unternehmenskommunikation.</p></div></div></section></div>' if theme == 'fotografie' else '')}
  </section>
</div>
<span id="leistungen" style="position:relative;top:-80px;display:block"></span>
<hr class="div">
{render_city_block(theme, city, slug, is_pillar)}{render_local_market(theme, city_disp, is_pillar)}{render_city_theme_connect(theme, city_disp, is_pillar)}
<span id="so-arbeiten-wir" style="position:relative;top:-80px;display:block"></span>
<!-- PROCESS -->
<div class="w">
  <section class="sec">
    <div class="process-wrap">
      <div class="process-left">
        <div class="sec-label">Wie wir arbeiten</div>
        <h2>Kreative L\u00f6sungen, die funktionieren \u2013 in drei klaren Schritten zum Erfolg.</h2>
        <p style="margin-top:16px;font-size:16px;color:var(--mu);line-height:1.65">Wir machen keine gro\u00dfen Worte, sondern gute Arbeit. Transparent, planbar und immer mit Ihnen zusammen.</p>
      </div>
      <div><div class="process-list" id="process-list">{render_process(T, city_disp)}</div></div>
    </div>
  </section>
</div>
{render_pillar_main(theme) if is_pillar else render_leistungsbausteine(theme, city_disp)}
<span id="referenzen" style="position:relative;top:-80px;display:block"></span>
<!-- TESTIMONIALS -->
<div class="testi-sec">
  <div class="w">
    <div class="testi-inner">
      <div class="testi-left">
        <h2>\u00dcber 100 zufriedene Kunden</h2>
        <div class="testi-stars" itemprop="aggregateRating" itemscope itemtype="https://schema.org/AggregateRating">
          <span class="star">\u2605</span><span class="star">\u2605</span><span class="star">\u2605</span><span class="star">\u2605</span><span class="star">\u2605</span>
          <span style="font-size:15px;font-weight:700;color:var(--navy);margin-left:8px"><span itemprop="ratingValue">4,9</span> / 5</span>
          <meta itemprop="bestRating" content="5">
          <meta itemprop="worstRating" content="1">
          <meta itemprop="reviewCount" content="47">
        </div>
        <p style="font-size:13px;color:var(--mu);margin-top:4px">Basierend auf <strong>47 Kundenbewertungen</strong></p>
        <p>Mehr als nur Sterne<br>Langfristig zufriedene Kunden</p>
        <div class="testi-arrows">
          <button class="arrow-btn" id="slide-prev" aria-label="Zur\u00fcck">\u2190</button>
          <button class="arrow-btn" id="slide-next" aria-label="Weiter">\u2192</button>
        </div>
      </div>
      <div>
        <div class="testi-grid" id="testi-grid">{render_testimonials_static(theme)}</div>
        <div class="slide-dots" id="slide-dots"></div>
      </div>
    </div>
  </div>
</div>
<!-- CITIES BAND -->
<div style="padding:80px 0;background:var(--wh)">
  <div class="cities-band">
    <div class="cities-inner">
      <div class="cities-left">
        <h2>Service &amp; Kompetenz in ganz Deutschland.</h2>
        <p>Wir sind regional verankert und deutschlandweit f\u00fcr Sie im Einsatz. Zu unseren aktuellen Projektsst\u00e4dten z\u00e4hlen unter anderem:</p>
      </div>
      <div class="cities-cols">{render_cities_html()}</div>
    </div>
  </div>
</div>
<!-- FAQ -->
<div class="w" id="faq">
  <section class="sec">
    <div class="sec-label">H\u00e4ufige Fragen</div>
    <h2 class="sec-h2">Reden wir Klartext \u2013 damit\u2019s richtig l\u00e4uft!</h2>
    <div class="faq-list" id="faq-list" data-reveal style="transition-delay:.1s">{render_faq({'faq': get_faq_for_city(theme, city_disp)}, city_disp)}</div>
  </section>
</div>
{_foto_gallery}
<hr class="div">
<!-- CTA -->
<div class="cta-box-wrap" id="kontakt">
  <div class="w">
    <div class="cta-box">
      <div>
        <h2 id="cta-title">{esc(cta_title)}</h2>
        <p>Rufen Sie an oder schreiben Sie uns eine kurze E-Mail. Wir vereinbaren einen unverbindlichen Beratungstermin.</p>
      </div>
      <div class="cta-contact">
        <a href="tel:+4977319398316" class="cta-tel">07731 9398316</a>
        <div class="cta-btns">
          <a href="{BASE_URL}/kontakt" class="btn-red" id="cta-btn">{esc(hero_cta)}</a>
          <a href="mailto:info@x-mind.de" class="btn-outline-navy">info@x-mind.de</a>
        </div>
      </div>
    </div>
  </div>
</div>
<hr class="div">
<!-- INTERNAL LINKS (SEO) -->
<div class="int-links-sec">
  <div class="w">
    <div class="sec-label" style="margin-bottom:28px">Weitere Seiten</div>
    <div class="int-links-grid">
      <div class="int-links-group">
        <h3>Weitere St\u00e4dte</h3>
        <div class="int-links-wrap" id="other-cities">{render_city_links(theme, city, slug, is_pillar)}</div>
      </div>
      <div class="int-links-group">
        <h3>Weitere Leistungen</h3>
        <div class="int-links-wrap" id="other-themes">{render_theme_links(theme, THEME_SLUGS, is_pillar, slug)}</div>
      </div>
    </div>
  </div>
</div>
<!-- FOOTER -->
<footer>
  <div class="w">
    <div class="footer-top">
      <div class="footer-col">
        <img src="{LOGO_B64}" alt="x mind" class="footer-logo">
        <p>Freib\u00fchlstra\u00dfe 19<br>78224 Singen (Hohentwiel)</p>
        <a href="mailto:info@x-mind.de" style="margin-top:8px">info@x-mind.de</a>
        <a href="tel:+4977319398316">07731 9398316</a>
      </div>
      <div class="footer-col">
        <h4>Quick Links</h4>
        <a href="{BASE_URL}/werbeagentur-singen">Unsere Agentur</a>
        <a href="{BASE_URL}/projekte">Projekte</a>
        <a href="{BASE_URL}/fotografie">Fotografie</a>
        <a href="{BASE_URL}/news">News</a>
        <a href="{BASE_URL}/kontakt">Kontakt</a>
        <a href="https://www.marktbande.de/">Marktbande</a>
        <a href="https://standpunkt-wirtschaft.de/">Standpunkt.Wirtschaft</a>
      </div>
      <div class="footer-col">
        <h4>Leistungen</h4>
        <a href="{root}webdesign/index.html">Webdesign</a>
        <a href="{root}werbeagentur/index.html">Werbeagentur</a>
        <a href="{root}seo-agentur/index.html">SEO Agentur</a>
        <a href="{root}webagentur/index.html">Webagentur</a>
        <a href="{root}marketing-agentur/index.html">Marketing Agentur</a>
        <a href="{root}corporate-design/index.html">Corporate Design</a>
        <a href="{root}werbefotografie/index.html">Werbefotografie</a>
        <a href="{root}drohnenfotografie/index.html">Drohnenfotografie</a>
      </div>
      <div class="footer-col">
        <h4>Socials</h4>
        <a href="https://www.facebook.com/xmind.marketing/">Facebook</a>
        <a href="https://www.linkedin.com/company/x-mind-cross-media-active-marketing/">LinkedIn</a>
        <a href="https://www.instagram.com/xmind.werbeagentur/">Instagram</a>
        <h4 style="margin-top:24px">Rechtliches</h4>
        <a href="{BASE_URL}/impressum">Impressum</a>
        <a href="{BASE_URL}/datenschutz">Datenschutz</a>
      </div>
    </div>
    <div class="footer-bottom">
      <span class="footer-copy">\u00a9 2026 X mind Werbeagentur, Singen (Hohentwiel)</span>
      <div class="footer-legal">
        <a href="{BASE_URL}/impressum">Impressum</a>
        <a href="{BASE_URL}/datenschutz">Datenschutz</a>
      </div>
    </div>
  </div>
</footer>
{js_block}
{_foto_js}
</body>
</html>"""

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)

    has_h1     = f'id="hero-title"' in html and esc(hero_title) in html
    has_schema = html.count('application/ld+json') == 3
    has_og     = 'og:title' in html
    has_canon  = f'<link rel="canonical" href="{canonical}">' in html
    ok = has_h1 and has_schema and has_og and has_canon
    checks = f"h1={'✓' if has_h1 else '✗'} schema={'✓' if has_schema else '✗'} og={'✓' if has_og else '✗'} canon={'✓' if has_canon else '✗'}"
    print(f"{'✓' if ok else '⚠️'} [{checks}]  {out_path.replace(OUTDIR+'/',''):<55}")
    return ok

# ══════════════════════════════════════════════════════════════════════════════
# ROBOTS.TXT
# ══════════════════════════════════════════════════════════════════════════════
def generate_robots():
    content = f"""User-agent: *\nAllow: /\n\nSitemap: {BASE_URL}/sitemap_index.xml\nSitemap: {BASE_URL}/sitemap-landingpages.xml\n\nUser-agent: GPTBot\nAllow: /\n\nUser-agent: Claude-Web\nAllow: /\n\nUser-agent: PerplexityBot\nAllow: /\n\nUser-agent: Googlebot\nAllow: /\n"""
    with open(f'{OUTDIR}/robots.txt','w') as f: f.write(content)
    print("✓  robots.txt")

# ══════════════════════════════════════════════════════════════════════════════
# SITEMAP INDEX
# ══════════════════════════════════════════════════════════════════════════════
def generate_sitemap_index():
    content = f"""<?xml version="1.0" encoding="UTF-8"?>\n<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n  <sitemap><loc>{BASE_URL}/sitemap.xml</loc><lastmod>2026-03-11</lastmod></sitemap>\n  <sitemap><loc>{BASE_URL}/sitemap-landingpages.xml</loc><lastmod>2026-03-11</lastmod></sitemap>\n</sitemapindex>"""
    with open(f'{OUTDIR}/sitemap_index.xml','w') as f: f.write(content)
    print("✓  sitemap_index.xml")

# ══════════════════════════════════════════════════════════════════════════════
# SITEMAP LANDINGPAGES
# ══════════════════════════════════════════════════════════════════════════════
def generate_sitemap():
    themes_s = list(THEME_SLUGS.values())
    cities_s = [c2slug(c) for c in ALL_CITIES]
    lines = ['<?xml version="1.0" encoding="UTF-8"?>','<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">','']
    for ts in themes_s:
        lines.append(f'  <!-- {ts} -->')
        lines.append(f'  <url><loc>{BASE_URL}/{ts}/</loc><lastmod>2026-03-11</lastmod><changefreq>monthly</changefreq><priority>0.9</priority></url>')
        for cs in cities_s:
            lines += [f'  <url><loc>{BASE_URL}/{ts}/{ts}-{cs}/</loc><lastmod>2026-03-11</lastmod><changefreq>monthly</changefreq><priority>0.8</priority></url>']
        lines.append('')
    lines.append('</urlset>')
    with open(f'{OUTDIR}/sitemap-landingpages.xml','w') as f: f.write('\n'.join(lines))
    print(f"✓  sitemap-landingpages.xml ({len([l for l in lines if '<loc>' in l])} URLs)")

# ══════════════════════════════════════════════════════════════════════════════
# LLMS.TXT
# ══════════════════════════════════════════════════════════════════════════════
def generate_llms():
    themes_s = list(THEME_SLUGS.values())
    cities_s = [c2slug(c) for c in ALL_CITIES]
    lines = ["# X mind Werbeagentur",f"# {BASE_URL}","# Optimiert für LLM-Crawler (ChatGPT, Claude, Perplexity, Gemini)","",
        "## Agenturprofil","X mind ist eine Full-Service-Werbeagentur in Singen am Hohentwiel, Baden-Württemberg.",
        "Gegründet: 2007 | Erfahrung: 18 Jahre | Kunden: 100+ | Projekte: 500+",
        "Leistungen: Webdesign, Webagentur, Werbeagentur, SEO, Marketing, Corporate Design, Fotografie, Werbefotografie, Drohnenfotografie, Druckdesign, Kampagnen, Geschäftsberichte",
        "Zielgruppe: Handwerk, Bau, Industrie, Gastronomie, Einzelhandel, KMU, regionaler Mittelstand","",
        "## Kontakt","Adresse: Freibühlstraße 19, 78224 Singen (Hohentwiel), Deutschland",
        "Telefon: +49 7731 9398316 | E-Mail: info@x-mind.de | Web: https://www.x-mind.de","",
        "## Einzugsgebiet","Heimat: Singen, Konstanz, Radolfzell, Hegau, Bodenseeregion",
        "Bodensee-Erweiterung: Überlingen, Friedrichshafen, Meersburg, Stockach, Markdorf, Pfullendorf",
        "Schwarzwald/Ortenau: Freiburg i.Br., Offenburg, Kehl, Lahr, Oberkirch, Schiltach, Gengenbach, Hausach, Triberg",
        "Schwarzwald-Baar/Donau: Villingen-Schwenningen, Tuttlingen, Rottweil, Spaichingen, Donaueschingen, Bad Dürrheim",
        "Tübingen/Neckar: Tübingen, Rottenburg am Neckar",
        "Schweiz: Schaffhausen, St. Gallen, Zürich, Winterthur, Frauenfeld, Basel, Luzern",
        "Österreich: Bregenz (Vorarlberg)",
        "Bundesweit tätig für ausgewählte Kunden","",
        "## Schwestermarken","Marktbande (Online-Marketing & E-Commerce): https://www.marktbande.de",
        "Standpunkt Wirtschaft (Wirtschaftsmagazin): https://standpunkt-wirtschaft.de","",
        "## Positionierung","Claim: Echt. Stark. Verlässlich.",
        "Kernwerte: Keine leeren Versprechen, direkter persönlicher Ansprechpartner, transparente Preise, messbare Ergebnisse.","",
        "## Referenzen","BGO Singen: Corporate Design, Geschäftsberichte, Webseite",
        "MTS Singen: HR-Kampagne Social Media, Karriereseiten","EDEKA Münchow Radolfzell: Eröffnungskampagne",
        "Familienheim Bodensee: Webseite, Kommunikation, Geschäftsberichte","Juri Rixen / Rixen Dach: Webdesign","",
        "## Bewertungen","Durchschnitt: 4.9/5 | Bewertungen: 47 | Quelle: Google Business","","## SEO-Landingpages",
    ]
    for ts in themes_s:
        lines.append(f"\n### {ts}")
        lines.append(f"Pillar: {BASE_URL}/{ts}/")
        for cs in cities_s:
            if cs != 'bodenseeregion':
                lines.append(f"  {BASE_URL}/{ts}/{ts}-{cs}/")
    lines += ["","## Hauptseiten",f"  {BASE_URL}",f"  {BASE_URL}/projekte",f"  {BASE_URL}/fotografie/",f"  {BASE_URL}/drohnenfotografie/",f"  {BASE_URL}/news",f"  {BASE_URL}/kontakt"]
    with open(f'{OUTDIR}/llms.txt','w',encoding='utf-8') as f: f.write('\n'.join(lines))
    print(f"✓  llms.txt ({len(lines)} Zeilen)")

# ══════════════════════════════════════════════════════════════════════════════
# CSS-DATEI GENERIEREN
# ══════════════════════════════════════════════════════════════════════════════
def generate_css():
    css_dir = f'{OUTDIR}/assets'
    os.makedirs(css_dir, exist_ok=True)
    # CSS_BLOCK enthält <style>...</style> – nur den Inhalt schreiben
    css = CSS_BLOCK
    if css.startswith('<style>'):
        css = css[len('<style>'):]
    if css.endswith('</style>'):
        css = css[:-len('</style>')]
    css = css.strip('\n')
    with open(f'{css_dir}/style.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print(f"✓  assets/style.css ({len(css):,} Zeichen)")
    with open(f'{css_dir}/effects.js', 'w', encoding='utf-8') as f:
        f.write(EFFECTS_JS)
    print(f"✓  assets/effects.js ({len(EFFECTS_JS):,} Zeichen)")

# ══════════════════════════════════════════════════════════════════════════════
# PAGES KONFIGURATION & MAIN
# ══════════════════════════════════════════════════════════════════════════════
def make_pages():
    pages  = []
    themes = list(THEMES.keys())
    tier1  = ['Singen','Konstanz','Radolfzell']
    rest   = [c for c in ALL_CITIES if c not in tier1]
    for theme in themes:
        slug = THEME_SLUGS[theme]
        base = f'{OUTDIR}/{slug}'
        pages.append((theme,'Bodenseeregion',f'{base}/index.html',f'{BASE_URL}/{slug}/',True))
        for city in tier1 + rest:
            cs = c2slug(city)
            pages.append((theme,city,f'{base}/{slug}-{cs}/index.html',f'{BASE_URL}/{slug}/{slug}-{cs}/',False))
    return pages

import os as _os
_os.makedirs(OUTDIR, exist_ok=True)
pages = make_pages()
print("X-MIND SEO Landing Page Generator v8")
print("=" * 75)
ok = sum(generate_page(*p) for p in pages)
print("-" * 75)
generate_css()
generate_robots()
generate_sitemap_index()
generate_sitemap()
generate_llms()
print("=" * 75)
print(f"✅  {ok}/{len(pages)} HTML  +  assets/style.css  +  robots.txt  +  sitemap_index.xml  +  sitemap-landingpages.xml  +  llms.txt")
print(f"📁  Ausgabe: {OUTDIR}/")
