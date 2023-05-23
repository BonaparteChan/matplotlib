# 移动坐标轴位置
# 移动坐标轴载体(轴脊)的位置，进而设置刻度线的位置，从而完成移动坐标轴的任务

# 导入可视化模块和数学模块
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# 设置编码格式和字体
# 设置编码格式和字体，需要研究一下，怎么用 editconfig 来统一配置，而不是每次都来声明
'''
按下 Alt+Shift+F10，然后按 0 来显示 Edit Configuration 对话框，或者从弹出窗口中选择配置并按 F4。
在 Run/Debug Configurations 对话框中，从 Python 运行/调试配置列表中选择目标配置。
在 Parameters 字段中点击 + 并从可用宏列表中选择一个宏。
'''
mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

# set some simple data 设置简单数据
x = np.linspace(-2 * np.pi, 2 * np.pi, 200)
y = np.sin(x)
y1 = np.cos(x)

ax = plt.subplot(111)

ax.plot(x, y, ls="-", lw=2, label="$\sin(x)$")
ax.plot(x, y1, ls="-", lw=2, label="$\cos(x)$")

ax.legend(loc="lower left")  # 图例位置，底部左边

plt.title("$\sin(x)$" + "和" + "$\cos(x)$" + "函数")
# set xlim
ax.set_xlim(-2 * np.pi, 2 * np.pi)

# set ticks 设置刻度
plt.xticks([-2 * np.pi, -3 * np.pi/2, -1 * np.pi, -1 * np.pi/2, 0, (np.pi)/2, np.pi, 3 * np.pi/2, 2 * np.pi],
           ["$-2 * np.pi$", "$-3 * np.pi/2$", "$-\pi$", "$-1\pi/2$", "$0$", "$\pi)/2$", "$\pi$", "$3\pi/2$", "$2\pi$"])

# 不显示右边和顶边的坐标轴
ax.spines["right"].set_color("none")
ax.spines["top"].set_color("none")

# 关键代码，将坐标轴移动到 0 的位置，中间
ax.spines["bottom"].set_position(("data", 0))  # 将底部轴脊移动到数据为 0 的位置
ax.spines["left"].set_position(("data", 0))  # 将左边轴脊移动到数据为 0 的位置

ax.xaxis.set_ticks_position("bottom")
ax.yaxis.set_ticks_position("left")

plt.show()