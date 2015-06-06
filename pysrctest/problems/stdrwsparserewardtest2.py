'''
Created on Mar 25, 2015

@author: A. Rupam Mahmood
'''
import unittest
import numpy as np
from pysrc.problems.stdrwsparsereward import StdRWSparseReward2 
from pysrc.algorithms.tdprediction.offpolicy.gtd import GTD
from pysrc.problems.mdp import PerformanceMeasure
from pysrctest.experiments import stdrwexp2 

class Test(unittest.TestCase):

  def teststdrwsparsereward2(self):
    ns = 13
    gamma = 0.9
    gm = np.ones(ns) * gamma
    gm[0] = gm[ns - 1] = 0
    Gamma = np.diag(gm)
    nzG              = np.diag(Gamma)!=0.0
    config = {
              'ftype'     : 'tabular',
              'ns'        : ns,
              'na'        : 2,
              'behavRight': 0.5,
              'targtRight': 0.9,
              'runseed'   : 1,
              'nf'        : np.sum(nzG),
              'Gamma'     : Gamma,
              'initsdist' : 'statemiddle',
              'Rstd'      : 0.0,
              'mdpseed'   : 1000
              }
    
    rwprob = StdRWSparseReward2(config)
    probvisit = np.zeros(ns)
    rwprob.initTrajectory(config['runseed'])
    ep = 0
    while ep < 200:
      rets = rwprob.step()
      assert((rets['s'] != ns - 2 and rets['R'] == 0.0) \
               or (rets['s'] == ns - 2 and rets['act'] == 0 and rets['R'] == 0.0)\
               or (rets['s'] == ns - 2 and rets['act'] == 1 and rets['R'] == 1.0))
      probvisit[rets['s']] += 1
      if rwprob.isTerminal(): ep += 1
    probvisit /= np.sum(probvisit)
    print(probvisit)
    print(rwprob.dsb)
    assert((np.abs(rwprob.dsb[nzG] - probvisit[nzG]) < 0.01).all())

  def testgtdonsparserewardtabular(self):
    ns = 13
    gamma = 0.9
    gm = np.ones(ns) * gamma
    gm[0] = gm[ns - 1] = 0
    Gamma = np.diag(gm)
    nzG              = np.diag(Gamma)!=0.0
    config2 = {
              'offpolicy' : True,
              'mdpseed'   : 1000,
              'Gamma'     : Gamma,
              'initsdist' : 'statemiddle',
              'Rstd'      : 0.0,
              'T'         : 200,
              'N'         : 200,
              'ftype'     : 'tabular',
              'ns'        : ns,
              'na'        : 2,
              'runseed'   : 1,
              'nf'        : np.sum(nzG),
              'behavRight': 0.5,
              'targtRight': 0.9,
              'lmbda'    : 0.5,
              'alpha'     : 0.02,
              'beta'      : 0.0
              }
    
    alg2       = GTD(config2)
    rwprob2   = StdRWSparseReward2(config2)
    perf2     = PerformanceMeasure(config2, rwprob2)
    stdrwexp2.runoneconfig(config2, rwprob2, alg2, perf2)
    print "tabular"
    print perf2.thstar.T
    print alg2.th
    assert (abs(perf2.thstar.T - alg2.th) < 0.1).all()

  def testgtdonsparserewardbinary(self):
    ns = 13
    gamma = 0.9
    gm = np.ones(ns) * gamma
    gm[0] = gm[ns - 1] = 0
    Gamma = np.diag(gm)
    nzG              = np.diag(Gamma)!=0.0
    config2 = {
              'offpolicy' : True,
              'mdpseed'   : 1000,
              'Gamma'     : Gamma,
              'initsdist' : 'statemiddle',
              'Rstd'      : 0.0,
              'T'         : 200,
              'N'         : 200,
              'ftype'     : 'binary',
              'ns'        : ns,
              'na'        : 2,
              'runseed'   : 1,
              'nf'        : int(np.ceil(np.log(np.sum(nzG)+1)/np.log(2))),
              'behavRight': 0.5,
              'targtRight': 0.9,
              'lmbda'    : 0.5,
              'alpha'     : 0.005,
              'beta'      : 0.0
              }

    alg         = GTD(config2)
    rwprob      = StdRWSparseReward2(config2)
    perf        = PerformanceMeasure(config2, rwprob)
    stdrwexp2.runoneconfig(config2, rwprob, alg, perf)
    thstarMSPBE = perf.getThstarMSPBE(config2['lmbda'])
    print "binary"
    print thstarMSPBE
    print alg.th
    assert (abs(thstarMSPBE - alg.th) < 0.05).all()
 
if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()



