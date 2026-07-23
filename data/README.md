# Data / 数据目录

## 中文

本目录只提交说明文档，不提交真实大数据。

推荐结构：

```text
data/
├── raw/        # 原始数据，不可覆盖
├── external/   # 第三方数据
├── interim/    # 可重新生成的中间数据
└── processed/  # 模型和评价直接使用的数据
```

原则：

1. 原始数据只读；
2. 中间数据可以删除后重建；
3. 成果数据必须记录年份、坐标系、分类体系和生成配置；
4. 第三方数据必须保留来源与许可证；
5. 涉密、受限或未授权数据不能上传 GitHub。

## English

Only documentation is tracked here. Raw imagery, third-party datasets,
intermediate products, labels, and final nationwide products remain local.
