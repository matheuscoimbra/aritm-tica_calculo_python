# coding=utf-8
import numpy as np
import math
import sys
# funcao X^{5}-4X^{2}+2=0 < 10^{-4} num intervalo qlqr

tolerancia = 0.0001
intervaloA_negativo = 0.8
intervaloB_positivo = 1.5


calc_funcao = lambda x: x**5 - 4*(x**2) +2



def funcao_tolerancia(x=float):
    return (abs(calc_funcao(x)))< tolerancia

def media(intervaloA=float, intervaloB=float):
    return (intervaloA + intervaloB) / 2


if calc_funcao(intervaloA_negativo) * calc_funcao(intervaloB_positivo) < 0:
    print("está no intervalo")
    x = media(intervaloA_negativo, intervaloB_positivo)

    bool = funcao_tolerancia(x)
    if bool == True:
        print(x)
    else:
        while bool == False:
            if calc_funcao(x) >= 0:
                intervaloB_positivo = x
            else:
                intervaloA_negativo = x

            x = media(intervaloA_negativo, intervaloB_positivo)
            bool = funcao_tolerancia(x)
            if bool == True:
                print(x)
                break

else:
    print("não está no intervalo")
