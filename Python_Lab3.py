import math
import numpy as np
a = 0.5
b = 1
e = 0.0001
def d(x):
    return x ** 3 + x - 1

def d1(x): #производная
    return 3 * x ** 2 + 1

def d2(x): #вторая производная
    return 6 * x

f = d(a)
f2 = d2(a)

if f * f2 > 0:
    x = b
    z = a
else: 
    x = a
    z = b

fz = d(z)
h = x - ((d(x)) / d(x) - d(a)) * (x - a)
while abs(h) >= e:
    f = d(x)
    h = ((x - z) * f) / (f - fz)
    x = x - h

f = d(x)
print('Metod Hord\nx =', x, '\nf(x) =', f)