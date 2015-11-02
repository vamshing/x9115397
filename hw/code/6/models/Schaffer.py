from __future__ import print_function, division
from time import strftime
from pprint import pprint
import math,random

import math,random,copy

__author__ = "Sattwik Pati aka ICE!V!an"
__copyright__ = "NA"
__license__ = "NA"
__version__ = "NA"

def compute(dec):
    return dec[0] ** 2 , (dec[0]-2)**2
    
class Schaffer():
    def __init__(self,hi,low,objhi=1.0,objlow=0.0):
        self.dec_list = []
        self.name = "Schaffer"
        self.low = low
        self.hi = hi
        self.upper_limits = [hi]
        self.lower_limits = [low]
        self.objhi = objhi
        self.objlow = objlow
        self.minobj = self.objlow
        self.maxobj = self.objhi
        self.steps = 10
        
    def generate(self):
        self.dec_list=[]
        for i,j in zip(self.upper_limits,self.lower_limits):
            self.dec_list.append(random.randrange(j,i,1))
        return self.dec_list
        
    def neighbor(self,old):
        return self.generate() 
    
    def norm(self,val):
        self.minobj = val if self.minobj > val else self.minobj
        self.maxobj = val if self.maxobj < val else self.maxobj
        return (val - self.objlow) / (self.objhi - self.objlow)
    
    def denorm(self,val):
        return val * (self.objhi - self.objlow) + self.objlow
    
    def compute_f(self,decision):
        f1, f2 = compute(decision)
        return self.norm(f1+f2)
    
    def retrieve_objs(self):
        return self.minobj,self.maxobj,self.name
    
    def objective_fns(self):
        return True
        
    def max_sol(self,c):
        iter = (self.upper_limits[c]-self.lower_limits[c])/self.steps
        best_solution = copy.copy(self.dec_list)
        for i in xrange(1,self.steps+1):
            self.dec_list[c] = self.lower_limits[c] + iter*i
            if self.objective_fns()==False:
                continue
            if (compute(self.dec_list)>compute(best_solution)):
                best_solution = copy.copy(self.dec_list)
        return best_solution
