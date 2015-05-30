'''
Created on Apr 8, 2015

@author: A. Rupam Mahmood
'''

import os
import sys
sys.path.insert(0, os.getcwd())
from pysrc.plot import plotdataprocess
import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as ppl
import pickle

def plotonealg(algname, params):
  path = "./results/usage-experiments/stdrw-sparse-reward-11-states-test/"+algname+"/"
  if not os.path.exists(path):
    path = "../."+path
  pathfileprefix      = path+"run_"
  plotfilesuffix      = "perfvs"+params[-1]+".plot"
  #if not os.path.isfile(pathfileprefix+plotfilesuffix):
  sys.argv  = ["", "5", pathfileprefix]
  sys.argv.extend(params)
  plotdataprocess.main()
  oisdata   = pickle.load(file(pathfileprefix+plotfilesuffix))
  ppl.errorbar(oisdata[:,0], oisdata[:,1], oisdata[:,2], label=algname)

def main():

#   plotonealg("gtd", ["3", "alpha", "beta", "lmbda", "1", "beta"])
  plotonealg("togtd", ["3", "alpha", "beta", "lambda", "1", "lambda"])
#   plotonealg("wtd", ["3", "eta", "initd", "lmbda", "1", "initd"])
#   plotonealg("wgtd", ["4", "eta", "initd", "beta", "lmbda", "1", "initd"])
#   plotonealg("wtogtd", ["4", "eta", "initd", "beta", "lmbda", "1", "initd"])
#   plotonealg("oislstd", ["2", "inita", "lmbda", "1", "inita"])
#   plotonealg("wislstd", ["2", "inita", "lmbda", "1", "inita"])
#   plotonealg("olstd2", ["2", "inita", "lmbda", "1", "inita"])
  ppl.ylim([0, 0.2])
  #ppl.yscale('log')
  #ppl.xscale('log')
  ppl.legend()
  #ppl.savefig('tmp.png')
  
if __name__ == '__main__':
    main()
    ppl.show()
