# case1 棉棒图的定制化展示
# 8.2 使用两种方法控制坐标轴刻度的显示
# 使用 step() 完成棉棒图的展示样式定制化调整

# 导入数学模块和可视化模块
import matplotlib.pyplot as plt
import numpy as np

# set some simple 设置一些简单数据
x = np.linspace(0.5, 2 * np.pi, 20)
y = np.random.randn(20)

markerline, stemlines, baseline = plt.stem(x, y)  # 画棉棒图
# 通过 stem() 获得实例 markerline、stemlines、baseline

# 对实例的属性值进行定制化设置
plt.setp(markerline, color="chartreuse", marker="D")
plt.setp(stemlines, linestyle="-.")
baseline.set_linewidth(2)

plt.show()