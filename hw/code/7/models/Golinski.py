from __future__ import print_function, division
from time import strftime
from pprint import pprint

import math,random,copy

__author__ = "Sattwik Pati aka ICE!V!an"
__copyright__ = "NA"
__license__ = "NA"
__version__ = "NA"

def f1(dec_list):
    f1 = 0.7854*dec_list[0]*math.pow(dec_list[1],2)*(10*math.pow(dec_list[2],2)/3 + \
         14.933*dec_list[2]-43.0934)-1.508*dec_list[0]*(math.pow(dec_list[5],2)+math.pow(dec_list[6],2)) + \
         7.477*(math.pow(dec_list[5],3)+math.pow(dec_list[6],3))+0.7854 * \
         (dec_list[3]*math.pow(dec_list[5], 2)+dec_list[4]*math.pow(dec_list[6],2))
    return f1

def f2(dec_list):
    f2 = math.sqrt(math.pow((745.0*dec_list[3])/(dec_list[1]*dec_list[2]),2)+1.69*math.pow(10,7)) / \
         (0.1 * math.pow(dec_list[5],3))
    return f2
    
def golinski(dec_list):
    return f1(dec_list)+f2(dec_list)
    
##Model
class Golinski():
    def __init__(self,hi,low,objhi=1.0,objlow=0.0):
        self.lower_limits=[2.6, 0.7, 17.0, 7.3, 7.3, 2.9, 5.0]
        self.upper_limits=[3.6, 0.8, 28.0, 8.3, 8.3, 3.9, 5.5]
        self.steps = 10
        self.dec_list = []
        
        self.low = low
        self.hi = hi
        self.objhi = objhi
        self.objlow = objlow
        self.minobj = self.objlow
        self.maxobj = self.objhi
        self.name = "Golinski"
        
    def objective_fns(self):
        objectives = []
        objectives.extend([1.0/(self.dec_list[0]*math.pow(self.dec_list[1],2)*self.dec_list[2]) - 1.0/27.0 <= 0,
        1.0/(self.dec_list[0]*math.pow(self.dec_list[1],2)*math.pow(self.dec_list[2],2)) - 1.0/397.5 <= 0,
        math.pow(self.dec_list[3],3)/(self.dec_list[1]*math.pow(self.dec_list[2],2)*math.pow(self.dec_list[5],4)) - 1.0/1.93 <= 0,
        math.pow(self.dec_list[4],3)/(self.dec_list[1]*self.dec_list[2]*math.pow(self.dec_list[6],4)) - 1.0/1.93 <= 0,
        self.dec_list[1]*self.dec_list[2] - 40 <= 0,
        self.dec_list[0]/self.dec_list[1] - 12 <= 0,
        5 - self.dec_list[0]/self.dec_list[1] <= 0,
        1.9 - self.dec_list[3] + 1.5*self.dec_list[5] <= 0,
        1.9 - self.dec_list[4] + 1.1*self.dec_list[6] <= 0,
        f2(self.dec_list)<=1300,
        math.sqrt(math.pow((745.0*self.dec_list[4]/(self.dec_list[1]*self.dec_list[2])),2)+(1.575*math.pow(10,8))) / \
    (0.1*math.pow(self.dec_list[6],3)) <= 1100
        ])
        for c in objectives:
            if not c:
                return False
        return True
        
    def generate(self):
        while True:
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
            if (golinski(self.dec_list)>golinski(best_solution)):
                best_solution = copy.copy(self.dec_list)
        return best_solution
    
    def norm(self,val):
        self.minobj = val if self.minobj > val else self.minobj
        self.maxobj = val if self.maxobj < val else self.maxobj
        return (val - self.objlow) / (self.objhi - self.objlow)
    
    def denorm(self,val):
        return val * (self.objhi - self.objlow) + self.objlow
    
    def compute_f(self,val):
        return self.norm(golinski(val))

    def retrieve_objs(self):
        return self.minobj,self.maxobj,self.name
    
    def neighbor(self,old):
        return self.generate()