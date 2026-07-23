# Datasets / 数据集构建

## 中文

该目录处理“如何从空间数据变成模型可用样本”。

- `sampling.py`：沿 LineString 或 MultiLineString 按距离生成点；
- `splitting.py`：进行分层训练/验证/测试划分；
- `organization.py`：按照标签整理 UID 命名影像；
- `validation.py`：检查缺失影像和 UID 对应关系。

这里不直接规定真实项目中的全部字段。接手者应通过配置或适配层映射自己的 `UID`、类别和线段编号字段。

## English

This package converts spatial records and image files into machine-learning
datasets. Field names are intentionally configurable because real projects often
use different UID and label schemas.
