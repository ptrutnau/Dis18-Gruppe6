import json
import random
import pywikibot
from pywikibot import pagegenerators

# === KONFIGURATION ===
DATA_FILE = "..data/mak_metadata_with_orcid.json"  # Datei mit ORCID-Daten
NUM_ENTRIES = 20                                 # Anzahl der Testeinträge

# === Wikidata-Verbindung aufbauen ===
site = pywikibot.Site("wikidata", "wikidata")
repo = site.data_repository()

# === Metadaten laden ===
with open(DATA_FILE, encoding="utf-8") as f:
    all_publications = json.load(f)

# Zufällige 20 auswählen
sampled = random.sample(all_publications, min(NUM_ENTRIES, len(all_publications)))

# === Wikidata-Testeinträge erstellen ===
for pub in sampled:
    try:
        title = pub.get("title", "Untitled")
        doi = pub.get("doi")
        year = pub.get("published", 2022)
        url = pub.get("url", "")
        authors = pub.get("authors", [])

        # Neues Item erstellen
        item = pywikibot.ItemPage(repo)
        item.editLabels(labels={"en": title[:250]}, summary="Set English label")

        # Titel (P1476)
        claim_title = pywikibot.Claim(repo, "P1476")
        claim_title.setTarget(pywikibot.WbMonolingualText(title, "en"))
        item.addClaim(claim_title, summary="Add publication title")

        # DOI (P356)
        if doi:
            claim_doi = pywikibot.Claim(repo, "P356")
            claim_doi.setTarget(doi)
            item.addClaim(claim_doi, summary="Add DOI")

        # Publikationsjahr (P577)
        if year:
            claim_date = pywikibot.Claim(repo, "P577")
            claim_date.setTarget(pywikibot.WbTime(year=int(year)))
            item.addClaim(claim_date, summary="Add publication year")

        # Volltext-URL (P953)
        if url:
            claim_url = pywikibot.Claim(repo, "P953")
            claim_url.setTarget(url)
            item.addClaim(claim_url, summary="Add full text URL")

        # Autoren (P50 oder P2093)
        for person in authors:
            name = person.get("name")
            orcid = person.get("orcid")

            if orcid:
                # Suche in Wikidata nach ORCID
                sparql = f'SELECT ?item WHERE {{ ?item wdt:P496 "{orcid}" }}'
                generator = pagegenerators.WikidataSPARQLPageGenerator(sparql, site=site)
                try:
                    author_item = next(generator)
                    claim_author = pywikibot.Claim(repo, "P50")
                    claim_author.setTarget(author_item)
                    item.addClaim(claim_author, summary="Add author with ORCID")
                except StopIteration:
                    if name:
                        claim_text = pywikibot.Claim(repo, "P2093")
                        claim_text.setTarget(name)
                        item.addClaim(claim_text, summary="Add author as string (no ORCID)")
            else:
                if name:
                    claim_text = pywikibot.Claim(repo, "P2093")
                    claim_text.setTarget(name)
                    item.addClaim(claim_text, summary="Add author as string")

        print(f"✅ Neuer Eintrag: {item.getID()} – {title}")

    except Exception as e:
        print(f"❌ Fehler bei DOI {pub.get('doi')}: {e}")
