import matplotlib.pyplot as plt
import numpy as np

x = np.arange(9, 11, 0.001)

y1 = pow(2.718281828, -2.291969677 * x) * pow(10, 9)

fig, ax1 = plt.subplots()

ax1.set_xlabel('gap distance w [Å]', color='black')
ax1.set_ylabel('IT [a.u.]', color='black')
ax1.plot(x, y1, 'blue')
ax1.set_ylim(0, 1.2)  # 设置y1范围

plt.xlim((9, 11))  # 设置x范围
plt.show()
# plt.savefig('1.png')
