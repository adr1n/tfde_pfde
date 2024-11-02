import numpy as np
from scipy.integrate import quad
import scipy.constants as const

# Definindo a função espectral de Planck
def planck(wavelength, temperature):
    """Calcula a densidade espectral de potência por unidade de comprimento de onda para um corpo negro"""
    # Constantes físicas
    h = const.h       # Constante de Planck (J s)
    c = const.c       # Velocidade da luz (m/s)
    k_B = const.k     # Constante de Boltzmann (J/K)

    # Função espectral de Planck
    return (2 * h * c**2 / wavelength**5) / (np.exp(h * c / (wavelength * k_B * temperature)) - 1)

# Temperatura do filamento (K)
temperature = 3000

# Limites de comprimento de onda para a faixa visível (em metros)
visible_min = 400e-9  # 400 nm
visible_max = 700e-9  # 700 nm

# Integração da função de Planck na faixa visível (400-700 nm)
visible_power, _ = quad(planck, visible_min, visible_max, args=(temperature,))

# Integração da função de Planck de 0 até o infinito (potência total)
total_power, _ = quad(planck, 1e-9, np.inf, args=(temperature,))

# Cálculo do percentual de energia na faixa visível
visible_fraction = (visible_power / total_power) * 100

print(f"Temperatura do corpo negro: {temperature} K")
print(f"Fração de potência irradiada na faixa visível (400 a 700 nm): {visible_fraction:.2f}%")
