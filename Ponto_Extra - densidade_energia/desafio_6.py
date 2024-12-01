import numpy as np
import matplotlib.pyplot as plt

#Constantes 
mv = 0.98 #Massa efetiva do eletron na banda de conducao [m_e] 
mc = 0.19 #Massa efetiva do eletron na banda de valencia [m_e]
Ec = 1.1 #Energia minima da banda de conducao [eV]
Ev = 0 #Energia minima da banda de valencia [eV]
h = 6.626e-34 #Constante de planck [J*s]
E = np.linspace(Ev - 0.1, Ec + 0.1, 1000) # Faixa de energia
N = 1000
pi = 3.141592

Dc = (1 / (2 * np.power(pi, 2))) * (((2 * mc) / (h^2))^(3/2)) * np.power(E - Ec, 1/2)
Dv = (1 / (2 * np.power(pi, 2))) * (((2 * mv) / (h^2))^(3/2)) * np.power(Ev - E, 1/2)

# for k in N:
#     # Cálculo da densidade de estados para o caso dos elétrons na banda de condução
#     if E(k) > Ec: # Garantir que estamos acima da energia mínima da banda de condução
#         Dc(k) = (1 / (2 * (pi^2))) * (((2 * mc) / (h^2))^(3/2)) * (E(k) - Ec)^(1/2);
#     else:
#         Dc(k) = 0; # Para energias abaixo de Ec, a densidade de estados é zero
    
#     if E(k) < Ev:
#         Dv(k) = (1 / (2 * (pi^2))) * (((2 * mv) / (h^2))^(3/2)) * (Ev - E(k))^(1/2);
#     else:
#         Dv(k) = 0;


plt.plot(Dc, E, 'r');
# plt.gcf();
plt.plot(Dv, E, 'r');
plt.title('Modelo Dinâmico: Lâmpada Elétrica de Filamento');
plt.xlabel('t [s]');
plt.ylabel('T [K]');
