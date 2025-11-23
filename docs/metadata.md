# Data Metadata Scheme

## Dataset 1: Endangered Species of China
- **Source:** IUCN Red List, China National Biodiversity Information Sharing Platform
- **File Name:** `AnimalsChina.csv`
- **Location:** `/data/raw/`
- **Description:** Core dataset containing biological, geographical, and conservation status data for 10 key species.
- **Update Frequency:** Static dataset (Snapshot Autumn 2025).

| Variable Name | Data Type | Description |
| :--- | :--- | :--- |
| `species_id` | Integer | Unique identifier for internal indexing. |
| `common_name_en` | String | English common name. |
| `scientific_name` | String | Latin scientific name (Taxonomy). |
| `iucn_status` | String | Current conservation status (e.g., Vulnerable, Endangered). |
| `population` | Integer | Estimated wild population count (aggregated). |
| `latitude/longitude` | Float | **Fuzzed Coordinates** (Approximate center of habitat to protect species from poaching). |
| `habitat_description` | String | Textual description of the ecosystem. |

## Dataset 2: Geospatial Habitat Imagery
- **Source:** Google Earth Satellite Imagery / OpenStreetMap
- **File Type:** `.jpg` / `.png`
- **Location:** `/assets/`
- **Ethical Note:** Precise nest locations are not shown. Images represent general habitat terrain to promote "Life on Land" (SDG 15) education without enabling illegal tracking.