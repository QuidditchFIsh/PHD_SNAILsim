set term png
set output 'Fidelity_All.png'

set title 'Fidelity vs time'

plot 'Fidelity111.txt' w l,'Fidelity011.txt' w l,'Fidelity101.txt' w l,'Fidelity110.txt' w l,'Fidelity100.txt' w l,'Fidelity010.txt' w l,'Fidelity001.txt' w l,'Fidelity000.txt' w l

set term x11



