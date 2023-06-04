# case5 颜色标尺的颜色使用模式
# 使用函数 colorbar() 生成颜色标尺将图形中的颜色和具体数值的映射关系进行可视化展示

import scipy.misc
import matplotlib as mpl
import matplotlib.pyplot as plt

ascent = scipy.misc.ascent()

# display an image on the axes
plt.imshow(ascent, cmap=mpl.cm.gray)

# add colorbar to a plot
plt.colorbar()

plt.show()

