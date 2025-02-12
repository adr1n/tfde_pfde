import numpy as np
import matplotlib.pyplot as plt

# Parte-I: Fotocondutivo
R1 = 0.996e3  # [ohms]
R2 = 0.99e6   # [ohms]

Vdc1a = np.array([0, 5, 10, 15, 20, 25])
Vdc2a = 12.05  # [V]
V1a = np.array([0, 3.25, 8.06, 12.97, 17.81, 22.7])
V2a = np.array([0, 100e-3, 215e-3, 360e-3, 461e-3, 511e-3])
Vled1a = Vdc1a - V1a
Vled2a = Vdc2a - V2a
Iled1a = V1a / R1
Iled2a = V2a / R2
P1a = Vled1a * Iled1a
P2a = Vled2a * Iled2a

plt.figure(1)
plt.plot(P1a, P2a, 'or')

# Parte-II: Fotovoltaico
Vdc1b = np.array([0, 5, 10, 15, 20, 25])
V1b = np.array([0, 3.12, 8.05, 12.90, 17.74, 22.7])
V2b = np.array([0, -86.5e-3, -224e-3, -280e-3, -361e-3, -427e-3])
Vled1b = Vdc1b - V1b
Vled2b = V2b
Iled1b = V1b / R1
Iled2b = V2b / R2
P1b = Vled1b * Iled1b
P2b = Vled2b * Iled2b

plt.figure(2)
plt.plot(P1b, P2b, 'or')

# Parte-III: I vs V Fotovoltaico
R = np.array([96e3, 196e3, 311e3, 398e3, 500e3, 640e3, 720e3, 850e3, 1.10e6, 1.27e6, 1.5e6, 2.02e6])
V = np.array([-52e-3, -105e-3, -162e-3, -20e-3, -250e-3, -320e-3, -350e-3, -14e-3, -510e-3, -581e-3, -634e-3, -450e-3, -842e-3])
Rmult = 20e6
Reff = 1 / ((1 / R) + (1 / Rmult))
Reff[-1] = 20e6  # Correção: Aqui apenas R do multímetro.
I = V / Reff
IL = I[0]  # IL ~ I(R pequeno), V ~ 0

plt.figure(3)
plt.plot(V, I, 'ro')
plt.plot(V, I, 'b')
plt.xlim([0, 1.4])
plt.ylim([0, 6e-7])
plt.title('I vs. V (Modo Fotovoltaico)')
plt.xlabel('V [volt]')
plt.ylabel('I [A]')

# Ajuste Linear da Parte-I
g = P1a  # Função Base
f = P2a
eta = np.sum(f * g) / np.sum(g * g)  # Ajuste da Constante do Modelo
print(eta)

plt.figure(1)
N = 100
x = np.linspace(0, np.max(P1a), N)
y = eta * x
plt.plot(x, y, 'b')
plt.title('P2 vs. P1 (Fotocondutivo)')
plt.xlabel('P1 [W]')
plt.ylabel('P2 [W]')

# Ajuste Linear da Parte-II
g = P1b  # Função Base
f = P2b
eta = np.sum(f * g) / np.sum(g * g)  # Ajuste da Constante do Modelo
print(eta)

plt.figure(2)
N = 100
x = np.linspace(0, np.max(P1b), N)
y = eta * x
plt.plot(x, y, 'b')
plt.title('P2 vs. P1 (Fotovoltaico)')
plt.xlabel('P1 [W]')
plt.ylabel('P2 [W]')

plt.show()