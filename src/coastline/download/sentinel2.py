"""Google Earth Engine Sentinel-2 export configuration."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from pathlib import Path


@dataclass(frozen=True)
class Sentinel2ExportConfig:
    project: str
    year: int
    bands: tuple[str, ...]
    output_directory: Path
    start_month_day: tuple[int, int] = (4, 1)
    end_month_day: tuple[int, int] = (10, 31)
    maximum_cloud_percent: float = 80.0
    accepted_scl_classes: tuple[int, ...] = (4, 5, 6, 7)
    scale: int = 10

    @property
    def start_date(self) -> date:
        return date(self.year, *self.start_month_day)

    @property
    def end_date(self) -> date:
        return date(self.year, *self.end_month_day)


def initialize_earth_engine(project: str) -> None:
    """Initialize Earth Engine without embedding a private project ID."""
    try:
        import ee
    except ImportError as exc:
        raise RuntimeError("Earth Engine support requires the 'gee' dependency.") from exc
    ee.Initialize(project=project)


def build_collection(config: Sentinel2ExportConfig):
    """Build a masked Sentinel-2 SR Harmonized image collection."""
    try:
        import ee
    except ImportError as exc:
        raise RuntimeError("Earth Engine support requires the 'gee' dependency.") from exc

    accepted = ee.List(list(config.accepted_scl_classes))

    def mask_clouds(image):
        scl = image.select("SCL")
        valid = accepted.map(lambda value: scl.eq(ee.Number(value))).reduce(ee.Reducer.anyNonZero())
        return image.updateMask(valid)

    return (
        ee.ImageCollection("COPERNICUS/S2_SR_HARMONIZED")
        .filterDate(config.start_date.isoformat(), config.end_date.isoformat())
        .filter(ee.Filter.lt("CLOUDY_PIXEL_PERCENTAGE", config.maximum_cloud_percent))
        .map(mask_clouds)
        .select(list(config.bands))
    )
