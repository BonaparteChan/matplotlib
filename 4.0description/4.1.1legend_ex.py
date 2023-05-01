# 图例 是用以标记每个图形所代表的内容，方便辨识

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
# 导入模块

mpl.rcParams["font.sans-serif"] = ["LiSu"]
mpl.rcParams["axes.unicode_minus"] = False
# 设置编码格式，utf-8

x = np.linspace(-2*np.pi, 2*np.pi, 200)
y = np.sin(x)  # 正弦曲线
y1 = np.cos(x)  # 余弦曲线

plt.plot(x, y, label=r"$\sin(x)$")
plt.plot(x, y1, label=r"$\cos(x)$")
# r"$$" 模式 matplotlib 自带的 TeX 功能，raw strings

plt.legend(loc="lower left")
# 设置图例展示在左下角

# 设置标题
plt.title("正弦曲线和余弦曲线的折线图")

# 输出结果
plt.show()