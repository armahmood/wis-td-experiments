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
  path = "./results/stdrw-experiments/stdrw-sparse-reward-11-states/"+algname+"/"
  if not os.path.exists(path):
    path = "../."+path
  pathfileprefix      = path+"run_"
  if not os.path.isfile(pathfileprefix+"perfvslambda.plot.pkl"):
    sys.argv  = ["", "50", pathfileprefix]
    sys.argv.extend(params)
    plotdataprocess.main()
  oisdata   = pickle.load(file(pathfileprefix+"perfvslambda.plot.pkl"))
  norm      = 0.914311143244
  ppl.errorbar(oisdata[:,0], oisdata[:,1]/norm, oisdata[:,2]/norm, label=algname)

def main():

  plotonealg("gtd", ["3", "alpha", "beta", "lambda", "1", "lambda"])
  plotonealg("togtd", ["3", "alpha", "beta", "lambda", "1", "lambda"])
  plotonealg("wtd", ["3", "eta", "initd", "lambda", "1", "lambda"])
  plotonealg("wgtd", ["4", "eta", "initd", "beta", "lambda", "1", "lambda"])
  plotonealg("wtogtd", ["4", "eta", "initd", "beta", "lambda", "1", "lambda"])
  plotonealg("oislstd", ["2", "inita", "lambda", "1", "lambda"])
  plotonealg("wislstd", ["2", "inita", "lambda", "1", "lambda"])
  plotonealg("lstdto", ["2", "inita", "lambda", "1", "lambda"])
  ppl.ylim([0, 0.15])
  ppl.legend(loc='lower left')
  #ppl.savefig('tmp.png')
  
if __name__ == '__main__':
    main()
    ppl.show()
