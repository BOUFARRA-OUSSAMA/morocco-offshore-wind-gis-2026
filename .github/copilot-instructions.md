# GitHub Copilot Instructions for Morocco Offshore Wind Farm Project

## Project Context
GIS-based multi-criteria decision analysis for offshore wind siting in Morocco using fuzzy AHP and weighted overlay. Source paper: Taoufik and Fekri (2021), Energy Conversion and Management: X 11 (2021) 100103.

## Coordinate Reference Systems
- TARGET_CRS = "EPSG:4326" (WGS 84)
- UTM_ZONE_28N = "EPSG:32628"
- RESOLUTION = 0.01 degrees (~1 km)
- Morocco EEZ bounds: west -20.0, south 21.0, east -1.0, north 36.0

## Criteria Order (matches pairwise matrix)
1) wind_speed (0.392)
2) water_depth (0.213)
3) distance_power_grid (0.127)
4) distance_ports (0.056)
5) distance_shoreline (0.056)
6) tourism_density (0.019)
7) distance_airports (0.032)
8) sediment_thickness (0.105)

## Imports Pattern
```
# Standard library
import os
from pathlib import Path

# Third-party
import numpy as np
import pandas as pd
import geopandas as gpd
import rasterio
from rasterio.warp import reproject, Resampling
import matplotlib.pyplot as plt

# Local modules
from src.data_processing import load_vector
from src.fuzzy_ahp import compute_fuzzy_weights
```

## Function Docstrings (Google style)
```
def reclassify_raster(input_path: str, output_path: str, rules: list) -> None:
    """Reclassify raster values according to suitability rules."""
```

## Error Handling Template
```
try:
    with rasterio.open(input_path) as src:
        data = src.read(1)
except FileNotFoundError:
    print(f"File not found: {input_path}")
    return
except Exception as exc:
    print(f"Error processing {input_path}: {exc}")
    return
```

## Common Patterns
- Load and reproject raster: use calculate_default_transform and reproject.
- Vector to distance raster: rasterize features, distance_transform_edt, convert pixels to km (distance_px * resolution * 111).
- Reclassify arrays: iterate rules (min, max, score) and assign with masks.

## Reclassification Rules (Table 5 examples)
- Wind speed: (-inf,4)->0, (4,5)->1, (5,6)->2, (6,7)->3, (7,8)->4, (8,inf)->5
- Water depth: (1000,inf)->0, (500,1000)->1, (200,500)->2, (100,200)->3, (50,100)->4, (-inf,50)->5
- Distance power grid: (50,inf)->1, (40,50)->2, (30,40)->3, (20,30)->4, (-inf,20)->5
- Distance ports: handled by custom two-range logic

## Fuzzy-AHP Constants
- Pairwise matrix (8x8) from Table 6 (use numpy array)
- RANDOM_CONSISTENCY_INDEX = 1.41 (n=8)
- CONSISTENCY_THRESHOLD = 0.10
- FUZZY_SCALE: {1:(1,1,1), 2:(1,2,3), 3:(2,3,4), 4:(3,4,5), 5:(4,5,6), 6:(5,6,7), 7:(6,7,8), 8:(7,8,9), 9:(9,9,9)}

## File Naming
- Raster: {criterion}_{stage}.tif (raw, processed, score)
- Vector: {feature}_{stage}.shp

## Common Issues
- CRS mismatch: always check and to_crs(TARGET_CRS).
- Large rasters: process in windows via block_windows.
- NoData handling: mask with src.nodata before calculations.

## Visualization Standards
- Suitability colors: 0 gray, 1 red, 2 orange, 3 yellow, 4 light green, 5 dark green.
- Figure DPI: 300, figure size about (12, 10).

## When Copilot Generates Code
1) Validate CRS compatibility.
2) Handle NoData and NaN.
3) Confirm outputs are written.
4) Add clear print or progress messages for long tasks.

## Testing Hint
Use small synthetic rasters/vectors to unit test reclassification, distance, and weighting functions before running on full data.
