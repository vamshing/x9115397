from __future__ import print_function, division
from time import strftime
from pprint import pprint
import math,random,numpy as np

__author__ = 'Vamshi Guduguntla'
__copyright__ = "NA"
__license__ = "NA"
__version__ = "1.0"

class Golinski:
    
    """
    :param num_decisions    - Number of decisions/dimension of the array
    :param num_objectives   - Number of objectives to evaluate (f1,f2,....)
    :param dec_high         - Max range of the decision
    :param dec_low          - Min range of the decision
    :param obj_high         - Max range of the objective
    :param obj_low          - Min range of the objective
    :param num_objectives   - Number of objectives to evaluate (f1,f2,....)
    :param evals            - Keeps the track of the number of evaluations
    
    :func  f1               - scores a candidate on first objective
    :func  f2               - scores a candidate on second objective
    :func  function_value   - A function that scores a candidate
    :func  constraint_ok    - A function that checks for constraints (none of Kursawe and Schaffer)
    :func  norm             - A function that computes the objective scores for each candidate(normalized)
    :func  reset_baseline   - Resets the baseline for obj_high and obj_low computation
    """
    
    def __init__(self,num_eval = 0.0,prob = 0.5,high = 10**6,low = -10**6):
        self.name = "Golinski"
        self.num_decisions = 7
        self.num_objectives = 2
        self.dec_high = [3.6,0.8,28.0,8.3,8.3,3.9,5.5]
        self.dec_low = [2.6,0.7,17.0,7.3,7.3,2.9,5.0]
        self.steps = 20
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
        
    def f1(self,dec):
        return 0.7854 * dec[0] * dec[1]**2 * ((10./3.)*dec[2]**2 + 14.933 * dec[2] - 43.0934) - 1.508 * dec[0] * (dec[5]**2 + dec[6]**2) + 7.477 * (dec[5]**3 + dec[6]**3) + 0.7854*(dec[3]*dec[5]**2 + dec[4]*dec[6]**2)
    
    def f2(self,dec):
        return math.sqrt(((745. * dec[3])/(dec[1]*dec[2]))**2 + 1.69 * 10**7)/(0.1 * dec[5]**3)
    
    def function_value(self,dec):
        return self.f1(dec) + self.f2(dec)
    
    def contraint_ok(self,dec):
        g1 =  ((1.)/(dec[0] * dec[1]**2 * dec[2])) - ((1.)/(27.)) <= 0 
        g2 =  ((1.)/(dec[0] * dec[1]**2 * dec[2])) - ((1.)/(27.)) <= 0 
        g3 =  ((dec[3]**3)/(dec[1] * dec[2]**2 * dec[5]**4)) - ((1.)/(1.93)) <= 0 
        g4 =  ((dec[4]**3)/(dec[1] * dec[2] * dec[6]**4)) - ((1.)/(1.93)) <= 0 
        g5 =  dec[1] * dec[2] - 40 <= 0
        g6 =  (dec[0]/dec[1]) - 12 <= 0
        g7 =  5 - (dec[0]/dec[1]) <= 0
        g8 =  1.9 - dec[3] + 1.5*dec[5] <= 0
        g9 = 1.9 - dec[4] + 1.1 * dec[6] <= 0
        g10 = self.f2(dec) <= 1300
        a = 745.0 * dec[4] / (dec[1] * dec[2])
        b = 1.575 * 10**8
        g11 = (math.sqrt(a**2 + b) / (0.1 * dec[6]**3)) <= 1100
        return g1 and g2 and g3 and g4 and g5 and g6 and g7 and g8 and g9 and g10 and g11 and (self.function_value(dec) >= self.threshold)
        
    def randomstate(self):
        while True:
            dec = list()
            for low,high in zip(self.dec_low,self.dec_high):
                dec.append(random.uniform(low,high))
            if self.contraint_ok(dec):
                return dec   
    
    def norm(self,state):
        return (self.function_value(state) - self.obj_low)/(self.obj_high - self.obj_low)
        
    def f1_norm(self,state):
        return (self.f1(state) - self.obj_low)/(self.obj_high - self.obj_low)
        
    def f2_norm(self,state):
        return (self.f2(state) - self.obj_low)/(self.obj_high - self.obj_low)
        
