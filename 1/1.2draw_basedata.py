import matplotlib.pyplot as plt
import numpy as np
# 导入 numPy 和 快速绘图模块 pyplot

x = np.linspace(0.5, 3.5, 100)
# 在 0.5 到 3.5 之间取 100 个数
y = np.sin(x)
y1 = np.random.randn(100)
# 在正态分布中随机取 100 个数

plt.plot(x, y, ls="-", lw="2", label="plot figure")

plt.legend()


plt.show()