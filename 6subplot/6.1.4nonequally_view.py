# 多次调用子区函数 subplot 实现非等分画布的绘图任务

# 导入可视化模块和数学模块
import matplotlib.pyplot as plt
import numpy as np

# 设置基础画布
fig = plt.figure()

# 设置数据
x = np.linspace(0.0, 2 * np.pi)
y = np.cos(x) * np.sin(x)

ax1 = fig.add_subplot(121)
ax1.margins(0.03)  # 设置数据范围的空白区域
ax1.plot(x, y, ls="-", lw=2, color="b")

ax2 = fig.add_subplot(222)
ax2.margins(0.7, 0.7)
# 实例方法 margins(m) m 倍的数据区间添加到原来数据区间的两端
# 数据范围的空白区域的调整类型既包括 x 轴也包括 y 轴的数据区间
# 参考值 m 的取值范围是大于 -0.5 的任意浮点数
ax2.plot(x, y, ls="--", lw=2, color="r")

ax3 = fig.add_subplot(224)
ax3.margins(x=0.1, y=0.3)
ax3.plot(x, y, ls="-.", lw=2, color="g")

plt.show()