"""DEM download helpers."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class BoundingBox:
    west: float
    south: float
    east: float
    north: float

    def validate(self) -> None:
        if self.west >= self.east or self.south >= self.north:
            raise ValueError("Invalid bounding box ordering.")
