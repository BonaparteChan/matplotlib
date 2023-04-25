import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
# 导入模块

mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False
# 设置编码格式，不设置就没法写中文

apple = np.random.randn(1000)

plt.boxplot(apple)

plt.xticks([1], ["随机数生成器 AlphaRM"])
plt.ylabel("随机数值")
plt.title("随机数生成器抗干扰能力的稳定性")

# 绘制网格线
plt.grid(axis="y", ls=":", lw=1, color="gray", alpha=0.4)
# ls 是线条风格，lw 是线条宽度，color 是颜色， alpha 是透明度
plt.show()