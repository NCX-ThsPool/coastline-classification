from __future__ import annotations

import argparse
from pathlib import Path

from coastline.utils.config import load_config

from coastline.datasets.sampling import sample_geometries_by_distance
from coastline.utils.vector import read_vector, write_vector


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate fixed-distance coastline sample points.")
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--spacing", type=float, default=100.0)
    arguments = parser.parse_args()

    frame = read_vector(arguments.input)
    points = sample_geometries_by_distance(frame.geometry, arguments.spacing)

    import geopandas as gpd

    output = gpd.GeoDataFrame(
        {"sample_id": range(len(points))},
        geometry=points,
        crs=frame.crs,
    )
    write_vector(output, arguments.output)


if __name__ == "__main__":
    main()
