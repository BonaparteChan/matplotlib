# 导入可视化模块
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 500)
y = np.sin(x) * np.cos(x)

line, = plt.plot(x, y)

line.set_linewidth(2)

plt.setp(line, linestyle="--", dashes=([10, 2, 5, 2]))
'''
关键词参数 linestyle 是 line2D 的属性(attr)，属性值(attrValue)为 "--"
函数 step() 将实例 line2D 的 linestyle 属性设置为 "--"
实例方法为 set_attr(attrValue)
'''
plt.show()