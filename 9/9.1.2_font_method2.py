# method2 调用签名中,用 “**font” 方法将字典变为关键字参数
# 第 9 章设置线条类型和标记类型的显示样式
# 9.1 不同调用签名形式的字典使用方法

# 导入可视化和数学模块
import matplotlib.pyplot as plt
import numpy as np

# 设置画布和子区
fig = plt.figure()
ax = fig.add_subplot(111)

# 设置字体样式
# font = {"family": "monospace", "color": "maroon", "weight": "bold", "size": 16}
font = dict(family="monospace", color= "maroon", weight= "bold", size= 16)
# 调用签名中,用 “**font” 方法将字典变为关键字参数;格式、颜色、粗细、尺寸
# 将文本属性和属性值都放在字典 font 里面

# some simple data 设置简单数据
x = np.linspace(0.0, 2 * np.pi, 500)
y = np.cos(x) * np.sin(x)

# 划曲线
ax.plot(x, y, color="k", ls="-", lw=2)  # 颜色、样式和宽度

# 设置标题、文本、标签
ax.set_title("key word mode is '**font'", **font)
ax.text(1.5, 0.4, "cos(x)*sin(x)", **font)  # 文本位置，文本内容，文本格式
ax.set_xlabel("time(h)", **font)
ax.set_ylabel(r"$\Delta$height(cm)", **font)
# 在实例方法 set_title()\。。。 作为关键词自参数 fontdict 的参数传递到实例方法调用签名中

# 设置 x 轴的区间
ax.set_xlim(0, 2 * np.pi)

plt.show()