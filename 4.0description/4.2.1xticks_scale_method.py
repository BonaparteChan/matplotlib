# 导入可视化模块
import matplotlib.pyplot as plt
# 导入数学模块
import numpy as np

# set some simple data 设置简单的数据
x = np.linspace(-2 * np.pi, 2 * np.pi, 200)
y = np.sin(x)  # 正弦曲线

# set subplot 设置子区函数 下一节讲解
plt.subplot(211)  # 两行一列的第一个图形

# set plot figure
plt.plot(x, y)

plt.subplot(212)  # 两行一列的第二个图形

# set x limit 设置 x 轴的极限，改变 x 轴的刻度范围，让绘图区域变得更加紧凑
plt.xlim(-2 * np.pi, 2 * np.pi)

# set tick 调整改变刻度标签，使得图形内容更便于观察和理解
plt.xticks([-2 * np.pi, -3 * np.pi / 2, -1 * np.pi, -1 * np.pi / 2, 0, (np.pi) / 2, np.pi, 3 * np.pi / 2, 2 * np.pi],
           [r"$-2\pi$", r"$-3\pi/2$", r"$-\pi$", r"$-\pi/2$", r"$0$", r"$\pi/2$", r"$\pi$", r"$3\pi/2$", r"$2\pi$"])

# plt.figure()
plt.plot(x, y)

plt.show()