import numpy as np
import matplotlib.pyplot as plt

size = 5
a = np.random.random(size)
b = np.random.random(size)
c = np.random.random(size)

x = np.arange(size)

plt.bar(x, a, width=0.5, label='a',fc='r')
plt.bar(x, b, bottom=a, width=0.5, label='b', fc='g')
plt.bar(x, c, bottom=a+b, width=0.5, label='c', fc='b')

plt.ylim(0, 2.5)
plt.legend()
plt.grid(True)
plt.show()
