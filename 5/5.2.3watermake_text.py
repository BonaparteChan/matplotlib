# 注解的水印效果

# 导入可视化模块
import matplotlib.pyplot as plt
# 导入数学模块
import numpy as np

# 设置数据
x = np.linspace(0.0, 10, 40)
y = np.random.randn(40)

plt.plot(x, y, ls="-", lw=2,  # 数值，样式和宽度
         marker="o", ms=20, mfc="orange", mec="green", alpha=0.6)  # 标记样式、尺寸、覆盖颜色、边缘颜色、透明度

# 网格线
plt.grid(ls=":", color="gray", alpha=0.5)  # 样式、颜色、透明度

plt.text(1, 2, "Matplotlib", fontsize=50, color="gray", alpha=0.5)
# alpha 透明度的设定实现水印效果 watermaker,取值越小，文本水印效果越明显

plt.show()