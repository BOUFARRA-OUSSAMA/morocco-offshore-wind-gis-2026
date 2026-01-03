# Morocco Offshore Wind Farm Suitability Analysis

GIS-based multi-criteria decision analysis using fuzzy AHP to locate offshore wind farm sites in Morocco's EEZ.

## Project Overview
- Approach: Fuzzy Analytic Hierarchy Process (Fuzzy-AHP) plus weighted overlay
- Source study: Taoufik and Fekri (2021) Energy Conversion and Management: X 11 (2021) 100103
- Study area: Atlantic and Mediterranean coasts, Morocco EEZ (~1.2 million km2)
- Goal: Identify sites totaling about 13.3 GW potential

## Project Structure
```
morocco-offshore-wind-gis/
├── data/
│   ├── raw/              # Original downloaded datasets (14 sources)
│   ├── processed/        # Cleaned, reprojected, clipped data
│   └── outputs/          # Final suitability maps and results
├── notebooks/
│   ├── 01_data_collection.ipynb       # Data download and inventory
│   ├── 02_data_preprocessing.ipynb    # CRS alignment, clipping
│   ├── 03_criteria_mapping.ipynb      # Distance calculations, KDE
│   ├── 04_fuzzy_ahp.ipynb             # Weight calculation
│   ├── 05_suitability_analysis.ipynb  # Weighted overlay
│   └── 06_visualization.ipynb         # Figure generation
├── src/
│   ├── data_processing.py    # Data I/O utilities
│   ├── fuzzy_ahp.py          # AHP and fuzzy AHP algorithms
│   ├── spatial_analysis.py   # GIS operations
│   └── visualization.py      # Plotting functions
├── requirements.txt
├── .gitignore
└── README.md
```

## Evaluation Criteria

### Technical (7)
1. Wind speed (38.5 percent weight)
2. Water depth (20.7 percent)
3. Distance from power grid (12.9 percent)
4. Distance from airports (3.4 percent)
5. Sediment thickness (10.4 percent)
6. Distance from submarine cables (exclusion < 500 m)
7. Shipping routes (exclusion)

### Socio-economic (5)
8. Distance from ports (6.0 percent)
9. Distance from shoreline (6.0 percent)
10. Tourism density (2.0 percent)
11. Blue Flag beaches (exclusion < 2000 m)
12. EEZ boundaries (exclusion outside EEZ)

### Environmental (2)
13. Protected areas (exclusion < 2000 m)
14. Migratory bird routes (exclusion < 1000 m)

## Data Sources (examples)
- Wind speed: Global Wind Atlas 3.0 (GeoTIFF) https://globalwindatlas.info/
- Bathymetry: GEBCO 2020 grid (NetCDF) https://www.gebco.net/
- Power grid: World Bank or OSM (Shapefile) https://energydata.info/
- Ports: Morocco ANP or Natural Earth (CSV or Shapefile) https://www.anp.org.ma/
- Shoreline: GSHHG v2.3.7 (Shapefile) https://www.soest.hawaii.edu/pwessel/gshhg/
- Tourism and airports: OpenStreetMap (Shapefile) https://download.geofabrik.de/
- Sediment thickness: NOAA Geophysics (NetCDF) https://www.ngdc.noaa.gov/mgg/sedthick/
- Submarine cables: TeleGeography (GeoJSON) https://github.com/telegeography/www.submarinecablemap.com
- Shipping routes: EMODnet (GeoTIFF) https://www.emodnet-humanactivities.eu/
- Protected areas: UNEP-WCMC (Shapefile) https://www.protectedplanet.net/
- EEZ boundaries: Marine Regions (Shapefile) https://www.marineregions.org/
- Blue Flag beaches: Blue Flag Global (CSV) https://www.blueflag.global/
- Bird migration: Movebank or BirdLife (Shapefile) https://www.movebank.org/

## Installation and Setup
1. Clone the repository.
2. Create a virtual environment (Python 3.10+).
3. Install dependencies: `pip install -r requirements.txt`.
4. Launch Jupyter or VS Code notebooks and select the desired kernel (local env or Colab).

## Usage Guide
- Step 1: Run `notebooks/01_data_collection.ipynb` to download or log all datasets.
- Step 2: Run `notebooks/02_data_preprocessing.ipynb` to align CRS, clip to EEZ, and resample.
- Step 3: Run `notebooks/03_criteria_mapping.ipynb` for distance rasters, KDE, and exclusion mask.
- Step 4: Run `notebooks/04_fuzzy_ahp.ipynb` to compute weights and consistency.
- Step 5: Run `notebooks/05_suitability_analysis.ipynb` for weighted overlay and classification.
- Step 6: Run `notebooks/06_visualization.ipynb` to generate maps.

## Expected Results
- Three high-potential sites (Essaouira, Boujdour, Dakhla) totaling about 13.3 GW estimated capacity.

## Development Tools
- Python libraries: geopandas, rasterio, xarray, numpy, pandas, scipy, scikit-fuzzy, shapely, pyproj, folium, seaborn, contextily, matplotlib.
- VS Code extensions: GitHub Copilot, Python, Jupyter, GitLens.

## Contribution
Contributions are welcome via pull requests. Please use feature branches and add concise commit messages.

## Status
- Project setup complete
- Data collection in progress
- Downstream phases pending
