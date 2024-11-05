import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import h, c, k

# Constantes e função de espectro de corpo negro
def blackbody_spectrum(wavelength, temperature):
    """Calcula o espectro de corpo negro para uma dada temperatura."""
    return (2 * h * c**2 / wavelength**5) / (np.exp(h * c / (wavelength * k * temperature)) - 1)

# Definindo os parâmetros
temperatures = {
    'Alpha Centauri A': 5790,  # Temperatura em Kelvin
    'Alpha Centauri B': 5260,
    'Proxima Centauri': 3042
}

# Intervalo de comprimento de onda em metros (visível e infravermelho próximo)
wavelengths = np.linspace(1e-7, 3e-6, 1000)  # De 100 nm a 3000 nm

# Plotando os espectros
plt.figure(figsize=(10, 6))

for star, temperature in temperatures.items():
    spectrum = blackbody_spectrum(wavelengths, temperature)
    plt.plot(wavelengths * 1e9, spectrum, label=f"{star} ({temperature}K)")

# Configurações do gráfico
plt.title("Espectros de Radiação de Corpo Negro das Estrelas do Sistema Alpha Centauri")
plt.xlabel("Comprimento de onda (nm)")
plt.ylabel("Intensidade espectral (W/m²·nm)")
plt.legend()
plt.grid(True)
plt.yscale("log")  # Escala logarítmica para visualização
plt.tight_layout()
plt.show()

