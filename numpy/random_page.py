import numpy as np
from numpy.random import randn  # 有明确使用需求

a = np.random.rand(10)

b = np.random.randn(10)

print("生成长度为 10 的数组，其中元素介于 0 和 1 之间:{}".format(a))

print("标准正态分布的样本容量为 10 的返回值，返回值形式是包含 10 个元素的数组:{}".format(b))