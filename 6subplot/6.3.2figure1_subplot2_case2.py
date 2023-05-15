# 函数 subplots() 的返回值是一个 (fig, ax) 的元组（tuple）
# fig 是 figure 示例，ax 可以是一个对象，有多个子区，ax 就是一个 axs 的对象数组

# 案例 1 创建一张画布和一个 2 子区的绘图模式

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import numpy as py
# 导入可视化和数学模块

# 设置编码格式和字体，需要研究一下，怎么用 editconfig 来统一配置，而不是每次都来声明
'''
按下 Alt+Shift+F10，然后按 0 来显示 Edit Configuration 对话框，或者从弹出窗口中选择配置并按 F4。
在 Run/Debug Configurations 对话框中，从 Python 运行/调试配置列表中选择目标配置。
在 Parameters 字段中点击 + 并从可用宏列表中选择一个宏。
'''
mpl.rcParams["font.sans-serif"] = ["LiSu"]
mpl.rcParams["axes.unicode_minus"] = False

font_style = dict(fontsize=18, weight="black")

# first create sample data 首先创建一个简单的数据
x = np.linspace(0, 2 * np.pi, 500)
y = np.sin(x) * np.exp(-x)

# create just a figure and only one subplot 创建一个画布一个子区
fig, ax = plt.subplots(1, 2, sharey=True)  # 横排；sharex-> 竖排
# fig, ax = plt.subplots(2, 1, sharex=True)  # 横排；sharex-> 竖排

# 使用 subplots_adjust(*agrs, *kwargs) 对空间进行控制
# left、right、bottom、top、hspace、wspace 均有默认值
# 前四个调整子区距离画布的距离，hspce 控制子区之间的高度，wspace 控制子区之间的宽度

# subplot(121)
ax1 = ax[0]
ax1.plot(x, y, "k--", lw=2)
ax1.set_title("折线图")
ax1.grid(ls=":", lw=1, color="gray", alpha=.8)

# subplot(122)
ax2 = ax[1]
ax2.scatter(x, y, s=10, c="skyblue", marker="o")
ax2.set_title("散点图")

plt.suptitle("创建一张画布两个子区的绘图模式", **font_style)

plt.show()