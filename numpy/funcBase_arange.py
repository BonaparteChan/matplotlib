# 直接调用 Api 非常方面生成样本数据
'''
函数 arange() 使用方法
arange(start, stop, step)
start：数组的起始值
stop:数组的终止值(通常不包括终止值)
step:数组之间的间隔值
获得的返回值是一个包含起始值且不包含终止值的数组
'''

import numpy as np
# 导入数学模块

a = np.arange(5)
print("只有终止值，不包含终止值，默认间隔为 1 的数组：{}".format(a))

b = np.arange(0, 10.1, 1)
print("起始值为 0，终止值为 10.1，间隔为 1 的数组：{}".format(b))

c = np.arange(2, 10, 2)
print("偶数数组：{}".format(c))