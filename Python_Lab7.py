#xi:   -1  0  1 3          -0.5  1.5  2   2.5
#f(xi): 1 -8 -3 25           ?    ?   ?    ?
import numpy as np
from numpy import*
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange   #writing functoin!!!

Xi = np.array([-1, 0, 1, 3])
Yi = np.array([1, -8, -3, 25])
Xi1 = np.array([-0.5, 1.5, 2, 2.5])
def Lagrange(x):
    Lxi = (((x - Xi[1]) * (x - Xi[2]) * (x - Xi[3])) / ((Xi[0] - Xi[1]) * (Xi[0] - Xi[2]) * (Xi[0] - Xi[3])) * Yi[0]) 
    Lxi = Lxi + (((x - Xi[0]) * (x - Xi[2]) * (x - Xi[3])) / ((Xi[1] - Xi[0]) * (Xi[1] - Xi[2]) * (Xi[1] - Xi[3])) * Yi[1]) 
    Lxi = Lxi + (((x - Xi[0]) * (x - Xi[1]) * (x - Xi[3])) / ((Xi[2] - Xi[0]) * (Xi[2] - Xi[1]) * (Xi[2] - Xi[3])) * Yi[2]) 
    Lxi = Lxi + (((x - Xi[0]) * (x - Xi[1]) * (x - Xi[2])) / ((Xi[3] - Xi[0]) * (Xi[3] - Xi[1]) * (Xi[3] - Xi[2])) * Yi[3])
    return (Lxi)

i = 0
while i <= 3:
    print('Lagrange Polinom, x', i, '(', Xi1[i], ') =', Lagrange(Xi1[i]))
    i = i + 1

x = linspace(-1, 3, 500)
y = Lagrange(x)
plt.plot(x, y, 'g--', color = 'red')
plt.scatter(Xi, Lagrange(Xi), color = 'orange', marker = 'o')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Polinom Lagrange')
plt.legend(['L(x)'])
plt.grid()
plt.show()

result = lagrange(Xi, Yi)
fig = plt.figure(figsize = (10,8))
plt.plot(x, result(x), 'b', Xi, Yi, 'ro')
plt.title('Lagrange Polynomial')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.show()