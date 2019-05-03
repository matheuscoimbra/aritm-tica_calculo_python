import numpy as np
import sympy as sp
x1,x2 =sp.symbols('x1,x2', real=True)

"""
QUESTÃO DA PÁGINA 205 DO LIVRO BASE
LETRA D
"""

# f1= 4*x1 - x1**3 + x2
# f2=(-x1**2)/9 + ((4*x2 - x2**2)/4) + 1
#
f1= 10*(x2-x1**2)
f2=1 - x1
# print(f1)
# print(f2)
Fun = sp.Matrix([f1,f2])
J = Fun.jacobian([x1,x2])
# print(J)


def F(x):
    y = np.zeros(2)
    # y[0] = 4*x[0] - x[0]**3 + x[1]
    # y[1] = (-x[0]**2)/9 + (4*x[1]-x[1]**2)/4 + 1
    y[0] = 10*(x[1]-x[0]**2)
    y[1] = 1 - x[0]
    return y

def JF(x):
    y = np.zeros((2, 2))
    # y[0, 0] = -3*x[0]**2 + 4
    # y[0, 1] = 1
    # y[1, 0] = -2*x[0]/9
    # y[1, 1] = -x[1]/2 + 1
    y[0, 0] = -20 * x[0]
    y[0, 1] = 10
    y[1, 0] = -1
    y[1, 1] = 0
    return y

#x0 = np.array([-1,-2])
x0 = np.array([-1.2,1])
TOL = 0.0001
N = 3
def newton(F, JF, x0, TOL, N):
    # preliminares

    x = np.copy(x0).astype('double')
    k = 0
    # iteracoes
    while (k < N):
        k += 1
        # iteracao Newton
        delta = -np.linalg.inv(JF(x)).dot(F(x))
        x = x + delta
        # criterio de parada
        if (np.linalg.norm(delta, np.inf) < TOL):
            print("\nResultado:",x)
    #raise NameError('num. max. iter. excedido.')
print("Sistema: \n",f1,"\n",f2)
print("Jacobiano:\n",J)
newton(F, JF, x0, TOL, N)