import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
# 导入模块

mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False
# 设置编码格式，不设置就没法写中文

apple = np.linspace(0.1, .6, 6)
box =np.exp(apple)

# 绘制 x, y 轴方向的误差范围
plt.errorbar(apple, box, fmt="bo:", yerr=.2, xerr=0.02)
# fmt 格式样式，yerr:y 轴方向的数据点的误差计算方法，xerr:x 轴方向的数据点的误差计算方法

plt.xlim(0, .7)
# x 轴上的最大值和最小值
plt.show()