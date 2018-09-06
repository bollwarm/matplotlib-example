import numpy as np
import matplotlib.pyplot as plt
np.random.seed(19680801)
mu1, sigma1 = 100, 15
mu2, sigma2 = 80, 15
x1 = mu1 + sigma1 * np.random.randn(10000)
x2 = mu2 + sigma2 * np.random.randn(10000)


n1, bins1, patches1 = plt.hist(x1, 50, density=True, facecolor='g', alpha=1)
n2, bins2, patches2 = plt.hist(x2, 50, density=True, facecolor='r', alpha=0.2)
plt.rcParams['font.sans-serif'] = ['SimHei'] 
plt.xlabel('智商')
plt.ylabel('置信度')
plt.title('IQ直方图')
plt.text(110, .025, r'$\mu=100,\ \sigma=15$')
plt.text(50, .025, r'$\mu=80,\ \sigma=15$')
# 设置坐标范围
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()
