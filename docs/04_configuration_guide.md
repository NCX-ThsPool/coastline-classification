# Configuration Guide / 配置指南

## 中文

### 为什么使用 YAML

科研脚本常把路径、年份和参数写在文件顶部。这样虽然方便一次运行，却会导致：

- 修改参数时容易漏改；
- 不同实验难以比较；
- 代码中泄露本机信息；
- 无法记录某个结果对应的完整配置。

YAML 将配置和算法分离。

### 配置优先级建议

1. 命令行显式参数；
2. 本地 YAML；
3. 环境变量；
4. 代码中的安全默认值。

### 环境变量

配置加载器支持：

```yaml
earth_engine:
  project: ${EE_PROJECT}
```

如果环境变量未设置，字符串会保持原样，调用外部服务前应主动检查。

### 命名建议

- `*.example.yaml`：可公开模板；
- `*.local.yaml`：本机真实配置；
- `experiment_*.yaml`：可复现实验配置；
- 不使用 `final2_new_latest.yaml` 一类无语义名称。

## English

YAML separates algorithms from experiment-specific and machine-specific values.
Public templates and ignored local files should be clearly distinguished.
