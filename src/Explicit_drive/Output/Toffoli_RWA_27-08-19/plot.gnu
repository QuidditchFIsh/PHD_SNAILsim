set term png
set output "Fidelity.png"

set title "Fidelity - RWA"
set xlabel 'Time (ns)'
set ylabel 'Fidelity'

#plot 'fidelity111-RWA-4_10_17.dat' w l ti '|111>', 'fidelity000-RWA-4_10_17.dat' w l ti '|000>'
plot 'fidelity111-4_10_17.dat' w l ti '|111>', 'fidelity000-4_10_17.dat' w l ti '|000>'
