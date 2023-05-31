# 字体主要属性的可视化展示
# 导入模块
import matplotlib.pyplot as plt

# 设置画布和子区
fig = plt.figure()
ax = fig.add_subplot(111)

# viewing family options
families = ["serif", "sans-serif", "fantasy", "monospace"]

# 设置文本内容
ax.text(-1, 1, "family", fontsize=18, horizontalalignment="center")

pi = [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]

for i, family in enumerate(families):
    ax.text(-1, pi[i], family, family=family, horizontalalignment="center")

# viewing size options
sizes = ["xx-small", "x-small", "small", "medium", "large", "x-large", "xx-large"]

# 设置文本内容
ax.text(-0.5, 1, "size", fontsize=18, horizontalalignment="center")

for i, size in enumerate(sizes):
    ax.text(-0.5, pi[i], size, size=size, horizontalalignment="center")

# viewing style options
styles = ["normal", "italic", "oblique"]

# 设置文本内容
ax.text(0, 1, "style", fontsize=18, horizontalalignment="center")

for i, style in enumerate(styles):
    ax.text(0, pi[i], style, style=style, family="sans-serif", horizontalalignment="center")

# viewing variant options
variants = ["normal", "small-caps"]

# 设置文本内容
ax.text(0.5, 1, "variant", fontsize=18, horizontalalignment="center")

for i, variant in enumerate(variants):
    ax.text(0.5, pi[i], variant, variant=variant, family="serif", horizontalalignment="center")

# viewing weight options
weights = ["light", "normal", "semibold", "bold", "black"]

# 设置文本内容
ax.text(1, 1, "weight", fontsize=18, horizontalalignment="center")

for i, weight in enumerate(weights):
    ax.text(1, pi[i], weight, weight=weight, horizontalalignment="center")

ax.axis([-1.5, 1.5, 0.1, 1.1])
ax.set_xticks([])
ax.set_yticks([])

plt.show()