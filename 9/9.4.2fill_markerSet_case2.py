# case2 标记填充样式的设置方法

# 导入可视化和数学模块
import matplotlib.pyplot as plt
import numpy as np

# 设置字体和标记样式字典
font_style = dict(family="sans-serif", color="saddlebrown", weight="semibold", size=16)
line_marker_style = dict(linestyle=":", linewidth=2,
                         color="cornflowerblue",
                         markerfacecoloralt="lightgrey",  # 替换 markerfacecolor 才能将填充名称为 "none" 的展示形式有效表现出来
                         marker="o", markersize=18)

# 设置画布和子区
fig = plt.figure()
ax = fig.add_subplot(111)

# 填充样式列表
fillstyleList = ["full", "left", "right", "bottom", "top", "none"]

# 设置简单数据
x = np.arange(3, 11, 1)
y = np.linspace(1, 1, 8)

# 设置文本
ax.text(4, 6.5, "fill style", **font_style)

for i, fs in enumerate(fillstyleList):
    ax.text(0, i + 0.4, "'{}'".format(fs), **font_style)
    ax.plot(x, (i + 0.5)*y, fillstyle=fs, **line_marker_style)

ax.set_xlim(-1, 11)
ax.set_ylim(0, 7)

ax.margins(0.3)  # 留空 0.3
ax.set_xticks([])
ax.set_yticks([])

plt.show()