'''
阶梯图，如同山间的阶梯时而上升，时而下降，很像折线图
反映数据趋势变化或周期规律
在时间序列数据可视化任务时，凸显时序数据的波动规律和周期
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

x = np.linspace(1, 10, 10)
y = np.sin(x)
# set simple data 设置简单数据

plt.step(x, y, color="#8dd3c7", where="pre", lw=2)
# where 的默认参数值是“pre”x 轴上的相邻数据点的取值是按照【左开右闭】区间进行数据点选取的
# plt.step(x, y, color="#8dd3c7", where="post", lw=2)
# where 的可选参数值是“post”x 轴上的相邻数据点的取值是按照【左闭右开】区间进行数据点选取的

# x, y 轴的最大值和最小值
plt.xlim(0, 11)
plt.xticks(np.arange(1, 11, 1))
plt.ylim(-1.2, 1.2)

# set yaxis grid
# plt.grid(lw=1, ls="-", color="gray")
# 加了网页先后，看不出 阶梯的变化


plt.show()