set term png
set output 'Toffoli_Fidelity_All.png'

set xlabel 'Time'
set ylabel 'Fidelity'
set title 'Toffoli Fiedlity graph'

plot 'fidelity111.dat' w l,'fidelity110.dat' w l,'fidelity101.dat' w l,'fidelity100.dat' w l,'fidelity011.dat' w l,'fidelity010.dat' w l,'fidelity001.dat' w l,'fidelity000.dat' w l
