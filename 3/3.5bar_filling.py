'''
可视化效果分为垂直样式和水平样式
可视化场景主要是定性数据的应用和离散数据的分布展示

装饰填充，设置主体填充样式

hatch “”，“/”，“\\”，“|”，“-”

字符串的符号数量越多，柱体的几何密集程度越高
'''
import matplotlib as mpl
import matplotlib.pyplot as plt
# 导入模块

mpl.rcParams["font.sans-serif"] = ["SimHei"]
# 字体设置
mpl.rcParams["axes.unicode_minus"] = False
# 处理坐标轴线的负刻度值的情况
# 设置编码格式，不设置就没法写中文

# some simple data 设置简单数据
x = [1, 2, 3, 4, 5]
y = [6, 10, 4, 5, 1]

# create bar 创建柱状图
plt.bar(x,
        y,
        align="center",
        color="c",
        tick_label=["A", "B", "C", "D", "E"],
        hatch="||")
'''
x 柱状图的标签值
y 柱状图的主体高度
align 对齐方式
color 柱体颜色
tick label 刻度标签值
alpha 柱体透明度
hatch 设置柱体填充样式
'''

# set x,y_axis label
plt.xlabel("测试难度")
plt.ylabel("测试份数")

# set yaxis grid
plt.grid(True, axis="y", ls=":", color="r", alpha=0.3)

plt.show()