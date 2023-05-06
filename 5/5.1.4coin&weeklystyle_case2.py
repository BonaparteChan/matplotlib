# 时间序列和货币序列的刻度标签设置方法

# 导入可视化模块
import matplotlib.pyplot as plt
# 导入数学模块
import numpy as np

# 从日历模块中导入月和日的名词
from calendar import month_name, day_name
# 从可视化模块 matplotlib 的 tick 轴的类里面导入格式设置函数
from matplotlib.ticker import FormatStrFormatter

# 设置画布
fig = plt.figure()
ax = fig.add_axes([0.2, 0.2, 0.7, 0.7])

# 设置简单数据 set some simple data
x = np.arange(1, 8, 1)
y = 2 * x

ax.plot(x, y, ls="-", color="orange", marker="o", ms=20, mfc="c", mec="r")
# mfc 里面的颜色，mec 边缘线条的颜色

# RMB ticklabel 人民币刻度标签文字
ax.yaxis.set_major_formatter(FormatStrFormatter(r"$\yen%1.1f$"))  # 格式化坐标轴标签，生成保留两位有效数字的人民币计量刻度标签
# dayName ticklabel 日期刻度标签文字
plt.xticks(x, day_name[0: 7], rotation=20)

# 最小值和最大值
ax.set_xlim(0, 8)
ax.set_ylim(0, 18)

plt.show()