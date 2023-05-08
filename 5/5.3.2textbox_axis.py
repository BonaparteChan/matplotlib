# 坐标轴标签添加文本框，调整文本框位置

import matplotlib.pyplot as plt
import numpy as np
# 导入可视化模块和数学模块

x = np.linspace(0.5, 3.5, 100)
y = np.sin(x)
# 设置数据

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)
# 设置画布

box = dict(facecolor="#6959cd", pad=2, alpha=.4)
ax.plot(x, y, c="b", ls="--", lw=2)
# 设置文本框字典变量，画线

# set text contents 文本内容
title = "$y=\sin({x})$"
xaxis_label = "$x\_axis$"
yaxis_label = "$y\_axis$"

ax.set_xlabel(xaxis_label, fontsize=18, bbox=box)
ax.set_ylabel(yaxis_label, fontsize=18, bbox=box)
ax.set_title(title, fontsize=23, va="bottom")

# 确定文本所在位置，取值范围 0.0~1.0，数值取负表示与坐标系相反的距离
ax.yaxis.set_label_coords(-0.08, 0.5)
ax.xaxis.set_label_coords(1.0, -0.05)

ax.grid(ls="-.", lw=1, color="gray", alpha=.5)

plt.show()