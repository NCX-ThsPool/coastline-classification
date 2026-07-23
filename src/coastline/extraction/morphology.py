"""
Morphological processing / 形态学处理

中文：
    连通域过滤用于移除小噪声，孔隙填充用于恢复被前景包围的内部空洞。
    参数过强可能删除真实小岛或填掉真实岛屿，应在典型区域验证。

English:
    Component filtering removes small noise and hole filling restores enclosed
    gaps. Aggressive parameters can alter real geographic features.
"""

from __future__ import annotations

import numpy as np


def filter_components(
    mask: np.ndarray,
    *,
    minimum_pixels: int = 5,
    require_2x2_structure: bool = False,
) -> np.ndarray:
    """Remove small connected components from a binary mask."""
    try:
        from scipy import ndimage
    except ImportError as exc:
        raise RuntimeError("Morphological filtering requires SciPy.") from exc

    binary = np.asarray(mask) > 0
    labels, count = ndimage.label(binary)
    if count == 0:
        return np.zeros(binary.shape, dtype=np.uint8)

    sizes = np.bincount(labels.ravel())
    keep = sizes >= max(1, minimum_pixels)
    keep[0] = False

    if require_2x2_structure:
        structure_hits = ndimage.binary_erosion(binary, structure=np.ones((2, 2), dtype=bool))
        component_ids = np.unique(labels[structure_hits])
        structural_keep = np.zeros_like(keep)
        structural_keep[component_ids] = True
        keep &= structural_keep

    return (keep[labels].astype(np.uint8) * 255)


def fill_holes(mask: np.ndarray) -> np.ndarray:
    """Fill internal holes without changing regions connected to the image edge."""
    try:
        from scipy import ndimage
    except ImportError as exc:
        raise RuntimeError("Hole filling requires SciPy.") from exc

    filled = ndimage.binary_fill_holes(np.asarray(mask) > 0)
    return filled.astype(np.uint8) * 255
