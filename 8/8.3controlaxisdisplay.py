# 控制坐标轴的显示
# 通过控制坐标轴的载体(轴脊)的显示来实现控制控制坐标轴的显示
# 轴脊上的刻度线和刻度标签组成了坐标轴

# 导入可视化模块和数学模块
import matplotlib.pyplot as plt
import numpy as np

# set some simple data 设置简单数据
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
y = np.sin(x)

# 子区一坐标轴的显示控制

ax1 = plt.subplot(221)  # 两行两列第一个图
ax1.spines["right"].set_color("none")  # 保留刻度线，去掉右边框
ax1.spines["top"].set_color("none")  # 保留刻度线，去掉顶边框
ax1.set_xlim(-2 * np.pi, 2 * np.pi)
ax1.set_ylim(-1.2, 1.2)
plt.title(r"$a$", y=-0.2, loc="left")
plt.scatter(x, y, marker="+", color="b")  # 绘制散点图

# 子区二坐标轴的显示控制

ax2 = plt.subplot(222)  # 两行两列第一个图
ax2.spines["right"].set_color("none")  # 去掉右边框
ax2.spines["top"].set_color("none")  # 去掉顶边框
ax2.xaxis.set_ticks_position("bottom")  # 去掉顶边框的刻度线
ax2.set_xlim(-2 * np.pi, 2 * np.pi)
ax2.set_ylim(-1.2, 1.2)
plt.title(r"$b$", y=-0.2, loc="right")
plt.scatter(x, y, marker="+", color="b")  # 绘制散点图

# 子区三坐标轴的显示控制

ax3 = plt.subplot(223)  # 两行两列第一个图
ax3.spines["right"].set_color("none")
ax3.spines["top"].set_color("none")
ax3.yaxis.set_ticks_position("left")
ax3.set_xlim(-2 * np.pi, 2 * np.pi)
ax3.set_ylim(-1.2, 1.2)
plt.title(r"$c$", loc="right", y=-0.2)
plt.scatter(x, y, marker="+", color="b")  # 绘制散点图

# 子区四坐标轴的显示控制

ax4 = plt.subplot(224)  # 两行两列第一个图
ax4.spines["right"].set_color("none")
ax4.spines["top"].set_color("none")
ax4.xaxis.set_ticks_position("bottom")
ax4.yaxis.set_ticks_position("left")
ax4.set_xlim(-2 * np.pi, 2 * np.pi)
ax4.set_ylim(-1.2, 1.2)
plt.title(r"$d$", loc="left", y=-0.2)
plt.scatter(x, y, marker="+", color="b")  # 绘制散点图

plt.show()

# upper、lower 只针对图例 并需要设定四分位所在位置