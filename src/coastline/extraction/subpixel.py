"""Subpixel contour extraction from raster masks."""

from __future__ import annotations

from collections.abc import Iterable

import numpy as np


def extract_pixel_contours(mask: np.ndarray, level: float = 0.5) -> list[np.ndarray]:
    """Return contours in pixel coordinates using marching squares."""
    try:
        from skimage.measure import find_contours
    except ImportError as exc:
        raise RuntimeError("Subpixel contour extraction requires scikit-image.") from exc

    normalized = (np.asarray(mask) > 0).astype(np.float32)
    padded = np.pad(normalized, 1, mode="constant", constant_values=0)
    contours = find_contours(padded, level=level)

    corrected: list[np.ndarray] = []
    for contour in contours:
        # find_contours returns rows and columns; remove padding offset.
        rows = contour[:, 0] - 1.0
        columns = contour[:, 1] - 1.0
        corrected.append(np.column_stack([columns, rows]))
    return corrected


def pixel_to_world(
    contour: np.ndarray,
    transform,
) -> np.ndarray:
    """Convert `(column, row)` contour coordinates to projected coordinates."""
    coordinates = [transform * (float(column), float(row)) for column, row in contour]
    return np.asarray(coordinates, dtype=np.float64)
