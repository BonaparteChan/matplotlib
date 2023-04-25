'''箱体图应用在测量或观测数据的比较场景中
   水平方向可视化 vert，不显示离群值 showfliers
'''
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
# 导入模块

mpl.rcParams["font.sans-serif"] = ["FangSong"]
mpl.rcParams["axes.unicode_minus"] = False
# 设置编码格式，utf-8

# set some simple data
testA = np.random.randn(5000)
testB = np.random.randn(5000)

testList = [testA, testB]
labels = ["随机数生成器 AlphaRM", "随机数生成器 BetaRM"]
colors = ["#1b9e77", "#d95f02"]

# set some variable 设置一些变量
whis = 1.6
width = 0.35

# bplot = plt.boxplot(testList, whis=whis, widths=width, sym="o", labels=labels, patch_artist=True)
'''testList 绘制箱线图的输入数据
   whis 四分位间距的倍数，用来确定箱体须包含数据的范围大小
   widths 箱体宽度
   sym 离群值的标记样式
   labels 绘制每个数据集的刻度标签
   patch_artist 是否给箱体添加颜色 True 是
   notch 是否添加 V 型凹痕， True 是
'''

bplot = plt.boxplot(testList, whis=whis, widths=width, sym="o", labels=labels, patch_artist=True, notch=True)

for patch, color in zip(bplot["boxes"], colors):
    patch.set_facecolor(color)
# 对每个箱体进行颜色填充

plt.ylabel("随机数值")
plt.title("生成器抗干扰能力的稳定性比较")

plt.grid(axis="y", ls=":", lw=1, color="gray", alpha=0.4)

plt.show()