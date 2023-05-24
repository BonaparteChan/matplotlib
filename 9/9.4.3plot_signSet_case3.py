import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 500)
y = np.sin(x)

# 设置画布和子区

# plt.plot(x, y, "ro:", linewidth=1, markersize=2, label="example1")

# 设置坐标轴、刻度、轴脊格式？？
plt.plot(x, y, "ro:", linestyle=":", linewidth=1, marker="o", markersize=2, color="r", label="example2")

plt.show()