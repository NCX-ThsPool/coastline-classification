# Old-to-New Mapping Examples / 旧代码到新结构的映射示例

## 中文

### 多个 Sentinel-2 下载脚本

旧工程可能为 B11、B8+B12、RGB 和 RGB+B11 分别复制脚本。新结构把共同逻辑放入：

```text
src/coastline/download/sentinel2.py
```

波段差异通过配置：

```yaml
bands: [B2, B3, B4, B8, B11, B12]
```

### 多个模型训练脚本

旧工程中每种模型重复数据加载、训练、验证和保存逻辑。新结构拆为：

```text
src/coastline/models/factory.py
src/coastline/training/trainer.py
configs/classification_*.example.yaml
scripts/training/
```

### 多个 `v1`、`v2` 文件

版本历史交给 Git 保存。功能差异应成为参数、配置或独立函数，而不是无限复制文件。

## English

Duplicated band-specific download scripts, model-specific training loops, and
version-suffixed files are consolidated into reusable modules and explicit
configuration. Git history should replace manual filename versioning.
