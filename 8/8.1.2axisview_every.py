# 8.1.2 调整已确定的坐标轴的显示、隐藏、与刻度范围等问题
# 第 8 章坐标轴的高阶应用
# 8.1 设置坐标轴的位置和展示形式


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
plt.ylim(0, 1.5)
plt.axis("image")  # 画面更紧凑

# set #2 plot
plt.axes([.3, .4, .3, .3], frameon=True, facecolor="y", aspect="equal")
# 只能在规则网格内进行视图布局
plt.plot(2 + np.arange(3), [0, 1, 0], color="blue", linewidth=2, linestyle="-")
plt.ylim(0, 15)
plt.axis([2.1, 3.9, 0.5, 1.9])  # 重新改变坐标轴范围
# axis([xmin, amax, ymin, ymax])

# set #3 plot
plt.axes([.55, .1, .3, .3], frameon=True, facecolor="y", aspect="equal")
plt.plot(4 + np.arange(3), [0, 1, 0], color="blue", linewidth=2, linestyle=":")
plt.ylim(0, 1.5)
plt.axis("off")  # 坐标轴完全隐藏，只显示函数 plot() 绘制的图形

plt.show()