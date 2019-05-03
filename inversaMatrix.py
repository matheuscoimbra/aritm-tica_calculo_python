from sympy import eye
from sympy import Matrix
import numpy as np
import sys

def det_zero(matrix):
  if (~matrix.any(axis=0)).any() or (~matrix.any(axis=1)).any():
    return True
  else:
    for i in range(len(matrix)-1):
      col = matrix[:,i]
      lin = matrix[i,:]
      for j in range(i,len(matrix)-1):
        if np.array_equal(matrix[:,j+1],col) or np.array_equal(matrix[j+1,:],lin) :
          return True

def row_zero(row):
    linha = np.array(row)
    linha = linha[0:3,]
    print(linha)
    if not np.any(linha): #all_zeros = not np.any(a)
        return True
    else:
        return False

def invert(matriz):

    X = matriz
    npArray = np.array(X)


    n = np.shape(X)[0]

    identity = np.eye(n, dtype=int)
    identity = identity.tolist()

    # add a Im no lado direito de X resultando em M[X|I]
    for i in range(0, n):
        X[i] += identity[i]
        print(X[i])
    print()
    i = 0
    for j in range(0, n):
        difZero = col_zero(X, i)

        # If X[i][j]==0, e x[i+1][j+1]!=0, troca as linhas
        if difZero != i:
            X = troca_linha(X, i, difZero)
        # divide X[i]/X[i][j] para tornar X[i][j] == 1
        if row_zero(X[i]) == True:
            print("Não tem inversa")
            # sys.exit(0)
        if X[i][j] == 0.0:
            print("Não tem inversa")
            return
        X[i] = [m / X[i][j] for m in X[i]]

        # rescala todas as outras linhas, fazendo ficar 0 abaixo de x[i][j]
        for q in range(0, n):
            if q != i:
                lposiCerta = [X[q][j] * m for m in X[i]]
                X[q] = [X[q][m] - lposiCerta[m] for m in range(0, len(lposiCerta))]
        # se ja pecorreu a matriz
        if i == n or j == n:
            break
        i += 1

    # retorna a parte direita da matriz com a inversa
    for i in range(0, n):
        X[i] = X[i][n:len(X[i])]

    return X


# retorna index do primeiro valor != zero da coluna no indice dado
def col_zero(X, i):
    difZero = -1
    for m in range(i, len(X)):
        if difZero == -1:
            difZero = m
    return difZero


def troca_linha(X, i, p):
    X[p], X[i] = X[i], X[p]
    return X


#matriz = [[1, 2, 3], [0, 1, 4], [5, 6, 0]]
#matriz = [[2, 1, 1], [1, 1, 1], [2, 3, 2]]
matriz =[[1, -1, 3], [1, 1, 1], [2, -1, 5]]
#matriz = [[3, -2, 3],[1, 3, 6],[2, 6, 12]]
X = invert(matriz)
print("Inversa ",X)

#M = Matrix([[1, 2, 3], [0, 1, 4], [5, 6, 0]])
#M = Matrix([[2, 1, 1], [1, 1, 1], [2, 3, 2]])
#M = Matrix([[3, -2, 3],[1, 3, 6],[2, 6, 12]])
M = Matrix([[1, -1, 3], [1, 1, 1], [2, -1, 5]])
try:
    print(M ** -1)
except Exception :
    print("Sem inversa")
