import numpy as np
"""
A matriz L é construída a partir da matriz identidade I, ao longo do escalona-
mento de A. Os elementos da matriz L são os múltiplos do primeiro elemento da
linha de A a ser zerado dividido pelo pivô acima na mesma coluna.

Por exemplo, para zerar o primeiro elemento da segunda linha de A, calculamos
L21 = A21/A11

e fazemos

A2,: ⇐ A2,: − L21A1,:

Para zerar o primeiro elemento da terceira linha de A, temos

L31 = A31/A11

e fazemos

A3,: ⇐ A3,: − L31A1,:
até chegarmos ao último elemento da primeira coluna de A.
"""

def fatoraLU(A):
    U = np.copy(A)
    n = np.shape(U)[0]

    L = np.eye(n)
    for j in np.arange(n - 1):
        for i in np.arange(j + 1, n):
            L[i, j] = U[i, j] / U[j, j]
            for k in np.arange(j + 1, n):
                U[i, k] = U[i, k] - L[i, j] * U[j, k]
            U[i, j] = 0
    return L, U


E = np.array([[6, -2, 2, 4], [12, -8, 6, 10],
              [3, 13, 9, 3],
              [-6, 4, 1, -18]], dtype='double')

A = E[:]

L, U = fatoraLU(E)

print("L->\n", L)
print("U->\n", U)

########
b = np.array([[12], [34], [27], [-38]], dtype='double')
E = np.append(L, b, axis=1)
print("Ly = b->\n", E)

#######

x = np.zeros(4)
x[0] = E[0, 4] / E[0, 0];
x[1] = (E[1, 4] - E[1, 0] * x[0]) / E[1, 1];
x[2] = (E[2, 4] - E[2, 0] * x[0] - E[2, 1] * x[1]) / E[2, 2]
x[3] = (E[3, 4] - E[3, 0] * x[0] - E[3, 1] * x[1] - E[3, 2] * x[2]) / E[3, 3]
print(x)

###########
b = np.array([[x[0]], [x[1]], [x[2]], [x[3]]], dtype='double')
E = np.append(U, b, axis=1)
print("Ux = y->\n", E)

x = np.zeros(4)
x[3] = E[3, 4] / E[3, 3];
x[2] = (E[2, 4] - E[2, 3] * x[3]) / E[2, 2];
x[1] = (E[1, 4] - E[1, 3] * x[3] - E[1, 2] * x[2]) / E[1, 1]
x[0] = (E[0, 4] - E[0, 3] * x[3] - E[0, 2] * x[2] - E[0, 1] * x[1]) / E[0, 0]

print("\nresultado=> ", x, "\n")
[print("x{}".format(i), "|", "{:.2f}".format(x[i]), "|") for i in range(len(x))]

s = np.dot(U, x)

print("\nAx  = b ")
print(str(np.c_[s, b]).replace('[', '').replace(']', ''))

ALU = np.dot(L,U)
print("\nA = LU.:\n")
print("LU ",ALU)
print("A ",A)