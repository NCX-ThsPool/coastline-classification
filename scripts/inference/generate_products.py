from __future__ import annotations

import argparse
from pathlib import Path

from coastline.utils.config import load_config

import pandas as pd

from coastline.inference.point_to_line import majority_label_by_group


def main() -> None:
    parser = argparse.ArgumentParser(description="Aggregate point predictions into line labels.")
    parser.add_argument("--input", required=True)
    parser.add_argument("--line-id-column", default="line_id")
    parser.add_argument("--label-column", default="predicted_label")
    parser.add_argument("--output", required=True)
    arguments = parser.parse_args()

    points = pd.read_csv(arguments.input)
    result = majority_label_by_group(
        points,
        group_column=arguments.line_id_column,
        label_column=arguments.label_column,
    )
    result.to_csv(arguments.output, index=False)


if __name__ == "__main__":
    main()
