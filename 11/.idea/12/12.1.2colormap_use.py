'''
颜色映射表的使用
method1 使用关键字参数 key variable
method2 使用 matplotlib.pyplot.set_cmap() 函数
全部内置的颜色映射表都可通过增加后缀 "_r" 的方式进行反转，"jet_r" 就是 "jet" 的反向循环颜色映射表
最常用的颜色映射表 autumn(秋)、bone、cool、copper、flag、gray、hot、hsv、jet、pink、prism、spring(春)、summer(夏)、winter(冬)
'''

import matplotlib.pyplot as plt
import numpy as np
# 导入绘图可视化模块和数学模块

# ColorBrewer Diverging：RdYlBu
hexHtml = ["#d73027", "#f45d43", "#fdae61",
           "#fee090", "#ffffbf", "#e0f3f8",
           "#abd9e9", "#74add1", "#4575b4"]
# data class 数据种类是 9 种
sample = 10000
fig, ax = plt.subplots(1, 1)

for j in range(len(hexHtml)):
    y = np.random.normal(0, 0.1, size=sample).cumsum()
    x = np.arange(sample)
    ax.scatter(x, y,
               label=str(j),
               linewidth=0.2,
               edgecolors="gray",
               facecolor=hexHtml[j])

ax.legend()

plt.show()