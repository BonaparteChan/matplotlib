# 结合多数据并列柱状图和误差棒图，历史数据不同时间不同数据不同属性的变化(ex:不同年份不同芒果园区不同的收割量)

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
# 导入模块

mpl.rcParams["font.sans-serif"] = ["LiSu"]
mpl.rcParams["axes.unicode_minus"] = False
# 设置编码格式，utf-8

# set some simple data 设置一些简单的数据
x = np.arange(5)
y1 = [100, 68, 79, 91, 82]
y2 = [120, 75, 70, 78, 85]
std_err1 = [7, 2, 6, 10, 5]
std_err2 = [5, 1, 4, 8, 9]

error_attri = dict(elinewidth=2, ecolor="black", capsize=3)
# 误差棒的属性和属性值
bar_width = 0.4
tick_label = ["园区 1", "园区 2", "园区 3", "园区 4", "园区 5"]

# create bar with errorbar 在误差棒图创建柱状
plt.bar(x, y1, bar_width,
        color="#87cee8",
        align="center",
        yerr=std_err1,
        error_kw=error_attri,  # 属性和属性值
        label="2021 年")

plt.bar(x+bar_width, y2, bar_width,
        color="#cd5c5c",
        align="center",
        yerr=std_err2,
        error_kw=error_attri,  # 属性和属性值
        label="2022 年")

# set x,y_axis label 设置 x,y 轴层
plt.xlabel("芒果种植区")
plt.ylabel("收割量")

# set xaxis tick_label
plt.xticks(x+bar_width/2, tick_label)

# set title of axis 设置标题
plt.title("不同年份的不同芒果种植区的单次收割量")

# set yaxis grid
plt.grid(True, axis="y", ls=":", color="gray", alpha=.2)

plt.show()