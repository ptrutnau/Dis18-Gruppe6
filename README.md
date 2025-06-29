 Researchers Wikidata MAK Collection

## 👥 Authors  
**Pablo Trutnau**  
**Kim Becker**

---

## 🎯 Project Goal

This project aims to **automatically integrate publication data from the MAK Collection** into **Wikidata**.  
It enriches the data with metadata and links researchers to their publications using ORCID.

Main metadata stored in Wikidata includes:
- Title of the publication (`P1476`)
- DOI (`P356`)
- Year of publication (`P577`)
- Authors via ORCID → `P50` (linked items)
- Authors without ORCID → `P2093` (plain text string)
- Full text URL (`P953`)
- Optionally: subject / topic classification

We use a structured JSON file (`mak_metadata_with_orcid.json`) enriched with ORCID data and additional external metadata (e.g. via [DataCite API](https://api.datacite.org/)).

---

## 📁 Project Structure
```
├── Scripts/
│   ├── Analyse_Daten.ipynb
│   ├── extract_datacite.py
│   ├── mak_doi_metadata_fetcher.ipynb
│   ├── orcid_ids.py
│   ├── push_publications_to_wikidata.py
│   ├── test_wikidata_upload.py
│   └── test_wikidata_upload_20.py
├── data/
│   ├── mak_metadata.json
│   ├── mak_metadata_with_orcid.json
│   ├── processed_dois.txt
│   └── ...
├── LICENSE
├── README.md
├── requirements.txt
└── user-config.py
```


## 🧪 Scripts Overview

### `push_publications_to_wikidata.py`
Main script for uploading publications to Wikidata using the enriched JSON metadata.

**Features:**
- Adds DOI, title, publication date, full text URL
- Links authors via ORCID (`P50`), or falls back to name (`P2093`)
- Avoids duplicates using `processed_dois.txt`

---

### `test_wikidata_upload.py`  
Basic example script to create a single publication manually.  
Used for Pywikibot testing and debugging.

---

### `test_wikidata_upload_20.py`  
Modernized test version of the script above.  
Creates 20 random publications

---

### `orcid_ids.py`  
Script to help complete missing ORCID IDs for authors.

**Usage:**
- Extracts authors without ORCID from the JSON
- Helps with manual or automated ORCID lookup

---

### `extract_datacite.py`  
Queries [DataCite](https://api.datacite.org/) for publication metadata using DOI.  
Returns metadata like title, authors, publication year, abstract, etc.  
Useful for enriching the base dataset.

---

### `Analyse_Daten.ipynb`  
Jupyter notebook for analyzing the original MAK metadata.  
Example use cases:
- Check how many entries have ORCID
- Detect duplicates or inconsistencies
- Visualize temporal distribution or completeness

---

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
