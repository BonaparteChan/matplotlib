'''
直方图，描述定量数据，柱体之间没有空隙
柱状图，描述定性数据，柱体之间存在空隙
'''
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
# 导入模块

mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False
# 设置编码格式，不设置就没法写中文

# set test scores
scoresT1 = np.random.randint(0, 100, 100)
scoresT2 = np.random.randint(0, 100, 100)
# 打字的时候，会覆盖后面的文字，按 insert 键进行取消

# some simple data 设置简单数据
x = [scoresT1, scoresT2]
colors = ["#8dd3c7", "#bebada"]
labels = ["班级 A", "班级 B"]

# plot histogram
bins = range(0, 101, 10)

plt.hist(x, bins=bins, color=colors, histtype="bar", rwidth=1.0, stacked=True, label=labels)
# 堆积柱状图
'''
连续性数据输入值 x
柱体个数或柱体边缘范围 bins
color 柱体颜色
histtype 柱体类型
rwidth 柱体宽度 取值范围在 0.0~0.1 之间
'''

# plt.hist(x, bins=bins, color=colors, histtype="bar", rwidth=1.0, stacked=False, label=labels)
# stacked=False 直方图，并排放置的直方图

# set x,y_axis label，设置图例
plt.xlabel("测试成绩（分）")
plt.ylabel("学生人数")

# set title 设置标题
plt.title("不同班级的测试成绩的直方图")

plt.legend(loc="upper left")

# set yaxis grid
# plt.grid(lw=1, ls="-", color="gray")

plt.show()