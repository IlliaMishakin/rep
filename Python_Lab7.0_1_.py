from numpy import*
import matplotlib.pyplot as plt

def f(t):
    return 5 * sin(10 * t) * sin(3 * t)
t = linspace(0, 4)
y = f(t)

t = linspace(0, 4)
plt.plot(t, y, 'g-', label = '5 * sin(10 * x) * sin(3 * x)', color = "pink")
plt.axis([0, 4, -5, 5]) 
plt.grid()
plt.xlabel('t')
plt.xlabel('y')
plt.title('5 * sin(10 * x) * sin(3 * x)')
plt.legend()
plt.show()