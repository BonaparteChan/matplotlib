# method1 使用保存按钮进行存储图形,生成的画布上，最后一个按钮就是保存按钮
# -*- coding:utf-8 -*-

import matplotlib as mpl  # 绘图模块
import matplotlib.pyplot as plt  # 导入绘图模块子类可视化
import numpy as np  # 导入可视化模块

mpl.rcParams["font.sans-serif"]=["SimHei"]  # 字体:细黑
mpl.rcParams["axes.unicode_minus"]=False  # 编码格式 utf-8
# 编码格式、设置字体

# 设置画布和子区
fig, ax1 = plt.subplots()
t = np.arange(0.05, 10.0, 0.01)  # 数字区间
s1 = np.exp(t)
ax1.plot(t, s1, c="b", ls="--")

# set x-axis label
ax1.set_xlabel("x 坐标轴")

# make the y-axis label，ticks and tick labels match the line color
ax1.set_ylabel("以 e 为底的指数函数", color="b")
ax1.tick_params("y", colors="b")

# ax1 shares x-axis with ax2 共享坐标轴 x
ax2 = ax1.twinx()

s2 = np.cos(t ** 2)
ax2.plot(t, s2, c="r", ls=":")

# make the y-axis label，ticks and tick labels match the line color
ax2.set_ylabel("余弦函数", color="r")
ax2.tick_params("y", colors="r")

# method2 通过执行语句进行保存
plt.savefig("I:\\Dropbox\\figure_demo.png")

plt.show()