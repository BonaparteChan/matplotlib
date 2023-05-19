# 8.1.1 向画布中任意位置添加任意数量的坐标轴
# 第 8 章坐标轴的高阶应用
# 8.1 设置坐标轴的位置和展示形式
# 通过向画布中添加坐标轴，实现一个坐标轴中嵌套多个坐标轴的视图布局

# 导入数学模块和可视化模块
import matplotlib.pyplot as plt
import numpy as np

# set #1 plot
plt.axes([.05, .7, .3, .3], frameon=True, facecolor="y", aspect="equal")
# back up note，axisbg 先生成看看，不行，要换成 facecolor
'''
axes(rect, frameon, facecolor)
关键字参数 rect 是一个四分 [left, bottom, width, height]
frameon: True 绘制四条轴脊，False 不绘制
facecolor：背景颜色
'''
plt.plot(np.arange(3), [0, 1, 0], color="blue", linewidth=2, linestyle="--")

# set #2 plot
plt.axes([.3, .4, .3, .3], frameon=True, facecolor="y", aspect="equal")
# 只能在规则网格内进行视图布局
plt.plot(2 + np.arange(3), [0, 1, 0], color="blue", linewidth=2, linestyle="-")

# set #3 plot
plt.axes([.55, .1, .3, .3], frameon=True, facecolor="y", aspect="equal")
plt.plot(4 + np.arange(3), [0, 1, 0], color="blue", linewidth=2, linestyle=":")

plt.show()