# method1 单一字符模式
# 第 9 章设置线条类型和标记类型的显示样式
# 9.3 标记类型的显示样式设置方法

# 导入可视化和数学模块
import matplotlib.pyplot as plt
import numpy as np

# 设置字体、标记和线条样式字典
font = dict(family="serif", color="navy", weight="black", size=12)
line_marker_style = dict(linestyle=":", linewidth=2, color="maroon", markersize=10)

# 设置画布和子区
fig = plt.figure()
ax = fig.add_subplot(111)

# 标记样式名称和标记样式列表
msNameList = ["'.'--point marker",
              "','--pixel marker",
              "'o'--circle marker",
              "'v'--triangle_down_marker",
              "'^'--triangle_up_marker",
              "'<'--triangle_left_marker",
              "'>'--triangle_right_marker",
              "'1'--tri_down_marker",
              "'2'--tri_up_marker",
              "'3'--tri_left_marker",
              "'4'--tri_right_marker",
              "'s'--square marker",
              "'p'--Pentagon marker",
              "'*'--star marker",
              "'h'--hexagon1 marker",
              "'H'--hexagon2 marker",
              "'+'--plus marker",
              "'x'--x marker",
              "'D'--diamond marker",
              "'d'--thin_diamond marker",
              "'|'--vline marker",
              "'_'--hline marker"]
markerstyleList = ['.', ',', 'o', 'v', '^', '<', '>', '1', '2', '3', '4', 's', 'p', '*', 'h', 'H', '+', 'x', 'D', 'd', '|', '_']

# set some simple data 设置简单数据
x = np.arange(5, 11, 1)
y = np.linspace(1, 1, 6)

# 设置文本
ax.text(4, 23, "marker styles", **font)
for i, ms in enumerate(markerstyleList):
    ax.text(0, i + 0.5, msNameList[i], **font)
    ax.plot(x, (i + 0.5)*y, marker=ms, **line_marker_style)

ax.set_xlim(-1, 11)
ax.set_ylim(0, 24)

ax.margins(0.3)
ax.set_xticks([])
ax.set_yticks([])

plt.show()