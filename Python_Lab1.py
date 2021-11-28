import math 

def funk(x):
    return x ** 4 + 2 * x ** 3 + 2 * x ** 2 + 6 * x - 3  
def funkPoh(x):
    return 12 * x ** 2 + 12 * x + 4
# f'=24x^3 + 24x^2 - 48x
# f''=72x^2 + 48x - 48
def metHord(a, b):
    if funk(a) * funkPoh(a) > 0:
        x0 = a
        xi = b
    else:
        x0 = b
        xi = a

    while abs((xi - (((xi - x0) / (funk(xi) - funk(x0))) * funk(xi))) - xi) <= 0.001:
        xi1 = xi - (((xi - x0) / (funk(xi) - funk(x0))) * funk(xi))
        if abs(xi1 - xi) <= 0.001:
            xi = xi1
  
    
    return print('Metod Hord = ', funk(xi))
metHord(-2, 6)
