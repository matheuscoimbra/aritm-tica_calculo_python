import numpy as np
import sys
import re

A = np.array([[6, 2, 0, 0, 0],
              [-1, 7, 2, 0, 0],
              [0, -2, 8, 2, 0],
              [0, 0, 3, 7, -2],
              [0, 0, 0, 0, 0]], dtype='double')

b = np.array([[2], [-3], [4], [-3], [0]], dtype='double')

# A = np.array([[1, 1, 1, 1, 1],
#               [1, 2, 4, 1, 1],
#               [0, 1, 2, 2, 2],
#               [1, 2, 1, 3, 1],
#               [3, 5, 1, 1, 1]], dtype='double')
#
# b = np.array([[0], [1], [1], [0], [0]], dtype='double')


# A = np.array([[1, 1, 1, 1, 1],
#               [1, 2, 4, 1, 1],
#               [0, 1, 2, 2, 2],
#               [1, 2, 1, 3, 1],
#               [0, 0, 0, 0, 0]], dtype='double')
#
# b = np.array([[0], [1], [1], [0], [3]], dtype='double')


# A = np.array([[1, 2, -3],
#               [6, 3, -9],
#               [7, 14, -21]
#               ], dtype='double')
#
# b = np.array([[2], [6], [13]], dtype='double')
# A = np.array([[4, -6, -3],
#               [1, 1, -2],
#               [4, -20, -4]
#               ], dtype='double')
#
# b = np.array([[12], [3], [6]], dtype='double')

# A = np.array([[1, -1, 3],
#              [1, 1, 1],
#              [2, -1, 5]
#              ], dtype='double')
#
# b = np.array([[1], [-3], [0]], dtype='double')

# A = np.array([[3, -2, 3],
#               [1, 3, 6],
#               [2, 6, 12],
#               ], dtype='double')
#
# b = np.array([[8], [-3], [-6]], dtype='double')

E = np.append(A, b, axis=1)
aux = np.copy(E[1, :])
E[1, :] = np.copy(E[0, :])
E[0, :] = np.copy(aux)

for i in range(1, len(E)):
    for j in range(i, len(E)):
        E[j, :] = E[j, :] - (E[j, i - 1] / E[i - 1, i - 1]) * E[i - 1, :]
print(E)


def det_zero(matrix):
    if (~matrix.any(axis=0)).any() or (~matrix.any(axis=1)).any():
        return True
    else:
        for i in range(len(matrix) - 1):
            col = matrix[:, i]
            lin = matrix[i, :]
            for j in range(i, len(matrix) - 1):
                if np.array_equal(matrix[:, j + 1], col) or np.array_equal(matrix[j + 1, :], lin):
                    return True


def row_zero(matrix):
    index = -1
    for i in range(len(matrix)):
        lin = matrix[i, :]
        if not np.any(lin) == True:
            index = i
            return index
    return index



Ab = np.append(A, b, axis=1)

rankA = np.linalg.matrix_rank(A)
rankAb = np.linalg.matrix_rank(Ab)
# print("RankA: ",rankA," rankAb: ",rankAb)
m, n = np.shape(A)
col = b.tolist()

X = np.zeros(n)

det = det_zero(A)

nonB = np.delete(E, m, 1)
# print(nonB)
B = E[:, m]



if m == n:
    ind = row_zero(nonB)
    if (rankAb == rankA) and ind == -1:
        print("Sistema é consistente e possui uma única solução")
    else:

        if ind != -1:
            if B[ind] != 0.0:  # verificar coluna tbm
                print("Sistema é inconsistente")
            else:
                print("Sistema possui infinitas soluções")
                E = np.delete(E, ind, 0)
                # print(E)
                b = E[:, m]
                a = np.delete(E, m, 1)
                tam = len(E)

                l = 0
                strr = ""
                for i in range(tam):

                    ei = a[i]  # linha
                    eii = a[i][i]
                    rep = 0
                    for k in range(len(ei)):
                        if ei[k] == 0.0 or ei[k] == eii:
                            if ei[k] == eii and rep !=1:
                                rep = 1
                                continue
                        strr += "{}x{} ".format(ei[k], k + 1)

                        regexp = re.compile(r'\s\d+(\s)?')
                        if regexp.search(strr):
                           # strr = strr.strip()
                            strr = strr.replace(" ", "+")


                    strr = "(" + strr + ")"
                    strr = strr.replace("+)", ")")
                    print("x{} ={} - {}/{}".format(i + 1, b[i], strr, eii))
                    strr = ""

all_zeros = not np.any(b)
if m < n:
    print("Sistema é inconsistente")
if m > n:
    if all_zeros == True:
        print("Sistema possui infinitas soluções")
        print("Sol.: ", X)
    if rankA == min(m, n):
        print("Sistema possui infinitas soluções")

