# 桑基图，sankey，权重权值流向的图形
# 指示箭头的宽度与权值的大小成比例
# 典型应用场景在可视化呈现流量，物质或成本过程中的转移情况
# ex:家庭支出，假期人流量，物理运输、军队

# 导入可视化模块
import matplotlib as mpl
import matplotlib.pyplot as plt
# 导入数学模块
import numpy as np

# 从可视化模块中导入桑基图的类
from matplotlib.sankey import Sankey

# 设置编码格式和中文字体
mpl.rcParams["font.sans-serif"] = ["FangSong"]
mpl.rcParams["axes.unicode_minus"] = False

# basedata
flows = [0.2, 0.1, 0.4, 0.3, -0.6, -0.05, -0.15, -0.2]  # 设置流量权值
labels = ["", "", "", "", "family 家庭", "trip 旅行", "education 教育", "sport 运动"]  # 设置标签文本
orientations = [1, 1, 0, -1, 1, -1, 1, 0]  # 权值流量显示的位置

# 生成桑基图示例
sankey = Sankey()

sankey.add(flows=flows,  # 权值，负值为流出，正值为流入
           labels=labels,
           orientations=orientations,  # 权值流量显示的位置，-1 显示在下方，0 显示在水平，1 显示在上方
           color="yellow",  # 边缘线条颜色
           fc="lightgreen",  # 覆盖颜色
           patchlabel="Life Cost 生活成本",
           alpha=0.7)  #透明度

diagrams = sankey.finish()
diagrams[0].texts[4].set_color("r")  # 修改第 5 个元素的颜色
diagrams[0].texts[4].set_weight("bold")  # 修改第 5 个元素的粗细
diagrams[0].text.set_fontsize(15)
diagrams[0].text.set_fontweight("bold")

plt.title("日常生活的成本开支流量图")

plt.show()