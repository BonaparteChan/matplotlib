# 线条类型的显示样式设置方法

# 导入可视化模块和数学模块
import matplotlib.pyplot as plt
import numpy as np

# 设置字体、颜色和线条宽度
font = dict(family="serif", color="navy", weight="black", size=16)
color = "skyblue"
linewidth = 3

# 设置画布和子区
fig = plt.figure()
ax = fig.add_subplot(111)

# 线条样式列表
linestyleList = ["-", "--", "-.", ":"]

# 设置简单数据 set some simple data
x = np.arange(1, 11, 1)
y = np.linspace(1, 1, 10)

# 设置文本
ax.text(4, 4.0, "line styles", **font)

# 划线展示每种样式，示例
for i, ls in enumerate(linestyleList):  # for 循环
    ax.text(0, i + 0.5, "'{}'".format(ls), **font)  # 格式化字符串，加入变量
    ax.plot(x, (i + 0.5)*y, linestyle=ls, color=color, linewidth=linewidth)

# 设置 x y 轴的最大值和最小值
ax.set_xlim(-1, 11)
ax.set_ylim(0, 4.5)

ax.margins(0.2)  # 设置数据范围的空白区域
ax.set_xticks([])
ax.set_yticks([])

plt.show()