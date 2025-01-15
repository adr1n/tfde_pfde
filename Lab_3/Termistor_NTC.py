import numpy as np
import matplotlib.pyplot as plt

#%Programa: Termistor_NTC.sce
#Cálculo da temperatura do termistor NTC 5D-9
R2 = 10 #Coloque aqui o valor do Resistor R2 [ohms]
Tamb = 21 #Temperatura Ambiente [Graus Centígrados]
K = 11e-3 #[W/Graus] Coeficiente Térmico de Dissipação por Convecção
#Pontos Experimentais
N = 8
#Coloque aqui os valores medidos de Va e Vb:
Va = np.array([0.554, 1.051, 1.519, 2.020, 2.500, 3.00, 3.47, 3.97]) #[V]
Vb = np.array([0.390, 0.742, 1.105, 1.517, 1.925, 2.39, 2.84, 3.31]) #[V]
#Cáculo da Corrente (I)) e da Resistência (R1)
I = Vb/R2 #[A]
Vab = Va - Vb #[V]
Pe = Vab * I # [W] Potência Elétrica sobre o termistor
R1 = Vab/I #[ohm] Resistência do Termistor
print("R1 =", R1)
#Sabendo que:Pe = P = K*(T-Tamb); #[W] Potência Térmica Dissipada
T = (Pe/K)+Tamb #[Graus] Temperatura do Termistor
print("T =", T)

plt.plot(T, R1,'ro')
plt.plot(T, R1,'b')
plt.xlabel('T[Graus]')
plt.ylabel('R1[Ohms]')
plt.title('Gráfico: R1 vs. T')
plt.show()
