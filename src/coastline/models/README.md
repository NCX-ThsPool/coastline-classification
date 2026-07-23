# Models / 模型

## 中文

该目录将“模型结构”与“训练过程”分开。

- `factory.py`：统一创建 ConvNeXt、ResNet、DenseNet、EfficientNet、Inception 和 VGG；
- `channel_attention.py`：实现先验初始化、训练中可修正的通道权重；
- 输入通道数不等于 3 时，会替换第一层卷积；
- 模型工厂不负责读取数据或保存权重。

## English

This package contains architecture construction only. Data loading, optimization,
checkpointing, and evaluation belong to other packages.
