# Researchers Wikidata MAK Collection

## 👥 Authors  
### Pablo Trutnau  
### Kim Becker

---

## 🎯 Project Goal

The aim of this project is the **automated integration of publications from the MAK Collection** into **Wikidata**.  
The following metadata is added in a structured way:

- Title of the publication
- DOI
- Year of publication
- Authors (linked via ORCID → `P50`, or as plain text → `P2093`)
- Full text URL
- Optionally: subject or topic classification

The foundation is a reliable JSON file containing metadata, enriched with ORCID information and, if needed, external sources such as the [DataCite API](https://api.datacite.org/).

---

## 📁 Project Structure & Scripts

### `push_publications_to_wikidata.py`  
Creates or updates Wikidata entries for MAK publications using the `mak_metadata_with_orcid.json` file.

Main features:
- Adds DOI (`P356`), title (`P1476`), year (`P577`), URL (`P953`)
- Links authors via ORCID (`P50`), if available
- Otherwise: stores name as string (`P2093`)
- Supports `UPDATE_ONLY` mode for enriching existing entries
- Progress tracking through `processed_dois.txt`

---

### `test_wikidata_upload.py`  
A minimal example script that manually creates a single Wikidata entry for testing purposes.  
Used to verify the `Pywikibot` setup and basic property usage.

---

### `test_wikidata_upload_20.py`  
A modernized test script for creating Wikidata entries using the current project structure.  
Uploads entries with the main fields: DOI, title, year, and URL.

---

### `orcid_ids.py`  
Utility script for retrieving missing ORCID IDs:
- Filters entries without ORCID
- Supports manual research or automated completion

---

### `extract_datacite.py`  
Queries DOI metadata using the [DataCite REST API](https://api.datacite.org/).  
Fetches metadata such as:
- Title
- Authors
- Year of publication
- Optional: license information  
Can be used for metadata completion or quality control.

---

## 📚 Example Source DOI

- DOI: `10.4126/FRL01-006453569`
- Title: *2,6-Diisopropylanilin*
- Full text: https://repository.publisso.de/resource/frl:6453569

---

## 🛠️ Requirements

- Python 3.8+
- Dependencies listed in `requirements.txt`
- Configuration files:
  - `user-config.py` (for Pywikibot)
  - Optional: API credentials for external data sources

---

## 💻 Using the Project on Another Machine

You can copy the entire project folder to a USB stick and continue working on another machine.  
Keep in mind:
- The `.git` structure is preserved (invisible in Finder, but visible in terminal using `ls -a`)
- You can continue using `git pull`, `git push`, etc.
- Ensure `Pywikibot` is installed and properly configured
