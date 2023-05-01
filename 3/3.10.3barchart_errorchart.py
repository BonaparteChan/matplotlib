# 结合柱状图和误差棒图，在反映数据测量误差方面的应用领域拓展

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
# 导入模块

mpl.rcParams["font.sans-serif"] = ["LiSu"]
mpl.rcParams["axes.unicode_minus"] = False
# 设置编码格式，utf-8

# set some simple data 设置一些简单的数据
x = np.arange(5)
y = [100, 68, 79, 91, 82]
std_err = [7, 2, 6, 10, 5]

error_attri = dict(elinewidth=2, ecolor="black", capsize=3)
# 误差棒的属性和属性值均为该关键词参数 error_attribute 实现控制，第 24 行代码

# create bar with errorbar 在误差棒图创建柱状
plt.bar(x, y,
        color="c", width=.6,
        align="center", yerr=std_err,  # 关键要点 yerr 单一数值的非对称形式误差范围。align 布局方式 居中
        error_kw=error_attri,  # 关键词参数来自第 17 行代码
        tick_label=["园区 1", "园区 2", "园区 3", "园区 4", "园区 5"])

# set x,y_axis label 设置 x,y 轴层
plt.xlabel("芒果种植区")
plt.ylabel("收割量")

# set title of axis 设置标题
plt.title("不同芒果种植区的单次收割量")

# set yaxis grid
plt.grid(True, axis="y", ls=":", color="gray", alpha=.2)

plt.show()