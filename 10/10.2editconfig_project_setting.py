# 10.2.1 修改项目层面的 matplotlib 配置的配置文件所在路径

import matplotlib.pyplot as plt
import numpy as np
# 导入绘图可视化包和数学模块

# 寻找当前活动的 matplotlibrc 文件路径，在 Python shell 使用
import matplotlib as mpl
mpl.matplotlib_fname()

# 抑制所有报错
import warnings
warnings.filterwarnings("ignore")

# normal plot 正常
plt.axes([0.1, 0.7, 0.3, 0.3], frameon=True, facecolor="y", aspect="equal")  # 图位置，轴脊，背景颜色
plt.plot(np.arange(3), [0.1, 0])
plt.cla()
plt.plot(np.arange(3), [0.1, 0])

# no plot
plt.axes([0.4, 0.4, 0.3, 0.3], frameon=True, facecolor="y", aspect="equal")  # 图位置，轴脊，背景颜色
plt.plot(2 + np.arange(3), [0.1, 0])

# no axes 无轴
plt.axes([0.7, 0.1, 0.3, 0.3], frameon=True, facecolor="y", aspect="equal")  # 图位置，轴脊，背景颜色
plt.plot(4 + np.arange(3), [0.1, 0])
plt.axis("off")

plt.show()