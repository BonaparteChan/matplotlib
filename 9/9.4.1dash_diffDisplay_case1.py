# “破折号”线条样式的不同展现形式的设置方法
# 标记类型为“--”控制数据点的抹去模式实现“”破折号样式的多种展现形式

# 导入可视化和数学模块
import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl

# 编码格式和文字设置
mpl.rcParams["font.sans-serif"] = ["LiSu"]
mpl.rcParams["axes.unicode_minus"] = False

# 设置样式字典，字体样式字典、线条样式字典、标记样式字典
font_style = dict(family="serif", weight="black", size=12)
line_marker_style1 = dict(linestyle="--", linewidth=2, color="maroon", markersize=10)
line_marker_style2 = dict(linestyle="--", linewidth=2, color="cornflowerblue", markersize=10)
line_marker_style3 = dict(linestyle="--", linewidth=2, color="turquoise", markersize=10)

# 设置画布和子区
fig = plt.figure()
ax = fig.add_subplot(111, facecolor="honeydew")

# 设置简单数据
x = np.linspace(0, 2 * np.pi, 500)
y = np.sin(x) * np.cos(x)

# 绘制折线
ax.plot(x, y, dashes=[10, 2], label="dashes=[10, 2]", **line_marker_style1)
# 线段长度为 10 个数据点，线段之间间隔为 2 个数据点
ax.plot(x, y + 0.2, dashes=[3, 1], label="dashes=[3, 1]", **line_marker_style2)
# 线段长度为 3 个数据点，线段之间间隔为 1 个数据点
ax.plot(x, y + 0.4, dashes=[2, 2, 8, 2], label="dashes=[2, 2, 8, 2]", **line_marker_style3)
# 线段长度为 2 个数据点，线段之间间隔为 2 个数据点，线段长度为 8 个数据点，线段之间间隔为 2 个数据点

# 设置坐标轴
ax.axis([0, 2 * np.pi, -0.7, 1.2])

# 设置图例
ax.legend(ncol=3, bbox_to_anchor=(0.00, 0.95, 1.0, 0.05), mode="expand", fancybox=True, shadow=True, prop=font_style)
# bbox_to_anchor：上方 0.0...fancybox 控制线框的直角或圆角，shadow 控制阴影
plt.show()