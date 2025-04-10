# Namen
Pablo Trutnau <br>
Kim Becker

# Forscher*innen Wikidata MAK Collection

---

## 🎯 Ziel des Projekts

Das Ziel dieses Projekts ist es, Publikationsdaten aus der **MAK Collection** systematisch in **Wikidata** zu integrieren.  
Durch die Nutzung vorhandener DOI-Verknüpfungen (Wiley-DOIs und MAK-DOIs bzw. FRL-DOIs) sollen relevante Metadaten wie:

- Titel der Publikation
- DOI
- Veröffentlichungsjahr
- Autoren (inkl. ORCID, sofern verfügbar)
- Volltext-URL
- ggf. Fachgebiet/Themen (Subject)

strukturiert im **Wikidata Knowledge Graph** gespeichert werden.

Die Idee ist, eine **automatisierte Pipeline** zu entwickeln, die auf Basis dieser Daten zuverlässige und reproduzierbare Wikidata-Einträge generiert. Grundlage sind dabei öffentlich verfügbare Schnittstellen wie die [DataCite API](https://api.datacite.org/).

---

## Erste Schritte

### Ziel der ersten Phase:
Bevor die eigentliche Pipeline gebaut wird, erfolgt ein **Testlauf mit einem einzelnen Eintrag**, um den Upload-Prozess mit `Pywikibot` zu verifizieren und zu dokumentieren.

---

## Überblick über die enthaltenen Skripte

### `test_wikidata_upload.py`

Dieses Skript erstellt **einen neuen Eintrag in Wikidata** basierend auf manuell festgelegten Metadaten zu einer Publikation aus der MAK Collection.

Es enthält:
- Verbindung zu Wikidata mit `pywikibot`
- Manuelles Setzen der folgenden Eigenschaften:
  - `P1476` – Titel der Publikation
  - `P356` – DOI
  - `P577` – Veröffentlichungsdatum
  - `P953` – URL zur Volltextversion (FRL)

Das Skript demonstriert den vollständigen Ablauf vom Aufbau einer Wikidata-Verbindung bis zur Erstellung eines neuen Items.

---

### `fetch_metadata_from_datacite.py` *(optional/vorbereitet)*

Dieses zweite Skript (bzw. Codeblock) dient zur **Abfrage von Metadaten** zu einer DOI über die DataCite API.

Es ermöglicht die automatische Extraktion von:
- Titel
- Autoren
- Jahr
- Abstract
- Lizenzinformationen
- und mehr

Diese Daten können im nächsten Schritt zur automatisierten Erstellung von Wikidata-Items verwendet werden.

---

## Beispielhafte Datenquelle

Beispiel-DOI zum Testen aus der MAK Collection:

- DOI: `10.4126/FRL01-006453569`
- Titel: *2,6-Diisopropylanilin*
- Volltext: https://repository.publisso.de/resource/frl:6453569

---

## Nächste Schritte

- [ ] Automatische Verarbeitung mehrerer DOIs aus der Excel-Datei (`data/`)
- [ ] Erweiterung der Wikidata-Einträge um Autoren, ORCID, Themen
- [ ] Sicherstellung von Duplikatprüfung (existiert DOI bereits in Wikidata?)
- [ ] Automatisierte Dokumentation und Log-Ausgabe pro Upload
