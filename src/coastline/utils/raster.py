"""Raster I/O helpers with optional Rasterio dependency."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import numpy as np


def read_raster(path: str | Path) -> tuple[np.ndarray, dict[str, Any]]:
    """Read all raster bands as an array shaped `(bands, rows, columns)`."""
    try:
        import rasterio
    except ImportError as exc:
        raise RuntimeError("Raster support requires the 'geo' optional dependencies.") from exc

    with rasterio.open(path) as dataset:
        return dataset.read(), dataset.profile.copy()


def write_raster(
    path: str | Path,
    array: np.ndarray,
    profile: dict[str, Any],
    *,
    nodata: float | int | None = None,
) -> Path:
    """Write a 2-D or 3-D array while preserving georeferencing."""
    try:
        import rasterio
    except ImportError as exc:
        raise RuntimeError("Raster support requires the 'geo' optional dependencies.") from exc

    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    data = array[np.newaxis, ...] if array.ndim == 2 else array

    output_profile = profile.copy()
    output_profile.update(
        count=data.shape[0],
        height=data.shape[1],
        width=data.shape[2],
        dtype=str(data.dtype),
        compress="lzw",
    )
    if nodata is not None:
        output_profile["nodata"] = nodata

    with rasterio.open(target, "w", **output_profile) as dataset:
        dataset.write(data)

    return target
