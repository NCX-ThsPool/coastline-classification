# 海岸线提取与分类研究系统
# Coastline Extraction and Classification Research System

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GIS](https://img.shields.io/badge/GIS-Remote%20Sensing-green.svg)]()
[![Deep Learning](https://img.shields.io/badge/Deep%20Learning-ConvNeXt-orange.svg)]()

[中文说明](#-中文说明) | [English Documentation](#-english-documentation)

---

# 🇨🇳 中文说明

## 📖 项目简介

本项目面向海岸线遥感提取、类型识别、产品生产与时空变化分析，构建了一套具有较强可读性、可学习性和可交接性的 Python 工程体系。

项目围绕两条相互关联但职责不同的研究主线展开：

1. **海岸线提取**：从 Sentinel-2 等遥感影像中识别水陆边界，生成连续海岸线；
2. **海岸线分类**：基于高分辨率 RGB 影像和中分辨率多通道特征，将海岸线划分为人工、生物、砂质、泥质和基岩五种类型。

本仓库并非简单汇总历史脚本，而是基于长期科研工作中形成的 469 个 Python 文件，对数据获取、遥感指数计算、岸线提取、训练样本构建、深度学习分类、推理、产品生成和精度评价等功能进行学习、筛选、合并和重构。

项目强调：

- **代码可读性**：关键模块具有明确职责、类型标注和注释；
- **教学友好性**：允许适度冗余，帮助新手理解完整工作流；
- **中英双语文档**：核心 README 与交接文档均提供中文和英文说明；
- **科研可追溯性**：保留配置、迁移清单和模块映射说明；
- **隐私与安全**：不提交本机绝对路径、私人账号、API 密钥和受限数据。

### 🎯 研究背景

海岸线是海洋与陆地相互作用的重要空间边界，也是海岸带生态环境、国土开发、港口建设、滩涂演变和防灾减灾研究中的基础地理要素。

传统海岸线提取和分类工作通常依赖人工解译，存在处理范围大、人工成本高、多时相数据难以统一、分类标准不一致和处理流程难以复现等问题。为此，本项目将遥感影像处理、GIS 空间分析和深度学习分类整合为可配置、可复用和可交接的研究工程。

### 🔬 研究方法

- **数据来源**：Sentinel-2、高分辨率 Google 影像、SRTM DEM、OSM 海岸线及公开参考产品；
- **提取方法**：遥感指数、Otsu 阈值分割、连通域过滤、孔隙填充、亚像素轮廓提取；
- **分类方法**：ConvNeXt、多通道输入适配、先验初始化通道权重；
- **分析方法**：独立精度评价、岸线长度统计、类型转换矩阵和空间热点分析；
- **技术栈**：Python、Rasterio、GeoPandas、Shapely、scikit-image、PyTorch、ArcGIS Pro、QGIS、Google Earth Engine。

## 🧭 海岸线分类体系

| 类别编号 | 中文名称 | 英文名称 | 典型特征 |
|---:|---|---|---|
| 0 | 人工岸线 | Artificial Coastline | 港口、码头、海堤和围填海岸线 |
| 1 | 生物岸线 | Biogenic Coastline | 红树林、盐沼和其他生物控制岸线 |
| 2 | 砂质岸线 | Sandy Coastline | 沙滩及砂质沉积岸线 |
| 3 | 泥质岸线 | Muddy Coastline | 淤泥质潮滩和细颗粒沉积岸线 |
| 4 | 基岩岸线 | Rocky Coastline | 岩石海岸、海蚀崖等硬质岸线 |

## 🧮 遥感特征体系

| 指数 | 英文名称 | 主要作用 |
|---|---|---|
| MNDWI | Modified Normalized Difference Water Index | 增强水体并抑制建筑和土壤干扰 |
| NDWI | Normalized Difference Water Index | 水体识别和水陆边界增强 |
| NDVI | Normalized Difference Vegetation Index | 辅助植被和生物岸线识别 |
| EVI | Enhanced Vegetation Index | 增强高覆盖植被响应 |
| RVI | Ratio Vegetation Index | 反映植被覆盖和活力 |
| NDBI | Normalized Difference Built-up Index | 建成区和人工岸线识别 |
| LTidel | Tidal-flat-related Index | 潮滩和泥质岸线辅助识别 |

## 🏗️ 项目结构

```text
coastline-classification/
├── assets/                                  # 文档展示资源
│   ├── README.md                            # 资源目录说明
│   ├── figures/                             # 正式流程图、成果图和示意图
│   └── screenshots/                         # 软件操作截图
├── checkpoints/                             # 模型权重说明
│   └── README.md
├── configs/                                 # 配置文件
│   ├── README.md
│   ├── paths.example.yaml                   # 本地路径模板
│   ├── extraction.example.yaml              # 海岸线提取配置
│   ├── classification_hr.example.yaml       # 高分辨率分类配置
│   └── classification_mr.example.yaml       # 中分辨率分类配置
├── data/                                    # 本地数据目录
│   └── README.md
├── docs/                                    # 中英双语项目文档
│   ├── README.md
│   ├── 01_project_overview.md
│   ├── 02_repository_structure.md
│   ├── 03_environment_setup.md
│   ├── 04_configuration_guide.md
│   ├── 05_data_workflow.md
│   ├── 06_coastline_extraction.md
│   ├── 07_dataset_preparation.md
│   ├── 08_model_training.md
│   ├── 09_inference_and_products.md
│   ├── 10_evaluation_and_analysis.md
│   ├── 11_testing_and_debugging.md
│   ├── 12_development_guide.md
│   ├── 13_old_to_new_mapping_examples.md
│   ├── code_migration_inventory.csv
│   ├── code_migration_report.md
│   ├── platform_dependencies.md
│   └── security_and_privacy.md
├── examples/                                # 小型公开示例
│   ├── README.md
│   ├── configs/
│   └── data/
├── outputs/                                 # 程序运行结果
│   ├── README.md
│   ├── figures/
│   ├── tables/
│   ├── evaluation/
│   ├── runs/
│   └── .gitkeep
├── scripts/                                 # 命令行工作流入口
│   ├── README.md
│   ├── extraction/
│   │   ├── README.md
│   │   ├── calculate_indices.py
│   │   └── extract_coastline.py
│   ├── dataset/
│   │   ├── README.md
│   │   ├── generate_sampling_points.py
│   │   └── split_dataset.py
│   ├── training/
│   │   ├── README.md
│   │   ├── train_hr.py
│   │   └── train_mr.py
│   ├── inference/
│   │   ├── README.md
│   │   └── generate_products.py
│   └── evaluation/
│       ├── README.md
│       ├── evaluate_products.py
│       └── analyze_transitions.py
├── src/
│   ├── README.md
│   └── coastline/
│       ├── README.md
│       ├── __init__.py
│       ├── constants.py
│       ├── download/
│       │   ├── README.md
│       │   ├── sentinel2.py
│       │   └── dem.py
│       ├── indices/
│       │   ├── README.md
│       │   ├── spectral.py
│       │   └── calculator.py
│       ├── extraction/
│       │   ├── README.md
│       │   ├── thresholding.py
│       │   ├── morphology.py
│       │   ├── subpixel.py
│       │   └── pipeline.py
│       ├── datasets/
│       │   ├── README.md
│       │   ├── sampling.py
│       │   ├── splitting.py
│       │   ├── organization.py
│       │   └── validation.py
│       ├── models/
│       │   ├── README.md
│       │   ├── factory.py
│       │   └── channel_attention.py
│       ├── training/
│       │   ├── README.md
│       │   ├── trainer.py
│       │   ├── metrics.py
│       │   └── reproducibility.py
│       ├── inference/
│       │   ├── README.md
│       │   ├── predictor.py
│       │   └── point_to_line.py
│       ├── evaluation/
│       │   ├── README.md
│       │   ├── classification.py
│       │   ├── transition.py
│       │   └── coastline_statistics.py
│       └── utils/
│           ├── README.md
│           ├── config.py
│           ├── filesystem.py
│           ├── logging.py
│           ├── raster.py
│           └── vector.py
├── tests/
│   ├── README.md
│   ├── test_indices.py
│   ├── test_splitting.py
│   ├── test_evaluation.py
│   ├── test_transition.py
│   └── test_point_to_line.py
├── .env.example
├── .gitignore
├── CONTRIBUTING.md
├── LICENSE
├── pyproject.toml
├── README.md
└── requirements.txt
```

## 🚀 主要功能

### 1. 遥感数据获取

- 基于 Google Earth Engine 构建 Sentinel-2 SR Harmonized 影像集合；
- 支持按年份、季节、云量和 SCL 类别筛选；
- 支持 RGB、NIR 和 SWIR 等波段组合；
- Earth Engine 项目名和本机路径通过配置读取；
- 为 DEM 和其他辅助数据提供扩展接口。

### 2. 遥感指数计算

- 支持 MNDWI、NDWI、NDVI、EVI、RVI、NDBI 和 LTidel；
- 对除零、NaN 和无穷值进行处理；
- 使用语义波段名称，避免波段顺序混乱；
- 将指数公式与栅格读写分离，便于测试。

### 3. 海岸线提取

- Otsu 自适应阈值；
- 0/255 二值掩膜；
- 连通域过滤；
- 可选 2 × 2 结构约束；
- 内部孔隙填充；
- marching squares 亚像素轮廓；
- 像素坐标到地理坐标转换；
- 分阶段质量检查。

### 4. 分类数据集构建

- 沿 LineString 和 MultiLineString 等距采样；
- 按类别进行分层数据划分；
- 按 UID 和类别整理影像；
- 检查样本表与影像文件对应关系；
- 提示相邻样本造成的空间数据泄漏风险。

### 5. 深度学习分类

- 支持 ConvNeXt、ResNet、DenseNet、EfficientNet、Inception 和 VGG；
- 支持三通道和多通道输入；
- 支持替换模型首层卷积；
- 支持先验初始化且可学习修正的通道权重；
- 将模型结构、训练循环和实验配置分离。

### 6. 模型训练

- 统一训练与验证循环；
- 自动保存最佳权重；
- 设置 Python、NumPy 和 PyTorch 随机种子；
- 支持高分辨率和中分辨率实验配置；
- 可扩展训练日志、曲线和环境信息记录。

### 7. 推理与产品生成

- 批量输出预测类别和概率；
- 按岸段编号聚合点预测；
- 通过多数表决生成线段类别；
- 可扩展概率平均和置信度加权；
- 建议保存模型版本、年份、配置哈希和支持点数量。

### 8. 精度评价与时空分析

- Overall Accuracy；
- Cohen's Kappa；
- Macro-F1；
- Precision、Recall、F1 和 IoU；
- 混淆矩阵；
- 岸线类型转换矩阵；
- 分类岸线长度和比例统计；
- 第三方产品统一分类对比。

## 📊 研究产品

### 高分辨率产品

```text
Coastline_HR_2025
```

- 数据源：高分辨率 RGB 影像；
- 年份：2025；
- 窗口：256 × 256；
- 模型：ConvNeXt；
- 任务：五类海岸线精细分类。

### 中分辨率产品

```text
Coastline_MR_2015
Coastline_MR_2020
Coastline_MR_2025
```

- 数据源：Sentinel-2 多通道特征；
- 分辨率：10 m；
- 窗口：32 × 32；
- 输入：14 通道；
- 模型：ConvNeXt 与类别敏感通道权重；
- 任务：多时相海岸线分类和变化分析。

## 🛠️ 安装使用

### 环境要求

- Python 3.10+
- 建议 16 GB 以上内存
- 深度学习训练建议使用 NVIDIA GPU
- ArcGIS Pro 3.x，可选
- QGIS 3.x，可选
- Google Earth Engine 账号，可选

### 安装步骤

1. **克隆仓库**

```bash
git clone https://github.com/NCX-ThsPool/coastline-classification.git
cd coastline-classification
```

2. **创建虚拟环境**

Windows：

```bash
python -m venv .venv
.venv\Scripts\activate
```

Linux / macOS：

```bash
python -m venv .venv
source .venv/bin/activate
```

3. **安装依赖**

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install -e .
```

4. **安装完整可选依赖**

```bash
pip install -e ".[geo,ml,gee,dev]"
```

### 配置本地路径

```bash
copy configs\paths.example.yaml configs\paths.local.yaml
```

Linux / macOS：

```bash
cp configs/paths.example.yaml configs/paths.local.yaml
```

`paths.local.yaml` 已被 `.gitignore` 排除，不会提交到 GitHub。

### 快速开始

#### 计算遥感指数

```bash
python scripts/extraction/calculate_indices.py ^
  --config configs/extraction.example.yaml ^
  --input data/raw/example/sentinel2_stack.tif ^
  --output-directory outputs/indices
```

#### 提取水体掩膜

```bash
python scripts/extraction/extract_coastline.py ^
  --config configs/extraction.example.yaml ^
  --input outputs/indices/mndwi.tif ^
  --output outputs/water_masks/mndwi_water_mask.tif
```

#### 沿岸线生成采样点

```bash
python scripts/dataset/generate_sampling_points.py ^
  --input data/processed/coastline/coastline.shp ^
  --output outputs/sampling/coastline_points.shp ^
  --spacing 100
```

#### 划分训练、验证和测试集

```bash
python scripts/dataset/split_dataset.py ^
  --input examples/data/training_table.csv ^
  --label-column label ^
  --output-directory outputs/dataset_split ^
  --validation-fraction 0.2 ^
  --test-fraction 0.1
```

#### 产品精度评价

```bash
python scripts/evaluation/evaluate_products.py ^
  --input examples/data/classification_example.csv ^
  --truth-column true_label ^
  --prediction-column predicted_label ^
  --output outputs/evaluation/classification_report.json
```

## 📈 关键方法说明

### Otsu 阈值分割

Otsu 方法根据有效像元的灰度分布自动寻找水陆分割阈值。项目实现会排除 NaN 和无穷值，并允许传入额外有效像元掩膜。

### 连通域过滤

连通域过滤用于删除面积较小的误分区域。阈值过大会删除小岛和狭窄水道，因此应在典型区域进行参数敏感性分析。

### 孔隙填充

孔隙填充用于修复被前景完全包围的内部空洞。该方法也可能误填真实岛屿，需要结合研究尺度使用。

### 亚像素轮廓提取

项目使用 marching squares 在像元内部插值边界，然后通过仿射变换将像素坐标转换为地理坐标。

### 类别敏感通道权重

中分辨率模型采用先验初始化的通道权重。该方法不是 Transformer 自注意力，而是在输入通道上增加先验权重与可学习修正项，并在反向传播中更新。

### 点标签向线要素传递

对同一岸段的多个采样点预测结果进行多数表决，得到最终线段类别。后续可扩展为概率平均、置信度加权和冲突标记。

## 🎨 可视化示例

项目可扩展生成：

- 遥感指数分布图；
- 水体掩膜和形态学处理对比图；
- 亚像素海岸线叠加图；
- 训练损失和验证精度曲线；
- 混淆矩阵；
- 岸线长度结构图；
- 多时相类型转换图；
- 类型变化热点地图；
- 第三方产品对比图。

程序自动生成图件建议保存到 `outputs/figures/`，经过确认后再复制到 `assets/figures/`。

## 🧪 测试

运行全部测试：

```bash
pytest
```

检查语法：

```bash
python -m compileall src scripts tests
```

当前测试覆盖：

- 遥感指数数值稳定性；
- 分层数据划分；
- 分类评价指标；
- 类型转换矩阵；
- 点到线多数表决。

## 📚 文档阅读顺序

```text
README.md
    ↓
docs/README.md
    ↓
docs/01_project_overview.md
    ↓
docs/02_repository_structure.md
    ↓
docs/03_environment_setup.md
    ↓
docs/04_configuration_guide.md
    ↓
docs/05_data_workflow.md
    ↓
docs/06_coastline_extraction.md
    ↓
docs/07_dataset_preparation.md
    ↓
docs/08_model_training.md
    ↓
docs/09_inference_and_products.md
    ↓
docs/10_evaluation_and_analysis.md
    ↓
docs/11_testing_and_debugging.md
    ↓
docs/12_development_guide.md
```

## 🔐 安全与隐私

公开仓库不得包含：

- 本机绝对路径；
- 私人 Earth Engine 项目名称；
- API Key、Token、Cookie 和密码；
- 私人邮箱和服务器地址；
- 未授权或受限数据；
- 模型权重；
- GIS 软件缓存；
- 包含敏感环境信息的日志。

本地配置应使用 `*.local.yaml`，私人变量应使用 `.env`。

## ⚠️ 当前限制

本仓库属于科研代码重构和教学交接版本：

1. 不包含全国原始遥感数据；
2. 不包含 Google 高分辨率影像；
3. 不包含完整人工标注样本；
4. 不包含训练权重；
5. 不包含 ArcGIS Pro 和 QGIS 工程；
6. 不包含第三方海岸线产品原始文件；
7. 完整训练仍需根据真实数据结构实现 Dataset 和 DataLoader；
8. ArcPy 和 QGIS 专用流程需在对应软件环境中适配；
9. 全国任务还需增加断点续算、任务调度和质量控制。

## 📄 许可证

本项目代码采用 MIT 许可证，详见 [LICENSE](LICENSE)。

MIT 许可证仅覆盖仓库代码。遥感影像、行政区划、参考产品、人工标签和模型权重可能具有独立许可证，使用者应遵守相应条款。

## 🙏 致谢

感谢以下开源项目、数据平台和 GIS 软件提供基础支持：

- Google Earth Engine；
- Copernicus Sentinel-2；
- OpenStreetMap；
- SRTM；
- NumPy；
- Pandas；
- Rasterio；
- GeoPandas；
- Shapely；
- scikit-image；
- scikit-learn；
- PyTorch；
- torchvision；
- timm；
- ArcGIS Pro；
- QGIS。

## 📚 参考资料

1. Sentinel-2 MSI and Copernicus Data Space Ecosystem;
2. OpenStreetMap Coastlines;
3. SRTM Digital Elevation Model;
4. Otsu, N. A Threshold Selection Method from Gray-Level Histograms;
5. Liu, Z., et al. A ConvNet for the 2020s;
6. Rasterio Documentation;
7. GeoPandas Documentation;
8. PyTorch Documentation;
9. scikit-image Documentation;
10. Google Earth Engine Documentation.

> **注意：本项目主要用于科研、教学和代码交接。所有数据获取、处理与发布行为均应遵守数据许可、平台服务条款及相关法律法规。**

---

# 🇬🇧 English Documentation

## 📖 Project Overview

This project provides a readable, educational, and handover-oriented Python
system for coastline extraction, coastline-type classification, product
generation, and spatiotemporal analysis.

It contains two related but distinct workflows:

1. **Coastline extraction**: identifying land-water boundaries from Sentinel-2
   and other remote-sensing imagery;
2. **Coastline classification**: assigning one of five semantic classes to each
   coastline segment.

The repository was reconstructed from 469 Python files accumulated during a
long-term research project. Historical versions, temporary scripts, hard-coded
paths, duplicated model programs, and platform-specific code were reviewed and
consolidated into reusable modules, YAML configurations, command-line scripts,
tests, and bilingual documentation.

### 🎯 Research Background

Coastlines are fundamental geographic features for coastal ecology, land
development, port construction, tidal-flat monitoring, disaster prevention, and
marine spatial planning.

Traditional manual interpretation is expensive and difficult to reproduce over
large regions and multiple years. This project integrates remote sensing, GIS,
and deep learning into a structured and transferable research workflow.

### 🔬 Research Methods

- **Data sources**: Sentinel-2, high-resolution Google imagery, SRTM DEM,
  OpenStreetMap coastlines, and public reference products;
- **Extraction methods**: spectral indices, Otsu thresholding, component
  filtering, hole filling, and subpixel contours;
- **Classification methods**: ConvNeXt, multi-channel input adaptation, and
  prior-initialized channel weighting;
- **Analysis methods**: independent validation, coastline-length statistics,
  transition matrices, and hotspot analysis;
- **Technology stack**: Python, Rasterio, GeoPandas, Shapely, scikit-image,
  PyTorch, ArcGIS Pro, QGIS, and Google Earth Engine.

## 🧭 Coastline Classes

| ID | English | Chinese | Typical interpretation |
|---:|---|---|---|
| 0 | Artificial Coastline | 人工岸线 | Ports, seawalls, and reclamation |
| 1 | Biogenic Coastline | 生物岸线 | Mangroves and salt marshes |
| 2 | Sandy Coastline | 砂质岸线 | Beaches and sand-dominated shores |
| 3 | Muddy Coastline | 泥质岸线 | Mudflats and fine-sediment shores |
| 4 | Rocky Coastline | 基岩岸线 | Rocky coasts and sea cliffs |

## 🚀 Main Features

### 1. Remote-sensing acquisition

- Sentinel-2 SR Harmonized collection construction;
- seasonal and cloud filtering;
- SCL-based masking;
- configurable band selection;
- externalized Earth Engine project and local path settings.

### 2. Spectral indices

- MNDWI, NDWI, NDVI, EVI, RVI, NDBI, and LTidel;
- finite-value and division-by-zero protection;
- semantic band names;
- independent numerical formulas and raster I/O.

### 3. Coastline extraction

- valid-pixel Otsu thresholding;
- uint8 binary masks;
- connected-component filtering;
- optional 2 × 2 structural filtering;
- hole filling;
- marching-squares subpixel contours;
- affine pixel-to-world conversion.

### 4. Dataset preparation

- fixed-distance line sampling;
- stratified data splitting;
- UID-based image organization;
- missing-file validation;
- spatial leakage guidance.

### 5. Deep-learning classification

- unified model factory;
- ConvNeXt, ResNet, DenseNet, EfficientNet, Inception, and VGG;
- configurable input channels;
- prior-initialized learnable channel weighting;
- separation of model, training, and experiment configuration.

### 6. Training

- reusable training and validation loop;
- best-checkpoint saving;
- random-seed control;
- high-resolution and mid-resolution configuration templates.

### 7. Inference and products

- batch prediction of classes and probabilities;
- point-to-line aggregation;
- majority voting;
- extension points for confidence weighting;
- traceable model and configuration metadata.

### 8. Evaluation and analysis

- overall accuracy;
- Cohen's Kappa;
- Macro-F1;
- precision, recall, F1, and IoU;
- confusion matrices;
- class-transition matrices;
- coastline-length statistics;
- third-party comparison interfaces.

## 🛠️ Installation

### Requirements

- Python 3.10+
- 16 GB RAM recommended
- NVIDIA GPU recommended for training
- ArcGIS Pro 3.x optional
- QGIS 3.x optional
- Google Earth Engine account optional

### Clone

```bash
git clone https://github.com/NCX-ThsPool/coastline-classification.git
cd coastline-classification
```

### Create an environment

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Linux / macOS:

```bash
python -m venv .venv
source .venv/bin/activate
```

### Install

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install -e .
```

Full optional dependencies:

```bash
pip install -e ".[geo,ml,gee,dev]"
```

## ⚡ Quick Start

### Calculate spectral indices

```bash
python scripts/extraction/calculate_indices.py   --config configs/extraction.example.yaml   --input data/raw/example/sentinel2_stack.tif   --output-directory outputs/indices
```

### Extract a water mask

```bash
python scripts/extraction/extract_coastline.py   --config configs/extraction.example.yaml   --input outputs/indices/mndwi.tif   --output outputs/water_masks/mndwi_water_mask.tif
```

### Generate sampling points

```bash
python scripts/dataset/generate_sampling_points.py   --input data/processed/coastline/coastline.shp   --output outputs/sampling/coastline_points.shp   --spacing 100
```

### Evaluate classification results

```bash
python scripts/evaluation/evaluate_products.py   --input examples/data/classification_example.csv   --truth-column true_label   --prediction-column predicted_label   --output outputs/evaluation/classification_report.json
```

## 🧪 Testing

```bash
pytest
python -m compileall src scripts tests
```

Current tests cover:

- spectral-index numerical stability;
- stratified dataset splitting;
- classification metrics;
- transition matrices;
- point-to-line majority voting.

## 🔐 Security and Privacy

The public repository must not contain:

- personal absolute paths;
- private Earth Engine project IDs;
- API keys, tokens, cookies, or passwords;
- private e-mail or server addresses;
- restricted datasets;
- model checkpoints;
- GIS cache files;
- logs containing sensitive environment information.

Use ignored local YAML files and environment variables for private settings.

## ⚠️ Current Limitations

This repository is a research-code refactoring and teaching edition. It does not
include nationwide imagery, high-resolution Google imagery, complete labels,
trained weights, GIS desktop projects, or third-party coastline datasets.

Complete model training still requires project-specific Dataset and DataLoader
adapters based on the actual local data schema.

## 📄 License

The source code is released under the MIT License. External imagery, boundaries,
reference products, labels, and model weights may have separate licenses.

## 🙏 Acknowledgements

This project benefits from Google Earth Engine, Copernicus Sentinel-2,
OpenStreetMap, SRTM, NumPy, Pandas, Rasterio, GeoPandas, Shapely, scikit-image,
scikit-learn, PyTorch, torchvision, timm, ArcGIS Pro, and QGIS.

> **Notice: This repository is intended for research, education, and code handover. All data acquisition, processing, and publication activities must comply with applicable licenses, service terms, privacy requirements, and laws.**
