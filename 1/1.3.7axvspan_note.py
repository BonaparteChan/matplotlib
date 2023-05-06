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
plt.axhspan(ymin=0.0, ymax=0.5, facecolor="r", alpha=0.3)
# 纵向水平线，ymin 区域起始位置， ymax 区域终止位置， facecolor 区域填充颜色，alpha 填充颜色透明度
plt.axvspan(xmin=4.0, xmax=6.0, facecolor="y", alpha=0.3)
# 横向水平线，xmin 区域起始位置， xmax 区域终止位置，facecolor 区域填充颜色， alpha 填充颜色透明度

plt.show()
# 函数 plot() 展现变量的趋势变化