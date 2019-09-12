set term png
set output 'Output/test1/RWA_WithTerms_Fidelity.png'

set title "Rotating Wave Approximation With Terms - Fidelity"
set xlabel "Time (ns)"
set ylabel "Fidelity"
set key outside

set yrange[0:1.05]

plot 'Output/test1/fidelity111-4_10_17.dat' w l title "|111>", 'Output/test1/fidelity000-4_10_17.dat' w l title "|000>"

set output 'Output/test1/RWA_WithTerms_Occupation.png'

set title "Rotating Wave Approximation With Terms - QuBit Occupation |111>"
set xlabel "Time (ns)"
set ylabel "Occupation Probability"



plot 'Output/test1/occupation_q1_111-4_10_17.dat' w l title 'q1','Output/test1/occupation_q2_111-4_10_17.dat' w l title 'q2','Output/test1/occupation_q3_111-4_10_17.dat' w l title 'q3'

set output 'Output/test1/RWA_WithTerms_SigmaZ.png'

set title "Rotating Wave Approximation With Terms - SigmaZ "
set xlabel "Time (ns)"
set ylabel "<sigmaZ>"

set yrange[-1.05:1]

plot 'Output/test1/sz1_111-4_10_17.dat' w l title "q1", 'Output/test1/sz2_111-4_10_17.dat' w l title "q2", 'Output/test1/sz3_111-4_10_17.dat' w l title "q3"

set output 'Output/RWA_vs_RWA_With_Terms - Fidelity.png'

set title "RWA vs RWA + Terms - (Fidelity) "
set xlabel "Time (ns)"
set ylabel "Fidelity"
set key inside bottom
set yrange[0:1.05]

plot 'Output/test1/fidelity111-4_10_17.dat' w l title "|111> (RWA + Terms)", 'Output/test1/fidelity000-4_10_17.dat' w l title "|000> (RWA + Terms)",'Output/test/fidelity111-4_10_17.dat' w l title "|111> (RWA)", 'Output/test/fidelity000-4_10_17.dat' w l title "|000> (RWA)"

set output 'Output/RWA_vs_RWA_With_Terms - Occupation.png'

set title "RWA vs RWA + Terms (Occupation Probability) "
set xlabel "Time (ns)"
set ylabel "Occupation Probability"
set key inside bottom
set yrange[0:1.05]

plot 'Output/test1/occupation_q1_111-4_10_17.dat' w l title 'q1','Output/test1/occupation_q2_111-4_10_17.dat' w l title 'q2','Output/test1/occupation_q3_111-4_10_17.dat' w l title 'q3','Output/test/occupation_q1_111-4_10_17.dat' w l title 'q1 RWA','Output/test/occupation_q2_111-4_10_17.dat' w l title 'q2 RWA','Output/test/occupation_q3_111-4_10_17.dat' w l title 'q3 RWA'

