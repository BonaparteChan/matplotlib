# 8.1.3 使用函数 axis() 绘制坐标轴
# 第 8 章坐标轴的高阶应用
# 8.1 设置坐标轴的位置和展示形式


# 导入数学模块和可视化模块
import matplotlib.pyplot as plt
import numpy as np

plt.axis([3, 7, -0.5, 3])
plt.plot(4 + np.arange(3), [0, 1, 0], color="blue", linewidth=2, linestyle="-")


plt.show()