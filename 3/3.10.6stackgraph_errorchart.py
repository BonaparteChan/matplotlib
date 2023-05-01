# 结合堆积柱状图和误差棒图，数据属性的变化和差异

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
# 导入模块

mpl.rcParams["font.sans-serif"] = ["LiSu"]
mpl.rcParams["axes.unicode_minus"] = False
# 设置编码格式，utf-8

# set some simple data 设置一些简单的数据
x = np.arange(5)
y1 = [1200, 2400, 1800, 2200, 1600]
y2 = [1050, 2100, 1300, 1600, 1340]
std_err1 = [150, 100, 180, 130, 80]
std_err2 = [120, 110, 170, 150, 120]

bar_width = 0.6
tick_label = ["家庭", "小说", "心理", "科技", "儿童"]
error_attribute = dict(ecolor="black", elinewidth=2, capsize=0)

# create horizontal bar 创建条形图
plt.bar(x, y1,
        bar_width,
        color="#6495ed",
        align="center",
        yerr=std_err1,
        label="海南",
        error_kw=error_attribute)

plt.bar(x, y2,
        bar_width,
        bottom=y1,  # 堆在 y1 上面
        color="#ffa500",
        align="center",
        yerr=std_err2,
        label="台湾",
        error_kw=error_attribute)

# set x,y_axis label 设置 x,y 轴层
plt.xlabel("订购数量")
plt.ylabel("图书种类")

# set title of axis 设置标题
plt.title("不同地区大型图书展销会的不同图书种类采购情况")

# set yaxis grid
plt.grid(True, axis="y", ls=":", color="gray", alpha=.2)
# axis 网络线 x 轴

plt.xticks(x, tick_label)

plt.legend()
# 图例

plt.show()