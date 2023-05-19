# 共享个别子区绘图区域的坐标轴
# 将某个子区的坐标轴范围作为共享坐标轴

# 导入可视化模块和数学模块
import matplotlib.pyplot as plt
import numpy as np

# create simple data 创建简单数据
x1 = np.linspace(0, 2 * np.pi, 400)
y1 = np.cos(x1 ** 2)

x2 = np.linspace(0.01, 10, 100)
y2 = np.sin(x2)

x3 = np.random.rand(100)
y3 = np.linspace(0, 3, 100)

x4 = np.arange(0, 6, 0.5)
y4 = np.power(x4, 3)

# set(2, 2) subplot
fig, ax = plt.subplots(2, 2)

# set chart of each subplot
ax1 = plt.subplot(221)
ax1.plot(x1, y1)

ax2 = plt.subplot(222)
ax2.plot(x2, y2)

ax3 = plt.subplot(223, sharey=ax2)  # 第二个图和第三个图共享 y 轴
ax3.scatter(x3, y3)
plt.autoscale(enable=True, axis="both", tight=True)
'''
函数 autoscale() 进行自适应调整
enable:进行坐标轴范围的自适应调整
axis：使 x, y 轴都进行适应调整
tight：让坐标轴的范围调整到数据范围上
'''

# ax4 = plt.subplot(224, sharex=ax1)  # 第一个图和第四个图共享 x 轴
ax4 = plt.subplot(224)
ax4.scatter(x4, y4)

plt.show()