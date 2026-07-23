# Evaluation and Analysis / 精度评价与时空分析

## 中文

### 分类指标

- OA：总体正确比例；
- Kappa：考虑随机一致性的总体指标；
- Macro-F1：各类别 F1 的等权平均；
- Precision：预测为某类的样本中有多少是真的；
- Recall：真实某类中有多少被识别；
- IoU：真阳性除以真阳性、假阳性和假阴性的并集。

### 混淆矩阵

矩阵的行列含义必须写清楚。常见约定是行表示真实类别、列表示预测类别。

### 转换矩阵

多时相转换分析需要空间对应关系。不能仅比较两个年份的全国总长度，就声称获得了逐岸段类型转换。

### 长度统计

长度应在合适投影下计算，并明确单位。不同年份必须使用一致岸线范围、拓扑规则和分类定义。

### 第三方比较

应先把第三方产品的分类体系映射到统一五类体系，并说明无法对应或被合并的类别。

## English

Evaluation includes classification metrics, confusion matrices, spatially
matched transition analysis, projected length summaries, and carefully mapped
third-party product comparisons.
