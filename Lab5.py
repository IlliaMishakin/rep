import numpy as np
from numpy import linalg

def gauss(a,b):
    n = len(b)
    for k in range(0,n-1):
        for i in range(k+1,n):
            if a[i,k] != 0.0:
                
                a[i,k+1:n]= a[i,k+1:n]- a[i,k]/a[k,k]*a[k,k+1:n]
                b[i]= b[i]- a[i,k]/a[k,k]*b[k]
                
    for k in range(n-1,-1,-1):
        b[k] =(b[k] - np.dot(a[k,k+1:n],b[k+1:n]))/a[k,k]
    return b 
print("Gauss Method:\n",gauss(np.matrix([[3,-5,3],[1,2,1],[2,7,-1]]),np.matrix([[1],[4],[8]])))


def ggauss():
    
    a = np.matrix([[3,-5,3],[1,2,1],[2,7,-1]])
    b = np.matrix([[1],[4],[8]])
    c = np.linalg.inv(a)*b
    print("Method Jordana-Gaussa\n",c)
    print('Solve\n', np.linalg.solve(a,b))
    return c
ggauss()