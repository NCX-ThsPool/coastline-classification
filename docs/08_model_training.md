# Model Training / 模型训练与实验管理

## 中文

### 模型与任务

高分辨率主线使用 RGB 和 256×256 图块。中分辨率主线使用 14 通道和
32×32 图块。两者的数据归一化和首层卷积不同，不能共享未经说明的权重。

### 统一训练器

统一训练器负责：

- 训练模式和验证模式切换；
- 梯度清零；
- 前向传播；
- 损失计算；
- 反向传播；
- 优化器更新；
- 训练和验证统计；
- 最佳模型保存。

### 每次实验应保存

```text
run/
├── config.yaml
├── environment.json
├── metrics.csv
├── training.log
├── curves.png
└── checkpoints/
```

### 随机性

应固定 Python、NumPy、PyTorch 和 CUDA 随机种子。固定种子提升可重复性，但不能保证不同硬件和库版本完全逐位一致。

### 注意力

本项目中的注意力属于通道权重，不是 Transformer 自注意力。先验权重经过归一化，并通过可学习修正项在反向传播中更新。

## English

The training system separates model architecture from optimization. Every run
should preserve its configuration, environment, metrics, logs, curves, and
checkpoints. Channel attention here is prior-initialized learnable weighting,
not Transformer self-attention.
