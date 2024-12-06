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
Iled = VR2/R2 #[A]
Rldr = np.array([1.25e3, 0.820e3, 0.64e3, 0.545e3, 0.482e3, 0.438e3])#[ohms]

plt.plot(Iled,Rldr,'or')
plt.ylabel('Rldr [ohms]')
plt.xlabel('Iled [A]')
plt.title('Resistência do LDR vs. Corrente do LED')
plt.show()

# MODELO:
# Gldr = C1*sqrt(Iled) + C2
VR2alvo = np.array([0, 0.507, 1.0, 1.501, 2.0, 2.5, 3.0])
VR1 = np.array([0, 5.19, 6.55, 7.28, 7.74, 8.07, 8.32])

Rldr = (12-VR1/(VR1/R2)  # Resistência em ohms
Iled = np.array([1, 2, 3, 4, 5, 6]) / 979  # Corrente em amperes
Gldr = 1 / Rldr  # Condutância

# Funções Base Não-Ortogonais
g1 = np.sqrt(Iled)
g2 = np.ones(len(Iled))
a11 = np.sum(g1 * g1)
a12 = np.sum(g1 * g2)
a21 = np.sum(g2 * g1)
a22 = np.sum(g2 * g2)
b1 = np.sum(Gldr * g1)
b2 = np.sum(Gldr * g2)

# Resolvendo o sistema linear
A = np.array([[a11, a12], [a21, a22]])
b = np.array([b1, b2])
C = np.linalg.solve(A, b)

print("C =", C)

# Gerando os dados para o gráfico
M = 100
Iledc = np.linspace(np.min(Iled), np.max(Iled), M)
Gldrc = C[0] * np.sqrt(Iledc) + C[1]
Rldrc = 1 / Gldrc

# Plotando os resultados
plt.plot(Iledc, Rldrc, 'b', label="Rldr Modelado")
plt.xlabel("Iled (A)")
plt.ylabel("Rldr (Ohms)")
plt.legend()
plt.grid()
plt.show()

# Calcular o modelo para os valores de Iled originais
Gldr0 = C[0] * np.sqrt(Iled) + C[1]
Rldr0 = 1 / Gldr0

# Erro Quadrático Médio Percentual
N = len(Rldr)
EQMP = 100 * (1 / N) * np.sum(((Rldr - Rldr0) / Rldr) ** 2)
print("EQMP% =", EQMP)