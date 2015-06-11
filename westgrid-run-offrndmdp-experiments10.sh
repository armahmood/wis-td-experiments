#!/bin/bash


for runseed in {1..50}
do
for alg in gtd togtd wislstd lstdto wtd wgtd wtogtd
#for alg in olstd2
do

echo '#!/bin/bash 
#PBS -S /bin/bash 
#PBS -M ashique@ualberta.ca
#PBS -m bea
#PBS -l walltime=01:00:00
#PBS 
cd $PBS_O_WORKDIR 
echo "Current working directory is `pwd`" 
module load application/python/2.7.3 

time python ./pysrc/experiments/offrndmdpexp.py 1000 '$runseed'  ~/wis-td-experiments2/wis-td-experiments/results/offpolicy-rndmdp-experiments/state-10-bpol-random-tpol-skewed-ftype-binary/ '$alg' > '$alg'-'$runseed'.txt' > $alg-$runseed.pbs 

qsub $alg-$runseed.pbs

done

done
