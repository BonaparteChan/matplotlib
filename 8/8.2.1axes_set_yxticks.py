# method1 使用 axes.set_xticks() 和 axes.set_yticks() 实例方法
# 8.2 使用两种方法控制坐标轴刻度的显示

# 导入可视化模块
import matplotlib.pyplot as plt
import numpy as np

ax1 = plt.subplot(121)  # 一行两列第一个图
# ax1.set_yticks(range(0, 11, 2))  # 设置 x 轴，从 0 开始，到 251 结束，50 间隔
ax1.set_yticks(np.arange(0.0, 1.1, 0.2))  # 设置 x 轴，从 0 开始，到 251 结束，50 间隔
plt.grid(True, axis="y")
# 设置刻度，包括设置刻度标签和刻度线

ax2 = plt.subplot(122)  # 一行二列第二个图形
ax2.set_yticks([])  # x 轴不设置
plt.grid(True, axis="y")  # 不设置坐标轴刻度，网格线也不会设置

plt.show()
