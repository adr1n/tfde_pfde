//Exemplo: Simula Resposta ao Degrau do Filamento
//%Programa:Simula_Degrau.sce
clear;
//Parâmetros
M = 4.6e-3; //[g] Massa do Filamento
R2 = 1; //[ohm]
Klt = 0.011; //[ohm/K] Constante do Filamento (Resistência)
Kr = 3.3e-14; //[W/K^4] Constante do Filamento (Radiação)
Tamb = 300;//[K] Temperatura Inicial (Ambiente)
cp = 0.13;//[J/g.K] Calor Específico
Ct = cp*M; //[J/k] Capacidade de Calor 
tmax = 360; //[s] Tempo da Simulação
t_desligamento = 2; //[3] Tempo para desligar
N = 50000; //Número de Pontos da Simulação
t = linspace(0,tmax,N); //Base de Plotagem do Mod
T = 0*t; //[K] Temperatura do Filamento
R1 = 0*t; //[ohms] Resistência da Lâmpada
I = 0*t; //[A] Corrente
dt = t(2)-t(1); //Passo de Tempo [s]
V = 9;//[V] Tensão Aplicada
k = 1; //Índice do Passo Inicial
T(1) = 300; //Temperatura Inicial
R1(1)= 3.4; //[ohms]
I(1)= V/(R1(1)+R2); //[A]
//LOOP DE SIMULAÇÃO
while(k<N)
    if t(k) >= t_desligamento then
        V = 0;
    end
    Pe = Klt*T(k)*((V/(Klt*T(k)+R2))^2); // [watts] Potência Elétrica
    Pr = Kr*((T(k))^4); //[watts] Potência Irradiada (Corpo Negro)
    T(k+1) = T(k) + (dt/Ct)*(Pe - Pr); //Cálculo da Evolução da Temperatura
    R1(k+1) = Klt*T(k+1); //[ohms] Resistência da Lâmpada
    I(k+1)= V/(R1(k+1)+R2); //[A] Corrente na Lâmpada
    k = k + 1; //Incrementa o Passo do tempo discreto   
end

// Parâmetros para cálculo
R_90 = max(R1)*0.9; // [ohms] Resistência de Equilíbrio
R_10 = max(R1)*0.1; // [ohms] 90% da Resistência de Equilíbrio (32.4 ohms)

// Índice onde ocorre o desligamento da tensão
indice_desligamento = find(t >= t_desligamento, 1);
R_inst = R1(indice_desligamento);

// Encontrar os dois indices de 90% e 10% da resistencia maxima observada
indice_t90 = find(R1(indice_desligamento:$) <= R_90, 1) + indice_desligamento - 1;
indice_t10 = find(R1(indice_desligamento:$) <= R_10, 1) + indice_desligamento - 1;

// Obter o tempo correspondente a 90% da resistência de equilíbrio
t_90 = t(indice_t90);
t_10 = t(indice_t10);
intervalo_t = t_10 - t_90;

// Exibir o resultado
mprintf("Tempo de transição (de 90%% ate 10%% do valor máximo observado): %.3f [s]\n", intervalo_t);
// mprintf("Resistencia encontrada: %.3f [ohm]", R_real);
//GRÁFICOS:
scf(1);
plot(t,T,'r');
title('Modelo Dinâmico: Lâmpada Elétrica de Filamento');
xlabel('t [s]');
ylabel('T [K]');
scf(2);
plot(t,I,'b');
title('Modelo Dinâmico: Lâmpada Elétrica de Filamento');
xlabel('t [s]');
ylabel('I [A]');
scf(3);
plot(t,R1,'g');
title('Modelo Dinâmico: Lâmpada Elétrica de Filamento');
xlabel('t [s]');
ylabel('R1 [ohm]');
