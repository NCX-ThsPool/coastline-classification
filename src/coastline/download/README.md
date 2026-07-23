# Download / 数据获取

## 中文

该目录负责描述“从哪里获取数据”和“如何构建下载任务”，而不是保存下载数据本身。

- `sentinel2.py`：构建 Sentinel-2 SR Harmonized 影像集合；
- `dem.py`：定义 DEM 下载或裁剪时使用的空间范围对象；
- Earth Engine 项目名通过环境变量或 YAML 传入；
- Google 影像和 QGIS 下载流程具有服务条款与平台依赖，不能假设普通 Python 环境可直接运行。

## English

This package defines acquisition configuration and remote-service helpers. It
does not store downloaded imagery. Credentials, project identifiers, and local
paths must be supplied externally.
