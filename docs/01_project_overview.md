# Project Overview / 项目总览

## 中文

### 项目解决的问题

该项目试图解决两个相互关联的问题：

1. 如何从多时相遥感影像中提取连续海岸线；
2. 如何将海岸线划分为人工、生物、砂质、泥质和基岩五类。

海岸线提取是几何问题，输出水陆边界；海岸线分类是语义问题，输出岸线类型。两者不能混为一谈。

### 两条数据主线

**高分辨率主线**

- 数据：高分辨率 RGB 影像；
- 窗口：256×256；
- 模型：ConvNeXt；
- 任务：2025 年精细岸线类型分类。

**中分辨率主线**

- 数据：Sentinel-2 与遥感指数等 14 通道特征；
- 窗口：32×32；
- 模型：ConvNeXt 与类别敏感通道权重；
- 任务：2015、2020、2025 多时相产品。

### 工程边界

代码仓库提供算法和接口，但不自动解决以下问题：

- 数据许可；
- 全国影像下载配额；
- 人工真值判读；
- ArcGIS/QGIS 软件安装；
- 不同产品分类体系映射；
- 论文成果的最终审图和发布。

## English

The project contains two related but distinct tasks: geometric coastline
extraction and semantic coastline-type classification. It supports a
high-resolution RGB workflow and a multi-temporal, multi-channel
mid-resolution workflow. Data licensing, manual interpretation, GIS desktop
installation, and product publication remain outside the portable codebase.
