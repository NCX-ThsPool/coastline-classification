"""Coastline class-transition analysis."""

from __future__ import annotations

import pandas as pd


def transition_matrix(
    frame: pd.DataFrame,
    *,
    from_column: str,
    to_column: str,
    weight_column: str | None = None,
    labels: list[int] | None = None,
) -> pd.DataFrame:
    """Build a count- or weight-based transition matrix."""
    for column in (from_column, to_column):
        if column not in frame.columns:
            raise KeyError(f"Missing column: {column}")

    if weight_column is None:
        result = pd.crosstab(frame[from_column], frame[to_column])
    else:
        if weight_column not in frame.columns:
            raise KeyError(f"Missing weight column: {weight_column}")
        result = pd.pivot_table(
            frame,
            values=weight_column,
            index=from_column,
            columns=to_column,
            aggfunc="sum",
            fill_value=0,
        )

    if labels is not None:
        result = result.reindex(index=labels, columns=labels, fill_value=0)
    return result
