#Programa: Trilha_1.py
#Ajuste por mínimos quadrados 
#PFDE - Lab#1  
import numpy as np #Manipulação numérica
import matplotlib.pyplot as plt #Visualização gráfica

N = 16 #Número de dados
Vi = [0, 0.444, 0.752, 1.042, 1.337, 1.665, 2.04, 2.42, 2.75, 3.13, 3.48, 
      3.81, 4.29, 4.40, 4.74, 5.22 ]     #Arranjo dos dados obtidos
i = np.arange(1,N+1,1)  #Array de índices    
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
plt.text(0.02,5,'EQM = ' + str(EQM))
plt.title("Trilha 1 - André Rodrigues")
plt.show()
