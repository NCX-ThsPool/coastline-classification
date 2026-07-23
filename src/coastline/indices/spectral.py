"""
Spectral-index formulas / 遥感指数公式

中文：
    本模块只负责 NumPy 数值计算。调用者必须提前完成波段读取、重采样、
    像元对齐和 NoData 掩膜。函数尽量保持无副作用，便于测试与复用。

English:
    This module contains pure NumPy formulas. Band loading, resampling,
    alignment, and NoData masking must be completed by the caller.
"""

from __future__ import annotations

import numpy as np

Array = np.ndarray


def safe_normalized_difference(a: Array, b: Array, epsilon: float = 1e-6) -> Array:
    """Calculate `(a - b) / (a + b)` with finite output."""
    numerator = a.astype(np.float32) - b.astype(np.float32)
    denominator = a.astype(np.float32) + b.astype(np.float32)
    result = np.divide(
        numerator,
        denominator,
        out=np.zeros_like(numerator, dtype=np.float32),
        where=np.abs(denominator) > epsilon,
    )
    return np.nan_to_num(result, nan=0.0, posinf=0.0, neginf=0.0)


def ndwi(green: Array, nir: Array) -> Array:
    return safe_normalized_difference(green, nir)


def mndwi(green: Array, swir1: Array) -> Array:
    return safe_normalized_difference(green, swir1)


def ndvi(nir: Array, red: Array) -> Array:
    return safe_normalized_difference(nir, red)


def ndbi(swir1: Array, nir: Array) -> Array:
    return safe_normalized_difference(swir1, nir)


def rvi(nir: Array, red: Array, epsilon: float = 1e-6) -> Array:
    return np.divide(
        nir.astype(np.float32),
        red.astype(np.float32),
        out=np.zeros_like(nir, dtype=np.float32),
        where=np.abs(red) > epsilon,
    )


def evi(
    nir: Array,
    red: Array,
    blue: Array,
    gain: float = 2.5,
    c1: float = 6.0,
    c2: float = 7.5,
    canopy: float = 1.0,
    epsilon: float = 1e-6,
) -> Array:
    numerator = gain * (nir.astype(np.float32) - red.astype(np.float32))
    denominator = (
        nir.astype(np.float32)
        + c1 * red.astype(np.float32)
        - c2 * blue.astype(np.float32)
        + canopy
    )
    return np.divide(
        numerator,
        denominator,
        out=np.zeros_like(numerator, dtype=np.float32),
        where=np.abs(denominator) > epsilon,
    )


def ltidel(
    blue: Array,
    green: Array,
    red: Array,
    nir: Array,
    swir2: Array,
    canopy: float = 0.5,
    epsilon: float = 1e-6,
) -> Array:
    """Calculate the LTidel tidal-flat index used by the research workflow."""
    maximum = np.maximum.reduce([blue, green, red, swir2]).astype(np.float32)
    nir_float = nir.astype(np.float32)
    numerator = (nir_float - maximum) * (1.0 + canopy)
    denominator = nir_float + maximum + canopy
    return np.divide(
        numerator,
        denominator,
        out=np.zeros_like(numerator, dtype=np.float32),
        where=np.abs(denominator) > epsilon,
    )
