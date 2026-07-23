# Configurations / 配置文件

## 中文

配置文件把易变参数从代码中分离出来。

- `paths.example.yaml`：本地数据目录模板；
- `extraction.example.yaml`：影像时期、波段、指数和形态学参数；
- `classification_hr.example.yaml`：高分辨率 RGB 分类；
- `classification_mr.example.yaml`：14 通道中分辨率分类。

公开仓库只提交 `*.example.yaml`。真实路径和私人项目名应写入
`*.local.yaml`，并由 `.gitignore` 排除。

## English

Example YAML files document public configuration schemas. Local paths and
private service identifiers must remain in ignored local files.
