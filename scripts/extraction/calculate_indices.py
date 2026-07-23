from __future__ import annotations

import argparse
from pathlib import Path

from coastline.utils.config import load_config

import numpy as np

from coastline.indices.calculator import calculate_index
from coastline.utils.raster import read_raster, write_raster


def main() -> None:
    parser = argparse.ArgumentParser(description="Calculate coastal spectral indices.")
    parser.add_argument("--config", required=True)
    parser.add_argument("--input", required=True, help="Six-band raster: blue, green, red, nir, swir1, swir2")
    parser.add_argument("--output-directory", required=True)
    arguments = parser.parse_args()

    config = load_config(arguments.config)
    array, profile = read_raster(arguments.input)
    if array.shape[0] < 6:
        raise ValueError("Input raster must contain at least six bands.")

    bands = dict(zip(("blue", "green", "red", "nir", "swir1", "swir2"), array[:6]))
    output = Path(arguments.output_directory)
    for name in config.get("indices", []):
        result = calculate_index(name, bands).astype(np.float32)
        write_raster(output / f"{name.lower()}.tif", result, profile, nodata=-9999.0)


if __name__ == "__main__":
    main()
