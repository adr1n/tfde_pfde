import matplotlib.pyplot as plt
import numpy as np
#Programa: LED_LDR_MQ_1.sce
#Ajuste do Modelo Não-linear do LED e LDR 
#Dados Experimentais - 1

R1 = 993
R2 = 981 #[ohms]
# MODELO:
# Gldr = C1*sqrt(Iled) + C2
VR2alvo = np.array([0.507, 1.0, 1.501, 2.0, 2.5, 3.0])
VR1 = np.array([5.19, 6.55, 7.28, 7.74, 8.07, 8.32])

Rldr = (12/VR1 - 1)*R1  # Resistência em ohm [conta simplificada de: (12 - VR1)/(VR1/R1) ]
                    #                                                   ^^^^^^^^   ^^^^^^
                    #                                              tensao no ldr   corrente no ldr (é a mesma no R1)
print("Rldr:", Rldr)

Ildr = (12 - VR1)/Rldr  
print("Ildr", Ildr)

Iled = VR2alvo / R2  # Corrente em amperes
print("Iled", Iled)

Gldr = 1 / Rldr # Condutância
print("Gldr:", Gldr)

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
plt.plot(Iledc, Gldrc, 'b', label="Gldr Modelado")
plt.plot(Iled, Gldr, 'or', label="Gldr Medido")
plt.xlabel("Iled (A)")
plt.ylabel("Gldrc (Ohms⁻¹)")
plt.legend()
plt.grid()
plt.show()


# Calcular o modelo para os valores de Iled originais
Gldr0 = C[0] * np.sqrt(Iled) + C[1]

# Erro Quadrático Médio Percentual
N = len(Gldr)
EQMP = 100 * (1 / N) * np.sum(((Gldr - Gldr0) / Gldr) ** 2)
print("EQMP% =", EQMP)