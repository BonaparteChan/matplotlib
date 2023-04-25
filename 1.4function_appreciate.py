import matplotlib.pyplot as plt
import numpy as np
# 导入 numPy 和 快速绘图模块 pyplot

from matplotlib import cm as cm

# define data 定义数据
x = np.linspace(0.05, 3.5, 100)
# 在 0.05 到 10 之间取 1000 个数
y = np.sin(x)
y1 = np.random.randn(100)
# 随机 1000 个数字

# scatter figure 散点图设置
plt.scatter(x, y, c="red", label="scatter figure")
# 散点图，c 是颜色；label 是 图形内容的文本

# plot figure 折线图设置
plt.plot(x, y, ls="-.", lw="2", c="c", label="plot figure")
# 散点图，c 是颜色；label 是 图形内容的文本

# set clean up(removing chartjunk)
# trun the top spine and the right spine off
for spine in plt.gca().spines.keys():
    if spine == "top" or spine == "right":
        plt.gca().spines[spine].set_color("none")

# turn bottom tick for x-axis on
plt.gca().xaxis.set_ticks_position("bottom")
# set tick_line position of buttom

# turn left tick for y-axis on
plt.gca().yaxis.set_ticks_position("left")
# set tick_line position of left

# set x,yaxis limit，设置 x、y 轴的最大值和最小值
plt.xlim(0.0, 4.0)
# x 轴上的最大值和最小值
plt.ylim(-3.0, 3.0)
# y 轴上的最大值和最小值

# set axes labels,设置 x,y 轴上文字
plt.xlabel("x-axis")
# x 轴上的标签文字
plt.ylabel("y-axis")
# y 轴上的标签文字

# set x,yaxis grid，设置 x，y 网格
'''plt.grid(True, Is=":", color="r")'''
# True 报错，未赋值什么是为 True...

plt.grid(linestyle="", color="b")
# linestyle 网格线的风格，color 是网格线颜色


# add a horizontal line across the axis 增加平行线穿过图形
plt.axhline(y=0.0, c="r", ls="--", lw=2)
# 横向水平线，y 出发点，c 颜色，ls 风格， lw 宽度
plt.axvline(x=4.0, c="y", ls="-.", lw=1)
# 纵向水平线，x 出发点，c 颜色， ls 风格， lw 宽度

# add a vertical span across the axis 增加覆盖区域在图形
plt.axvspan(xmin=1.0, xmax=2.0, facecolor="y", alpha=.3)
# 横向水平线，xmin 区域起始位置， xmax 区域终止位置，facecolor 区域填充颜色， alpha 填充颜色透明度
plt.axhspan(ymin=0.0, ymax=0.5, facecolor="r", alpha=0.3)
# 纵向水平线，ymin 区域起始位置， ymax 区域终止位置， facecolor 区域填充颜色，alpha 填充颜色透明度

# set annotating info 增加备注中的信息
plt.annotate("maximum",
             xy=(np.pi/2, 1.0),
             xytext=((np.pi/2)+0.15, 1.5),
             weight="bold",
             color="b",
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color="b"))
"""string 注释文本;
xy 注释文本所在的位置坐标；
xytext 注释文本所在的位置坐标；
weight 注释文本的粗细风格；
color 注释文本的字体颜色；
arrowprops 注释内容的箭头属性字典，arrowstyle 箭头风格，connectionstyle 箭头形状，color 箭头颜色"""

plt.annotate("spines",
             xy=(0.75, -3),
             xytext=(0.35, -2.25),
             weight="bold",
             color="r",
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color="r"))

plt.annotate("space",
             xy=(0, -2.78),
             xytext=(0.4, -2.32),
             weight="bold",
             color="y",
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color="y"))

plt.annotate("",
             xy=(3.5, -2.98),
             xytext=(3.6, -2.70),
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color="b"))

# set text info 增加文本信息
plt.text(3.6, -2.70, "'|' is tickline", weight="bold", color="b")
# 无指向文本 text，注释文本内容所在的横坐标和纵坐标，注释文本内容，weight 注册文本的粗细风格，color 注释文本的颜色
plt.text(3.6, -2.95, "3.5 is ticklabel", weight="bold", color="b")

# set title 设置标题
plt.title("structure of matplotlib")
# 图形内容的标题 string

# set legend
plt.legend()
plt.show()
# 函数 plot() 展现变量的趋势变化