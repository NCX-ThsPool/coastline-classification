"""
Classification evaluation / 分类精度评价

中文：
    提供总体精度、Kappa、Macro-F1、混淆矩阵以及逐类
    Precision、Recall、F1 和 IoU。

English:
    Provides overall accuracy, Kappa, Macro-F1, a confusion matrix, and
    per-class precision, recall, F1, and IoU.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from sklearn.metrics import (
    accuracy_score,
    cohen_kappa_score,
    confusion_matrix,
    precision_recall_fscore_support,
)


@dataclass(frozen=True)
class ClassificationReport:
    accuracy: float
    kappa: float
    macro_f1: float
    confusion: np.ndarray
    per_class: list[dict[str, float]]


def evaluate_classification(
    true_labels,
    predicted_labels,
    *,
    labels: list[int] | None = None,
) -> ClassificationReport:
    """Calculate OA, Kappa, Macro-F1, per-class metrics, and IoU."""
    truth = np.asarray(true_labels)
    predictions = np.asarray(predicted_labels)
    labels = labels or sorted(set(truth.tolist()) | set(predictions.tolist()))

    precision, recall, f1, support = precision_recall_fscore_support(
        truth,
        predictions,
        labels=labels,
        zero_division=0,
    )
    matrix = confusion_matrix(truth, predictions, labels=labels)

    rows: list[dict[str, float]] = []
    for index, label in enumerate(labels):
        true_positive = float(matrix[index, index])
        false_positive = float(matrix[:, index].sum() - true_positive)
        false_negative = float(matrix[index, :].sum() - true_positive)
        denominator = true_positive + false_positive + false_negative
        iou = true_positive / denominator if denominator else 0.0
        rows.append(
            {
                "label": float(label),
                "precision": float(precision[index]),
                "recall": float(recall[index]),
                "f1": float(f1[index]),
                "iou": float(iou),
                "support": float(support[index]),
            }
        )

    return ClassificationReport(
        accuracy=float(accuracy_score(truth, predictions)),
        kappa=float(cohen_kappa_score(truth, predictions)),
        macro_f1=float(np.mean(f1)),
        confusion=matrix,
        per_class=rows,
    )
