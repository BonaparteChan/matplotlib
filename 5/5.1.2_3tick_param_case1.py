# 要想图表有更多的调整和定制化展示，应该使用 matplotlib 的面向对象的操作方法
# 模块 pyplot 中的刻度样式的设置是通过函数 tick_parmas() 实现的

# 通过调整 x 轴的刻度标签和 y 轴的刻度线的样式，讲解面向对象的操作方法

# 导入可视化模块
import matplotlib.pyplot as plt
# 导入数学模块
import numpy as np

# 设置画布
fig = plt.figure(facecolor=(1.0, 1.0, 0.9412))
ax = fig.add_axes([0.1, 0.4, 0.5, 0.5])  # 四分列表

# 调用实例方法 get_ticklabels() 获得 Text 实例列表
for ticklabel in ax.xaxis.get_ticklabels():
    ticklabel.set_color("slateblue")
    ticklabel.set_fontsize(10)
    ticklabel.set_rotation(30)

for tickline in ax.yaxis.get_ticklines():
    tickline.set_color("lightgreen")
    tickline.set_markersize(10)
    tickline.set_markeredgewidth(1)

plt.show()