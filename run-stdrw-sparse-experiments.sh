#!/bin/bash


for runseed in {1..1}
do
for alg in gtd togtd wtd wtogtd wgtd wislstd lstdto
do
time python pysrc/experiments/stdrwexp.py $runseed StdRWSparseReward  results/stdrw-experiments/stdrw-sparse-reward-11-states/$alg/ &

done

done


echo "Invoking matplotlib plot for the experiment ..."
python ./pysrc/plot/plotstdrwsparseexp.py

