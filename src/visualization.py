"""Mapping utilities for static and interactive outputs."""
from pathlib import Path
from typing import Optional

import folium
import matplotlib.pyplot as plt
import numpy as np
import rasterio
from rasterio.plot import show


def plot_raster(path: Path, cmap: str = "viridis", title: Optional[str] = None) -> None:
    """Render a raster with matplotlib."""
    with rasterio.open(path) as src:
        fig, ax = plt.subplots(figsize=(8, 6))
        show(src, cmap=cmap, ax=ax)
        if title:
            ax.set_title(title)
        plt.tight_layout()
        plt.show()


def add_raster_to_map(path: Path, m: Optional[folium.Map] = None, colormap: str = "YlGnBu") -> folium.Map:
    """Overlay a raster on a folium map."""
    if m is None:
        m = folium.Map(location=[33.6, -7.6], zoom_start=5, tiles="CartoDB positron")
    with rasterio.open(path) as src:
        data = src.read(1)
        bounds = [[src.bounds.bottom, src.bounds.left], [src.bounds.top, src.bounds.right]]
        folium.raster_layers.ImageOverlay(image=data, bounds=bounds, colormap=lambda x: plt.cm.get_cmap(colormap)(x), opacity=0.6).add_to(m)
    return m
