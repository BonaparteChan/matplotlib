import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

x = np.linspace(0, 2 * np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.exp(x)
y4 = np.power(x, 2)

plt.subplot(411)
plt.plot(x, y1, ls="-", lw=2, label="sin(x) 正弦函数")

plt.subplot(412)
plt.plot(x, y2, ls="--", lw=2, label="cos(x) 余弦函数")

plt.subplot(413)
plt.plot(x, y3, ls="-.", lw=2, label="exp(x) 指数函数")

plt.subplot(414)
plt.plot(x, y4, ls=":", lw=2, label="power(x) 正弦函数")

# plt.margins(0.5)
# plt.xticks([0, 1, 2, 3, 4, 5, 6])
# plt.yticks([])

plt.show()