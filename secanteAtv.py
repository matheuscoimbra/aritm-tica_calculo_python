# coding=utf-8
from __future__ import division
import numpy as np
import math
import sys
from sympy import *
init_printing(use_unicode=True)

#define x como variávei simbólica
x = symbols('x')

erro = 0.0001

escolha = int(input("Escolha uma das equações abaixo:\n"
                    "1) -> x/2 -tg(x) = 0\n"
                    "2) -> 2cos(x) - e^(x/2) = 0\n"
                    "3) -> x^5 - 6 = 0\n"))
if escolha == 1:
    def f(x): return (x/2) - tan(x)
   # print(f(x))
    x0 = 3.8
    x1 = 4.5
elif escolha == 2:
    def f(x): return (2*math.cos(x) - Pow(math.e,(x/2)))
#    print(f(x))
    x0 = 0.0
    x1 = 1.0
elif escolha == 3:
    def f(x): return (x**5 - 6)
   # print(f(x))
    x0 = 1.4
    x1 = 2.0
else:
    sys.exit(0)


x2 = 0.0



def funcao_tolerancia(x1=float):
   # return (abs(x ** 2 + np.log(x))) < tolerancia
    return (abs(f(x1))) < erro

def funcao(xk0=float,xk=float):
    return (xk0*f(xk) - xk*f(xk0))/(f(xk) - f(xk0))

x2 = funcao(x0, x1)
#print(x2)


bool = funcao_tolerancia(x2)

cont = 0
if bool == True:
    print(x2)
else:
    x3 = 0.0
    while bool == False:
        x3 = funcao(x2,x1)
       # print(x3)
        bool = funcao_tolerancia(x3)
        if bool == True:
            print(x3)
            #print(cont)
            break
        else:
            x1 = x2
            x2 = x3
            cont += 1