import math
import numpy as np

a = 4.85
b = 5.2
e = 0.05
def d(x):
    return x ** 3 - 3 * x - 0.4

while abs(b - a) >= e:
    if d(a) * d((a + b) / 2) < 0:
        b = (a + b) / 2
    else:
        a = (a + b) / 2

x = (a + b) / 2
print('Metod Polovinnogo Dilennya\nx =', x,)
