# 结合统计图形和数据表格，凸显数据规律和特点

# 导入数据可视化模块
import matplotlib as mpl
import matplotlib.pyplot as plt

# 设置编码格式、字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

# set some simple data 设置简单数据，exam level 考试难度
labels = "A 难度水平", "B 难度水平", "C 难度水平", "D 难度水平"
students = [0.35, 0.15, 0.20, 0.30]
explode = (0.1, 0.1, 0.1, 0.1)
colors = ["#377eb8", "#e41a1c", "#4daf4a", "#984ea3"]

# explode pie chart
plt.pie(students,
        explode=explode,  # 饼片边缘偏离半径的百分比
        labels=labels,
        autopct="%1.1f%%",  # 设置百分比位数样式
        startangle=45,  # 开始饼片的逆时针旋转角度
        shadow=True,  # 设置阴影
        colors=colors)

# 标题 title
plt.title("选择不同难度测试试卷的学生占比")

# add table to pie figure
colLabels = ["A 难度水平", "B 难度水平", "C 难度水平", "D 难度水平"]
rowLabels = ["学生选择试卷人数"]
studentValues = [[350, 150, 200, 300]]
colColors = ["#377eb8", "#e41a1c", "#4daf4a", "#984ea3"]

# 绘制表格
plt.table(cellText=studentValues,  # 表格中的数值
          cellLoc="center",  # 表格中的数据行，左右对齐，左对齐，居中对齐和右对齐
          colLabels=colLabels,  # 每一列的名称
          colColours=colColors,  # 每列的颜色
          rowLabels=rowLabels,  # 每行的名称
          rowLoc="center",  # 表格中的数据，上下对齐？？ 存疑
          loc="bottom")  # 表格在画布中的位置

plt.show()