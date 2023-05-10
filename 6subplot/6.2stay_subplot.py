# 通过 使用 subplot2grid() 函数的 rowspan 和 colspan 参数，实现让子区跨越固定网格布局的多个行和列，实现不同的子区布局

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
# 导入可视化和数学模块

# 设置编码方式，文本字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

# set subplot 设置画布
plt.subplot2grid((2, 3), (0, 0), colspan=2)  # subplot2grid(shape, loc)
# 2 行 3 列，从第一行和第三列作为起始位置，跨越两行
# 设置数据
x = np.linspace(0.0, 4.0, 100)
y = np.random.randn(100)
plt.scatter(x, y, c="c")
plt.title("散点图")

plt.subplot2grid((2, 3), (0, 2))  # 图形位置的起始点是从 0 开始计算的
plt.title("空白绘图区域")

plt.subplot2grid((2, 3), (1, 0), colspan=3)
x = np.linspace(0.0, 4.0, 100)
y1 = np.sin(x)
plt.plot(x, y, lw=2, ls="-")
plt.xlim(0, 3)
plt.grid(True, ls=":", c="r")
plt.title("折线图")

# set figure
plt.suptitle("subplot2grid() 函数实例的展示", fontsize=25)  # 绘制画布标题的内容、字体

plt.show()
