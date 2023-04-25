'''
堆积折线图通过绘制不同数据集的折线图生成的
堆积折线图是按垂直方向上彼此堆叠且不相互覆盖的排列顺序，绘制若干条折线图而形成的组合图形
'''
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
# 导入模块

mpl.rcParams["font.sans-serif"] = ["SimHei"]
# 字体设置
mpl.rcParams["axes.unicode_minus"] = False
# 处理坐标轴线的负刻度值的情况
# 设置编码格式，不设置就没法写中文

# some simple data 设置简单数据
x = np.arange(1, 6, 1)
y = [0, 4, 3, 5, 6]
y1 = [1, 3, 4, 2, 7]
y2 = [3, 4, 1, 6, 5]
# 数据格式为 list 列表

labels = ["blueplanet 蓝球", "brownplanet 粽球", "greenplanet 绿球"]
color = ["#8da0cb", "#fc8d62", "#66c2a5"]

# create bar 创建条形图
plt.stackplot(x, y, y1, y2, labels=labels, colors=color)

# set yaxis grid
plt.grid(True, axis="y", ls=":", color="r", alpha=0.3)

plt.legend(loc="upper left")
# 表示不同图形的文本标签示例

plt.show()