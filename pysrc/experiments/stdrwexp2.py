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
from pysrc.problems.mdp import PerformanceMeasure
from pysrc.problems.stdrwsparsereward import StdRWSparseReward2
from pysrc.problems.stdrwfreqreward import StdRWFreqReward2
from pysrc.algorithms.tdprediction.offpolicy import oislstd
from pysrc.algorithms.tdprediction.offpolicy import wislstd
from pysrc.algorithms.tdprediction.offpolicy import gtd
import cPickle as pickle

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
      
def main():
  parser          = argparse.ArgumentParser()
  parser.add_argument("run", help="used as a seed of an independent run", type=int)
  parser.add_argument("probname", help="name of the problem to run experiment on")
  parser.add_argument("path", help="location of the config file")
  args = parser.parse_args()
  configpathname  = args.path + "config2.pkl"
  cf              = open(configpathname, 'rb')
  configs         = pickle.load(cf)  
    
  filepathname  = args.path + "run_"\
                  +str(args.run) + ".dat"
  f             = open(filepathname, 'wb')
  
  algs  = {
           'oislstd':oislstd.OISLSTD,
           'wislstd':wislstd.WISLSTD,
           'gtd':gtd.GTD,
           }
  probs = {
           'StdRWSparseReward2'  : StdRWSparseReward2,
           'StdRWFreqReward2'    : StdRWFreqReward2,
           }
  algname   = configs[0]['algname']
  rwprob   = probs[args.probname](configs[0])
  perf      = PerformanceMeasure(configs[0], rwprob)
  print("Running algorithm " + algname + " on problem " + args.probname + ", runseed: " + str(args.run) )
  for config in configs:
    alg            = algs[algname](config)
    config['runseed'] = args.run
    runoneconfig(config, rwprob, alg, perf)
    config['error']     = perf.MSPVE
    pickle.dump(config, f, -1)

if __name__ == '__main__':
    main()   
    

