
import numpy as np
import cPickle as pickle
  
def main():
  ns          = 10
  N           = 500
  gamma       = 0.99
  configs     = \
                   {
                   'Gamma'      : gamma,
                   'ftype'      : 'binary',
                   'numzerogs'  : 2,
                   'T'          : N,
                   'N'          : N,
                   'ns'         : ns,
                   'na'         : 3,
                   'nf'         : int(np.ceil(np.log(ns+1)/np.log(2))),
                   'b'          : 3,
                   'rtype'      :'uniform', 
                   'rparam'     :1,
                   'Rstd'       : 0.0,
                   'initsdist'  : 'statezero',
                   'bpoltype'   : 'random',
                   'tpoltype'   : 'skewed',
                   }
  
  f = open('configprob.pkl', 'wb')
  
  pickle.dump(configs, f)
  
if __name__ == "__main__":
  main()  

