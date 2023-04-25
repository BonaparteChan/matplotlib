import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
# 导入模块

mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False
# 设置编码格式，不设置就没法写中文

apple = np.random.randn(100)
boy = np.random.randn(100)

# colormap:RdYlBu
# 气泡图，二维数据借助气泡大小展示三维数据

plt.scatter(apple, boy,
            s=np.power(10*apple+20*boy, 2),
            c=np.random.rand(100),
            cmap=mpl.cm.RdYlBu,
            marker="o")
# s 散点标记大小；
# c 散点标记颜色；
# cmap 将浮点数映射到颜色的颜色映射表
plt.show()