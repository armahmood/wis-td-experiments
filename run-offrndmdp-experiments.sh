#!/bin/bash


for runseed in {1..1}
do
for alg in gtd togtd wtd wtogtd wgtd wislstd lstdto
do
time python pysrc/experiments/offrndmdpexp.py 1000 $runseed results/offpolicy-rndmdp-experiments/state-100-bpol-random-tpol-skewed-ftype-binary/ $alg &

done

done


echo "Invoking matplotlib plot for the experiment ..."
python ./pysrc/plot/plotoffrndmdpexp.py

