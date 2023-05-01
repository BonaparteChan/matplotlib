# 为饼图 piechart 提添加图例，实现绘图区域的清晰布局

import matplotlib as mpl
import matplotlib.pyplot as plt
# 导入数据可视化模块

mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False
# 设置编码格式 utf-8,字体 SimHei

# set some simple data
element = ["面粉", "砂糖", "奶油", "草莓酱", "坚果"]
weight = [40, 15, 20, 10, 15]
colors = ["#1b9e77", "#d95f02", "#7570b3", "#66a61e", "#e6ab02"]

wedges, texts, autotexts = plt.pie(weight, autopct="%3.1f%%",  # 数值百分比样式
                                   textprops=dict(color="w"),
                                   colors=colors)  # 颜色
# 设置图例
plt.legend(wedges, element, fontsize=12,
           title="配料表",
           loc="center left",
           bbox_to_anchor=(0.91, 0, 0.3, 1))

plt.setp(autotexts, size=15, weight="bold")
plt.setp(texts, size=12)

plt.title("果酱面包配料比例表")

plt.show()