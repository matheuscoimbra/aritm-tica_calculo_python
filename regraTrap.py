import math
import numpy as np

"QUESTÃO SOBRE A REGRA DO TRAPÉZIO"
#n: número de subintervalos
#f:função
#a,b: limite superior e inferior
def trap(f,a,b,n):
    h = (b-a)/n
    #xn+1 = xn + h
    x = np.zeros(n+1)
    x[0] = a
    n = n+1
    sumfx = []
    for i in range(1,n):
        x[i] = x[i - 1] + h
        sumfx.append(f(x[i]) if i<n-1 else 0)
    print(x)
    sumfx = sum(sumfx)
    resul = float((h/2)*((f(x[0]) + f(x[n-1]))+2*sumfx))
    print("Resultado: ",resul)
f = lambda x: math.e**x #primeira f(x)
trap(f,1.0,2.0,20)
f = lambda x: math.sqrt(x) #segunda f(x)
trap(f,1.0,4.0,20)

