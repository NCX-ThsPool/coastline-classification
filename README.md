# Coastline Classification / 海岸线提取与分类

[中文](#中文说明) · [English](#english-documentation)

---

# 中文说明

## 1. 项目简介

本项目是一套面向海岸线遥感研究的教学型、可复现 Python 工程，覆盖以下主要任务：

1. Sentinel-2 遥感影像获取与配置；
2. 海岸遥感指数计算；
3. 水陆分割与海岸线提取；
4. 训练样本点和影像图块构建；
5. 基于 ConvNeXt 的五类海岸线分类；
6. 点预测结果向线要素传递；
7. 分类产品精度评价与时空变化分析。

本仓库由一个长期科研项目中的 469 个 Python 文件归纳、比较和重构而来。旧项目中存在大量历史版本、临时脚本、硬编码路径、模型对比代码和 GIS 平台专用代码。本仓库没有机械复制这些文件，而是将重复功能整理为职责明确的模块、配置文件、命令行脚本和教学文档。

本项目强调“可读、可学、可交接”。因此，代码和文档会有一定信息冗余。它不是以最少文件数量为目标，而是尽量让第一次接触遥感、GIS 或深度学习工程的新成员能够理解每一步为什么存在、输入是什么、输出是什么，以及如何扩展。

## 2. 研究对象与分类体系

海岸线划分为五种类型：

| 类别编号 | 中文名称 | 英文名称 | 典型含义 |
|---:|---|---|---|
| 0 | 人工岸线 | Artificial | 港口、码头、堤坝、围填海岸线 |
| 1 | 生物岸线 | Biogenic | 红树林、盐沼或其他生物控制岸线 |
| 2 | 砂质岸线 | Sandy | 沙滩和以砂质沉积物为主的岸线 |
| 3 | 泥质岸线 | Muddy | 淤泥质潮滩和细颗粒沉积岸线 |
| 4 | 基岩岸线 | Rocky | 岩石海岸、海蚀崖等稳定硬质岸线 |

## 3. 总体工作流

```text
数据获取
  ↓
波段整理与空间分辨率统一
  ↓
MNDWI、NDWI、NDVI、EVI、RVI、NDBI、LTidel
  ↓
Otsu 水陆分割
  ↓
连通域过滤与孔隙填充
  ↓
亚像素海岸线提取
  ↓
沿海岸线生成样本点
  ↓
裁剪高分辨率或多通道影像图块
  ↓
训练/验证/测试集划分
  ↓
ConvNeXt 模型训练
  ↓
影像分类推理
  ↓
点标签向岸线段传递
  ↓
精度评价、长度统计、类型转换和热点分析
```

详细说明见 [`docs/README.md`](docs/README.md) 和
[`docs/01_project_overview.md`](docs/01_project_overview.md)。

## 4. 目录结构

```text
coastline-classification/
├── assets/          # 文档中的正式图片和截图
├── checkpoints/     # 本地模型权重放置说明
├── configs/         # YAML 配置模板
├── data/            # 本地数据目录说明，不提交真实数据
├── docs/            # 中英双语教学与代码交接文档
├── examples/        # 小型、无敏感信息的示例
├── outputs/         # 程序运行结果，默认不提交
├── scripts/         # 可直接执行的工作流入口
├── src/coastline/   # 可复用的核心 Python 包
└── tests/           # 稳定函数的单元测试
```

每个主要目录均具有自己的中英双语 `README.md`。

## 5. 安装

建议 Python 3.10 或更高版本。

```bash
python -m venv .venv
```

Windows：

```bash
.venv\Scripts\activate
```

安装基础依赖：

```bash
pip install -e .
```

安装 GIS、深度学习和测试依赖：

```bash
pip install -e ".[geo,ml,gee,dev]"
```

说明：

- ArcPy 随 ArcGIS Pro 安装，不能通过普通 `pip` 安装；
- QGIS Python 代码需要在 QGIS 自带的 Python 环境中执行；
- Earth Engine 需要单独登录和授权；
- PyTorch CUDA 版本应与本机显卡驱动匹配。

## 6. 配置

复制公开模板：

```bash
copy configs\paths.example.yaml configs\paths.local.yaml
```

然后编辑本机路径。`paths.local.yaml` 已加入 `.gitignore`，不会被 Git 提交。

环境变量示例：

```bash
copy .env.example .env
```

不要把 API 密钥、令牌、私人项目名称和本机绝对路径写入公开配置。

## 7. 快速示例

### 7.1 计算遥感指数

输入栅格需按照蓝、绿、红、近红外、短波红外 1、短波红外 2 的顺序保存六个波段。

```bash
python scripts/extraction/calculate_indices.py ^
  --config configs/extraction.example.yaml ^
  --input data/raw/example/sentinel2_stack.tif ^
  --output-directory outputs/indices
```

### 7.2 提取水体掩膜

```bash
python scripts/extraction/extract_coastline.py ^
  --config configs/extraction.example.yaml ^
  --input outputs/indices/mndwi.tif ^
  --output outputs/water_mask.tif
```

### 7.3 划分数据集

```bash
python scripts/dataset/split_dataset.py ^
  --input examples/data/training_table.csv ^
  --label-column label ^
  --output-directory outputs/dataset_split
```

### 7.4 评价分类结果

```bash
python scripts/evaluation/evaluate_products.py ^
  --input examples/data/classification_example.csv ^
  --output outputs/evaluation.json
```

## 8. 阅读顺序

新成员建议按照以下顺序学习：

1. `docs/01_project_overview.md`
2. `docs/02_repository_structure.md`
3. `docs/03_environment_setup.md`
4. `docs/04_configuration_guide.md`
5. `docs/05_data_workflow.md`
6. `docs/06_coastline_extraction.md`
7. `docs/07_dataset_preparation.md`
8. `docs/08_model_training.md`
9. `docs/09_inference_and_products.md`
10. `docs/10_evaluation_and_analysis.md`
11. `docs/11_testing_and_debugging.md`
12. `docs/12_development_guide.md`

## 9. 数据与权重

本仓库不包含：

- 全国 Sentinel-2 影像；
- Google 高分辨率影像；
- SRTM DEM 全量数据；
- 行政区划和第三方海岸线产品；
- 人工核查样本；
- 完整训练数据；
- `.pth`、`.pt` 或 `.ckpt` 权重；
- ArcGIS Pro 和 QGIS 工程文件。

这些数据可能具有较大体积、许可限制、隐私要求或平台依赖。获取方式和本地组织方法见 `data/README.md`。

## 10. 项目状态

本版本是一套科研代码重构和交接框架。数值计算、数据划分、评价指标和基础推理组件可以直接复用；与真实数据结构强绑定的影像裁剪、完整 DataLoader、ArcPy 处理链和全国产品生成流程，需要接手者根据本地数据字段和软件环境继续适配。

---

# English Documentation

## 1. Project overview

This repository is a teaching-oriented and reproducible Python project for
remote-sensing-based coastline research. It covers:

1. Sentinel-2 acquisition and configuration;
2. coastal spectral-index calculation;
3. land-water segmentation and coastline extraction;
4. sampling-point and image-tile preparation;
5. five-class coastline classification with ConvNeXt;
6. transfer of point predictions to line features;
7. product validation and spatiotemporal analysis.

The repository was reconstructed from 469 Python files in a long-running
research workspace. Instead of copying historical versions, temporary scripts,
hard-coded paths, and duplicated model programs, the stable behavior was
organized into reusable modules, YAML configuration, command-line entry points,
tests, and extensive handover documentation.

Readability and learning value are deliberate design goals. Some explanatory
redundancy is retained so that new developers can understand the purpose,
inputs, outputs, assumptions, and extension points of each stage.

## 2. Coastline classes

| ID | English | Chinese | Typical interpretation |
|---:|---|---|---|
| 0 | Artificial | 人工岸线 | Ports, seawalls, reclaimed shorelines |
| 1 | Biogenic | 生物岸线 | Mangroves, salt marshes, biologically controlled coasts |
| 2 | Sandy | 砂质岸线 | Beaches and sand-dominated shores |
| 3 | Muddy | 泥质岸线 | Mudflats and fine-sediment shores |
| 4 | Rocky | 基岩岸线 | Rocky coasts and sea cliffs |

## 3. Installation

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -e ".[geo,ml,gee,dev]"
```

ArcPy and QGIS Python APIs are optional platform-specific dependencies and
cannot be installed as ordinary portable PyPI packages.

## 4. Suggested reading order

Start with `docs/README.md`, then follow the numbered bilingual guides from
`01_project_overview.md` to `12_development_guide.md`.

## 5. Reproducibility boundary

The repository does not include nationwide imagery, restricted labels,
third-party products, GIS desktop projects, or model checkpoints. The package
implements stable and reusable computational components, while data-specific
adapters must be completed against the actual local datasets.
