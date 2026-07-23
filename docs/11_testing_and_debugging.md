# Testing and Debugging / 测试与调试

## 中文

### 测试层次

1. 单元测试：纯函数和小数组；
2. 集成测试：一个小栅格或小矢量文件；
3. 流程测试：一个网格的完整处理；
4. 大规模运行：全国数据。

不要直接用全国数据作为第一次测试。

### 常见问题

**导入失败**

检查是否执行 `pip install -e .`。

**Rasterio/GDAL 安装失败**

优先使用 Conda 或匹配 Python 版本的预编译包。

**ArcPy 找不到**

必须进入 ArcGIS Pro 的 Python 环境。

**CUDA 不可用**

检查驱动、PyTorch CUDA 构建和显卡兼容性。

**输出为空**

逐步检查有效像元、阈值、前景方向、连通域参数和坐标系。

### 日志

异常应包含文件路径、阶段、参数和原始异常。不要使用空 `except:` 静默跳过全部错误。

## English

Testing should progress from pure unit tests to tiny integration data, one-grid
workflow tests, and only then national-scale processing. Debug empty outputs
stage by stage rather than rerunning the entire pipeline blindly.
