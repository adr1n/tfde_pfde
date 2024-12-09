// Criando o eixo e espaço de energia (E)
E = [0:0.1:10];  // Vetor para simular os valores de energia
Nc = exp((E - 5));  // Simulando curva Nc (pode ser ajustado conforme necessário)
Nv = exp((5 - E));  // Simulando curva Nv (pode ser ajustado conforme necessário)

// Plotando as curvas Nc e Nv
plot(E, Nc, 'b-');  // Curva azul para Nc
plot(E, Nv, 'r-');  // Curva vermelha para Nv

// Marcar os níveis de energia Ec, Ev e Ei
Ec = 5;  // Exemplo de nível Ec
Ev = 3;  // Exemplo de nível Ev
Ei = 4;  // Exemplo de nível Ei

// Linhas horizontais para Ec, Ev, e Ei
xMin = gca().data_bounds(1,1);
xMax = gca().data_bounds(1,2);
plot([xMin, xMax], [Ec, Ec], 'k--'); // Linha para Ec
plot([xMin, xMax], [Ev, Ev], 'k--'); // Linha para Ev
plot([xMin, xMax], [Ei, Ei], 'k--'); // Linha para Ei

// Adicionando labels para Ec, Ev, Ei
xstring(xMax-3, Ec, 'E_c');
xstring(xMax-3, Ev, 'E_v');
xstring(xMax-3, Ei, 'E_i');

title('Curvas de Nc e Nv com níveis de energia');
xlabel('E (Energia)');
ylabel('Densidade de Estado');
legend(['Nc', 'Nv', 'E_níveis']);


