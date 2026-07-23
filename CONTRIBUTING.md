# Contributing / 参与开发

## 中文

提交代码前请完成：

```bash
pytest
python -m compileall src scripts tests
```

新增 Python 文件应包括：

- 模块级中英双语说明或至少清晰英文 docstring；
- 类型标注；
- 对公开函数的参数、返回值和异常说明；
- 不含本机绝对路径或秘密信息；
- 对应测试；
- 对应 README 或 docs 更新。

提交信息推荐：

```text
feat: add spatial block dataset split
fix: preserve NoData during Otsu masking
docs: expand bilingual inference guide
test: add transition matrix edge cases
```

## English

Before submitting code, run the tests and syntax compilation. New modules should
include clear documentation, type hints, focused error handling, no private
machine information, corresponding tests, and updated handover documentation.
