set term png

set xlabel 'Time (ns)'
set ylabel 'Fidelity'

set key samplen 2 width 0.2
set key box opaque
set border back

set output 'fidelity_000.png'
set key outside
set key right top
set xrange[0:3000]
plot '../fidelity000-4_10_17.dat' w l title 'Full Drive', '../fidelity000-RWA-4_10_17.dat' w l title 'RWA'

set output 'fidelity_111.png'
unset xrange
set key inside
set key bottom right
plot '../fidelity111-4_10_17.dat' w l title 'Full Drive', '../fidelity111-RWA-4_10_17.dat' w l title 'RWA'


set output 'fidelity_All.png'
set key top right
plot '../fidelity111-4_10_17.dat' w l title 'Full Drive - |111>', '../fidelity111-RWA-4_10_17.dat' w l title 'RWA - |111>', '../fidelity000-4_10_17.dat' w l title 'Full Drive - |000>', '../fidelity000-RWA-4_10_17.dat' w l title 'RWA - |000>'

set output 'fidelity_All-RWA.png'
set key top right
plot  '../fidelity111-RWA-4_10_17.dat' w l title 'RWA - |111>', '../fidelity000-RWA-4_10_17.dat' w l title 'RWA - |000>'

set term x11
 
