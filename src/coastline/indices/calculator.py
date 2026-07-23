"""Band-aware index calculator."""

from __future__ import annotations

from collections.abc import Mapping

import numpy as np

from .spectral import evi, ltidel, mndwi, ndbi, ndvi, ndwi, rvi

_REQUIRED_BANDS = {
    "mndwi": ("green", "swir1"),
    "ndwi": ("green", "nir"),
    "ndvi": ("nir", "red"),
    "evi": ("nir", "red", "blue"),
    "rvi": ("nir", "red"),
    "ndbi": ("swir1", "nir"),
    "ltidel": ("blue", "green", "red", "nir", "swir2"),
}


def calculate_index(name: str, bands: Mapping[str, np.ndarray]) -> np.ndarray:
    """Calculate one index from a semantic band mapping."""
    normalized = name.lower()
    if normalized not in _REQUIRED_BANDS:
        raise ValueError(f"Unsupported index: {name}")

    missing = [band for band in _REQUIRED_BANDS[normalized] if band not in bands]
    if missing:
        raise KeyError(f"Missing bands for {normalized}: {', '.join(missing)}")

    functions = {
        "mndwi": lambda: mndwi(bands["green"], bands["swir1"]),
        "ndwi": lambda: ndwi(bands["green"], bands["nir"]),
        "ndvi": lambda: ndvi(bands["nir"], bands["red"]),
        "evi": lambda: evi(bands["nir"], bands["red"], bands["blue"]),
        "rvi": lambda: rvi(bands["nir"], bands["red"]),
        "ndbi": lambda: ndbi(bands["swir1"], bands["nir"]),
        "ltidel": lambda: ltidel(
            bands["blue"],
            bands["green"],
            bands["red"],
            bands["nir"],
            bands["swir2"],
        ),
    }
    return functions[normalized]()
