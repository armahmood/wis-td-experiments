'''
Created on Mar 24, 2015

@author: A. Rupam Mahmood

This module instantiates an algorithm and a random walk 
problem (see Mahmood, van Hasselt & Sutton 2014, nips) and runs an experiment.

'''

import os
import sys
sys.path.insert(0, os.getcwd())
import argparse
from pysrc.problems.mdp import PerformanceMeasure
from pysrc.problems.stdrwsparsereward import StdRWSparseReward2
from pysrc.problems.stdrwfreqreward import StdRWFreqReward2

def runoneconfig(config, prob, alg, perf):
  prob.initTrajectory(config['runseed'])
  ep = 0
  while ep < config['N']:
    probstep          = prob.step()
    s                 = probstep['s']
    a                 = probstep['act']
    probstep['l']     = config['lmbda']
    probstep['lnext'] = config['lmbda']
    probstep['rho']   = prob.getRho(s,a)
    alg.step(probstep)
    if prob.isTerminal():  
      perf.calcMSPVE(alg, ep)
      ep += 1
      prob.step()
      alg.initepisode()
      

    

