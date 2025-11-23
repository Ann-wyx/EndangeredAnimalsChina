# Endangered Species of China: Geospatial & Trend Visualization
### Interim Implementation Submission (Autumn 2025)

## 1. Project Overview
This project aims to visualize the habitats, population trends, and conservation status of China's top endangered species. By integrating geospatial data with biological statistics, the prototype tells an interactive narrative to raise awareness for **SDG 15 (Life on Land)**.

The current prototype utilizes a hybrid approach: structured data processing via Python and an interactive frontend built with StoryMapJS, enhanced by high-resolution satellite imagery to represent complex natural habitats.

---

## 2. Repository Structure

```text
/EndangeredAnimalsChina
│
├── data/
│   └── raw/                  # Original dataset source (AnimalsChina.csv)
│
├── src/
│   ├── generate_maps.py      # Python script for programmatic map generation (PrettyMapp)
│   └── (Optional) clean_data.py # Basic data verification script
│
├── assets/
│   ├── teaser_figure.png     # Screenshot of the final working prototype
│   ├── icons/                # Vector icons used in the prototype
│   └── habitat_maps/         # Satellite imagery used in the prototype
│
├── docs/
│   ├── metadata.md           # Data dictionary and source definitions
│   ├── architecture.jpg      # System architecture diagram draft
│   └── data_pipeline.png     # Data processing flowchart
│
├── requirements.txt          # Python dependencies for reproduction
└── README.md                 # Project documentation and replication steps
## 3. Environment and Dependencies

While the final prototype is hosted online, the data exploration and experimental visualization phase relied on a Python environment.

### Prerequisites
- Python 3.8 or higher
- `pip` (Python package installer)
- Git

### Python Dependencies
The dependencies required to run the scripts in `/src/` are listed in `requirements.txt`:
- `pandas` (Data manipulation)
- `prettymapp` & `osmnx` (Experimental geospatial visualization based on OpenStreetMap)
- `matplotlib` (Plotting support)

## 4. Replication Steps (Data & Code Component)

To replicate the development environment and run the experimental visualization scripts:

1.  **Clone the Repository:**
    ```bash
    git clone [Your GitHub Repository URL Here]
    cd EndangeredAnimalsChina
    ```
    *(Replace `[Your GitHub Repository URL Here]` with your actual link before saving)*

2.  **Install Dependencies:**
    It is recommended to use a virtual environment.
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Visualization Script:**
    ```bash
    python src/generate_maps.py
    ```
    *Note: See "Known Issues" below regarding running this script.*

## 5. How to Access the Working Prototype (Build/Serve)

As this is an interim prototype focusing on narrative and visualization, the "build" is served via the StoryMapJS platform using assets prepared in this repository.

### **>>> [Click Here to View the Interactive Prototype] <<<**
*(Please replace this text with your actual StoryMapJS share link, e.g., https://uploads.knightlab.com/storymapjs/...)*

### Prototype Construction Workflow:
The prototype was constructed by combining elements stored in this repository:
1.  **Data Ingestion:** Location coordinates and biological data were extracted from `/data/raw/AnimalsChina.csv`.
2.  **Asset Preparation:** Due to limitations in vector data for remote regions (see section 6), high-resolution satellite imagery was manually curated and stored in `/assets/habitat_maps/`. Flat-style icons were stored in `/assets/icons/`.
3.  **Integration:** Data points and assets were integrated into the StoryMapJS platform to create the final interactive narrative.