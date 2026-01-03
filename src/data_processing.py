"""Data extraction, cleaning, and reprojection utilities."""
from pathlib import Path
from typing import List

import geopandas as gpd


def load_vector(path: Path) -> gpd.GeoDataFrame:
    """Load a vector file into a GeoDataFrame."""
    return gpd.read_file(path)


def reproject_layers(layers: List[gpd.GeoDataFrame], crs: str) -> List[gpd.GeoDataFrame]:
    """Reproject multiple layers to a common CRS."""
    return [layer.to_crs(crs) for layer in layers]


def clip_to_boundary(layer: gpd.GeoDataFrame, boundary: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    """Clip a layer to the provided boundary."""
    return gpd.overlay(layer, boundary, how="intersection")


def export_layer(layer: gpd.GeoDataFrame, path: Path) -> None:
    """Write a GeoDataFrame to disk."""
    path.parent.mkdir(parents=True, exist_ok=True)
    layer.to_file(path)
