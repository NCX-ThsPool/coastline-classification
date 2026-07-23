"""
Thresholding / 阈值分割

中文：
    本模块从连续指数栅格生成二值掩膜。Otsu 阈值只基于有限且有效的像元。
    输出使用 uint8，0 表示背景，255 表示前景。

English:
    This module converts a continuous index array into a uint8 binary mask.
    Otsu estimation uses only finite valid pixels.
"""

from __future__ import annotations

import numpy as np


def otsu_threshold(values: np.ndarray, valid_mask: np.ndarray | None = None) -> float:
    """Calculate an Otsu threshold from finite valid pixels."""
    data = np.asarray(values, dtype=np.float32)
    mask = np.isfinite(data)
    if valid_mask is not None:
        mask &= np.asarray(valid_mask, dtype=bool)

    valid = data[mask]
    if valid.size == 0:
        raise ValueError("No valid pixels are available for Otsu thresholding.")

    try:
        from skimage.filters import threshold_otsu
    except ImportError as exc:
        raise RuntimeError("Otsu thresholding requires scikit-image.") from exc

    return float(threshold_otsu(valid))


def create_binary_mask(
    values: np.ndarray,
    threshold: float,
    *,
    valid_mask: np.ndarray | None = None,
    invert: bool = False,
) -> np.ndarray:
    """Create an unsigned-byte mask containing only 0 and 255."""
    data = np.asarray(values)
    valid = np.isfinite(data)
    if valid_mask is not None:
        valid &= np.asarray(valid_mask, dtype=bool)

    foreground = data > threshold
    if invert:
        foreground = ~foreground

    output = np.zeros(data.shape, dtype=np.uint8)
    output[valid & foreground] = 255
    return output
