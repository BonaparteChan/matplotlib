# 通过调整函数 subplots() 中的参数 sharey( 或参数 sharex) 的不同取值情况，从而实现共享不同子区的绘图区域的坐标轴的需求
'''
"all" 等同于 "True"，"none" 等同于 "False";
"row"
"col"
6.3.2 第 28 行代码
'''

# 导入可视化和数学模块
import matplotlib.pyplot as plt
import numpy as np

# create sample data 创建简单数据
x1 = np.linspace(0, 2 * np.pi, 400)
y1 = np.cos(x1 ** 2)

x2 = np.linspace(0.01, 10, 100)
y2 = np.sin(x2)

x3 = np.random.rand(100)
y3 = np.linspace(0, 3, 100)

x4 = np.arange(0, 6, 0.5)
y4 = np.power(x4, 3)

# fig, ax = plt.subplots(2, 2)  # 相当于 sharex="none"，sharex=False
# fig, ax = plt.subplots(2, 2, sharex=True)
# fig, ax = plt.subplots(2, 2, sharex="all")
fig, ax = plt.subplots(2, 2, sharex="row")
# 将子区中的每一列的图形的 y 轴取值范围实现共享，而且选择每列中的图形 y 轴取值范围上线最大的那个取值范围作为共享范围
# fig, ax = plt.subplots(2, 2, sharex="col")
# 将子区中的每一列的图形的 x 轴取值范围实现共享，而且选择每列中的图形 x 轴取值范围上线最大的那个取值范围作为共享范围

# set chart of each subplot
ax1 = ax[0, 0]
ax1.plot(x1, y1)

ax2 = ax[0, 1]
ax2.plot(x2, y2)

ax3 = ax[1, 0]
ax3.scatter(x3, y3)

ax4 = ax[1, 1]
ax4.scatter(x4, y4)

# show  figure and subplot(s)
plt.show()