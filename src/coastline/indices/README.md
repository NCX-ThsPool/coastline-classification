# Indices / 遥感指数

## 中文

该目录实现七种海岸研究常用指数。公式函数只接受 NumPy 数组，不负责猜测波段顺序。

- `spectral.py`：单个指数的纯数值公式；
- `calculator.py`：根据语义波段名称选择公式；
- 所有归一化差值都处理除零、NaN 和无穷值；
- 输入反射率应处于一致尺度；
- B11、B12 的空间分辨率统一应在计算前完成。

## English

The module implements pure NumPy index formulas and a semantic band-aware
calculator. It deliberately avoids guessing band order or silently resampling
rasters.
