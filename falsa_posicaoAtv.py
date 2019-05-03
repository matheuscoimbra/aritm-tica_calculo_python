# coding=utf-8
import math
from sympy import *

tolerancia = 0.05
A = 0.5
B = 1.0

f = lambda x: x ** 2 + math.log(x)



def funcao_tolerancia(x=float):
    return (abs(f(x)))< tolerancia

def media(a=float, b=float):
    return (a*f(b) - b*f(a)) / (f(b) - f(a))


if f(A) * f(B) < 0:
    print("está no intervalo")
    x = media(A, B)
    bool = funcao_tolerancia(x)
    if bool == True:
        print(x)
    else:
        while bool == False:
            if f(x) >= 0:
                A = x
            else:
                B = x

            x = media(A, B)
            bool = funcao_tolerancia(x)
            print(x)
            print(funcao_tolerancia(x))
            if bool == True:
                print(x)
                break

else:
    print("não está no intervalo")
