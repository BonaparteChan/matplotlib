# 圆角线框有弧度指示的注解

# 导入可视化模块
import matplotlib.pyplot as plt
# 导入数学模块
import numpy as np

# 设置数据
x = np.linspace(0, 10, 2000)
y = np.sin(x) * np.cos(x)

# 设置画布
fig = plt.figure()
ax = fig.add_subplot(111)

# 画线
ax.plot(x, y, ls="-", lw=2)

# define 定义矩形，箭头
bbox = dict(boxstyle="round", fc="#7ec0ee", ec="#9b30ff")
arrowprops = dict(arrowstyle="-|>",
                  connectionstyle="angle,angleA=0,angleB=90,rad=10",  # 键值对来完成有弧度的指示线
                  color="r")

ax.annotate("singel point",
            (5, np.sin(5) * np.cos(5)),
            xytext=(2, np.sin(2) * np.cos(2)),
            fontsize=12, color="r",
            bbox=bbox, arrowprops=arrowprops)

ax.grid(ls=":", color="gray", alpha=0.6)

plt.show()