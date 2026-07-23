# Extraction / 海岸线提取

## 中文

提取流程分为多个可独立检查的阶段：

1. `thresholding.py`：计算 Otsu 阈值并生成 0/255 二值掩膜；
2. `morphology.py`：删除小连通域并填充内部孔洞；
3. `subpixel.py`：使用 marching squares 提取亚像素轮廓；
4. `pipeline.py`：把前三个阶段组织成便于调用的流水线。

分阶段设计有助于定位问题。例如，岸线断裂可能来自阈值、连通域阈值、NoData 或轮廓闭合，而不是模型本身。

## English

The extraction workflow is intentionally split into thresholding, component
filtering, hole filling, and subpixel contour extraction so that every stage can
be inspected independently.
