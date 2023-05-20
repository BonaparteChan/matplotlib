# case2 坐标轴的样式和位置定制化展示
# 8.2 使用两种方法控制坐标轴刻度的显示
# 使用 step() 对刻度标签、刻度线、轴脊等定制化调整

# 导入数学模块和可视化模块
import matplotlib.pyplot as plt
import numpy as np

from calendar import day_name
from matplotlib.ticker import FormatStrFormatter

# 生成画布
fig = plt.figure()

# 设置画布
ax = fig.add_axes([.2, .2, .7, .7])
ax.spines["bottom"].set_position(("outward", 10))  # 轴脊向下移动 10 个距离点
ax.spines["left"].set_position(("outward", 10))  # 轴脊向左移动 10 个距离点
ax.spines["top"].set_color("pink")  # 设置顶部轴脊颜色为粉红色，红色太显眼了
ax.spines["right"].set_color("none")

# set some simple data 设置简单数据
x = np.arange(1, 8, 1)
y = 2 * x + 1

# 生成散点图
ax.scatter(x, y, c="orange", s=50, edgecolors="orange")

# 设置 x 轴刻度线
for tickline in ax.xaxis.get_ticklines():
    tickline.set_color("blue")
    tickline.set_markersize(8)
    tickline.set_markeredgewidth(5)

# 设置 x 轴刻度标签
for ticklabel in ax.get_xmajorticklabels():
    ticklabel.set_color("slateblue")
    ticklabel.set_fontsize(15)
    ticklabel.set_rotation(20)

ax.yaxis.set_major_formatter(FormatStrFormatter(r"$\yen%1.1f$"))  # 设置 y 轴标签格式单位，元
plt.xticks(x, day_name[0:7], rotation=20)  # 设置 x 轴标签格式单位，星期
ax.yaxis.set_ticks_position("left")  # 设置 y 轴标签显示位置，左侧
ax.xaxis.set_ticks_position("bottom")  # 设置 x 轴标签显示位置，底部

# 设置 y 轴刻度线
for tickline in ax.yaxis.get_ticklines():
    tickline.set_color("lightgreen")
    tickline.set_markersize(8)
    tickline.set_markeredgewidth(5)

# 设置 y 轴刻度标签
for ticklabel in ax.get_ymajorticklabels():
    ticklabel.set_color("green")
    ticklabel.set_fontsize(18)

# 设置网格线
ax.grid(ls=":", lw=1, color="gray", alpha=0.5)

plt.show()