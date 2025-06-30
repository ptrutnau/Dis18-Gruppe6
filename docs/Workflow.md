# Project Workflow

The workflow consists of several steps:

```mermaid
graph TD
    A[Start: Excel list from MAK] --> B[ORCID API]
    B --> C[DataCite Lookup]
    C --> D[Generate JSON files]
    D --> E[QuickStatements for Wikidata]
    E --> F[Upload to Wikidata]
