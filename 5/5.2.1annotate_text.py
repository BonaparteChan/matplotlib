# 注解 annotate，面向对象的实例方法 axe.annotate()
# 对细节做出标志的有指示注解 annotate()
# 对整体做出说明的无指示注解 text()

# 导入数学模块
import numpy as np
# 导入可视化模块
import matplotlib.pyplot as plt

# 设置一些简单的数据
x = np.linspace(0.5, 3.5, 100)
y = np.sin(x)

# 设置画布
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)

# 绘制曲线
ax.plot(x, y, c="b", ls="--", lw=2)

# Annotate the point xy with text with the “arrowstyle”
ax.annotate("maximum", xy=(np.pi/2, 1.0),  # 注解内容，xy:被解释的位置
            xycoords="data", xytext=((np.pi/2)+0.15, 0.8),  # xycoords 的坐标系统，参数值 ’data‘ 表示与折线图使用相同的坐标系统
                                                            # xytext 注释内容所在的位置，如把注释内容想象成一个矩形，xytext 标记的是左下角顶点位置
            textcoords="data", weight="bold", color="r",    # textcoords xytext 的坐标体系，weight 注解内容显示风格，color 注解内容的颜色
            arrowprops=dict(arrowstyle="->",  # 箭头的风格
                            connectionstyle="arc3",  # 连线的风格
                            color="r"))  # 箭头的颜色

# Annotate the whole points with text without the “arrowstyle”
# add text to the axes
ax.text(2.8, 0.4, "$y=\sin(X)$", fontsize=20, color="b",  # 注解的横纵坐标，注解内容，字体尺寸，字体颜色
        bbox=dict(facecolor="y", alpha=0.5))   # 方形区域的颜色和透明度

plt.show()
