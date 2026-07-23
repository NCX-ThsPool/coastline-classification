from __future__ import annotations

import argparse
from pathlib import Path

from coastline.utils.config import load_config

from coastline.extraction.pipeline import extract_water_mask
from coastline.utils.raster import read_raster, write_raster


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract a cleaned binary water mask.")
    parser.add_argument("--config", required=True)
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    arguments = parser.parse_args()

    config = load_config(arguments.config)
    array, profile = read_raster(arguments.input)
    index_array = array[0]

    morphology = config.get("morphology", {})
    segmentation = config.get("segmentation", {})
    result = extract_water_mask(
        index_array,
        invert=bool(segmentation.get("invert", False)),
        minimum_component_pixels=int(morphology.get("minimum_component_pixels", 5)),
        require_2x2_structure=bool(morphology.get("require_2x2_structure", True)),
    )
    write_raster(arguments.output, result.filled_mask, profile, nodata=0)
    print(f"Otsu threshold: {result.threshold:.6f}")


if __name__ == "__main__":
    main()
