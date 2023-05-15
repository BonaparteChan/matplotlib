
# 导入可视化模块和数学模块

import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

# 设置编码格式和字体，需要研究一下，怎么用 editconfig 来统一配置，而不是每次都来声明
'''
按下 Alt+Shift+F10，然后按 0 来显示 Edit Configuration 对话框，或者从弹出窗口中选择配置并按 F4。
在 Run/Debug Configurations 对话框中，从 Python 运行/调试配置列表中选择目标配置。
在 Parameters 字段中点击 + 并从可用宏列表中选择一个宏。
'''
mpl.rcParams["font.sans-serif"] = ["LiSu"]
mpl.rcParams["axes.unicode_minus"] = False

mu = 0.0
sigma = 1.0
# 设置数据
x6 = np.random.randn(10000)
n, bins, patches = plt.hist(x6, bins=30, histtype="stepfilled",
                            cumulative=True, density=True,  # 累积的阶梯填充型直方图 密度数值标识直方图高度
                            color="cornflowerblue", label="Test")
# 密度/频度 的关键词要换成 density
y = (1 / (np.sqrt(2 * np.pi)) * np.exp(-0.5 * (1 / (bins - mu)) ** 2))
y = y.cumsum()
y /= y[-1]

plt.plot(bins, y, "r--", linewidth=1.5, label="Theory")
plt.ylim(0.0, 1.1)
plt.grid(ls=":", lw=1, color="gray", alpha=.5)
plt.legend(loc="upper left", fontsize=8, shadow=True, fancybox=True, framealpha=.8)

plt.show()