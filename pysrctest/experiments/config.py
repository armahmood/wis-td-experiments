
import numpy as np
import cPickle as pickle
  
def main():
  
  ns          = 13
  ftype       = 'tabular'
  if ftype=='tabular':  nf = ns-2
  elif ftype=='binary': nf = int(np.ceil(np.log(ns-1)/np.log(2)))
  alphas    = np.arange(0, 1.6, .1)
  betas     = np.array([0, 0.1, 1.])
  lms       = np.concatenate((np.arange(0, .9, .1), np.arange(.9, 1.01, .01)))
  configs     = [
                   {
                   'algname'   : 'gtd',
                   'gamma'     : 1.0,
                   'N'      : 100,
                   'ftype'     : ftype,
                   'ns'        : ns,
                   'nf'        : nf,
                   'inits'     : (ns-1)/2,
                   'mright'    : 0.5,
                   'pright'    : 0.99,
                   'alpha'     : alpha,
                   'beta'      : beta,
                   'lambda'    : lm
                   }
                   for alpha in alphas
                   for beta in betas
                   for lm in lms
                ]
  
  f = open('config.pkl', 'wb')
  
  pickle.dump(configs, f)
  
if __name__ == "__main__":
  main()  

