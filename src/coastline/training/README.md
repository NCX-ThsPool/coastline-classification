# Training / 模型训练

## 中文

- `trainer.py`：统一训练和验证循环；
- `metrics.py`：累计平均值等训练期指标；
- `reproducibility.py`：设置 Python、NumPy 和 PyTorch 随机种子。

训练器保存验证精度最高的 `best_model.pth`。真实项目仍需提供 DataLoader、数据增强和归一化参数。

## English

The trainer implements a reusable supervised classification loop. Project-specific
Dataset and DataLoader adapters remain outside the generic trainer.
