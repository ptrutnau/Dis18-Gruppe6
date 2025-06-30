# Code Overview

The code is divided into several Python scripts to handle different parts of the workflow:

1. **`data/orcid_from_excel.py`**: Extracts ORCID IDs from researcher names in the Excel file.
2. **`data/create_orcid_json.py`**: Queries the ORCID API to fetch full data for each researcher and stores it in JSON format.
3. **`data/create_datacite_json.py`**: Extracts DataCite metadata for the researchers' publications.
4. **`wikidata/qs_creator.py`**: Generates QuickStatements (QS) to add researchers to Wikidata.
5. **`wikidata/qs_upload.py`**: Uses pywikibot to upload QuickStatements to Wikidata.

The code is formatted using [Black](https://black.readthedocs.io/en/stable/).
