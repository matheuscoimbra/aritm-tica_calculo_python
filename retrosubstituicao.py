"""
Tarefa 1: Escrevam um algoritmo que a partir de uma matriz triangularizada nxn (aumentada n+1 colunas).
 Solucione o sistema linear pelo método da retrosubstituição.
"""
import numpy as np
import sys
from sympy import *
from sympy import Matrix
matriz = [[2,3,-1,1,5],
          [0,-2,-1,2,-7],
          [0, 0,2,3,15],
          [0, 0,0,3,15]]

print("Matriz triangularizada ")
m = np.matrix(matriz)
m = str(m).replace("[","").replace("]","")
print(m,"\n")

B = Matrix(matriz)
B2 = Matrix(matriz)


B2.col_del(4)


if not B2.is_upper:
    print("Não é triangular superior.")
    sys.exit(0)

B = list(B.col(4))

a = np.array(B2.tolist(),dtype='double')
b = np.array(B, dtype='double')

print("a ",a)
print("b ",b)
tam = len(B)
#retrosubstituição   xi = (bi − ai,i+1xi+1 · · · − ai,nxn)/ai,i,
for k in range(tam-1,-1,-1):
    b[k] = (b[k] - np.dot(a[k,k+1:tam],b[k+1:tam]))/a[k,k]
    print("x{} = {}".format(k+1,b[k]))

print("Ax = b.:\n", np.dot(a, b)," = ",B)