# 散点图的颜色使用模式

import matplotlib.pyplot as plt  # 导入可视化模块
import matplotlib as mpl  # 导入绘图模块
import numpy as np  # 导入数学模块

# simple data 设置一些简单数据
a = np.random.randn(100)
b = np.random.randn(100)
exponent = 2

# 一行三列第一个图形
plt.subplot(131)
# colormap:jet 颜色映射模式 jet
plt.scatter(a, b,
            np.sqrt(np.power(a, exponent)+ np.power(b, exponent))* 100,
            c=np.random.rand(100), cmap=mpl.cm.jet,
            marker="o", zorder=1)  # 标记样式，zorder 指定绘图顺序

# 一行三列第二个图形
plt.subplot(132)
plt.scatter(a, b, marker="o", zorder=10)  # 标记样式，zorder 指定绘图顺序

# 一行三列第三个图形
plt.subplot(133)
# colormap:BuPu 颜色映射模式 RuPu
plt.scatter(a, b, 50,
            c=np.random.rand(100), cmap=mpl.cm.BuPu,
            marker="+", zorder=100)  # 标记样式，zorder 指定绘图顺序

plt.show()