# 共享单一绘图区域的坐标轴，多图放在同一个绘图区域
# 借助共享坐标轴的方法实现一个绘图区域绘制多幅图形的目的

# 导入可视化和数学模块
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# 声明中文字体和编码格式
mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

# 设置画布和数据
fig, ax1 = plt.subplots()
t = np.arange(0.05, 10.0, 0.01)
s1 = np.exp(t)
ax1.plot(t, s1, c="b", ls="-")

# set x-axis label
ax1.set_xlabel("x 坐标轴")

# make the y-axis label，ticks and tick labels match the line colors
ax1.set_ylabel("以 e 为底指数函数", color="b")
ax1.tick_params("y", colors="b")

# ax1 shares x-axis with ax2
ax2 = ax1.twinx()  # 满足 x 轴的可视化需求
# axis.twiny() 实例方法满足 y 轴的可视化需求

s2 = np.cos(t ** 2)
ax2.plot(t, s2, c="r", ls=":")

# make the y-axis label，ticks and tick labels match the line colors
ax2.set_ylabel("余弦函数", color="r")
ax2.tick_params("y", colors="r")

plt.show()