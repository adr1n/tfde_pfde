// Dados principais para o gráfico
x = [0, 1, 2, 3, 4, 5];
y = [2, 4, 6, 8, 10, 12];

// Plotando o gráfico original
plot(x, y, '-o');
xlabel('Eixo X');
ylabel('Eixo Y');
title('Gráfico com Linha de Altura');

// Altura que será destacada
altura = 7;

// Adicionando a linha horizontal
xMin = gca().data_bounds(1, 1);  // Obtém o limite inferior do eixo X
xMax = gca().data_bounds(1, 2);  // Obtém o limite superior do eixo X
plot([xMin, xMax], [altura, altura], 'r--'); // Linha horizontal em y=altura

// Adicionando a label
xLabelPos = xMax - (xMax - xMin) * 0.2;  // Define a posição da label no eixo X
yLabelPos = altura + 0.3;  // Define a posição da label acima da linha
xstring(xLabelPos, yLabelPos, 'Altura = 7');

legend(['Dados', 'Altura Marcada']);
