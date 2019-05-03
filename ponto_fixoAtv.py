# coding=utf-8
from sympy import *
import numdifftools as nd

tolerancia = 0.0001
x0 = 1.5
intervaloA = 1.0
intervaloB = 2.0
# funcao  F(x)=x-x^{3}-4x^{2}+10 , x_{0}=1,5.
f = lambda x: x - x**3 - 4*(x**2) + 10

def funcao_tolerancia(x=float):
    return (abs(f(x)))< tolerancia

#x_{k+1}=1/2(\sqrt{x_{k}-x^{3}_{k}+10})
def funcao(xk=float):
    return 0.5*(sqrt(xk-xk**3+10))


if (f(intervaloA)>0 and f(intervaloB)<0) or (f(intervaloA)<0 and f(intervaloB)>0):
    print("está no intervalo")
    x1 = funcao(x0)

    bool = funcao_tolerancia(x1)
    if bool == True:
        print(x1)
    else:
        while bool == False:
            x1 = funcao(x1)
            bool = funcao_tolerancia(x1)
            if bool == True:
                print(x1)
                break

else:
    print("não está no intervalo")
