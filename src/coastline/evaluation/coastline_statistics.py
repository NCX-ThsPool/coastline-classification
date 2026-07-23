"""Length and proportion summaries for classified coastline products."""

from __future__ import annotations

import pandas as pd


def summarize_length(
    frame: pd.DataFrame,
    *,
    class_column: str,
    length_column: str,
) -> pd.DataFrame:
    """Aggregate total length and percentage by coastline class."""
    for column in (class_column, length_column):
        if column not in frame.columns:
            raise KeyError(f"Missing column: {column}")

    summary = (
        frame.groupby(class_column, dropna=False)[length_column]
        .sum()
        .rename("length")
        .reset_index()
    )
    total = summary["length"].sum()
    summary["percentage"] = summary["length"] / total * 100 if total else 0.0
    return summary
