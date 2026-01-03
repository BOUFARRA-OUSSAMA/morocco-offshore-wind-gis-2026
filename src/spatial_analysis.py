"""Spatial analysis routines for suitability mapping."""
from pathlib import Path
import numpy as np
import rasterio
from rasterio.enums import Resampling


def resample_raster(src_path: Path, dst_path: Path, scale: float = 1.0, resampling: Resampling = Resampling.bilinear) -> None:
    """Resample a raster by a scale factor."""
    with rasterio.open(src_path) as src:
        transform = src.transform * src.transform.scale(scale, scale)
        profile = src.profile.copy()
        profile.update({"height": int(src.height * scale), "width": int(src.width * scale), "transform": transform})
        data = src.read(out_shape=(src.count, profile["height"], profile["width"]), resampling=resampling)
    dst_path.parent.mkdir(parents=True, exist_ok=True)
    with rasterio.open(dst_path, "w", **profile) as dst:
        dst.write(data)


def weighted_sum(layers: list[np.ndarray], weights: list[float]) -> np.ndarray:
    """Combine standardized raster layers via weighted sum."""
    arr = np.stack(layers)
    w = np.array(weights).reshape(-1, 1, 1)
    return np.sum(arr * w, axis=0)
