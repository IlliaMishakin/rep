import math
import numpy as np
a = 4.85
b = 5.2
e = 0.001
def d(x):
    return x ** 3 - 3 * x - 0.4

def d1(x): #производная
    return 3 * x ** 2 - 3

def d2(x): #вторая производная
    return 6 * x 
while abs(a - b) < 2 * e:
    if d(a) * d2(a) < 0:
        a = a - d(a) * (a - b) / (d(a) / d(b))
    else:
        a = a = d(a) / d1(a)
    if d(b) * d2(b ) > 0:
        b = b - d(b) * (b - a) / (d(b) - d(a))
    else:
        b = b - d(b) / d1(b)

x = (a + b) / 2

print('Metod Combinovanui\nx =', x)
