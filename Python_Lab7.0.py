from numpy import*
import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4])
plt.show()

def f(t):
    return t **2 * exp(-t ** 2)
t = linspace(0, 3, 51)
y = f(t)
plt.plot(t, y)
plt.show()

t = linspace(0, 3, 51)
plt.plot(t, y, 'g--', label = 't^2*exp(-t^2)')
plt.axis([0, 3, -0.05, 0.5]) 
plt.xlabel('t')
plt.xlabel('y')
plt.title('My first normal plot')
plt.legend()
plt.show()

y1 = t ** 2 * exp(-t ** 2)
y2 = t ** 4 * exp(-t ** 2)
y3 = t ** 6 * exp(-t ** 2)
plt.plot(t, y1, 'g^', t, y2, 'b--', t, y3, 'ro-')
plt.xlabel('t')
plt.ylabel('y')
plt.title('Plotting with markers')
plt.legend(['t^2*exp(-t^2)','t^4*exp(-t^2)', 't^6*exp(-t^2)'], loc = 'upper left')
plt.show()

def f1(t):
    return 5 * sin(10 * t) * sin(3 * t)
t = linspace(0, 4)
y = f1(t)

t = linspace(0, 4)
plt.plot(t, y, 'g-', label = '5 * sin(10 * x) * sin(3 * x)', color = "pink")
plt.axis([0, 4, -5, 5]) 
plt.grid()
plt.xlabel('t')
plt.xlabel('y')
plt.title('5 * sin(10 * x) * sin(3 * x)')
plt.legend()
plt.show()