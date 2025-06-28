import pandas as pd
import requests
import json
import time
import openpyxl


# Pfade
input_file = "./data/2023-11-17_mapping_makDoi_frlDoi.xlsx"
output_file = "./data/mak_metadata.json"

# Excel einlesen
df = pd.read_excel(input_file)
dois = df["frl_doi"].dropna().unique()

def fetch_metadata(doi):
    url = f"https://api.datacite.org/dois/{doi}"
    try:
        r = requests.get(url)
        if r.status_code != 200:
            print(f"Fehler bei {doi}: Status {r.status_code}")
            return None
        data = r.json().get("data", {}).get("attributes", {})
        authors = []
        for c in data.get("creators", []):
            name = c.get("name")
            orcid = None
            if c.get("nameIdentifiers"):
                orcid = c["nameIdentifiers"][0].get("nameIdentifier")
            authors.append({"name": name, "orcid": orcid})
        return {
            "doi": doi,
            "title": data.get("titles", [{}])[0].get("title"),
            "published": data.get("publicationYear"),
            "url": data.get("url"),
            "authors": authors
        }
    except Exception as e:
        print(f"Fehler bei {doi}: {e}")
        return None

# Alle DOIs verarbeiten
results = []
for doi in dois:
    print(f"Verarbeite {doi} ...")
    metadata = fetch_metadata(doi)
    if metadata:
        results.append(metadata)
    time.sleep(1)  # Rate-Limit beachten

# Speichern
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"✅ Gespeichert unter: {output_file}")
