set term png
set output 'Occupation_111.png'

set key box opaque
set border back

set title 'Occupation Probability for Each Qubit - Inital state |111>'
set xlabel 'Time (ns)'
set ylabel 'Occupation Probability'
set yrange [0:1.01]
plot 'occupation_q1_111-4_10_17.dat' w l ti 'q1', 'occupation_q2_111-4_10_17.dat' w l ti 'q2', 'occupation_q3_111-4_10_17.dat' w l ti 'q3'

set output 'Occupation_000.png'
set yrange [0:0.5]
set title 'Occupation Probability for Each Qubit - Inital state |000>'
plot 'occupation_q1_000-4_10_17.dat' w l ti 'q1', 'occupation_q2_000-4_10_17.dat' w l ti 'q2', 'occupation_q3_000-4_10_17.dat' w l ti 'q3'

set yrange [0:1.01]

set output 'Fidelity_Perturbations.png'
set title 'Fidelity - Perturbations'
set xlabel 'Time (ns)'
set ylabel 'Fidelity'
plot 'fidelity000-4_10_17.dat' w l ti '|000>', 'fidelity111-4_10_17.dat' w l ti '|111>'


set output 'Fidelity_RWA.png'
set title 'Fidelity - RWA'
set xlabel 'Time (ns)'
set ylabel 'Fidelity'
plot 'fidelity000-RWA-4_10_17.dat' w l ti '|000>', 'fidelity111-RWA-4_10_17.dat' w l ti '|111>'
