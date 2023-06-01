'''
缩写模式
b -》 蓝色(blue)
g -》 绿色(green)
r -》 红色(red)
c -》 青色(cyan-blue)
m -》 洋红色(megenta)
y -》 黄色(yellow)
k -》 黑色(？)
w -》 白色(white)
'''

# 导入绘图可视化模块和数学模块
import matplotlib.pyplot as plt
import numpy as np

barslices = 12

theta = np.linspace(0.0, 2 * np.pi, barslices, endpoint=False)
radii = 30 * np.random.rand(barslices)
width = 2 * np.pi /barslices
colors = np.array(["c", "m", "y", "b",  # 英文缩写模式的基本颜色
                   "#C67171", "#C1CDCD", "#FFEC8B", "#A0522D",  # Hex 模式的 #RRGGBB 字符串
                   "red", "burlywood", "chartreuse", "green",  # HTML/CSS 模式的颜色名
                   float("0.5291"), float("0.8078"), float("0.9216")])  # Decimal 模式的归一化到 [0, 1] 的 (R, G, B) 元组

# 画布和子区设置
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)

bars = ax.bar(theta, radii, width=width, color=colors, bottom=0.0)
plt.show()
