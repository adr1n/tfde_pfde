//Exemplo: Ajuste de Modelo da Lâmpada por Mínimos Quadrados
//%Programa:MQ_Lâmpada.sce
clear;
//Pontos Experimentais
N = 7; //Número de pontos experimentais
//SUBSTITUA AQUI OS VALORES MEDIDOS:
yp = [ 0 1 2 3 4 5 6 ]; //Corrente [A]
xp = [ 0 2 4 6 8 10 12 ]; //Tensão [V]
plot(xp,yp,'or');
//Obs:R1 = xp./yp;
//Modelo Adotado: y = k*(x^p)
p = 3/5; //Expoente Fracionário (Modelo)
g = xp.^p; //Função Base
k = sum(yp.*g)/sum(g.*g); //Ajuste da Constante do Modelo
xc = linspace(min(xp),max(xp),100); //Base de Plotagem do Modelo
yc = k*(xc.^p); //Modelo Ajustado
plot(xc,yc,'b');
title('Modelo Ajustado (azul) e Pontos Experimentais (vermelho)');
//Erro Quadrático Médio
ym = k*(xp.^p);//Valores da corrente
EQM = (1/N)*sum((ym-yp).^2);
disp(EQM);

