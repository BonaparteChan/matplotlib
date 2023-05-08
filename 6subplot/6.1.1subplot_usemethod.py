# 一行两列子区，分别绘制正弦曲线和余弦曲线
# subplot(numRows,numCols,plotNum) 行列位置

import matplotlib.pyplot as plt
import numpy as np
# 导入可视化和数学模块

# 设置数据
x = np.linspace(-2 * np.pi, 2 * np.pi, 200)
y = np.sin(x)
y1 = np.cos(x)

# set figure 设置画布 1,1 行 2 列第 1 个图形
plt.subplot(121)

plt.plot(x, y, ls="--")

# 设置画布 2，1 行 2 列第 2 个图形
plt.subplot(122)

plt.plot(x, y1, ls="-.")

plt.show()