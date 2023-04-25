import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
# 导入模块

mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False
# 设置编码格式，不设置就没法写中文

barSlices = 12
theta = np.linspace(0.0, 2*np.pi, barSlices, endpoint=False)
# 每个标记所在射线与极径的夹角
r = 30*np.random.rand(barSlices)
# 每个标记到原点的距离

# 在极坐标轴上绘制折线图
plt.polar(theta, r, color="chartreuse", linewidth=2, marker="*", mfc="b", ms=10)
plt.show()