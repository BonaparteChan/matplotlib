# case1 模拟图的颜色使用模式

import matplotlib.pyplot as plt
import numpy as np
# 导入绘图模块和数学模块

rd = np.random.rand(10, 10)
plt.pcolor(rd, cmap="BuPu")
# 参数值是根据 colorbrewer 的颜色界定的，使用颜色映射表类型 colorbrewer sequential
plt.colorbar()

plt.show()