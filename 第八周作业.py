'''
name: 黄锦清
student number: 1619100043
function：拟合数据
'''
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

x = np.arange(1, 13, 1)
y1 = np.array([17,19,21,28,33,38,37,37,31,23,19,18])
y2 = np.array([-62,-59,-56,-46,-32,-18,-9,-13,-25,-46,-52,-58])
def func(x,a,b,c):
    return a*np.sin(2*np.pi*b*x)+c
popt, pcov = curve_fit(func, x, y1)
a=popt[0] 
b=popt[1]
c=popt[2]
yvals1=func(x,a,b,c)
plot1=plt.plot(x, y1, '*',label='maximum air temperature')
plot2=plt.plot(x, yvals1, 'r',label='curve_fit values')

popt, pcov = curve_fit(func, x, y2)
a=popt[0] 
b=popt[1]
c=popt[2]
yvals2=func(x,a,b,c)
plot3=plt.plot(x, y2, '*',label='minimum air temperature')
plot4=plt.plot(x, yvals2, 'b',label='curve_fit values')

plt.xlabel('month')
plt.ylabel('temperature')
plt.legend(loc=4) 
plt.title('curve_fit')
plt.show()