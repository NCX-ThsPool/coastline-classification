# Dataset Preparation / 分类数据集构建

## 中文

### 空间采样

沿线采样前必须把岸线投影到以米为单位的合适坐标系。100 米间距表示真实地面距离，而不是经纬度中的 100 度。

### 影像图块

每个样本需要记录：

- UID；
- 中心点；
- 数据源和年份；
- 影像路径；
- 类别；
- 影像分辨率；
- 窗口大小；
- 波段顺序；
- 数据质量标记。

### 数据泄漏

相邻岸线样本高度相关。随机按图块划分可能让相邻样本同时进入训练和验证集，造成乐观精度。更严格的方法是按空间区块、岸段或区域划分。

### 类别不平衡

需要记录每类样本数量。可以使用分层抽样、类别权重、重采样或增强，但不能只报告总样本数。

### 人工核查

独立验证点不能直接由模型预测结果当作真值。应进行人工判读或使用可信参考数据，并保存核查状态和证据来源。

## English

Dataset preparation must document spatial sampling units, tile metadata, band
order, class balance, and leakage controls. Independent validation labels must
not be derived from the evaluated model itself.
