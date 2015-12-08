
# coding: utf-8

# In[130]:

from __future__ import print_function, division
from time import strftime
from pprint import pprint
import math,random,numpy as np

__author__ = 'Vamshi Guduguntla'
__copyright__ = "NA"
__license__ = "NA"
__version__ = "1.0"


class DTLZ7:
    
    """
    DTLZ7 with M objectives N decisions.
    
    :param num_decisions    - Number of decisions/dimension of the array
    :param num_objectives   - Number of objectives to evaluate (f1,f2,....)
    :param dec_high         - Max range of the decision
    :param dec_low          - Min range of the decision
    :param obj_high         - Max range of the objective
    :param obj_low          - Min range of the objective
    :param evals            - Keeps the track of the number of evaluations
    :func  g                - scores a candidate on function g
    :func  function_value   - A function that scores a candidate and returns a vector of f
    :func  constraint_ok    - A function that checks for constraints (none of Kursawe and Schaffer)


    """
    
    def __init__(self,num_objectives,num_decisions,high = 10**6,low = -10**6):
        
        self.name = "DTLZ7"
        self.num_decisions = num_decisions
        self.num_objectives = num_objectives
        self.dec_high = [1 for _ in range(self.num_decisions)]
        self.dec_low = [0 for _ in range(self.num_decisions)]
        self.dec = []
        
        
    def g(self,dec):
        k = self.num_decisions - self.num_objectives+1
        g = 1. + (((9.)/(k)) * np.sum(self.dec[:self.num_objectives]))
        return g
        
    def h(self,dec):
        h = self.num_objectives
        for i in range(self.num_objectives-1):
            h -= (self.dec[i]/(1 + self.g(dec))) * (1 + math.sin(3 * math.pi * self.dec[i]))        
        return h

        
    def function_value(self,dec):
        f = []
        
        for i in range(self.num_objectives):
            val = 0.0
            if i == self.num_objectives - 1:
                val += (1+self.g(dec)) * self.h(dec)
            else:
                val += self.dec[i]
            f.append(val)         
        return f
        
    def contraint_ok(self,dec):
        return True # no constraints
        
    def randomstate(self):
        while True:
            dec = list()
            for low,high in zip(self.dec_low,self.dec_high):
                dec.append(random.uniform(low,high))
            if self.contraint_ok(dec):
                return dec


# In[ ]:



