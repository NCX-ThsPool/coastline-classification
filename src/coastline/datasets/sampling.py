"""Spatial sampling along line geometries."""

from __future__ import annotations

from collections.abc import Iterable
from typing import Any


def sample_line_by_distance(line: Any, spacing: float, include_endpoint: bool = True) -> list[Any]:
    """Generate points at a fixed map-unit spacing along one line."""
    if spacing <= 0:
        raise ValueError("spacing must be positive")
    if line.is_empty:
        return []

    distances: list[float] = []
    distance = 0.0
    while distance < line.length:
        distances.append(distance)
        distance += spacing

    if include_endpoint and (not distances or distances[-1] < line.length):
        distances.append(float(line.length))

    return [line.interpolate(distance) for distance in distances]


def sample_geometries_by_distance(
    geometries: Iterable[Any],
    spacing: float,
    include_endpoint: bool = True,
) -> list[Any]:
    """Sample LineString or MultiLineString geometries."""
    output: list[Any] = []
    for geometry in geometries:
        if geometry is None or geometry.is_empty:
            continue
        if geometry.geom_type == "LineString":
            output.extend(sample_line_by_distance(geometry, spacing, include_endpoint))
        elif geometry.geom_type == "MultiLineString":
            for part in geometry.geoms:
                output.extend(sample_line_by_distance(part, spacing, include_endpoint))
        else:
            raise TypeError(f"Unsupported geometry type: {geometry.geom_type}")
    return output
