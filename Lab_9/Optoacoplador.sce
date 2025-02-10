//%Programa:Optoacoplador.sce
clear;
R1 = 0.996e3; //[ohms]
R2 = 0.99e6; //[ohms]

//Parte-I: Fotocondutivo
Vdc1a = [0 5.01 9.99 14.98 19.73 25.0];
Vdc2a = 12.05; //[V]
V1a = [0 2.20 7.11 12.11 16.84 22.1];
V2a = [0 67.5e-3 211e-3 345e-3 453e-3 561e-3];
Vled1a = Vdc1a - V1a;
Vled2a = Vdc2a - V2a;
Iled1a = V1a./R1;
Iled2a = V2a./R2;
P1a = Vled1a.*Iled1a;
P2a = Vled2a.*Iled2a;
scf(1);
plot(P1a,P2a,'or');

//Parte-II: Fotovoltaico
Vdc1b = [0 5.06 10.00 15.00 20.0 25];
//Vdc2b = 12.05; //[V]
V1b = [0 2.22 7.03 11.97 16.98 21.9];
V2b = [0 -52.6e-3 -166.0e-3 -270e-3 -364e-3 -447e-3];
Vled1b = Vdc1b - V1b;
//Vled2b = Vdc2b - V2b;
Vled2b = V2b;
Iled1b = V1b./R1;
Iled2b = V2b./R2;
P1b = Vled1b.*Iled1b;
P2b = Vled2b.*Iled2b;
scf(2);
plot(P1b,P2b,'or');

//Parte-III: I vs V Fotovoltaico
// Com Rmult = 20e6 => Vca = 1258e-3
R = [19.55e3 0.502e6 1.006e6 1.507e6 1.98e6 2.46e6 2.97e6 3.45e6 3.95e6 4.44e6 4.95e6 20e6];
V = [9.8e-3 242e-3 456e-3 647e-3 819e-3 971e-3 1084e-3 1144e-3 1174e-3 1191e-3 1202e-3 1258e-3];
Rmult = 20e6;//20e6;
Reff = 1./((1./R)+(1./Rmult));
Reff(12) = 20e6; //Correção: Aqui apenas R do multímetro.
I = V./Reff;
IL = I(1); //IL ~ I(R pequeno), V ~ 0
scf(3);
plot(V,I,'ro');
plot(V,I,'b');
replot([0 0 1.4 6e-7],'tight');
title('I vs. V (Modo Fotovoltaico)');
xlabel('V [volt]');
ylabel('I [A]');

//Ajuste Linear da Parte-I
//Modelo: y = eta*x 
g = P1a; //Função Base
f = P2a; 
eta = sum(f.*g)/sum(g.*g); //Ajuste da Constante do Modelo
disp(eta);
scf(1);
N = 100;
x = linspace(0,max(P1a),N);
y = eta*x;
plot(x, y,'b');
title('P2 vs. P1 (Fotocondutivo)');
xlabel('P1 [W]');
ylabel('P2 [W]');

//Ajuste Linear da Parte-II
//Modelo: y = eta*x 
g = P1b; //Função Base
f = P2b; 
eta = sum(f.*g)/sum(g.*g); //Ajuste da Constante do Modelo
disp(eta);
scf(2);
N = 100;
x = linspace(0,max(P1b),N);
y = eta*x;
plot(x, y,'b');
title('P2 vs. P1 (Fotovoltaico)');
xlabel('P1 [W]');
ylabel('P2 [W]');










