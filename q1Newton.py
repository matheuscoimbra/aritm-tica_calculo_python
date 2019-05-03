from __future__ import division
import numpy as np
"""
QUESTAO: ENCONTRE UM P5(X) PELO MÉTODO DE NEWTON E ESTIME PARA F(1,23)
"""

x = np.array([0.0,0.5,1.0,1.5,2.0,2.5], dtype="double")
y = np.array([-2.78,-2.41,-1.65,-0.594,1.34,4.564], dtype="double")
#inicializando a tabela
T = np.zeros((6,6))
#primeira ordem
T[:,0]=y
#segunda ordem
T[1,1]=(T[1,0]-T[0,0])/(x[1]-x[0])
T[2,1]=(T[2,0]-T[1,0])/(x[2]-x[1])
T[3,1]=(T[3,0]-T[2,0])/(x[3]-x[2])
T[4,1]=(T[4,0]-T[3,0])/(x[4]-x[3])
T[5,1]=(T[5,0]-T[4,0])/(x[5]-x[4])
#terceira ordem
T[2,2]=(T[2,1]-T[1,1])/(x[2]-x[0])
T[3,2]=(T[3,1]-T[2,1])/(x[3]-x[1])
T[4,2]=(T[4,1]-T[3,1])/(x[4]-x[2])
T[5,2]=(T[5,1]-T[4,1])/(x[5]-x[3])
#quarta ordem
T[3,3]=(T[3,2]-T[2,2])/(x[3]-x[0])
T[4,3]=(T[4,2]-T[3,2])/(x[4]-x[1])
T[5,3]=(T[5,2]-T[4,2])/(x[5]-x[2])
#Quinta ordem
T[4,4]=(T[4,3]-T[3,3])/(x[4]-x[0])
T[5,4]=(T[5,3]-T[4,3])/(x[5]-x[1])
#Sexta ordem
T[5,5]=(T[5,4]-T[4,4])/(x[5]-x[0])
print(T)

#polinomio interpolador
#P5(X)
X = 1.23
P0 = T[0,0]
P1 = P0 + (X-x[0])*T[1,1]
P2 = P1 + (X-x[0])*(X-x[1])*T[2,2]
P3 = P2 + (X-x[0])*(X-x[1])*(X-x[2])*T[3,3]
P4 = P3 + (X-x[0])*(X-x[1])*(X-x[2])*(X-x[3])*T[4,4]
P5 = P4 + (X-x[0])*(X-x[1])*(X-x[2])*(X-x[3])*(X-x[4])*T[5,5]
# print(T[0,0])
# print(T[1,1])
# print(T[2,2])
# print(T[3,3])
# print(T[4,4])
# print(T[5,5])
print("P(1,23)=", P5)
