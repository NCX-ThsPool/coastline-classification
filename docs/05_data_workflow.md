# Data Workflow / 数据流与目录管理

## 中文

### 数据分层

**Raw 原始数据**

未经项目算法修改的数据。应只读保存。

**External 第三方数据**

来自其他机构或产品的数据。必须记录来源、版本和许可。

**Interim 中间数据**

指数、掩膜、裁剪图块和临时矢量。应能够重新计算。

**Processed 处理后数据**

训练表、验证表和最终产品。应有明确字段字典和生成配置。

### 数据命名

推荐：

```text
{grid_id}_{sensor}_{content}_{year}.{extension}
```

示例：

```text
120_3E30_4N_S2_RGB_B11_2025.tif
```

避免仅使用：

```text
result2_final_new.tif
```

### 坐标系

每个空间处理步骤应明确：

- 输入 CRS；
- 输出 CRS；
- 距离和面积使用的投影；
- 是否发生重采样；
- 像元对齐方式。

在 EPSG:4326 中直接把“度”当作“米”是常见错误。

## English

Data should be separated into raw, external, interim, and processed layers.
Every spatial stage must document CRS, units, resampling, alignment, and naming.
