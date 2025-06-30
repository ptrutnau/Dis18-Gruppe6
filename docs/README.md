 Researchers Wikidata MAK Collection

## 👥 Authors  
**Pablo Trutnau** 11142860 <br>
**Kim Becker** 11137944

---

## 🎯 Project Goal

The goal of this project is the **systematic enrichment and integration of scientific publications from the MAK Collection into Wikidata**.<br>
The MAK Collection, a curated set of toxicological and occupational health-related publications, is maintained in a structured repository, often identified through **Wiley or FRL DOIs**.  

The key aim is to **transform these raw metadata records into linked open data** in Wikidata, making the authorship, publication details, and digital identifiers **machine-readable, searchable, and citable**.

This includes:

- Enhancing the data with **ORCID identifiers** (when available) to uniquely link authors  
- Avoiding duplicate or unlinked authors by **resolving and linking existing Wikidata profiles**  
- Automatically creating **new entries in Wikidata** when missing  
- Cleaning and standardizing the data before integration  

---

## 🔄 Data Pipeline Overview

The structured integration of the MAK Collection into Wikidata follows this multi-step pipeline:

1. **📥 Raw Data Collection**
   - Source: `2023-11-17_mapping_makDoi_frlDoi.xlsx`
   - Contains base metadata (MAK DOIs, FRL DOIs)
  
 ![grafik](https://github.com/user-attachments/assets/c36d8d11-3557-430a-ba58-5ae91997334f)

 | Column       | Description                                                                                         |
|--------------|-----------------------------------------------------------------------------------------------------|
| **`wiley_doi`**  | DOI of the publication on the **Wiley platform**. Typically starts with `10.1002/...`. Refers to the version published by the academic publisher. |
| **`frl_doi`**    | DOI of the same publication in the **FRL repository** (MAK Collection). Starts with `10.4126/FRL01...`. Used for the Open Access reference. |
| **`frl_uri`**    | **Direct URL** to the publication in the Publisso FRL repository. This resolves the `frl_doi` to the accessible full-text publication. |
| **`frl_id`**     | **Internal ID** of the publication within the FRL system, derived from the DOI. Used as a unique identifier. |


  
2. **🌐 Metadata Completion & Conversion to json**
   - Script: `extract_datacite.py`
   - Uses [DataCite API](https://api.datacite.org/) to fetch:
     - Title
     - Authors
     - Publication year
     - License info
     - publisoo url
  - Returns data in json format: `mak_metadata.json`

![grafik](https://github.com/user-attachments/assets/69697874-5b59-44b9-b524-b0ab67a8b629)


3. **🧠 ORCID Enrichment**
   - Script: `orcid_ids.py`
   - Adds missing ORCID IDs based on author names
   - Produces: `mak_metadata_with_orcid.json`

![grafik](https://github.com/user-attachments/assets/59a954aa-c9f4-4a54-90ed-a9f523690282)

4. **📊 Analysis
   - script: `Analyse_Daten.ipynb`
   - little analysis `mak_metadata_with_orcid.json`

   *Findings*:
   ![grafik](https://github.com/user-attachments/assets/c863752b-4011-4208-bf2a-cc30549d6bb4)

   
6. **🧪 Testing**
   - Scripts:
     - `test_wikidata_upload.py`
     - `test_wikidata_upload_20.py`
   - Used to verify that uploads and bot configuration (e.g. `pywikibot`) work correctly before bulk runs.

7. **📤 Wikidata Upload**
   - Script: `push_publications_to_wikidata.py`
   - Uploads structured data from `mak_metadata_with_orcid.json` to Wikidata:
     - Adds `P1476`, `P356`, `P577`, `P953`
     - Authors via `P50` (if ORCID exists) or `P2093` (as string)
   - Tracks progress in `processed_dois.txt`

<img width="913" alt="Bildschirmfoto 2025-06-30 um 16 57 20" src="https://github.com/user-attachments/assets/8c4e2da7-5982-4c28-ade5-a3e20299d5b9" />



 *Random DOI's* <br>
10.4126/FRL01-006456173 -> [url to wikidata](https://www.wikidata.org/wiki/Q134997925) <br>
10.4126/FRL01-006457805 -> [url to wikidata](https://www.wikidata.org/wiki/Q134999826) <br>
10.4126/FRL01-006455910 -> [url to wikidata](https://www.wikidata.org/wiki/Q134997669)

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
Jupyter notebook for analyzing `mak_metadata_with_orcid.json`.  
Example use cases:
- Checks amoumt of authors and publications
- Check how many entries have ORCID
- Detect duplicates or inconsistencies

---

---

## 🛠️ Requirements

- Python 3.8+
- Dependencies listed in `requirements.txt`
- Configuration files:
  - `user-config.py` (for Pywikibot)
  - Optional: API credentials for external data sources

