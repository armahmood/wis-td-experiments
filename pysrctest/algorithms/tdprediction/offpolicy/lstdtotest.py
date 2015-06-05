'''
Created on Mar 27, 2015

@author: A. Rupam Mahmood
'''

import unittest
import numpy as np
from pysrc.problems.stdrwsparsereward import StdRWSparseReward
from pysrc.problems.stdrwfreqreward import StdRWFreqReward
from pysrc.algorithms.tdprediction.offpolicy.lstdto import LSTDTO
import pysrc.experiments.stdrwexp as stdrwexp
from pysrc.problems.stdrw import PerformanceMeasure

class Test(unittest.TestCase):

  def testlstdtoonsparserewardtabular(self):
    ns = 7
    config = {
              'N'      : 200,
              'ftype'     : 'tabular',
              'ns'        : ns,
              'inits'     : (ns-1)/2,
              'mright'    : 0.5,
              'pright'    : 0.9,
              'runseed'   : 1,
              'nf'        : ns-2,
              'gamma'     : 0.9,
              'lambda'    : 0.5,
              'inita'     : 0.01,
              }
    alg         = LSTDTO(config)
    rwprob      = StdRWSparseReward(config)
    perf      = PerformanceMeasure(config, rwprob)
    stdrwexp.runoneconfig(config, rwprob, alg, perf)
    print perf.thstarMSE.T[0]
    print alg.th
    assert (abs(perf.thstarMSE.T[0] - alg.th) < 0.01).all()

  def testlstdtoonsparserewardbinary(self):
    ns = 7
    config = {
              'N'      : 200,
              'ftype'     : 'binary',
              'ns'        : ns,
              'inits'     : (ns-1)/2,
              'mright'    : 0.5,
              'pright'    : 0.9,
              'runseed'   : 1,
              'nf'        : int(np.ceil(np.log(ns-1)/np.log(2))),
              'gamma'     : 0.9,
              'lambda'    : 0.0,
              'inita'     : 0.01,              
              }
    alg         = LSTDTO(config)
    rwprob      = StdRWSparseReward(config)
    perf      = PerformanceMeasure(config, rwprob)
    stdrwexp.runoneconfig(config, rwprob, alg, perf)
    print perf.thstarMSPBE.T[0]
    print alg.th
    assert (abs(perf.thstarMSPBE.T[0] - alg.th) < 0.05).all()

  def testlstdtoonfreqrewardtabular(self):
    ns = 7
    config = {
              'N'      : 200,
              'ftype'     : 'tabular',
              'ns'        : ns,
              'inits'     : (ns-1)/2,
              'mright'    : 0.5,
              'pright'    : 0.9,
              'runseed'   : 1,
              'nf'        : ns-2,
              'gamma'     : 0.9,
              'lambda'    : 0.5,
              'inita'     : 0.1,              
              }
    alg         = LSTDTO(config)
    rwprob      = StdRWFreqReward(config)
    perf      = PerformanceMeasure(config, rwprob)
    stdrwexp.runoneconfig(config, rwprob, alg, perf)
    print perf.thstarMSE.T[0]
    print alg.th
    assert (abs(perf.thstarMSE.T[0] - alg.th) < 0.1).all()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()