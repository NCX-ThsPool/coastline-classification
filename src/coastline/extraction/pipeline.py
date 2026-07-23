"""High-level index-to-coastline raster pipeline."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from .morphology import fill_holes, filter_components
from .thresholding import create_binary_mask, otsu_threshold


@dataclass(frozen=True)
class ExtractionResult:
    threshold: float
    raw_mask: np.ndarray
    filtered_mask: np.ndarray
    filled_mask: np.ndarray


def extract_water_mask(
    index_array: np.ndarray,
    *,
    valid_mask: np.ndarray | None = None,
    invert: bool = False,
    minimum_component_pixels: int = 5,
    require_2x2_structure: bool = True,
) -> ExtractionResult:
    """Run Otsu segmentation, component filtering, and hole filling."""
    threshold = otsu_threshold(index_array, valid_mask)
    raw = create_binary_mask(
        index_array,
        threshold,
        valid_mask=valid_mask,
        invert=invert,
    )
    filtered = filter_components(
        raw,
        minimum_pixels=minimum_component_pixels,
        require_2x2_structure=require_2x2_structure,
    )
    filled = fill_holes(filtered)
    return ExtractionResult(threshold, raw, filtered, filled)
