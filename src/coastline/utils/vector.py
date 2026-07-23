"""Vector data helpers with optional GeoPandas dependency."""

from __future__ import annotations

from pathlib import Path
from typing import Any


def read_vector(path: str | Path):
    """Read a vector dataset with GeoPandas."""
    try:
        import geopandas as gpd
    except ImportError as exc:
        raise RuntimeError("Vector support requires the 'geo' optional dependencies.") from exc
    return gpd.read_file(path)


def write_vector(frame: Any, path: str | Path) -> Path:
    """Write a GeoDataFrame, creating its parent directory first."""
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    frame.to_file(target)
    return target
