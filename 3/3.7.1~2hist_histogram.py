'''
直方图，定量数据的可视化场景，连续性数据的可视化展示
柱状图，定性数据的可视化场景
'''
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
# 导入模块

mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False
# 设置编码格式，不设置就没法写中文

# set test scores
scoresT = np.random.randint(0, 100, 100)

# some simple data 设置简单数据
x = scoresT

# plot histogram
bins = range(1, 101, 10)

plt.hist(x, bins=bins, color="#377eb8", histtype="bar", rwidth=1.0)
'''
连续性数据输入值 x
柱体个数或柱体边缘范围 bins
color 柱体颜色
histtype 柱体类型
rwidth 柱体宽度 取值范围在 0.0~0.1 之间
'''

# set x,y_axis label，设置图例
plt.xlabel("测试成绩")
plt.ylabel("学生人数")

# set yaxis grid
plt.grid(lw=1, ls="-", color="gray")

plt.show()