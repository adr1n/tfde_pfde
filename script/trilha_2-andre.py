#Programa: Trilha_1.py
#Ajuste por mínimos quadrados 
#PFDE - Lab#1  
import numpy as np
import matplotlib.pyplot as plt

N = 8
Vi = [0, 0.919, 1.791, 2.65, 3.28, 3.63, 4.03, 5.22]     
i = np.arange(1,N+1,1)
W = 0.01
xi = W*(i-1) + W/2
plt.plot(xi, Vi, 'r.')

#Ajuste do Modelo
g = xi - W/2
k = np.sum(Vi*g)/np.sum(g*g)
xc = np.linspace(np.min(xi),np.max(xi),100)
yc = k*(xc - W/2)
plt.plot(xc, yc, 'b')
plt.xlabel('x [m]')
plt.ylabel('V [volt]')

#EQM
EQM = (1/N)*sum(np.square(Vi-k*(xi-W/2)))
print("EQM =", EQM)
plt.text(0.02,5,'EQM = ' + str(EQM))
plt.title("Trilha 2 - André Rodrigues")
plt.show()