from __future__ import annotations

import argparse
from pathlib import Path

from coastline.utils.config import load_config

import pandas as pd

from coastline.datasets.splitting import stratified_split


def main() -> None:
    parser = argparse.ArgumentParser(description="Create stratified train/validation/test tables.")
    parser.add_argument("--input", required=True)
    parser.add_argument("--label-column", default="label")
    parser.add_argument("--output-directory", required=True)
    parser.add_argument("--validation-fraction", type=float, default=0.2)
    parser.add_argument("--test-fraction", type=float, default=0.1)
    arguments = parser.parse_args()

    frame = pd.read_csv(arguments.input)
    split = stratified_split(
        frame,
        arguments.label_column,
        validation_fraction=arguments.validation_fraction,
        test_fraction=arguments.test_fraction,
    )

    output = Path(arguments.output_directory)
    output.mkdir(parents=True, exist_ok=True)
    split.train.to_csv(output / "train.csv", index=False)
    split.validation.to_csv(output / "validation.csv", index=False)
    split.test.to_csv(output / "test.csv", index=False)


if __name__ == "__main__":
    main()
