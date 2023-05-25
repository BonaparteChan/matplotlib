'''
通过代码层面的配置，按照具体项目需求，灵活进行 matplotlib 的相关属性值的配置

实现改变 matplotlib 的相关属性值的两种方法

method1 调用属性字典 matplotlib.rcParams 或是属性字典 matplotlib.pyplot.rcParams

method2 调用函数 matplotlib.rc() 或是函数 matplotlib.pyplot.rc()

如需回复标准的 matplotlib 默认设置，则可以调用函数 matplotlib.rcdefaults() 或是函数 matplotlib.pyplot.rcdefaults()
'''

# method1 调用函数 matplotlib.rc()

import matplotlib as mpl  # 导入绘图包

# usage of package matplotlib
# method1 of setting attribution
mpl.rc("lines", linewidth=2, color="c", linestyle="--")  # 将 lines 的相关属性以关键字参数进行复制

# method2 of setting attribution
line = {"linewidth": 2, "color": "c", "linestyle": "--"}  # 将属性和属性值放在一个字典里面
mpl.rc("lines", **line)  # 字典作为关键词参数，用 **line 形式进行参数调用

