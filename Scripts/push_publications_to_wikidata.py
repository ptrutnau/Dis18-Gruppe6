import json
import os
import pywikibot
from pywikibot import pagegenerators

# Wikidata-Verbindung
site = pywikibot.Site("wikidata", "wikidata")
repo = site.data_repository()

# Metadaten laden
with open("..data/mak_metadata_with_orcid.json", "r", encoding="utf-8") as f:
    publications = json.load(f)

# Bereits verarbeitete DOIs laden
processed_file = "..data/processed_dois.txt"
if os.path.exists(processed_file):
    with open(processed_file, "r", encoding="utf-8") as f:
        processed_dois = set(line.strip() for line in f)
else:
    processed_dois = set()

def check_doi_exists(doi):
    """Prüft, ob ein Eintrag mit dieser DOI schon existiert"""
    sparql = f'SELECT ?item WHERE {{ ?item wdt:P356 "{doi}" }}'
    generator = pagegenerators.WikidataSPARQLPageGenerator(sparql, site=site)
    return any(generator)

def add_publication(entry):
    title = entry.get("title")
    doi = entry.get("doi")
    published = entry.get("published")
    url = entry.get("url")
    authors = entry.get("authors", [])

    if not title or not doi:
        print(f"⚠️ Übersprungen (unvollständig): {doi}")
        return False

    if check_doi_exists(doi):
        print(f"✅ Bereits vorhanden: {doi}")
        return True

    # Neuen Eintrag erstellen
    item = pywikibot.ItemPage(repo)
    #item.editLabels(labels={"en": title}, summary="Add publication label")
    short_title = title[:250]  # max. 250 Zeichen
    item.editLabels(labels={"en": short_title}, summary="Add publication label")

    # Titel
    claim_title = pywikibot.Claim(repo, "P1476")
    claim_title.setTarget(pywikibot.WbMonolingualText(title, "en"))
    item.addClaim(claim_title, summary="Add title")

    # DOI
    claim_doi = pywikibot.Claim(repo, "P356")
    claim_doi.setTarget(doi)
    item.addClaim(claim_doi, summary="Add DOI")

    # Veröffentlichungsjahr
    if published:
        claim_date = pywikibot.Claim(repo, "P577")
        claim_date.setTarget(pywikibot.WbTime(year=int(published)))
        item.addClaim(claim_date, summary="Add publication year")

    # URL
    if url:
        claim_url = pywikibot.Claim(repo, "P953")
        claim_url.setTarget(url)
        item.addClaim(claim_url, summary="Add fulltext URL")

    # Autor:innen
    for person in authors:
        name = person.get("name")
        orcid = person.get("orcid")

        if orcid:
            # Suche nach ORCID in Wikidata
            sparql = f'SELECT ?item WHERE {{ ?item wdt:P496 "{orcid}" }}'
            generator = pagegenerators.WikidataSPARQLPageGenerator(sparql, site=site)
            try:
                author_item = next(generator)
                # Verlinke Person über P50
                claim_author = pywikibot.Claim(repo, "P50")
                claim_author.setTarget(author_item)
                item.addClaim(claim_author, summary="Add author with ORCID")
            except StopIteration:
                # Kein Wikidata-Eintrag gefunden → fallback zu P2093
                claim_text = pywikibot.Claim(repo, "P2093")
                claim_text.setTarget(name)
                item.addClaim(claim_text, summary="Add author name as string")
        else:
            # Kein ORCID → P2093 (Name als Freitext)
            if name:
                claim_text = pywikibot.Claim(repo, "P2093")
                claim_text.setTarget(name)
                item.addClaim(claim_text, summary="Add author name as string")

    print(f"🚀 Neuer Wikidata-Eintrag für DOI: {doi} erstellt.")
    return True


# Hauptschleife mit Fortschrittskontrolle
for pub in publications:
    doi = pub.get("doi")
    if doi in processed_dois:
        print(f"⏭️  Übersprungen (bereits verarbeitet): {doi}")
        continue

    success = add_publication(pub)

    if success:
        with open(processed_file, "a", encoding="utf-8") as f:
            f.write(doi + "\n")
    
# ✅ Fortschrittsanzeige nach dem Durchlauf
with open("..data/processed_dois.txt") as f:
    done = len(f.readlines())

with open("..data/mak_metadata_with_orcid.json", encoding="utf-8") as f:
    total = len(json.load(f))

print(f"\n📊 Fortschritt: {done} von {total} DOIs verarbeitet ({round(done/total*100, 2)}%)\n")
