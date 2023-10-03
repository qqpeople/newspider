import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-2,10,1)
y = 0.9 * x + np.sin(x)

print(y)

print(' ')
print('*' * 10000)
print(' ')



moudle = np.polyfit(x,y,deg=4)
print(moudle)

print(' ')
print('*' * 10000)
print(' ')

x2 = np.arange(-2,12,0.5)
y2 = np.polyval(moudle,x2)
print(y2)

print(' ')
print("*" * 10000)
print(' ')

plt.plot(x,y,'o',x2,y2,'x')
plt.show()





