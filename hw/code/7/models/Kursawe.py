from __future__ import print_function, division
from time import strftime
from pprint import pprint
import math,random

import math,random,copy

__author__ = "Sattwik Pati aka ICE!V!an"
__copyright__ = "NA"
__license__ = "NA"
__version__ = "NA"


def kursawe(dec_list):
    f1,f2=0,0
    for i in xrange(0,len(dec_list)):
        if (i!=len(dec_list)-1):
            f1 += -10*math.e**(-0.2 * math.sqrt(dec_list[i]**2 + dec_list[i+1]**2))
        f2+=abs(dec_list[i])**0.8 + 5*math.sin(dec_list[i]**3)
    return (f1+f2)
    
##Model
class Kursawe():
    def __init__(self,hi,low,objhi=1.0,objlow=0.0):
        self.upper_limits=[5, 5, 5]
        self.lower_limits=[-5, -5, -5]
        self.steps = 10
        self.dec_list = []
        
        self.low = low
        self.hi = hi
        self.objhi = objhi
        self.objlow = objlow
        self.minobj = self.objlow
        self.maxobj = self.objhi
        self.name = "Kursawe"
        
    def objective_fns(self):
        return True
        
    def generate(self):
        self.dec_list=[]
        for i,j in zip(self.upper_limits,self.lower_limits):
            self.dec_list.append(random.uniform(j,i))
        if self.objective_fns():
            return self.dec_list
    
    def max_sol(self,c):
        iter = (self.upper_limits[c]-self.lower_limits[c])/self.steps
        best_solution = copy.copy(self.dec_list)
        for i in xrange(1,self.steps+1):
            self.dec_list[c] = self.lower_limits[c] + iter*i
            if self.objective_fns()==False:
                continue
            if (kursawe(self.dec_list)>kursawe(best_solution)):
                best_solution = copy.copy(self.dec_list)
        return best_solution
    
    def norm(self,val):
        self.minobj = val if self.minobj > val else self.minobj
        self.maxobj = val if self.maxobj < val else self.maxobj
        return (val - self.objlow) / (self.objhi - self.objlow)
    
    def denorm(self,val):
        return val * (self.objhi - self.objlow) + self.objlow
    
    def compute_f(self,val):
        return self.norm(kursawe(val))

    def retrieve_objs(self):
        return self.minobj,self.maxobj,self.name
    
    def neighbor(self,old):
        return self.generate()