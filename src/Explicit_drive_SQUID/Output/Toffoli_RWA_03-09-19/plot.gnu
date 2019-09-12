set term png
set output 'Fidelity.png'

set key box opaque
set border back
set title 'Fidelity - Perturbations'
set xlabel 'Time (ns)'
set ylabel 'Fidelity'
plot 'fidelity000-RWA-4_10_17.dat' w l ti '|000>', 'fidelity111-RWA-4_10_17.dat' w l ti '|111>'
