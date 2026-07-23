# Utilities / 通用工具

## 中文

该目录只放跨业务模块都可能使用的底层功能：

- `config.py`：读取 YAML 并展开环境变量；
- `filesystem.py`：目录创建和文件枚举；
- `logging.py`：统一日志格式；
- `raster.py`：Rasterio 读写；
- `vector.py`：GeoPandas 读写。

“工具类”不应成为无法分类代码的堆放位置。

## English

Utilities are small cross-cutting helpers. Domain-specific algorithms should
remain in their own packages rather than becoming an unstructured utility
collection.
