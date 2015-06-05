'''
Created on May, 2015

@author: A. Rupam Mahmood

Implementation of LSTD-TO(lambda)
by Dann, Neumann and Peters (2014)

'''

import numpy as np
import pylab as pl
from pysrc.algorithms.tdprediction.tdprediction import TDPrediction
 
# implementation of off-policy LSTD lambda by Dann et al. (2014)
 
class LSTDTO(TDPrediction):
  
  def __init__(self, config):
    
    TDPrediction.__init__(self,config)
    self.z = np.zeros(self.nf)
    self.inita = config['inita']
    self.A = np.eye(self.nf)*self.inita
    self.b = np.zeros(self.nf)
    
  def initepisode(self):
    self.z = np.zeros(self.nf)
    
  def step(self, params):
    f=params['phi']; R=params['R']; fnext=params['phinext']
    g=params['g']; l=params['l']; gnext=params['gnext']
    rho=params['rho']; lnext=params['lnext']
    
    self.z = rho*(g*l*self.z + f)
    self.b = self.b + R*self.z
    self.A = self.A + np.outer(self.z, f - gnext*fnext)
    self.th = np.dot(pl.pinv(self.A), self.b)
