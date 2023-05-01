'''
在条形图基础上绘制而成，主要用来可视化定性数据的相同指标在时间维度上的指标值变化情况，
实现定性数据的相同指标的变化情况而定有效直观比较

间断条形图
'''
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
# 导入模块

mpl.rcParams["font.sans-serif"] = ["SimHei"]
# 字体设置 换了一个字体
mpl.rcParams["axes.unicode_minus"] = False
# 处理坐标轴线的负刻度值的情况
# 设置编码格式，不设置就没法写中文

plt.broken_barh([(30, 100), (180, 50), (260, 70)], (20, 8), facecolors="#1f78b4")
plt.broken_barh([(60, 90), (190, 20), (230, 30), (290, 60)], (10, 8), facecolors=("#7fc97f", "#fdc086", "#beaed4", "#ffff99"))
# 列表里面的 数据结构 元组 tuple，从 60 位置开始向正方向移动 90 个单位(长度) x 轴
# 列表后面的 数据结构 元组 tuple，从 10 位置开始向正方向移动 8 个单位(高度) y 轴

# x, y 轴的最大值和最小值
plt.xlim(0, 360)
plt.ylim(5, 35)
plt.xlabel("演出时间")
# x 轴上的提示文本

plt.xticks(np.arange(0, 361, 60))
plt.yticks([15, 25], ["歌剧院 A", "歌剧院 B"])
# set yaxis grid
plt.grid(lw=1, ls="-", color="gray")

plt.title("不同地区的歌剧院的演出时间比较")
plt.show()