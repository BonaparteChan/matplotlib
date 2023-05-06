import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
# 导入模块

mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False
# 设置编码格式，不设置就没法写中文

# set test scores
boxWeight = np.random.randint(0, 10, 100)
x = boxWeight

# plot histogram
bins = range(0, 11, 1)

plt.hist(x, bins=bins, color="g", histtype="bar", rwidth=1, alpha=0.6)
# some simple data 设置简单数据
'''x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [3, 1, 4, 5, 8, 9, 7, 2]

# create bar 创建直方图
plt.barh(x, y, align="center", color="r", tick_label=["q", "a", "c", "e", "r", "j", "b", "p"], hatch="/")'''

# set x,y_axis label
plt.xlabel("箱子重量(kg)")
plt.ylabel("销售数量(个)")

plt.show()