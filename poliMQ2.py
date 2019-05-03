import numpy as np
"""
CONSTRUIR O MELHOR POLINOMIO P2(X) QUE SE AJUSTE AOS DADOS PELO MÉTODO DOS MINIMOS QUADRADOS
"""

def poli(xData,yData,m):
    a = np.zeros((m+1,m+1))
    b = np.zeros((m+1,1))
    s = np.zeros(2*m+1)
    for i in range(len(xData)):
        temp = yData[i]
        for j in range(m+1):
            b[j,] = b[j,] + temp
            temp = temp*xData[i]
        temp = 1.0
        for j in range(2*m+1):
            s[j] = s[j] + temp
            temp = temp*xData[i]
    for i in range(m+1):
        for j in range(m+1):
            a[i, j] = s[i + j]
    a = np.array(a)
    b = np.array(b)
    print("equações normais:\n")
    print(a)
    print(b)

    E = np.append(a, b, axis=1)
    for i in range(1, len(E)):
        for j in range(i, len(E)):
            E[j, :] = E[j, :] - (E[j, i - 1] / E[i - 1, i - 1]) * E[i - 1, :]

    x = np.zeros(3)
    x[0] = E[2, 3] / E[2, 2]
    x[1] = (E[1, 3] - E[1, 2] * x[0]) / E[1, 1]
    x[2] = (E[0, 3] - E[0, 2] * x[0] - E[0, 1] * x[1]) / E[0, 0]
    return x

#DADOS
# xData = np.array([1.0,4.0,6.0,7.0], dtype="double")
# yData = np.array([-3.0,-2.0,-1.0,2.0], dtype="double")
xData = np.array([0.0,0.25,0.50,0.75,1.00], dtype="double")
yData = np.array([-153.0,64.0,242.0,284.0,175.0], dtype="double")

m=2
poli = poli(xData,yData,m)
print("\nResultado:")
print("P2(x)={}x² +({}x) + ({})".format(round(poli[0],2),round(poli[1],2),round(poli[2],2)))