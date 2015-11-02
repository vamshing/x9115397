from __future__ import print_function, division
from time import strftime
from pprint import pprint

import math,random,copy

__author__ = "Sattwik Pati aka ICE!V!an"
__copyright__ = "NA"
__license__ = "NA"
__version__ = "NA"


def osyczka(dec_list):
    f1 = -(25 * (dec_list[0] - 2)**2 + (dec_list[1] - 2)**2 + (dec_list[2] - 1)**2 * (dec_list[3] - 4)**2 + (dec_list[4] - 1)**2)
    f2 = sum([i**2 for i in dec_list])
    return (f1+f2)
    
##Model
class Osyczka_model():
    def __init__(self,hi,low,objhi=1.0,objlow=0.0):
        self.upper_limits=[10, 10, 5, 6, 5, 10]
        self.lower_limits=[0, 0, 1, 0, 1, 0]
        self.steps = 10
        self.dec_list = []
        
        self.low = low
        self.hi = hi
        self.objhi = objhi
        self.objlow = objlow
        self.minobj = self.objlow
        self.maxobj = self.objhi
        
    def objective_fns(self):
        objectives = []
        objectives.extend([self.dec_list[0] + self.dec_list[1] - 2,
        6 - self.dec_list[0] - self.dec_list[1],
        2 - self.dec_list[1] + self.dec_list[0],
        2 - self.dec_list[0] + 3*self.dec_list[1],
        4 - self.dec_list[3] - (self.dec_list[2] - 3)**2,
        (self.dec_list[4] - 3)**3 + self.dec_list[5] - 4
        ])
        for c in objectives:
            if c < 0:
                return False
        return True
        
    def random_sol(self):
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
            if (osyczka(self.dec_list)>osyczka(best_solution)):
                best_solution = copy.copy(self.dec_list)
        return best_solution
    
    def norm(self,val):
        self.minobj = val if self.minobj > val else self.minobj
        self.maxobj = val if self.maxobj < val else self.maxobj
        return (val - self.objlow) / (self.objhi - self.objlow)
    
    def denorm(self,val):
        return val * (self.objhi - self.objlow) + self.objlow
    
    def compute(self,val):
        return self.norm(osyczka(val))

    def retrieve_objs(self):
        return self.minobj,self.maxobj

##Optimizer
def MWS(model,val=False,kmax=1000,maxtries=50,maxchanges=100,threshold=200,p=0.5):
    best_solution = model.random_sol()
    be_en = model.compute(best_solution)
    output = ""
    threshold = model.norm(threshold)
    for i in xrange(0,maxtries):
        model.dec_list = model.random_sol()
        for j in xrange(0,maxchanges):
            record = " ."
            curr_en = model.compute(model.dec_list)
            if curr_en>threshold:
                best_solution = copy.copy(model.dec_list)
                be_en = curr_en
                if (val==True):
                    return model.retrieve_objs()
                else:
                    print(output)
                    return best_solution,model.denorm(be_en)
            c =  random.randint(0,5)
            oldsolution = copy.copy(model.dec_list)
            old_en = curr_en
            if p< random.random():
                lives = 10
                while True:
                    model.dec_list[c] = random.uniform(model.lower_limits[c],model.upper_limits[c])
                    lives -=1
                    if((model.objective_fns())or(lives==0)):
                        curr_en = model.compute(model.dec_list)
                        break
                if((model.objective_fns()==False)and(lives==0)):
                    model.dec_list = copy.copy(oldsolution)
                    curr_en = model.compute(model.dec_list)
            else:
                model.dec_list = model.max_sol(c)
                curr_en = model.compute(model.dec_list)
            if(old_en==curr_en):
                record = " ."
            elif(old_en>curr_en):
                    record = " ?"
            else:
                if(old_en<curr_en):
                    record = " +"
            if(be_en<curr_en):
                best_solution = copy.copy(model.dec_list)
                be_en = curr_en
                record = " !"
            output += record
    if (val==True):
        return model.retrieve_objs()
    else:
        print(output)
        return best_solution,be_en


##Initiator
def hw5():
    print("### saDemo ##################################################")
    print("# " + strftime("%Y-%m-%d %H:%M:%S"))
    print("# Basic study.")
    print("!!! Osyczka\n")
    print("Osyczka\n")
    hi = 1
    low = 0
    minobj,maxobj = MWS(Osyczka_model(hi,low),True)
    best,en = MWS(Osyczka_model(hi,low,maxobj,minobj))
    print("Best State",best)
    print("Best energy",en)
    
if __name__ == "__main__":
  hw5()
