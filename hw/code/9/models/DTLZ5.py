
# coding: utf-8

# In[122]:

from __future__ import print_function, division
from time import strftime
from pprint import pprint
import math,random,numpy as np

__author__ = 'Vamshi Guduguntla'
__copyright__ = "NA"
__license__ = "NA"
__version__ = "1.0"


class DTLZ5:
    
    """
    DTLZ5 with M objectives N decisions.
    
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
        
        self.name = "DTLZ5"
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
    g = 0.
    for i in range(decs - objs+1):
        g += (dec[i] - 0.5)**2
    return g
    
def function_value(dec,objs,decs):
    f = []
    g = 0.
    
    for x  in dec[objs-1:]:
        g = g+(x-.5)**2
    theta = [math.pi * dec[0] * .5]
    
    for x in dec[1:objs-1]:
        theta.append((1+2*g*x)*math.pi/(4*(1+g)))
    
    for i in xrange(objs):
        tmp = 1+g
        
        for x in theta[:objs-1-i]:
            tmp = tmp * math.cos(x*math.pi*.5)
        
        if not i == 0:
            tmp=tmp*math.sin(theta[objs-i-1]*math.pi/2)
        
        f.append(tmp)
    
    return f
        
    """f = []
    theta = []
    for x in dec[1:objs-1]:
        theta.append(((math.pi)/(4*(1+g(dec,objs,decs))))*(1 + 2*g(dec,objs,decs)*x))
    
    
    for i in range(objs):
        val = (1+g(dec,objs,decs))
        for x in theta[:objs-(i+1)]:
            val *= math.cos(x * math.pi * 0.5)
        if i != 0:
            val *= val*(math.sin(theta[objs-(i+1)] * math.pi * 0.5))
        f.append(val)         
    return f"""
        
