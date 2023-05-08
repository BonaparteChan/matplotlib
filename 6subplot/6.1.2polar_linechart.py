import matplotlib.pyplot as plt
import numpy as np

# 设置数据
radii = np.linspace(0, 1, 100)
theta = 2 * np.pi * radii

# 画布和极坐标
ax = plt.subplot(111, polar=True)  # 极坐标轴

# 画线
ax.plot(theta, radii, color="r", linestyle="-.", linewidth=2)  # 颜色、样式、线宽

plt.show()