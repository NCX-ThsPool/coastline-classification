# Documentation Center / 文档中心

## 中文

本目录面向首次接手项目的新成员。文档不仅说明“如何运行”，还说明：

- 每个模块解决什么问题；
- 为什么需要该步骤；
- 输入与输出的数据结构；
- 常见错误；
- 哪些参数可以修改；
- 哪些假设不能随意改变；
- 如何把旧科研脚本迁移为可维护代码。

### 推荐阅读顺序

| 顺序 | 文档 | 主要内容 |
|---:|---|---|
| 1 | `01_project_overview.md` | 项目目标、研究主线与边界 |
| 2 | `02_repository_structure.md` | 每个目录和文件的职责 |
| 3 | `03_environment_setup.md` | Python、GIS、深度学习环境 |
| 4 | `04_configuration_guide.md` | YAML、环境变量和路径配置 |
| 5 | `05_data_workflow.md` | 原始、中间和成果数据流 |
| 6 | `06_coastline_extraction.md` | 指数、Otsu、形态学和亚像素提取 |
| 7 | `07_dataset_preparation.md` | 采样、裁剪、增强和数据划分 |
| 8 | `08_model_training.md` | 模型、训练循环、权重和日志 |
| 9 | `09_inference_and_products.md` | 推理、点到线、产品生成 |
| 10 | `10_evaluation_and_analysis.md` | 精度、转换矩阵和长度统计 |
| 11 | `11_testing_and_debugging.md` | 单元测试、调试和问题定位 |
| 12 | `12_development_guide.md` | 二次开发、代码规范和交接 |

## English

This directory is designed for developers who are new to the project. The
documents explain not only how to run the workflow, but also why each stage
exists, what it consumes and produces, which assumptions are important, and how
to extend the code safely.

Follow the numbered guides in order for a complete onboarding path.
