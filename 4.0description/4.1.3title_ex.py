import matplotlib.pyplot as plt
import numpy as np
# 导入模块，

x = np.linspace(-2, 2, 1000)
y = np.exp(x)

plt.plot(x, y, ls="-", lw=2, color="g")

plt.title("center demo")
plt.title("left demo", loc="left",
          fontdict={"size": "xx-large",
                    "color": "r",
                    "family": "Times New Roman"})
plt.title("right demo", loc="right",
          size=20,  # 字体大小
          color="c",  # 字体颜色
          family="Comic Sans MS",  # 字体类别
          style="oblique")  # 字体风格

plt.show()