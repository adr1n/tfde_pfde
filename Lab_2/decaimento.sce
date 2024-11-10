// Parâmetros
M = 4.6e-3; // [g] Massa do Filamento
R2 = 1; // [ohm]
Klt = 0.011; // [ohm/K] Constante do Filamento (Resistência)
Kr = 3.3e-14; // [W/K^4] Constante do Filamento (Radiação)
Tamb = 300; // [K] Temperatura Inicial (Ambiente)
cp = 0.13; // [J/g.K] Calor Específico
Ct = cp * M; // [J/k] Capacidade de Calor 
tmax = 800e-3; // [s] Tempo da Simulação
N = 10000; // Número de Pontos da Simulação
t = linspace(0, tmax, N); // Base de Plotagem do Mod
T = 0 * t; // [K] Temperatura do Filamento
R1 = 0 * t; // [ohms] Resistência da Lâmpada
I = 0 * t; // [A] Corrente
dt = t(2) - t(1); // Passo de Tempo [s]
V_inicial = 9; // [V] Tensão Inicial Aplicada
V = V_inicial; // Definimos a tensão inicial
t_desligamento = tmax / 2; // Tempo em que a tensão cai para 0V (ajuste conforme necessário)
k = 1; // Índice do Passo Inicial
T(1) = Tamb; // Temperatura Inicial
R1(1) = Klt * Tamb; // Resistência Inicial do Filamento
I(1) = V / (R1(1) + R2); // [A] Corrente

// LOOP DE SIMULAÇÃO
while (k < N)
    // Ajusta a tensão para 0V após t_desligamento
    if t(k) >= t_desligamento
        V = 0;
    end
    
    // Cálculo das potências e evolução da temperatura
    Pe = Klt * T(k) * ((V / (R1(k) + R2))^2); // [watts] Potência Elétrica
    Pr = Kr * (T(k)^4); // [watts] Potência Irradiada (Corpo Negro)
    T(k + 1) = T(k) + (dt / Ct) * (Pe - Pr); // Cálculo da Evolução da Temperatura
    R1(k + 1) = Klt * T(k + 1); // [ohms] Resistência da Lâmpada
    I(k + 1) = V / (R1(k + 1) + R2); // [A] Corrente na Lâmpada
    k = k + 1; // Incrementa o Passo do tempo discreto   
end

// Cálculo do Tempo para atingir 90% da Resistência de Equilíbrio
R_equilibrio = 36; // [ohms] Resistência de Equilíbrio
R_target = 0.9 * R_equilibrio; // [ohms] 90% da Resistência de Equilíbrio

t_90 = t(find(R1 <= R_target, 1)); // Tempo para atingir 90% da resistência de equilíbrio (após desligamento)

// Exibir Resultado
mprintf('Tempo para atingir 90% da resistência de equilíbrio: %.3f [s]\n', t_90);

