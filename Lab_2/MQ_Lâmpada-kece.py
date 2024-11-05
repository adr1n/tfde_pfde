#Programa: MQ_Lâmpada.py
#Ajuste por mínimos quadrados 
#PFDE - Lab#2  
import numpy as np
import matplotlib.pyplot as plt

#Pontos Experimentais
N = 7 #Número de Pontos Experimentais
yp = [ 0.10, 0.16, 0.21, 0.25, 0.28, 0.31 ] #Corrente [A]     
xp = [ 1.9, 3.55, 5.57, 7.53, 9.10, 11.38 ] #Tensão [V]
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
plt.title('Modelo Ajustado - Kece')

#Erro Quadrático Médio
ym = k*np.power(xp,p) #Valores da Corrente
EQM = (1/N)*sum(np.square(yp-ym))
plt.text(2,0.30,'EQM = ' + str(EQM))
# plt.show()

# Cálculo de R1 para V_AB = -7.0 V usando o modelo
V_AB = -7.0
I_AB = k * np.power(abs(V_AB), p)  # Corrente prevista para V_AB (usando valor absoluto)
R1_AB = V_AB / I_AB  # R1 = V_AB / I_AB

# Resultados calculados
print(k, I_AB, EQM, R1_AB)