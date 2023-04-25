import matplotlib.pyplot as plt
import numpy as np
# 导入 numPy 和 快速绘图模块 pyplot

x = np.linspace(0.05, 10, 1000)
# 在 0.05 到 10 之间取 1000 个数
y = np.sin(x)

# 随机 1000 个数字

plt.plot(x, y, ls="-.", lw="2", c="c", label="plot figure")
# 散点图，c 是颜色；label 是 图形内容的文本

plt.legend(loc="lower right")
plt.title("y=sin(x)")
# loc 图例在途中的地理位置
plt.show()
# 函数 plot() 展现变量的趋势变化