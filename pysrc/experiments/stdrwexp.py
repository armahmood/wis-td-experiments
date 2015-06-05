'''
Created on Mar 24, 2015

@author: A. Rupam Mahmood

This module instantiates an algorithm and the standard random walk 
problem (see Mahmood, van Hasselt & Sutton 2014, nips) and runs an experiment.

'''

import os
import sys
sys.path.insert(0, os.getcwd())
import argparse
from pysrc.problems.stdrw import PerformanceMeasure
from pysrc.problems.stdrwsparsereward import StdRWSparseReward
from pysrc.problems.stdrwfreqreward import StdRWFreqReward

def runoneconfig(config, prob, alg, perf):
  prob.setrunseed(config['runseed'])
  for ep in range(config['N']):
    prob.initepisode()
    alg.initepisode()
    while not prob.isterminal():
      probstep          = prob.step()
      s                 = probstep['s']
      a                 = probstep['act']
      probstep['l']     = config['lambda']
      probstep['lnext'] = config['lambda']
      probstep['rho']   = prob.getRho(s,a)
      alg.step(probstep)
    perf.calcMse(alg, ep)
      
    

