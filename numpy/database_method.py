import numpy as np
# 导入数学模块

# 将 list 列表转化为数组 array

# 设置列表基础数据
a = [1, 3, 5, 7, 9]
b = [2, 4, 6, 8, 10]
ab = [a, b]

# 生成数组
array_A = np.array(a)
array_B = np.array(b)
array_AB = np.array(ab)

print("数组 array_A({})".format(array_A))
print("数组 array_B({})".format(array_B))
print("数组 array_AB({})".format(array_AB))