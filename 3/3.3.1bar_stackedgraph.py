'''
堆积图，将若干统计图形堆叠起来的统计图形，组合式图形
堆积柱状图和堆积条形图
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
y = [6, 10, 4, 8, 5]
y1 = [2, 6, 3, 5, 1]
# 数据格式为 list 列表

# create horizontal bar 创建条形图
plt.bar(x, y, align="center", color="#66c2a5", tick_label=["A", "B", "C", "D", "E"], label="班级 A")
plt.bar(x, y1, align="center", color="#8da0cb", label="班级 B")
'''
x 柱状图的标签值
y 柱状图的主体高度
align 对齐方式
color 柱体颜色
tick label 刻度标签值
alpha 柱体透明度
'''

# set x,y_axis label
plt.xlabel("测试难度")
plt.ylabel("试卷份数")

# set yaxis grid
plt.grid(True, axis="y", ls=":", color="r", alpha=0.3)

plt.legend()
# 表示不同图形的文本标签示例

plt.show()