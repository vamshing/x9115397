
# coding: utf-8

# In[101]:


from __future__ import print_function, division
from time import strftime
from pprint import pprint
import math,random,numpy as np

__author__ = 'Vamshi Guduguntla'
__copyright__ = "NA"
__license__ = "NA"
__version__ = "1.0"


class DTLZ1:
    
    """
    DTLZ1 with M objectives N decisions.
    
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
        
        self.name = "DTLZ1"
        self.num_decisions = num_decisions
        self.num_objectives = num_objectives
        self.dec_high = [1 for _ in range(self.num_decisions)]
        self.dec_low = [0 for _ in range(self.num_decisions)]
        self.dec = []
        self.dec_2 = []
        self.randomstate()
        
        
    def function_value(self,dec,decs,objs):
        f = function_value(dec,decs,objs)
        return f
        
    def contraint_ok(self,dec):
        return True # no constraints
        
    def randomstate(self):
        while True:
            dec = list()
            for low,high in zip(self.dec_low,self.dec_high):
                dec.append(random.uniform(low,high))
            if self.ok(dec):
                break
        return dec
    
    def ok(self,dec):
        for i in range(0,self.num_decisions):
            if dec[i]<self.dec_low[i] or dec[i]>self.dec_high[i]:
                return False
        return True

def g(dec,objs,decs):
    g = decs - objs+1
    for x in dec[objs - 1:]:
        g += (x - 0.5)**2 - math.cos(20 * math.pi * (x - 0.5))
    return g*100.    
        
def function_value(dec,decs,objs):
    f = []
    for i in range(objs):
        val = (1+g(dec,objs,decs)) * 0.5
        for x in dec[:objs-(i+1)]:
            val *= x
        if not i == 0:
            val=val*(1-dec[objs-i])
        f.append(val)         
    return f
