# 没有文本的指示箭头作为趋势线来反映折线的趋势变化和周期规律
# 实现有指示箭头作为趋势线的可视化需求

# 导入可视化模块
import matplotlib.pyplot as plt
import matplotlib as mpl
# 导入数学模块
import numpy as np

# 设置编码格式、字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

# 设置数据
x = np.linspace(0, 10, 2000)
y = np.sin(x)  # 正弦曲线

# 设置画布
fig = plt.figure()
ax = fig.add_subplot(111)

# 画曲线
ax.plot(x, y, ls="-", lw=2)

# y 轴最小值和最大值
ax.set_ylim(-1.5, 1.5)

arrowprops = dict(arrowstyle="-|>", color="r")

ax.annotate("红色",
            (3 * np.pi/2, np.sin(3 * np.pi/2) + 0.05),
            xytext=(np.pi/2, np.sin(np.pi/2) + 0.05),
            color="r",
            arrowprops=arrowprops)

ax.arrow(0.0, -0.4, np.pi/2, 1.2,
         head_width=0.05, head_length=0.1,
         fc="g", ec="g")

ax.grid(ls=":", color="gray", alpha=0.6)

plt.show()