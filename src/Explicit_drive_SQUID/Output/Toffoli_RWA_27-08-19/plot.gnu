set term png
set output 'Fidelity.png'

set key box opaque
set border back
set title 'Fidelity - Perturbations'
set xlabel 'Time (ns)'
set ylabel 'Fidelity'
plot 'fidelity000-25.132741232_62.83185308_106.814150236.dat' w l ti 'Perturbations-|000>', 'fidelity111-25.132741232_62.83185308_106.814150236.dat' w l ti 'Perturbations-|111>','fidelity000-RWA-25.132741232_62.83185308_106.814150236.dat' w l ti 'RWA-|000>', 'fidelity111-RWA-25.132741232_62.83185308_106.814150236.dat' w l ti 'RWA-|111>'
