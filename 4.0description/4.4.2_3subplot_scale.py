# subplot 绘制几何形状相同的网格区域
# 将画布分成若干个子画布

# 4.2.3 逆序设置坐标轴刻度标签
# 导入可视化模块
import matplotlib as mpl
import matplotlib.pyplot as plt
# 导入数学模块
import numpy as np

# 设置编码格式、字体
mpl.rcParams["font.sans-serif"] = ["FangSong"]
mpl.rcParams["axes.unicode_minus"] = False

# set some simple data 设置一些简单的数据
time = np.arange(1, 11, .5)
machinePower = np.power(time, 2) + 0.7

# 折线图
plt.plot(time, machinePower,
         linestyle="-",
         linewidth=2,
         color="r")

# 设置 x 轴的范围
plt.xlim(10, 1)  # 将 xlim(min, max) 的参数调换顺序实现，xlim(max, min)

# 设置 x，y 轴的文字
plt.xlabel("使用年限")
plt.ylabel("机器功率")

# 设置标题
plt.title("机器损耗曲线")

# 网格曲线属性
plt.grid(ls="-", lw=1, color="gray", alpha=0.5)

plt.show()