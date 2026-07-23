from __future__ import annotations

import argparse
from pathlib import Path

from coastline.utils.config import load_config

import pandas as pd

from coastline.evaluation.transition import transition_matrix


def main() -> None:
    parser = argparse.ArgumentParser(description="Calculate a coastline class-transition matrix.")
    parser.add_argument("--input", required=True)
    parser.add_argument("--from-column", required=True)
    parser.add_argument("--to-column", required=True)
    parser.add_argument("--weight-column")
    parser.add_argument("--output", required=True)
    arguments = parser.parse_args()

    frame = pd.read_csv(arguments.input)
    matrix = transition_matrix(
        frame,
        from_column=arguments.from_column,
        to_column=arguments.to_column,
        weight_column=arguments.weight_column,
        labels=[0, 1, 2, 3, 4],
    )
    matrix.to_csv(arguments.output)


if __name__ == "__main__":
    main()
