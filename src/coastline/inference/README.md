# Inference / 模型推理

## 中文

- `predictor.py`：对 DataLoader 批量输出预测类别和概率；
- `point_to_line.py`：按线段编号对点预测结果进行多数表决；
- 产品生成时应保存类别、置信度、模型版本和数据年份，避免只有最终类别而无法追溯。

## English

Inference produces class IDs and probabilities, while point-to-line aggregation
converts sampled predictions into line-level labels.
