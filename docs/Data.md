# Data Pipeline

Our project processes data from three main sources:

1. **Excel Input File**: Contains names and some metadata for researchers.
2. **ORCID API**: We use ORCID API to fetch researcher IDs and links to their profiles.
3. **DataCite**: Provides information about researcher publications and associated DOIs.

The workflow includes:
- Extracting data from the Excel file and enriching it with ORCID and DataCite data.
- Converting the enriched data into a suitable format for uploading to Wikidata.
- Using QuickStatements to add the data to Wikidata.

The dataset includes:
- Researcher names
- ORCID IDs
- Publication data
- Institutional information
