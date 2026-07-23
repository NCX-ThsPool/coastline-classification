"""
Dataset splitting / 数据集划分

中文：
    提供可重复的分层随机划分。该方法保持类别比例，但不能自动避免空间泄漏。
    全国岸线研究更严格时，应按区域、岸段或空间区块划分。

English:
    The function performs deterministic stratified splitting. It preserves class
    ratios but does not automatically prevent spatial leakage.
"""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd
from sklearn.model_selection import train_test_split


@dataclass(frozen=True)
class DatasetSplit:
    train: pd.DataFrame
    validation: pd.DataFrame
    test: pd.DataFrame


def stratified_split(
    frame: pd.DataFrame,
    label_column: str,
    *,
    validation_fraction: float = 0.2,
    test_fraction: float = 0.1,
    random_state: int = 42,
) -> DatasetSplit:
    """Split a table while preserving class proportions."""
    if label_column not in frame.columns:
        raise KeyError(f"Missing label column: {label_column}")
    if validation_fraction < 0 or test_fraction < 0:
        raise ValueError("Split fractions cannot be negative")
    if validation_fraction + test_fraction >= 1:
        raise ValueError("Validation and test fractions must sum to less than 1")

    holdout_fraction = validation_fraction + test_fraction
    if holdout_fraction == 0:
        empty = frame.iloc[0:0].copy()
        return DatasetSplit(frame.copy(), empty, empty)

    train, holdout = train_test_split(
        frame,
        test_size=holdout_fraction,
        stratify=frame[label_column],
        random_state=random_state,
    )

    if test_fraction == 0:
        return DatasetSplit(train, holdout, holdout.iloc[0:0].copy())
    if validation_fraction == 0:
        return DatasetSplit(train, holdout.iloc[0:0].copy(), holdout)

    relative_test = test_fraction / holdout_fraction
    validation, test = train_test_split(
        holdout,
        test_size=relative_test,
        stratify=holdout[label_column],
        random_state=random_state,
    )
    return DatasetSplit(train, validation, test)
