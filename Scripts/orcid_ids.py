import json
import requests
from time import sleep
from pathlib import Path

# === Konfiguration ===
BLACKLIST = [
    "MAK Commission",
    "Deutsche Forschungsgemeinschaft",
    "Senatskommission",
    "Arbeitsstoffe"
]

# === Hilfsfunktion: ORCID-Suche ===
def search_orcid(first_name, last_name):
    query = f"given-names:{first_name} AND family-name:{last_name}"
    url = f"https://pub.orcid.org/v3.0/expanded-search/?q={query}"
    headers = {"Accept": "application/json"}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            results = data.get("expanded-result", [])
            if len(results) == 1:  # Nur wenn eindeutiger Treffer
                return results[0].get("orcid-id")
    except Exception as e:
        print(f"Fehler bei Suche nach {first_name} {last_name}: {e}")
    return None

# === Datei laden ===
data_path = Path("..data/mak_metadata.json")
with open(data_path, "r", encoding="utf-8") as f:
    data = json.load(f)

updated = 0
checked = 0
skipped_blacklist = 0
ambiguous = 0

# === Autoren durchsuchen ===
for entry in data:
    for author in entry.get("authors", []):
        name = author.get("name", "")

        # Organisationen und Sammelbezeichnungen überspringen
        if any(bl in name for bl in BLACKLIST):
            skipped_blacklist += 1
            continue

        if author.get("orcid") is None and "," in name:
            last, first = [x.strip() for x in name.split(",", 1)]
            checked += 1
            orcid_id = search_orcid(first, last)
            if orcid_id:
                author["orcid"] = orcid_id
                updated += 1
                print(f"✔️ ORCID gefunden: {name} → {orcid_id}")
            else:
                ambiguous += 1
                print(f"❌ Keine eindeutige ORCID für {name}")
            sleep(1.0)  # Schonung der API

# === Neue Datei speichern ===
out_path = Path("..data/mak_metadata_with_orcid.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# === Statistik ausgeben ===
print("\n🔍 ORCID-Suche abgeschlossen:")
print(f"  ✅ Gefundene ORCID-IDs: {updated}")
print(f"  ❌ Keine eindeutigen Treffer: {ambiguous}")
print(f"  ⏭️  Übersprungen (Blacklist): {skipped_blacklist}")
print(f"  🔎 Gesamt geprüft: {checked}")
