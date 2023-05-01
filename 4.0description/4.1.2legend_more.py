# 图例 是用以标记每个图形所代表的内容，方便辨识

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
# 导入模块

mpl.rcParams["font.sans-serif"] = ["LiSu"]
mpl.rcParams["axes.unicode_minus"] = False
# 设置编码格式，utf-8

x = np.arange(0, 2.1, 0.1)
y = np.power(x, 3)
y1 = np.power(x, 2)
y2 = np.power(x, 1)

plt.plot(x, y, ls="-", lw=2, label=r"$x^{3}$")
plt.plot(x, y1, ls="-", lw=2, c="r",  label=r"$x^{2}$")
plt.plot(x, y2, ls="-", lw=2, c="y",  label=r"$x^{1}$")  # 样式、宽度、颜色、层标注文字
# r"$$" 模式 matplotlib 自带的 TeX 功能，raw strings

plt.legend(loc="upper left", bbox_to_anchor=(0.05, .95), ncol=3,
           title="power function", shadow=True, fancybox=True)
'''
loc:位置参数，center right，center left；upper right，upper left；lower right，lower left
bbox_to_anchor：线框位置参数，四元元组
title：图例标签内容
shadow：线框阴影
fancybox：线框圆角控制
'''
# 设置图例展示在左下角

# 设置标题
# plt.title("正弦曲线和余弦曲线的折线图")

# 输出结果
plt.show()