# 函数 subplots() 的返回值是一个 (fig, ax) 的元组（tuple）
# fig 是 figure 示例，ax 可以是一个对象，有多个子区，ax 就是一个 axs 的对象数组

# 案例 1 创建一张画布和一个子区的绘图模式

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
mpl.rcParams["font.sans-serif"] = ["FangSong"]
mpl.rcParams["axes.unicode_minus"] = False

font_style = dict(fontsize=18, weight="black")

# first create sample data 首先创建一个简单的数据
x = np.linspace(0, 2 * np.pi, 500)
y = np.sin(x) * np.cos(x)

# create just a figure and only one subplot 创建一个画布一个子区
fig, ax = plt.subplots(1, 1, subplot_kw=dict(facecolor="cornflowerblue"))

ax.plot(x, y, "k--", lw=2)
ax.set_xlabel("时间(秒)", **font_style)
ax.set_ylabel("振幅", **font_style)
ax.set_title("简单折线图", **font_style)

ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-0.65, 0.65)

ax.grid(ls=":", lw=1, color="gray", alpha=.8)

plt.show()