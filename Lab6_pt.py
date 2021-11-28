from scipy import optimize
import math
def f1(x):
    return(0.8 - math.cos(x + 0.5))
def f2(y):
    return(0.5 * math.sin(y) + 0.8)
def d1(x):
    return(math.sin(x + 0.5))
def d2(y):
    return(0.5 * math.cos(y))
if abs(d1(1.5)) < 1:  
    n = 1
    x0 = 1.25
    y0 = 0.75
    r = 1
    print('y 0 = ',x0)
    print('x 0 = ',y0)
    while r > 0.0001:
        xn = f2(y0)
        r = abs(xn - x0)
        x0 = xn
        print('y', n ,'= ',xn)
        
        while r > 0.0001:
            yn = f1(xn)
            r = abs(xn - x0)
            y0 = yn
            print('x', n ,'= ',yn)
            n = n + 1


def fun(x): 
    return[math.cos(x[0] + 0.5) + x[1] - 0.8, math.sin(x[1])- 2 * x[0] - 1.6]
sol = optimize.root(fun, [0.75, 1.25], method= 'hybr')
print(sol.x)