import numpy as np
from matplotlib import pyplot as plt
import matplotlib
print(matplotlib.__version__)

plt.rcParams['font.sans-serif'] = 'Arial Unicode MS'
plt.rcParams['axes.unicode_minus'] = False

# x=np.arange(1,11)
# print(type(x))
# y=2*x+5
# plt.title("测试")
# plt.xlabel("x轴")
# plt.ylabel("y轴")

# plt.plot(x,y)
# plt.show()

#参考
#[快速解决Mac无法显示matplotlib中文问题（anaconda3） 小白也能看懂！！_Pericles_HAT的博客-CSDN博客](https://blog.csdn.net/Pericles_HAT/article/details/109605283)

#柱状图
#创建图形对象
fig = plt.figure()
#添加子图区域，参数值表示[left, bottom, width, height ]
ax = fig.add_axes([0.1,0.1,0.88,0.88])
#准备数据
langs = ['C', 'C++', 'Java', 'Python', 'PHP']
students = [23,17,35,29,12]
#绘制柱状图
ax.bar(langs,students)
plt.show()