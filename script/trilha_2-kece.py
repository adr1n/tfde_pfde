#Programa: Trilha_1.py
#Ajuste por mínimos quadrados 
#PFDE - Lab#1  
import numpy as np #Manipulação numérica
import matplotlib.pyplot as plt #Visualização gráfica

N = 8 #Número de dados
Vi = [0, 1.34, 1.74, 2.29, 2.83, 3.30, 4.02, 4.62] #Arranjo dos dados obtidos
i = np.arange(1,N+1,1) #Número de dados
W = 0.01 #Definindo a largura dos eixos
xi = W*(i-1) + W/2 #Cálculo das posições dos dados
plt.plot(xi, Vi, 'r.') #Plotando os pontos medidos em vermelho

#Ajuste do Modelo
g = xi - W/2 #Translação das coordenadas
k = np.sum(Vi*g)/np.sum(g*g) #Fórmula de mínimos quadrados
xc = np.linspace(np.min(xi),np.max(xi),100) #Xc cria um array com 100 pontos igualmente espaçados entre os valores mínimos e máximos de xi
yc = k*(xc - W/2) #Yc calcula os valores ajustados correspondentes.
plt.plot(xc, yc, 'b') #Plotando a linha de ajuste em azul
plt.xlabel('x [m]')
plt.ylabel('V [volt]')

#EQM
EQM = (1/N)*sum(np.square(Vi-k*(xi-W/2))) #Cálculo de EQM
print("EQM =", EQM)
plt.text(0.02, 4.5,'EQM = ' + str(EQM))
plt.title("Trilha 2 - Kece Line")
plt.show()
