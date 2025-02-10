//Constantes 
mv = 5.101208e-31 //Massa efetiva do eletron na banda de conducao [m_e] 
mc = 1.002023e-30 //Massa efetiva do eletron na banda de valencia [m_e]
Ec = 1.794352e-19 //Energia minima da banda de conducao [eV]
Ev = 0 //Energia minima da banda de valencia [eV]
Ei = (Ec + Ev)/2
h = 6.626e-34 //Constante de planck [J*s]
E = linspace(Ev - 0.1, Ec + 0.1, 1000) // Faixa de energia
N = 1000
pi = 3.141592
k_B = 0.025 //Constante de Boltzman [eV]
e = 2.718281828
Dc = zeros(1, N);
Dv = zeros(1, N);
f = zeros(1, N);
F = zeros(1, N);
F1 = zeros(1, N);
F_int = 0;
F1_int = 0;

for k = 1:N
    // Cálculo da densidade de estados para o caso dos elétrons na banda de condução
    if E(k) > Ec // Garantir que estamos acima da energia mínima da banda de condução
        Dc(k) = (1 / (2 * (pi^2))) * (((2 * mc) / (h^2))^(3/2)) * sqrt(E(k) - Ec);
    else
        Dc(k) = 0; // Para energias abaixo de Ec, a densidade de estados é zero
    end
    
    if E(k) < Ev
        Dv(k) = (1 / (2 * (pi^2))) * (((2 * mv) / (h^2))^(3/2)) * sqrt(Ev - E(k));
    else
        Dv(k) = 0;
    end
    f(k) = 1/(e^((E(k)-Ei)/k_B)+1);
    F(k) = Dc(k)*f(k);
    F1(k) = Dv(k)*(1-f(k));
end

function y=D(E),y=(1 / (2 * (pi^2))) * (((2 * mc) / (h^2))^(3/2)) * (E - Ec)^(1/2)
endfunction

function y=f1(E),y=1/(e^((E-Ei)/k_B)+1)
endfunction

function y=F2(E),y=D(E)*f1(E)
endfunction

I=intg(Ec,1,F2)


disp(I);


clf;
figure(0);
plot(0, Ei, '-o');
plot(Dc, E, 'r');
plot(Dv, E, 'b');

title('Densidade de Estados');
ylabel('Energia (J)');
xlabel('Densidade de Estados');
legend(['Dc (Banda de condução)', 'Dv (Banda de valência)']);

figure(1);
clf;  // Limpa a nova janela gráfica
plot(f, E, 'g-');
title('Função de Distribuição');
ylabel('Energia (J)');
xlabel('f(E)');
legend('Função de Distribuição');

figure(2);
clf;  // Limpa a nova janela gráfica
plot(F, E, 'r-');
plot(F1, E, 'g-');
title('Curvas para o ni');
ylabel('Energia (J)');
xlabel('f(E)*D(E)');
legend('Ec', 'Ev');
