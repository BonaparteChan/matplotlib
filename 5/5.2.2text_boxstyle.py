# 改变文本框的展示样式

# 导入可视化模块
import matplotlib.pyplot as plt
# 导入数学模块
import numpy as np

# 设置数据
x = np.linspace(0.0, 10, 40)
y = np.random.randn(40)

plt.plot(x, y, ls="-", lw=2,
         marker="o", ms=20, mfc="orange", mec="green", alpha=0.6)

plt.grid(ls=":", color="gray", alpha=0.5)

plt.text(6, 0, "Matplotlib", size=30, rotation=30.,
         bbox=dict(boxstyle="round", ec="#8968cd", fc="#ffe1ff"))  # round 圆角矩形

# plt.text(6, 0, "Matplotlib", size=30, rotation=30., bbox=dict(boxstyle="square", ec="#8968cd", fc="#ffe1ff"))
# square 直角

plt.show()