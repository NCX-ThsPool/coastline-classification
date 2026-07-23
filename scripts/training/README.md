# Training Scripts / 训练脚本

`train_hr.py` 与 `train_mr.py` 当前负责检查和展示配置。真实数据接入时，应实现 Dataset/DataLoader 适配层，再调用统一 Trainer。不要重新复制多个模型训练循环。
