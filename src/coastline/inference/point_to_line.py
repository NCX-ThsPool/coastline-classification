"""Transfer point predictions to line segments."""

from __future__ import annotations

import pandas as pd


def majority_label_by_group(
    points: pd.DataFrame,
    *,
    group_column: str,
    label_column: str,
) -> pd.DataFrame:
    """Return one majority label and point count per line/group identifier."""
    for column in (group_column, label_column):
        if column not in points.columns:
            raise KeyError(f"Missing column: {column}")

    grouped = points.groupby(group_column)[label_column]
    result = grouped.agg(
        predicted_label=lambda series: series.mode().iloc[0],
        supporting_points="size",
    )
    return result.reset_index()
