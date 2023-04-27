# 案例 2，case 2 水平方向的无离群值箱线图
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
# 导入模块

mpl.rcParams["font.sans-serif"] = ["FangSong"]
mpl.rcParams["axes.unicode_minus"] = False
# 设置编码格式，utf-8

x = np.random.randn(1000)

plt.boxplot(x, vert=False, showfliers=False)
# showfilers 为 false 不显示离群值

plt.xlabel("随机数值")
plt.yticks([1], ["随机数生成器 alphaRM"], rotation=90)
plt.title("随机数生成器抗干扰能力的稳定性")

plt.grid(axis="x", ls=":", lw=1, color="gray", alpha=.4)

plt.show()