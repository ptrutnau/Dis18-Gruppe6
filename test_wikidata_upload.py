import pywikibot

# Verbindung zu Wikidata aufbauen
site = pywikibot.Site("wikidata", "wikidata")
repo = site.data_repository()

# Beispiel-Metadaten aus DataCite-API
title = "2,6-Diisopropylanilin"  
doi = "10.4126/FRL01-006453569"
publication_year = 2022
fulltext_url = "https://repository.publisso.de/resource/frl:6453569"

# Neues Item erstellen
item = pywikibot.ItemPage(repo)
item.editLabels(labels={"en": title}, summary="Set English label")

# Titel (P1476)
claim_title = pywikibot.Claim(repo, "P1476")
claim_title.setTarget(pywikibot.WbMonolingualText(title, "en"))
item.addClaim(claim_title, summary="Add publication title")

# DOI (P356)
claim_doi = pywikibot.Claim(repo, "P356")
claim_doi.setTarget(doi)
item.addClaim(claim_doi, summary="Add DOI")

# Publikationsdatum (P577)
claim_date = pywikibot.Claim(repo, "P577")
claim_date.setTarget(pywikibot.WbTime(year=publication_year))
item.addClaim(claim_date, summary="Add publication year")

# Volltext-URL (P953)
claim_url = pywikibot.Claim(repo, "P953")
claim_url.setTarget(fulltext_url)
item.addClaim(claim_url, summary="Add full text URL")

print("Wikidata-Eintrag erstellt.")
print("Neuer Wikidata-Eintrag:", item.getID())
