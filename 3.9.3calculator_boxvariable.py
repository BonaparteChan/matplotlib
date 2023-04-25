'''箱线图组成部分，箱体、箱须、离群值
   箱体由第一四分位数、中位数和第三四分位数组成
   箱须又分为上箱须和下箱须
   define variable 定义变量值
   Q1 为第一四分位数
   Q3 为第三四分位数
   whis 四分位间距的倍数
   IQR  四分位差 inter quartile range
   outlier_value 离群值
   IQR = Q3-Q1
   outlier value 的判断标准 (Q3+whis*IQR)<value<(Q1-whis*IQR)，或 or， value 是数据集 data 中的数据点
   上箱须和下下箱须的确定方法是在绘制箱线图的原始数据集 data 中分别寻找
   不大于 Q3+whis*IQR 的最大值 value^max 和不小于 Q1-whis*IQR 的最小值 value^min

'''

import numpy as np
# 导入数学模块

# set data
data = [10, 2, 25, 11, 24, 13, 54, 4, 42, -3]
pc = np.array(data)

array_value = np.percentile(pc, np.arange(0, 100, 25))

print(array_value)

'''计算结果 [-3.    5.5  12.   24.75]
 Q1 为第一四分位数
   Q3 为第三四分位数
   whis 四分位间距的倍数
   IQR  四分位差 inter quartile range
   outlier_value 离群值
   IQR = Q3-Q1
   outlier value 的判断标准 (Q3+whis*IQR)<value<(Q1-whis*IQR)，或 or， value 是数据集 data 中的数据点
   上箱须和下下箱须的确定方法是在绘制箱线图的原始数据集 data 中分别寻找
   不大于 Q3+whis*IQR 的最大值 value^max 和不小于 Q1-whis*IQR 的最小值 value^min
'''

q1 = 5.5
q3 = 24.75
midian = 12
whis = 1.5

IQR = q3 - q1
value_min = q1 - whis * IQR
value_max = q3 + whis * IQR

print(IQR, value_max, value_min)
print("离群值 outlier 为 54")
print("四分位差是 {}".format(IQR))
print("离群值最大值 {}".format(value_max))
print("离群值最小值 {}".format(value_min))