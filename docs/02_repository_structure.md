# Repository Structure / 仓库结构详解

## 中文

### `src/coastline`

保存可复用代码。任何需要被多个脚本调用、需要单元测试、或需要在其他项目中导入的逻辑，都应优先放入这里。

### `scripts`

保存命令行入口。一个脚本应尽量只做四件事：解析参数、读取配置、调用核心函数、保存结果。

### `configs`

保存参数模板。路径、年份、波段、窗口、批量大小和学习率等易变参数不应散落在代码中。

### `data`

只描述本地数据布局。真实栅格、矢量和标签不进入 Git。

### `outputs`

保存程序自动生成的结果。该目录中的内容应可以通过代码和配置重新生成。

### `assets`

保存经过人工确认、用于文档展示的图片。它不是临时输出目录。

### `tests`

保存小而稳定的自动测试。测试不依赖全国数据，也不应需要数小时训练。

### `docs`

保存知识传递。代码告诉计算机做什么，文档告诉新成员为什么这样做。

## English

The package code, executable scripts, configuration, data placeholders,
generated outputs, documentation assets, tests, and handover guides have
separate responsibilities. Keeping these boundaries clear prevents the
repository from becoming another research workspace dump.
