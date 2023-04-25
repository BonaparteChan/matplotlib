import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
# 导入模块

mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False
# 设置编码格式，不设置就没法写中文

apple = np.linspace(0.5, 2*np.pi, 20)
boy = np.random.randn(20)

# create cotton swap diagram 创建棉棒图
# 离散有序的数据

plt.stem(apple, boy, linefmt="-.", markerfmt="o", basefmt="-")
# linefmt 棉棒的样式；
# markerfmt 棉棒末端样式；
# basefmt 指定基线的样式

plt.show()