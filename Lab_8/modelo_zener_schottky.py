import numpy as np
import matplotlib.pyplot as plt

# Função para simular a curva I x V para o diodo Schottky
def schottky_iv_curve(V, I_s=1e-9, n=1, T=300):
    q = 1.602e-19  # Carga do elétron (C)
    k = 1.381e-23  # Constante de Boltzmann (J/K)
    I = I_s * (np.exp((q * V)/(n * k * T)) - 1)
    return I

# Função para simular a curva I x V para o diodo Zener
def zener_iv_curve(V, Vz=6.2, Iz_max=50e-3, I_s=1e-12, n=1.5, T=300):
    q = 1.602e-19
    k = 1.381e-23
    I = np.where(V >= 0, I_s * (np.exp((q * V)/(n * k * T)) - 1), -Iz_max * np.exp((V + Vz)/0.1))
    return I

def exp(V):
    e = 2.71
    result = pow(e, V)
    return result

# Geração de tensões para simulação
V = np.linspace(-10, 10, 1000)  # Tensão de -10V a 1V

# Cálculo das correntes para cada diodo
I_schottky = schottky_iv_curve(V)
I_zener = zener_iv_curve(V)

# Plot das curvas I x V
plt.figure(figsize=(12, 6))

# Plot para o diodo Schottky
plt.subplot(1, 2, 1)
plt.plot(V, exp(V), label='Schottky - 30 Hz')
plt.yscale('log')
plt.xlabel('Tensão (V)')
plt.ylabel('Corrente (A)')
plt.title('Curva I x V - Diodo Schottky')
plt.grid(True)
plt.legend()

# Plot para o diodo Zener
plt.subplot(1, 2, 2)
plt.plot(V, I_zener, label='Zener - 30 Hz', color='r')
plt.yscale('log')
plt.xlabel('Tensão (V)')
plt.ylabel('Corrente (A)')
plt.title('Curva I x V - Diodo Zener')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
