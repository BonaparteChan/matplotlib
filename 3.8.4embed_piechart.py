'''内嵌环形饼图，对比展示多数据集的比例分布情况
'''
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
# 导入模块

mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False
# 设置编码格式，utf-8

# set some simple data
elements = ["面粉", "砂糖", "奶油", "草莓酱", "坚果"]

weight1 = [40, 15, 20, 10, 15]
weight2 = [30, 25, 15, 20, 10]

colormapList = ["#e41a1c", "#377eb8", "#4daf4a", "#984ea3", "#ff7f00"]
outer_colors = colormapList
inner_colors = colormapList

wedges1, texts1, autotexts1 = plt.pie(weight1, autopct="%3.1f%%",
                                      radius=1, pctdistance=.85,
                                      colors=outer_colors, textprops=dict(color="w"),
                                      wedgeprops=dict(width=0.3, edgecolor="w"))

wedges2, texts2, autotexts2 = plt.pie(weight2, autopct="%3.1f%%",
                                      radius=.7, pctdistance=.75,
                                      colors=inner_colors,
                                      textprops=dict(color="w"), wedgeprops=dict(width=0.3, edgecolor="w"))

plt.legend(wedges1, elements, fontsize=12, title="配料表", loc="center left", bbox_to_anchor=(0.91, 0, 0.3, 1))

plt.setp(autotexts1, size=12, weight="bold")
plt.setp(autotexts2, size=12, weight="bold")
plt.setp(texts1, size=10)
# 绘制线的属性
# plt.setp(texts2, size=12)

plt.title("不同果酱面包配料比例表")

plt.show()