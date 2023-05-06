import matplotlib.pyplot as plt
import numpy as np
# 导入 numPy 和 快速绘图模块 pyplot

x = np.linspace(0.05, 10, 1000)
# 在 0.05 到 10 之间取 1000 个数
y = np.sin(x)

# 随机 1000 个数字

plt.plot(x, y, ls="-.", lw="2", c="c", label="plot figure")
# 散点图，c 是颜色；label 是图形内容的文本

plt.legend()
plt.annotate("maximum",
             xy=(np.pi/2, 1.0),
             xytext=((np.pi/2)+1.0, .8),
             weight="bold",
             color="b",
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color="y"))
"""string 注释文本;
xy 注释文本所在的位置坐标；
xytext 注释文本所在的位置坐标；
weight 注释文本的粗细风格；
color 注释文本的字体颜色；
arrowprops 注释内容的箭头属性字典，arrowstyle 箭头风格，connectionstyle 箭头形状，color 箭头颜色"""

plt.show()
# 函数 plot() 展现变量的趋势变化