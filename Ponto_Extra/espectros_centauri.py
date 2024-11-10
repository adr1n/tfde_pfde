import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import h, c, k #Constantes usadas

#Aluno: André Jacinto Rodrigues
#Matrícula: 221007822

#Calcula o espectro de corpo negro para uma dada temperatura.
def espectro_corponegro(comprimento_onda, temperatura):
    # Calcula o espectro de corpo negro para uma dada temperatura.
    W = (2 * h * c**2 / comprimento_onda**5) / (np.exp(h * c / (comprimento_onda * k * temperatura)) - 1)
    return W

#Definindo os parâmetros
dic_temperaturas = {
    'Alpha Centauri A': 5790,  # Temperatura em Kelvin
    'Alpha Centauri B': 5260,
    'Proxima Centauri': 3042
}

# Intervalo de comprimento de onda em metros (visível e infravermelho próximo)
comprimento_onda = np.linspace(1e-7, 3e-6, 1000)  # De 100 nm a 3000 nm

# Plotando os espectros
plt.figure(figsize=(10, 6))

for estrela, temperatura in dic_temperaturas.items():
    espectro = espectro_corponegro(comprimento_onda, temperatura)
    plt.plot(comprimento_onda, espectro, label=f"{estrela} ({temperatura}K)")

# Configurações do gráfico
plt.title("Espectros de Radiação de Corpo Negro das Estrelas do Sistema Alpha Centauri")
plt.xlabel("Comprimento de onda [nm]")
plt.ylabel("Intensidade espectral [W/m²·nm]")
plt.legend()
plt.grid(True)
plt.yscale("log")  # Escala logarítmica para visualização
plt.tight_layout()
plt.show()

