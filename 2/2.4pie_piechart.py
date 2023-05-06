import matplotlib as mpl
import matplotlib.pyplot as plt
# import numpy as np
# 导入模块

mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False
# 设置编码格式，不设置就没法写中文

kinds = "简易箱", "保温箱", "行李箱", "密封箱"
colors = ["#66b266", "#ff6060", "#0ebeff", "#fdc9d8", "#dde1e4"]

soldNums = [0.05, 0.45, 0.15, 0.35]
# some simple data 设置简单数据
'''x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [3, 1, 4, 5, 8, 9, 7, 2]

# create bar 创建直方图
plt.barh(x, y, align="center", color="r", tick_label=["q", "a", "c", "e", "r", "j", "b", "p"], hatch="/")'''

# pie chart 创建饼图，主要要百分比，占比分析
plt.pie(soldNums, labels=kinds, autopct="%3.lf%%", startangle=60, colors=colors)

# set title
plt.title("不同类型箱子的销售数量占比")

plt.show()