#Programa: MQ_Lâmpada.py
#Ajuste por mínimos quadrados 
#PFDE - Lab#2  
import numpy as np
import matplotlib.pyplot as plt

#Pontos Experimentais
N = 7 #Número de Pontos Experimentais
#SUBSTITUA AQUI OS VALORES MEDIDOS:
yp = [ 0.12, 0.16, 0.21, 0.25, 0.28, 0.32 ] #Corrente [A]     
xp = [ 1.89, 3.55, 5.57, 7.53, 9.11, 11.38 ] #Tensão [V]
plt.plot(xp, yp, 'r.')
#Obs: R1 = xp/yp
#Modelo Adotado: y = k*(x^p)
p = 3/5 #Expoente Fracionário (Modelo) 
g = np.power(xp,p) #Função Base
k = np.sum(yp*g)/np.sum(g*g)
xc = np.linspace(np.min(xp),np.max(xp),100)
yc = k*np.power(xc,p) #Modelo Ajustado
plt.plot(xc, yc, 'b')
plt.xlabel('Tensão [V]')
plt.ylabel('Corrente [A]')
plt.title('Modelo Ajustado - André')

#Erro Quadrático Médio
ym = k*np.power(xp,p) #Valores da Corrente
EQM = (1/N)*sum(np.square(yp-ym));
plt.text(2,0.30,'EQM = ' + str(EQM))
plt.show()
