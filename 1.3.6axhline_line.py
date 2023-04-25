import matplotlib.pyplot as plt
import numpy as np
# 导入 numPy 和 快速绘图模块 pyplot

x = np.linspace(0.05, 10, 1000)
# 在 0.05 到 10 之间取 1000 个数
y = np.sin(x)

# 随机 1000 个数字

plt.plot(x, y, ls="-.", lw="2", c="c", label="plot figure")
# 散点图，c 是颜色；label 是 图形内容的文本

plt.legend()
plt.axhline(y=0.0, c="r", ls="--", lw=2)
# 横向水平线，y 出发点，c 颜色，ls 风格， lw 宽度
plt.axvline(x=4.0, c="y", ls="-.", lw=1)
# 纵向水平线，x 出发点，c 颜色， ls 风格， lw 宽度

plt.show()
# 函数 plot() 展现变量的趋势变化