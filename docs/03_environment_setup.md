# Environment Setup / 环境安装

## 中文

### 基础 Python 环境

```bash
python -m venv .venv
.venv\Scriptsctivate
python -m pip install --upgrade pip
pip install -e ".[geo,ml,gee,dev]"
```

### GIS 依赖

`rasterio`、`geopandas`、`shapely`、`pyogrio`、`scipy` 和
`scikit-image` 用于可移植 GIS 处理。

ArcPy 必须使用 ArcGIS Pro 自带环境。QGIS Python 必须使用 QGIS 的
Python 环境。不要把 ArcPy 或 `qgis.core` 加入普通 requirements 并期望
所有机器都能安装。

### 深度学习依赖

建议先根据 CUDA 环境安装 PyTorch，再执行项目安装。应记录：

- Python 版本；
- PyTorch 版本；
- CUDA 版本；
- GPU 型号；
- torchvision 和 timm 版本。

### 环境验证

```bash
python -c "import coastline; print(coastline.__version__)"
pytest
```

## English

Use a virtual environment for portable dependencies. ArcPy and QGIS APIs require
their vendor environments. Record the complete Python, PyTorch, CUDA, GPU, and
package versions for reproducibility.
