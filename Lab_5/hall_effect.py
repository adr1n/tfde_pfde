import numpy as np
import matplotlib.pyplot as plt

# Programa: MQ_Hall.py
# Exemplo: Ajuste de Modelo por Mínimos Quadrados do Sensor Hall

# Dados Experimentais
Vs_max = 4.42  # [V] Valor medido no ângulo teta = 0 graus
ks = 3.125e-3  # [V/Gauss] Constante do Sensor (Dados do Fabricante)
N = 12  # Número de Pontos Experimentais
Vso = 2.48  # [V] Valor medido na ausência de campo magnético
teta = np.array([0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330])  # ângulo [graus]

# Valores medidos da tensão de saída Vs para cada valor de ângulo
Vs = np.array([4.81, 4.52, 3.58, 2.47, 1.437, 0.611, 0.410, 0.525, 1.307, 2.56, 3.44, 4.31])  # [V]

# Cálculo de B0
B0 = (Vs_max - Vso) / ks  # [Gauss]

# Cálculo de Bz em função de B0, para cada ângulo
Bz = B0 * np.cos(np.radians(teta))  # [Gauss]

# Ajuste do Modelo Não-linear
g1 = np.cos(np.radians(teta))
g2 = np.ones(N)
a11 = np.sum(g1 * g1)
a12 = np.sum(g1 * g2)
a21 = np.sum(g2 * g1)
a22 = np.sum(g2 * g2)
b1 = np.sum(Vs * g1)
b2 = np.sum(Vs * g2)

# Sistema linear
A = np.array([[a11, a12], [a21, a22]])
b = np.array([b1, b2])
alfa = np.linalg.solve(A, b)
print("alfa (Não-linear) =", alfa)

# Modelo ajustado
M = 100
angulo = np.linspace(np.min(teta), np.max(teta), M)
gc1 = np.cos(np.radians(angulo))
gc2 = np.ones(M)
Vs_lin = alfa[0] * gc1 + alfa[1] * gc2

# Plotando o Modelo Não-linear
plt.figure(1)
plt.plot(teta, Vs, 'or', label="Pontos Experimentais")
# plt.plot(angulo, Vs_lin, 'b', label="Modelo Ajustado Não-linear")
plt.xlabel('Ângulo [graus]')
plt.ylabel('Vs [volts]')
plt.title('Sensor Hall - Modelo Não-linear')
plt.legend()
plt.grid()

# Erro Quadrático Médio (Não-linear)
Vs_mod_lin = alfa[0] * g1 + alfa[1] * g2
EQM_nl = (1 / N) * np.sum((Vs_mod_lin - Vs) ** 2)
print("EQM (Mod. Não-linear) =", EQM_nl)

# Ajuste do Modelo Linear
g1 = Bz
g2 = np.ones(N)
a11 = np.sum(g1 * g1)
a12 = np.sum(g1 * g2)
a21 = np.sum(g2 * g1)
a22 = np.sum(g2 * g2)
b1 = np.sum(Vs * g1)
b2 = np.sum(Vs * g2)

# Sistema linear
A = np.array([[a11, a12], [a21, a22]])
b = np.array([b1, b2])
alfa = np.linalg.solve(A, b)
print("alfa (Linear) =", alfa)

# Modelo ajustado
campo_z = np.linspace(np.min(Bz), np.max(Bz), M)
gc1 = campo_z
gc2 = np.ones(M)
Vs_nlin = alfa[0] * gc1 + alfa[1] * gc2

# Plotando o Modelo Linear
plt.figure(2)
plt.plot(Bz, Vs, 'or', label="Pontos Experimentais")
plt.plot(campo_z, Vs_nlin, 'b', label="Modelo Ajustado Linear")
plt.xlabel('Bz [Gauss]')
plt.ylabel('Vs [volts]')
plt.title('Sensor Hall - Modelo Linear')
plt.legend()
plt.grid()

# Erro Quadrático Médio (Linear)
Vs_mod_nlin = alfa[0] * g1 + alfa[1] * g2
EQM_l = (1 / N) * np.sum((Vs_mod_nlin - Vs) ** 2)
print("EQM (Mod. Linear) =", EQM_l)

plt.show()
