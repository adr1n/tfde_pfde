// Função para simular a curva I x V para o diodo Schottky
function I = schottky_iv_curve(V, I_s, n, T)
    q = 1.602e-19;  // Carga do elétron (C)
    k = 1.381e-23;  // Constante de Boltzmann (J/K)
    I = I_s * (exp(q * V / (n * k * T)) - 1);
endfunction

// Função para simular a curva I x V para o diodo Zener
function I = zener_iv_curve(V, Vz, Iz_max, I_s, n, T)
    q = 1.602e-19;
    k = 1.381e-23;
    I = zeros(V);
    for i = 1:length(V)
        if V(i) >= 0 then
            I(i) = I_s * (exp(q * V(i) / (n * k * T)) - 1);
        else
            I(i) = -Iz_max * exp((V(i) + Vz)/0.1);
        end
    end
endfunction

// Geração de tensões para simulação
V = linspace(-1, 5, 1000);

// Cálculo das correntes para cada diodo
I_schottky = schottky_iv_curve(V, 1e-9, 1.1, 300);
I_zener = zener_iv_curve(V, 6.2, 50e-3, 1e-12, 1.5, 300);

// Plot das curvas I x V
clf;
figure(0);
plot(V, I_schottky);
xlabel('Tensão (V)');
ylabel('Corrente (A)');
title('Curva I x V - Diodo Schottky');

figure(1);
plot(V, I_zener, 'r');
xlabel('Tensão (V)');
ylabel('Corrente (A)');
title('Curva I x V - Diodo Zener');

