import numpy as np
import matplotlib.pyplot as plt

cc= np.linspace(0,2,100)
plt.rcParams['font.sans-serif'] = ['SimHei'] 
plt.plot(cc,cc,label='linear')
plt.plot(cc,cc**2,label='两倍')
plt.plot(cc,cc**3,label='三倍')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("折线图")
plt.legend()
plt.show()

cc = np.linspace(0,2,100)
plt.plot(cc,cc,label ='linear')
plt.plot(cc,cc ** 2,label ='quadratic')
plt.plot(cc,cc ** 3,label ='cubic')
plt.xlabel('x label')
plt.ylabel('y label')