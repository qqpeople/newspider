# 一次函数计算出值并画图
import matplotlib.pyplot as plt
import numpy as np

k = float(input("请输入斜率："))
b = float(input("请输入截距："))
x = np.linspace(0, 10, 1000)
y = k * x + b
plt.plot(x, y)
plt.show()



