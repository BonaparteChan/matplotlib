# method2 methtext 模式
# 第 9 章设置线条类型和标记类型的显示样式
# 9.3 标记类型的显示样式设置方法
# 关键字参数 mathtext 取值是原始字符串 (raw strings) r"$text\text$" 模式

# 导入可视化模块和数学模块
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# 编码格式和文字设置
mpl.rcParams["font.sans-serif"] = ["LiSu"]
mpl.rcParams["axes.unicode_minus"] = False

# set some simple data 设置简单数据
x = np.arange(1, 13, 1)
y = np.array([12, 34, 22, 30, 18, 13, 15, 19, 24, 28, 23, 27])

# 设置画布和子区
fig, ax = plt.subplots(2, 2)  # 两行两列

# subplot(221)
ax[0, 0].scatter(x, y * 1.5, marker=r"$\clubsuit$", c="#fb8072", s=500)
ax[0, 0].locator_params(axis="x", tight=True, nbins=11)  # nbins 控制刻度数量，如没有足够空间来创建刻度，则会创建比该值更少的刻度
ax[0, 0].set_xlim(0, 13)
ax[0, 0].set_xticks(x)
ax[0, 0].set_title("显示样式 {} 的散点图".format(r"$\clubsuit$"))

# subplot(222)
ax[0, 1].scatter(x, y * 1.5, marker=r"$\heartsuit$", c="#fb8072", s=500)
ax[0, 1].locator_params(axis="x", tight=True, nbins=11)
ax[0, 1].set_xlim(0, 13)
ax[0, 1].set_xticks(x)
ax[0, 1].set_title("显示样式 “%s” 的散点图" % r"$\heartsuit$")

# subplot(223)
ax[1, 0].scatter(x, y * 1.5, marker=r"$\diamondsuit$", c="#fb8072", s=500)
ax[1, 0].locator_params(axis="x", tight=True, nbins=11)
ax[1, 0].set_xlim(0, 13)
ax[1, 0].set_xticks(x)
ax[1, 0].set_title("显示样式 “%s” 的散点图" % r"$\diamondsuit$")

# subplot(224)
ax[1, 1].scatter(x, y * 1.5, marker=r"$\spadesuit$", c="#fb8072", s=500)
ax[1, 1].locator_params(axis="x", tight=True, nbins=11)
ax[1, 1].set_xlim(0, 13)
ax[1, 1].set_xticks(x)
ax[1, 1].set_title("显示样式 {} 的散点图".format(r"$\spadesuit$"))

plt.suptitle("不同原始字符串作为标记类型的展示效果", fontsize=16, weight="black")

plt.show()