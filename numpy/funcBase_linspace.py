# linspace() 和 arange() 使用方法类似
'''
linspace(start, stop, num=50, endpoint=True)
start：起始值
stop：终止值(通常包含终止值)
num：数组的长度(数组中的元素个数，默认长度是包含 50 个元素)
endpoint:是否包括数组终止值(默认为 True 包括，不包括则等于 False)
'''

import numpy as np
# 导入数学模块

a = np.linspace(1, 10, 10)
print("开始为 1，结束为 10(包括),数量为 10 的数组：{}".format(a))

b = np.linspace(1, 10, 5)
print("开始为 1， 结束为 10(包括)，数量为 5 的数组{}".format(b))

c = np.linspace(1, 10, 4, endpoint=False)
print("开始为 1， 结束为 10(不包括)，数量为 4 的数组：{}".format(c))