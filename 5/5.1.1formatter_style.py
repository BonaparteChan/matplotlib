# 设置坐标轴的刻度样式
# 刻度是统计图形的一部分，由刻度标签和刻度线组成
# 刻度定位器(locator)用来设置刻度线的位置；
# 刻度格式器(formatter)用来设置刻度表现的显示样式

# 导入可视化模块
import matplotlib.pyplot as plt
# 导入数学模块
import numpy as np
# 导入刻度的类
from matplotlib.ticker import AutoMinorLocator, MultipleLocator, FuncFormatter

# 设置简单的数据 set some simple data
x = np.linspace(0.5, 3.5, 100)
y = np.sin(x)  # x 的正弦曲线

# 构建一个画布对象
figure = plt.figure(figsize=(8, 8))
ax = figure.add_subplot(111)  # 画布分区，第一行，第一列的子区

# set x,y-major tick locator，设置 x 和 y 的主刻度线的位置
ax.xaxis.set_major_locator(MultipleLocator(1.0))  # 在 x 轴的 1 倍处设置主刻度线
ax.yaxis.set_major_locator(MultipleLocator(1.0))  # 在 y 轴的 1 倍处设置主刻度线

# set x,y-minor tick locator 设置 x 和 y 的次刻度线的位置
ax.xaxis.set_minor_locator(AutoMinorLocator(4))  # 将 x 轴的每一份主刻度线区间等分为 4 份
ax.yaxis.set_minor_locator(AutoMinorLocator(4))  # 将 y 轴的每一份主刻度线区间等分为 4 份

# set x-minor tick formatter，设置 x 次刻度线的精度
def minor_tick(x, pos):  # n%n=0;n=m(m<n)
    if not x % 1.0:
        return ""
    return "%.2f" % x

ax.xaxis.set_minor_formatter(FuncFormatter(minor_tick))

# change the appearance of ticks and tick labels,刻度的样式设置
ax.tick_params("y", which="major",  # 设置主刻度线的样式
               length=15, width=2.0,  # 设置主刻度线的长度和宽度
               color="r")  # 设置主刻度线和主刻度线标签的颜色
ax.tick_params(which="minor",  # 设置次刻度线的样式
               length=5, width=1.0,  # 设置次刻度线的长度和宽度
               labelsize=10, labelcolor="0.25")  # 设置次刻度线标签大小(labelsize)和次刻度线标签颜色(labelcolor)

# set x,y axis limit
ax.set_xlim(0, 4)
ax.set_ylim(0, 2)

# plot subplot 画布
ax.plot(x, y, c=(0.25, 0.25, 1.00), lw=2, zorder=10)  # pair 0
# ax.plot(x, y, c=(0.25, 0.25, 1.00), lw=2, zorder=0)  # pair 1

# set grid
# ax.grid(linestyle="-", linewidth=0.5, color="r", zorder=0)  # pair 0
ax.grid(linestyle="-", linewidth=0.5, color="r", zorder=10)  # pair 1
# ax.grid(linestyle="--", linewidth=0.5, color=".25", zorder=0)  # pair 2

plt.show()