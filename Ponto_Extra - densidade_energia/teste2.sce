// Function written in the Scilab language
function y=f(x),y=x*sin(30*x)/sqrt(1-((x/(2*%pi))^2))
    endfunction
exact=-2.5432596188;
I=intg(0,%pi,f)
abs(exact-I)
mprintf("%.3f", I)
