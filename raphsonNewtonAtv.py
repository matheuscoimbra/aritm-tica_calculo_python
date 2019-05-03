# coding=utf-8
import numpy as np
import math
import sys
from sympy import *
init_printing(use_unicode=True)

#define x como variávei simbólica
x = symbols('x')

erro = 0.0001

x1 = 0.0

escolha = int(input("Escolha uma das equações abaixo:\n"
                    "1) -> x/2 -tg(x) = 0\n"
                    "2) -> 2cos(x) - e^(x/2) = 0\n"
                    "3) -> x^5 - 6 = 0\n"))
if escolha == 1:
    def f(x): return (x/2) - tan(x)
   # print(f(x))
    x0 = 4.5
elif escolha == 2:
    def f(x): return (2 * cos(x) -  math.e ** (x / 2))
    x0 = 1.0
elif escolha == 3:
    def f(x): return (x**5 - 6)
   # print(f(x))
    x0 = 1.4 #certo
else:
    sys.exit(0)


#print(diff(f(x), x))

def funcao_tolerancia(x1=float,x0=float):
    return (abs(x1-x0)) < erro

def funcao(xn=float):
    return xn - (f(xn)/(diff(f(x),x).subs(x,xn)))  #avaliar a derivada em um ponto

x1 = funcao(x0)
#print(x1)
bool = funcao_tolerancia(x1,x0)

cont = 0
if bool == True:
    print(x1)
else:
    x2 = 0.0
    while bool == False:


        x2 = funcao(x1)
        #print(x2)
        bool = funcao_tolerancia(x2,x1)
        if bool == True:
            print(x2)
            #print(cont)
            break
        else:
            x1 = x2
            cont += 1
