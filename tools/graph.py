# coding=gbk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator

x = np.linspace(-5, 5, 101)
y = 2 * x * x

plt.plot(x, y, c='red')
plt.title('Gradient Descent', fontsize=24)
plt.tick_params(axis='both', which='major', labelsize=14)
plt.xlabel('w', fontsize=14)
plt.ylabel('Loss', fontsize=14)

# 设置坐标轴刻度
x_major_locator = MultipleLocator(4)
y_major_locator = MultipleLocator(20)
ax = plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
ax.yaxis.set_major_locator(y_major_locator)
plt.xlim(-10, 10)
plt.ylim(-5, 110)

plt.show()
