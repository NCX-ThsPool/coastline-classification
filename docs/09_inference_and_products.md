# Inference and Product Generation / 推理与产品生成

## 中文

### 模型加载

推理时必须保证以下内容与训练一致：

- 模型名称；
- 输入通道；
- 波段顺序；
- 图块大小；
- 归一化参数；
- 类别编号；
- 权重版本。

### 概率与类别

不要只保存 `argmax` 类别。建议同时保存最高概率、完整概率向量或至少置信度，以便质量控制。

### 点到线

多个点对应一个岸段时，可以使用多数表决。还可以扩展为：

- 概率平均；
- 距离加权；
- 置信度阈值；
- 最小支持点数量；
- 冲突标记。

### 成果字段建议

```text
segment_id
class_id
class_name
confidence
support_count
source
year
model_version
config_hash
```

## English

Inference must reproduce the training input specification exactly. Product
records should preserve confidence, support, source year, model version, and
configuration identity for traceability.
