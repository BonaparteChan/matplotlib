# 等高线图的颜色使用模式
# 函数 contour() 是用来绘制等高线图的
# 等高线图是三维图形 z 轴 的投影图
# 投影图需要用等值线刻画三维图形 z 轴的趋势变化，等值线是将 z 轴上的函数值相等的点连接起来的
# 函数值是通过二元函数计算得出的

# 导入绘图模块、导入绘图模块的可视化实例，导入数学模块
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

s = np.linspace(-0.5, 0.5, 1000)

x, y = np.meshgrid(s, s)

fig, ax = plt.subplots(1, 1)

z = x ** 2 + y ** 2 + np.power(x ** 2 + y ** 2, 2)

# a contourSet object returned by contour
cs = plt.contour(x, y, z, cmap=mpl.cm.hot)

# add label to contour 给等高线图增加标签
plt.clabel(cs, fmt="%3.2f")

# mappable is contourSet object
plt.colorbar(cs)

plt.show()