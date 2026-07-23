# Development and Handover Guide / 二次开发与代码交接

## 中文

### 新增功能的推荐步骤

1. 在文档中定义问题、输入和输出；
2. 在 `src/coastline` 中实现可复用函数；
3. 添加类型标注和文档字符串；
4. 编写最小单元测试；
5. 在 `scripts` 中增加薄入口；
6. 在 `configs` 中增加示例参数；
7. 更新对应目录 README；
8. 使用小数据验证；
9. 记录迁移或版本说明。

### 文件命名

推荐：

```text
calculate_indices.py
generate_sampling_points.py
evaluate_products.py
```

不推荐：

```text
draft.py
test2.py
new_final_v5.py
```

### 函数设计

函数应具有明确输入和返回值。避免依赖全局变量和隐式工作目录。

### 异常处理

捕获能够处理的具体异常。无法恢复时应抛出包含上下文的信息，而不是打印后继续生成不完整结果。

### 代码审查清单

- 是否存在绝对路径；
- 是否存在密钥或项目 ID；
- 是否正确处理 NoData；
- CRS 和单位是否明确；
- 波段顺序是否记录；
- 是否有随机种子；
- 输出是否可追溯；
- 是否补充测试和文档；
- 是否把生成结果误提交到 Git。

## English

New functionality should be documented, implemented as reusable package code,
tested on small data, exposed through a thin script, configured through YAML,
and accompanied by updated bilingual handover documentation.
