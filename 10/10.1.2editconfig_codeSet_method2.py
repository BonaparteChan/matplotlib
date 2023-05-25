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
mpl.rcParams["lines.linewidth"] = 2
mpl.rcParams["lines.color"] = "c"
mpl.rcParams["lines.linestyle"] = "--"
