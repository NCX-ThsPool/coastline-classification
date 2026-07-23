# Checkpoints / 模型权重

## 中文

模型权重默认不提交 Git。

本地建议结构：

```text
checkpoints/
├── hr/
│   └── convnext_rgb_256/
└── mr/
    └── convnext_14ch_attention_32/
```

每个发布权重应同时提供：

- 模型名称和版本；
- 输入通道及顺序；
- 输入窗口大小；
- 类别编号映射；
- 训练配置；
- 评价指标；
- SHA-256；
- 数据和权重许可证。

## English

Checkpoint binaries are excluded from Git. Any released weight should be
accompanied by complete model metadata, configuration, metrics, checksum, and
license information.
