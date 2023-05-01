'''误差棒值可很好实现总参数估计的置信区间的角色
   误差棒的计算方法(method):单一数值、置信区间、标准差、标准误；
   误差棒可视化展示(view):水平误差棒、垂直误差棒、对称误差棒、非对称误差棒；
   通过抽样获得样本，对总体参数进行估计会由于样本的随机性导致参数估计值出现波动，
   需要用误差值置信区间来表示对总体参数估计的可靠范围
'''

import matplotlib.pyplot as plt
import numpy as np
# 导入可视化模块和数学模块

x = np.linspace(0.1, 0.6, 10)
y = np.exp(x)

error = 0.05 + 0.15 * x
lower_error = error
upper_error = 0.3 * error
error_limit = [lower_error, upper_error]

plt.errorbar(x, y,
             yerr=error_limit, fmt="o",
             ecolor="y", elinewidth=4,
             ms=5, mfc="c", mec="r",
             capthick=1, capsize=2)
'''yerr：单一数值的非对称形式误差范围；
   fmt：数据点标记样式和数据点标记的连接线样式
   ecolor:误差棒的线条颜色
   elinewidth:误差棒的线条粗细
   ms:数据点的大小
   mfc：数据点的标记颜色
   mec：数据点标记边缘颜色
   capthick:误差棒边界横杠的厚度
   capsize:误差棒边界横杠的大小'''
plt.xlim(0, 0.7)

plt.show()
