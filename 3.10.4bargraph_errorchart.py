# 结合条形图和误差棒图，在反映数据定性数据的分布特征，分布的波动特征

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
# 导入模块

mpl.rcParams["font.sans-serif"] = ["LiSu"]
mpl.rcParams["axes.unicode_minus"] = False
# 设置编码格式，utf-8

# set some simple data 设置一些简单的数据
x = np.arange(5)
y = [1200, 2400, 1800, 2200, 1600]
std_err = [150, 100, 180, 130, 80]

bar_width = 0.6
colors = ["#e41a1c", "#377eb8", "#4daf4a", "#984ea3", "#ff7f00"]

# create horizontal bar 创建条形图
plt.barh(x, y, bar_width, color=colors, align="center",  # 数据，条形宽度，颜色，布局方式
         xerr=std_err,  # 关键字参数 xerr 单一数值的非对称误差范围
         tick_label=["家庭", "小说", "心理", "科技", "儿童"])

# set x,y_axis label 设置 x,y 轴层
plt.xlabel("订购数量")
plt.ylabel("图书种类")

# set title of axis 设置标题
plt.title("大型图书展销会的不同图书种类采购情况")

# set yaxis grid
plt.grid(True, axis="x", ls=":", color="gray", alpha=.2)
# axis 网络线 x 轴

plt.show()