# 标题和坐标轴的投影效果，需要引入新类 patheffects(路径效果)

# 导入可视化模块
import matplotlib.pyplot as plt
import matplotlib.patheffects as pes
# 导入数学模块
import numpy as np

# 设置数据
x = np.linspace(0.5, 3.5, 100)
y = np.sin(x)

fontsize = 23

# plot a sin(x) function 画个正弦函数图
plt.plot(x, y, ls="--", lw=2)  # 数值，样式和线宽

# set text contents 设置文本内容
title = "$y=\sin({x})$"
xaxis_label = "$x\_axis$"
yaxis_label = "$y\_axis$"

# get text instance 设置文本格式
title_text_obj = plt.title(title, fontsize=fontsize, va="bottom")  # 文本、文本大小，位置在底部
xaxis_label_text_obj = plt.xlabel(xaxis_label, fontsize=fontsize-3, alpha=1.0)  # 文本，文本大小，透明度
yaxis_label_text_obj = plt.ylabel(yaxis_label, fontsize=fontsize-3, alpha=1.0)

# set shadow 设置阴影
title_text_obj.set_path_effects([pes.withSimplePatchShadow()])
pe = pes.withSimplePatchShadow(offset=(1, -1),  # 偏离距离，文本内容投影相对文本内容本身的偏离距离
                               shadow_rgbFace="gray",  # 投影颜色
                               alpha=0.3)  # 透明度，范围 0.0~1.0， 数值越大透明度越小
xaxis_label_text_obj.set_path_effects([pe])
yaxis_label_text_obj.set_path_effects([pe])

plt.show()