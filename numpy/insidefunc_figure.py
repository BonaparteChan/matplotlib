import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

mpl.rcParams["font.sans-serif"] = ["LiSu"]
mpl.rcParams["axes.unicode_minus"] = False

x = np.linspace(0, 2 * np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.exp(x)
y4 = np.power(x, 2)

fig, ax = plt.subplots(2, 2)

# plt.subplot(411)
ax[0, 0].plot(x, y1, ls="-", lw=2)
ax[0, 0].set_title("sin(x) 正弦函数")

# plt.subplot(412)
ax[0, 1].plot(x, y2, ls="--", lw=2)
ax[0, 1].set_title("cos(x) 余弦函数")

# plt.subplot(413)
ax[1, 0].plot(x, y3, ls="-.", lw=2)
ax[1, 0].set_title("exp(x) 指数函数")

# plt.subplot(414)
ax[1, 1].plot(x, y4, ls=":", lw=2, label="power(x) ?函数")
ax[1, 1].set_title("power(x) ?函数")

# plt.margins(0.5)
# plt.xticks([0, 1, 2, 3, 4, 5, 6])
# plt.yticks([])

plt.suptitle("不同内置函数的图形", fontsize=10, weight="black")

plt.show()