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

Dc = @(E) (E > Ec) .* (1 / (2 * (pi^2))) .* ((2 * mc / h^2)^(3/2)) .* sqrt(E - Ec);
Dv = @(E) (E < Ev) .* (1 / (2 * (pi^2))) .* ((2 * mv / h^2)^(3/2)) .* sqrt(Ev - E);
f = @(E) (1/(exp((E - Ei) / k_B) + 1));
F = @(E) Dc(E) .* f(E);
F1 = @(E) Dv(E) .* (1 - f(E));

I=intg(0,%pi,F);
disp(I);
