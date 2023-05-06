import matplotlib.pyplot as plt
import numpy as np
# 导入 numPy 和 快速绘图模块 pyplot

x = np.linspace(0.05, 10, 1000)
# 在 0.05 到 10 之间取 1000 个数
y = np.cos(x)

# 正弦

plt.plot(x, y, ls="--", lw="2", label="plot figure")
# 折线图，ls 是线条风格，lw 是线条宽度
plt.legend()


plt.show()
# 函数 plot() 展现变量的趋势变化