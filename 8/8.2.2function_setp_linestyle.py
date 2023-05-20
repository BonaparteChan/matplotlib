# 导入可视化模块
import matplotlib.pyplot as plt

line, = plt.plot([1, 2, 3])
plt.setp(line, linestyle="--")
'''
关键词参数 linestyle 是 line2D 的属性(attr)，属性值(attrValue)为 "--"
函数 step() 将实例 line2D 的 linestyle 属性设置为 "--"
实例方法为 set_attr(attrValue)
'''
plt.show()