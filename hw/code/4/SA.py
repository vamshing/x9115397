from __future__ import print_function, division
from time import strftime
from pprint import pprint
import math,random

__author__ = "Sattwik Pati aka ICE!V!an"
__copyright__ = "NA"
__license__ = "NA"
__version__ = "NA"


def compute(dec):
    return dec ** 2 , (dec-2)**2
    
##Model
class Schaffer_model():
    def __init__(self,hi,low):
        self.low = low
        self.hi = hi
        self.objhi = 1.0
        self.objlow = 0.0
        self.minobj = self.objlow
        self.maxobj = self.objhi
        
    def generate(self):
        return random.randrange(self.low,self.hi,1)
        
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

##Optimizer
def SA(model,kmax=1000,cooling=5):
    k = 0
    state = model.generate()
    en = model.compute_f(state)
    b_state,be_en = state,en
    reading = ""
    while k<kmax-1:
        k = k+1
        state_reading = " ."
        neigh_state = model.neighbor(state)
        neigh_en = model.compute_f(neigh_state)
        if neigh_en< be_en:
            state_reading = " !"
            b_state,be_en = neigh_state,neigh_en
        elif neigh_en< en:
            state_reading = " +"
            state,en = neigh_state,neigh_en
        elif math.e**((en - neigh_en)/((1-(k/kmax))))>random.random():
            state_reading = " ?"
            state,en = neigh_state,neigh_en
        reading +=  state_reading
        if  k % 25 == 0 :
            print(str(model.denorm(be_en))+reading)
            reading = ""
    print(model.maxobj,model.minobj)
    return b_state,be_en

##Initiator
def hw4():
    print("### saDemo ##################################################")
    print("# " + strftime("%Y-%m-%d %H:%M:%S"))
    print("# Basic study.")
    print("!!! Schaffer\n")
    print("Schaffer\n")
    hi = 100
    low = -hi
    best,en = SA(Schaffer_model(hi,low))
    print(best,en)
    
if __name__ == "__main__":
  hw4()
