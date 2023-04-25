import matplotlib.pyplot as plt
import numpy as np
# 导入 numPy 和 快速绘图模块 pyplot

x = np.linspace(0.05, 10, 1000)
# 在 0.05 到 10 之间取 1000 个数
y = np.random.randn(1000)

# 随机 1000 个数字

plt.scatter(x, y, c="yellow", label="scatter figure")
# 散点图，c 是颜色；label 是 图形内容的文本
plt.legend()

plt.xlim(0.05, 10)
# x 轴上的最大值和最小值
plt.ylim(0, 1)
# y 轴上的最大值和最小值

plt.show()
# 函数 plot() 展现变量的趋势变化