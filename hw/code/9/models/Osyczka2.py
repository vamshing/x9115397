from __future__ import print_function, division
from time import strftime
from pprint import pprint
import math,random,numpy as np

__author__ = 'Vamshi Guduguntla'
__copyright__ = "NA"
__license__ = "NA"
__version__ = "1.0"



class Osyczka2:
    
    """
    :param num_decisions    - Number of decisions/dimension of the array
    :param num_objectives   - Number of objectives to evaluate (f1,f2,....)
    :param dec_high         - Max range of the decision
    :param dec_low          - Min range of the decision
    :param obj_high         - Max range of the objective
    :param obj_low          - Min range of the objective
    :param num_objectives   - Number of objectives to evaluate (f1,f2,....)
    :param evals            - Keeps the track of the number of evaluations
    
    :func  function_value   - A function that scores a candidate
    :func  constraint_ok    - A function that checks for constraints (none of Kursawe and Schaffer)
    :func  norm             - A function that computes the objective scores for each candidate(normalized)
    :func  reset_baseline   - Resets the baseline for obj_high and obj_low computation
    """
    
    def __init__(self,num_eval = 0.0,prob = 0.5,high = 10**6,low = -10**6):
        self.name = "Osyczka2"
        self.num_decisions = 6
        self.num_objectives = 2
        self.dec_high = [10,10,5,5,6,10]
        self.dec_low = [0,0,1,1,0,0]
        self.steps = 10
        self.evals = num_eval
        self.obj_high = high
        self.obj_low = low
        self.threshold = -100
        self.reset_baseline()
        self.threshold = self.obj_low
        
        
    def reset_baseline(self):
        high = -10**6
        low = 10**6
        for _ in range(1000):
            dec = self.randomstate()
            en = self.function_value(dec)
            
            if en > high:
                high = en
            if en < low:
                low = en
        
        self.obj_high = high
        self.obj_low = low
        
    def contraint_ok(self,dec):
        g1 =  dec[0] + dec[1]-2 >= 0 
        g2 =  6 - dec[0] - dec[1] >= 0
        g3 =  2 - dec[1] + dec[0] >= 0
        g4 =  2 - dec[0] + 3 * dec[1] >= 0
        g5 =  4 - (dec[2] - 3)**3 + dec[5] - 4 >= 0
        g6 =  (dec[4] - 3)**3 + dec[5] -4 >= 0 
        return g1 and g2 and g3 and g4 and g5 and (self.function_value(dec) >= self.threshold)
        
    def randomstate(self):
        while True:
            dec = list()
            for low,high in zip(self.dec_low,self.dec_high):
                dec.append(random.randrange(low,high))
            if self.contraint_ok(dec):
                return dec   
        
    def function_value(self,dec):
        f1 = -(25*(dec[0]-2)**2 + (dec[1]-2)**2 + ((dec[2]-1)**2)*(dec[3]-4)**2 + (dec[4]-1)**2)
        f2 = dec[0]**2 + dec[1]**2 + dec[2]**2 + dec[3]**2 + dec[4]**2 + dec[5]**2
        return f1+f2 
    
    def norm(self,state):
        return (self.function_value(state) - self.obj_low)/(self.obj_high - self.obj_low)
