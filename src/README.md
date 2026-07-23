# Source Package / 核心代码包

## 中文

`src/coastline` 是项目中最重要的目录。这里存放可以被其他程序导入和复用的核心代码。

基本原则：

1. 模块中不硬编码本机路径；
2. 模块导入时不自动开始大规模处理；
3. 输入参数通过函数、类或配置传入；
4. 通用逻辑放在 `src`，一次性执行流程放在 `scripts`；
5. 关键函数具有类型标注、文档字符串和异常说明；
6. 平台依赖应延迟导入，并给出明确错误提示。

示例：

```python
from coastline.indices.calculator import calculate_index

result = calculate_index("ndvi", bands)
```

## English

`src/coastline` contains reusable package code. It should not contain personal
paths or start a large workflow merely because a module is imported. Reusable
logic belongs here; command-line orchestration belongs in `scripts`.
