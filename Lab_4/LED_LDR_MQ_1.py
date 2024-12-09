import matplotlib.pyplot as plt
import numpy as np
#Programa: LED_LDR_MQ_1.sce
#Ajuste do Modelo Não-linear do LED e LDR 
#Dados Experimentais - 1
N = 6
#Descartando ponto com Iled = 0, onde o LED está apagado.
R1 = 993
R2 = 981 #[ohms]
VR2 = np.array([0.530, 1.0, 1.507, 2.0, 2.51, 3.0]) #[V]
Iled1 = VR2/R2 #[A]
Rldr1 = np.array([1.25e3, 0.820e3, 0.64e3, 0.545e3, 0.482e3, 0.438e3])#[ohms]

plt.plot(Iled1,Rldr1,'or')
plt.ylabel('Rldr [ohms]')
plt.xlabel('Iled [A]')
plt.title('Resistência do LDR vs. Corrente do LED')
plt.show()