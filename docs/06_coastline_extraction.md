# Coastline Extraction / 海岸线提取详解

## 中文

### 1. 指数

MNDWI 和 NDWI 用于增强水体。植被、建设用地和潮滩指数主要服务于后续分类，也可辅助质量检查。

### 2. Otsu

Otsu 根据有效像元的灰度分布自动寻找阈值。必须排除 NoData，否则极端无效值会改变阈值。

### 3. 二值方向

代码使用 255 表示前景、0 表示背景。`invert` 参数必须根据输入指数的物理意义确认，不能仅凭显示颜色判断。

### 4. 连通域过滤

小连通域通常是云、噪声、船舶或局部误分。阈值过大会删除小岛和狭窄水道，因此应在典型区域进行敏感性分析。

### 5. 孔隙填充

只填充被前景完全包围的内部背景。它可能填掉真实岛屿，因此不能无条件用于所有尺度。

### 6. 亚像素轮廓

`find_contours` 在像元内部插值边界。输出首先是像素坐标，再通过仿射变换转为地理坐标。

### 7. 质量检查

每个阶段建议输出：

- 阈值；
- 前景像元比例；
- 连通域数量；
- 删除像元数量；
- 填充像元数量；
- 轮廓数量和总长度；
- 随机抽样可视化。

## English

The extraction pipeline includes index calculation, valid-pixel Otsu
thresholding, binary-mask orientation, component filtering, hole filling, and
subpixel contour conversion. Each stage should emit diagnostic statistics and
visual samples.
