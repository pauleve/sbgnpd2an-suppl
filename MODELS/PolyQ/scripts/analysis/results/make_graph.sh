#!/bin/bash
gnuplot -e 'set terminal png;set key off;set title "Probability of the misfolded protein to be degraded \ndepending on the propensity of the sequestration process";set xlabel "propensity";set ylabel "probability";plot "MODELS/PolyQ/analysis/results/probas.txt" every ::1 using 1:2 with lines' > MODELS/PolyQ/analysis/results/probas.png

