# Scripts / 工作流执行入口

## 中文

`scripts` 中的文件面向命令行用户。它们负责：

1. 解析命令行参数；
2. 读取 YAML 配置；
3. 调用 `src/coastline` 中的核心函数；
4. 保存结果并输出简明日志。

脚本不应复制核心算法。需要在其他程序中复用某项功能时，应导入 `src` 中的函数，而不是导入脚本。

## English

Scripts are thin command-line entry points. Reusable algorithms belong in the
package under `src/coastline`.
