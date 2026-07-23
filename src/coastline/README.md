# `coastline` Package / `coastline` 核心包

| 子目录 | 中文职责 | English responsibility |
|---|---|---|
| `download` | 遥感数据下载配置与外部平台连接 | acquisition configuration and external services |
| `indices` | 遥感指数公式与批量计算 | spectral-index formulas and calculation |
| `extraction` | 水陆分割、形态学和岸线提取 | segmentation, morphology, and contour extraction |
| `datasets` | 采样、数据划分、文件整理与检查 | sampling, splitting, organization, validation |
| `models` | 模型创建和通道注意力 | model construction and channel attention |
| `training` | 训练循环、指标和随机种子 | training loops, metrics, reproducibility |
| `inference` | 批量预测与点到线标签传递 | prediction and point-to-line aggregation |
| `evaluation` | 分类精度与时空统计 | classification and spatiotemporal evaluation |
| `utils` | 配置、日志、栅格和矢量底层工具 | configuration, logging, raster, vector utilities |

新成员应先阅读每个子目录中的 `README.md`，再阅读具体 `.py` 文件。
