# Evaluation / 精度评价与统计

## 中文

- `classification.py`：OA、Kappa、Macro-F1、Precision、Recall、F1、IoU；
- `transition.py`：类别转换矩阵；
- `coastline_statistics.py`：不同类别的岸线长度与比例。

评价数据必须具有独立真值。训练集准确率不能代替产品独立验证。

## English

This package implements classification metrics, class-transition matrices, and
coastline-length summaries. Independent reference labels are required for a
credible product assessment.
