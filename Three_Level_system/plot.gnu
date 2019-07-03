set terminal epslatex color
set out 'plot.tex'
plot [-5:5] [-1.5:1.5] sin(x+pi) title "$\\sin(x+\\pi)$"
set out