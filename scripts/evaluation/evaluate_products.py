from __future__ import annotations

import argparse
from pathlib import Path

from coastline.utils.config import load_config

import json

import pandas as pd

from coastline.evaluation.classification import evaluate_classification


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate predicted coastline classes.")
    parser.add_argument("--input", required=True)
    parser.add_argument("--truth-column", default="true_label")
    parser.add_argument("--prediction-column", default="predicted_label")
    parser.add_argument("--output", required=True)
    arguments = parser.parse_args()

    frame = pd.read_csv(arguments.input)
    report = evaluate_classification(
        frame[arguments.truth_column],
        frame[arguments.prediction_column],
        labels=[0, 1, 2, 3, 4],
    )
    payload = {
        "accuracy": report.accuracy,
        "kappa": report.kappa,
        "macro_f1": report.macro_f1,
        "confusion_matrix": report.confusion.tolist(),
        "per_class": report.per_class,
    }
    Path(arguments.output).write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
