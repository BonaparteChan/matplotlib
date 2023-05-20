# method2 调用函数 setp()
# 8.2 使用两种方法控制坐标轴刻度的显示

# 导入可视化模块
import matplotlib.pyplot as plt

ax1 = plt.subplot(221)  #二行二列的第一个图形
plt.setp(ax1.get_xticklabels(), visible=True)  # 设置刻度标签，显示
plt.setp(ax1.get_xticklines(), visible=True)  # 设置刻度线，显示
plt.grid(True, axis="x")

ax2 = plt.subplot(222)  #二行而二的第二个图形
plt.setp(ax2.get_xticklabels(), visible=True)  # 设置刻度标签，显示
plt.setp(ax2.get_xticklines(), visible=False)  # 设置刻度线，不显示
plt.grid(True, axis="x")

ax3 = plt.subplot(223)  #二行而二的第三个图形
plt.setp(ax3.get_xticklabels(), visible=False)  # 设置刻度标签 不显示
plt.setp(ax3.get_xticklines(), visible=True)  # 设置刻度线，显示
plt.grid(True, axis="x", linestyle="--")  # 设置网格线为破折线风格

ax4 = plt.subplot(224)  #二行而二的第四个图形
plt.setp(ax4.get_xticklabels(), visible=False)  # 设置刻度标签，不显示
plt.setp(ax4.get_xticklines(), visible=False)  # 设置刻度线，不显示
# 先画出刻度元素，然后将其隐藏
plt.grid(True, axis="x")

plt.show()