# 借助 subplots() 创建多种统计图形的组合展示的可视化模式

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

# 画布基本配置
fig, ax = plt.subplots(2, 3)

# subplot(231) 2 行 3 列第一个图形
colors = ["#8dd3c7", "#ffffb3", "#bebada"]
ax[0, 0].bar([1, 2, 3 ], [0.6, .2, .8], color=colors, width=.5, hatch="///", align="center")  # 柱状图
# hatch 横纹样式及密集程度
ax[0, 0].errorbar([1, 2, 3], [0.6, .2, .8], yerr=0.1, capsize=0, ecolor="#377eb8", fmt="o:")  # 误差棒图
# capsize 误差棒边界横杠的大小；fmt 标准样式
ax[0, 0].set_ylim(0, 1.0)

# subplot(232) 2 行 3 列第二个图形
ax[0, 1].errorbar([1, 2, 3], [20, 30, 36], xerr=2, ecolor="#4daf4a", elinewidth=2, fmt="s", label="ETN")
ax[0, 1].legend(loc=3, fancybox=True, shadow=True, fontsize=10, borderaxespad=.4)  # 图例样式设置
ax[0, 1].set_xlim(-2, 6)
ax[0, 1].set_ylim(10, 40)
ax[0, 1].grid(ls=":", lw=1, color="grey", alpha=.5)

# subplot(233) 2 行 3 列第三个图形
x3 = np.arange(1, 10, .5)
y3 = np.cos(x3)
# 设置简单数据，余弦函数
ax[0, 2].stem(x3, y3, basefmt="r-", linefmt="b-", markerfmt="bo", label="life signal")  # 棉棒图
# linefmt 棉棒样式；markfmt 末端样式；basefmt 指定基线样式
ax[0, 2].legend(loc=2, frameon=False, borderpad=0.0, fontsize=8, borderaxespad=.6)  # 图例样式设置
ax[0, 2].set_xlim(0, 11)
ax[0, 2].set_ylim(-1.1, 1.1)

# subplot(234) 2 行 3 列第四个图形
x4 = np.linspace(0, 2 * np.pi, 500)
x4_1 = np.linspace(1, 2 * np.pi, 1000)
y4 = np.cos(x4) * np.exp(-x4)
y4_1 = np.sin(2 * x4_1)
# 设置简单的数据
line1, line2, = ax[1, 0].plot(x4, y4, "k--", x4_1, y4_1, "r-", lw=2)
ax[1, 0].legend((line1, line2), ("energy", "patience"),
                loc="upper center", fontsize=8, ncol=2,
                framealpha=0.3, mode="expand",
                columnspacing=2, borderpad=0.1)
# 设置图例样式
ax[1, 0].set_xlim(-2, 2)
ax[1, 0].set_ylim(0, 2 * np.pi)

# subplot(235) 2 行 3 列第五个图形
x5 = np.random.rand(100)
ax[1, 1].boxplot(x5, vert=False, showmeans=True, meanprops=dict(color="g"))  # 箱线图
# vert 不显示离群值，箱线图的水平放置
ax[1, 1].set_xlim(-1.1, 1.1)
ax[1, 1].set_xticks([])
ax[1, 1].set_ylabel("Micro SD Card")
ax[1, 1].text(-1.0, 1.2, "net weight",
              fontsize=20, style="italic",
              weight="black", family="monospace")
# 水印设置

# subplot(236) 2 行 3 列第六个图形
mu = 0.0
sigma = 1.0
# 设置数据
x6 = np.random.randn(10000)
n, bins, patches = ax[1, 2].hist(x6, bins=30, histtype="stepfilled",
                                 cumulative=True, density=True,
                                 color="cornflowerblue", label="Test")
y = (1 / (np.sqrt(2 * np.pi)) * np.exp(-0.5 * (1 / (bins - mu)) ** 2))
y = y.cumsum()
y /= y[-1]

ax[1, 2].plot(bins, y, "r--", linewidth=1.5, label="Theory")
ax[1, 2].set_ylim(0.0, 1.1)
ax[1, 2].grid(ls=":", lw=1, color="gray", alpha=.5)
ax[1, 2].legend(loc="upper left", fontsize=8, shadow=True,
                fancybox=True, framealpha=.8)

# adjust subplot() layout
plt.subplots_adjust()

plt.show()


