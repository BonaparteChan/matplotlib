'''
堆积图，可视化展示
分块图对比数据分布差异
多数据并列柱状图和多数据平行条形图
'''
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
# 导入模块

mpl.rcParams["font.sans-serif"] = ["SimHei"]
# 字体设置
mpl.rcParams["axes.unicode_minus"] = False
# 处理坐标轴线的负刻度值的情况
# 设置编码格式，不设置就没法写中文

# some simple data 设置简单数据
x = np.arange(5)
y = [6, 10, 4, 5, 1]
y1 = [2, 6, 3, 8, 5]
# 数据格式为 list 列表

bar_width = 0.35
tick_label = ["A", "B", "C", "D", "E"]
# 宽度和标签定义

# create bar 创建平行条状图
plt.barh(x, y, bar_width, align="center", color="c", label="班级 A", alpha=.5)
plt.barh(x+bar_width, y1, bar_width, align="center", color="b", label="班级 B", alpha=.6)
'''
x 柱状图的标签值
y 柱状图的主体长度
align 对齐方式
color 柱体颜色
tick label 刻度标签值
alpha 柱体透明度
'''

# set x,y_axis label
plt.xlabel("测试难度")
plt.ylabel("试卷份数")

# set yaxis ticks and ticklabels
plt.yticks(x+bar_width/2, tick_label)

# set yaxis grid
plt.grid(True, axis="y", ls=":", color="r", alpha=0.3)

plt.legend()
# 表示不同图形的文本标签示例

plt.show()