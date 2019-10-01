set terminal pngcairo
set output 'test.png'

set datafile separator ","
set palette rgbformulae 33,13,10

# Set margins to keep colorbox label inside the picture
set lmargin screen 0.12
set rmargin screen 0.85

set xlabel "time [s] (no operation)"
set ylabel "ranges"
set cblabel "devices"

unset key

set yrange  [1e-8:1e5]
set ytics format "1e%+T"
set logscale y

set view map
set cbrange [0:50]
set zrange [0:50]

splot "Max_occupation.dat" u 1:2:3 
