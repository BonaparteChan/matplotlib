# case3 极区图的颜色使用模式

# 导入绘图模块、可视化实例、数学模块
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

barslice = 12
theta = np.linspace(0.0, 2 * np.pi, barslice, endpoint=False)
radii = 30 * np.random.rand(barslice)
width = np.pi/ 4 *np.random.rand(barslice)

fig = plt.figure()
ax = fig.add_subplot(111, polar=True)

bars = ax.bar(theta, radii, width=width, bottom=0.0)

for r, bar in zip(radii, bars):
    bar.set_facecolor(mpl.cm.Accent(r / 30.))
    bar.set_alpha(r / 30.)

plt.show()