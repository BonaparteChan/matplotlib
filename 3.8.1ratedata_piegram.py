'''
饼图展示定性数据比例分布特征
清楚观察出数据占比情况
'''

import matplotlib as mpl
import matplotlib.pyplot as plt
# 导入模块

mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False
# 设置编码格式，utf-8

# set some sample data 设置一些简单数据
labels = "A 难度水平", "B 难度水平", "C 难度水平", "D 难度水平"  # string 字符串
students = [0.35, .15, 0.20, 0.30]  # list 列表
colors = ["#377eb8", "#4daf4a", "#984ea3", "#ff7f00"]
explode = (0.1, 0.1, 0.1, 0.1)  # tuple 元组

# exploded pie chart
plt.pie(students, explode=explode, labels=labels, autopct="%3.1f%%", startangle=45, shadow=True, colors=colors)
# 饼片代表的百分比
'''explode: 饼片边缘偏离半径的百分比；
   labels：标记每份饼片的文本标签内容；
   autopic:饼片文本标签内容对应的数值百分比样式，保留一位有效数字
   startangel:从 x 作为起始位置，第一个饼片逆时针旋转的角度(开始角度)
   shadow：是否绘制饼片的阴影；
   colors：饼片的颜色'''

plt.title("选择不同难度测试试卷的学生占比")
plt.show()