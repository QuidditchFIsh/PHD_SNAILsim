set term png

set output 'occupation.png'
set title 'occupation'

#set yrange [-0.0001:0.004]

set ylabel 'Occupation Probability'
set xlabel 'Time (ns)'

plot 'occupation_q1_000-4_10_17.dat' w l ti 'q1','occupation_q2_000-4_10_17.dat' w l ti 'q2', 'occupation_sm_000-4_10_17.dat' w l ti 'qS'




