# Tests / 测试

## 中文

测试用于确认稳定的基础逻辑没有在重构中被破坏。

- `test_indices.py`：指数结果有限且能处理除零；
- `test_splitting.py`：数据划分不丢失样本；
- `test_evaluation.py`：完美分类得到 1.0；
- `test_transition.py`：转换矩阵维度和计数正确；
- `test_point_to_line.py`：多数表决正确。

运行：

```bash
pytest
```

## English

Tests protect stable numerical and tabular behavior. GIS integration and
large-model training require additional environment-specific integration tests.
