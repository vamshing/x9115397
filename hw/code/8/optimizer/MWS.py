from __future__ import print_function, division
from time import strftime
from pprint import pprint
from type2 import type2
from models import *


import math,random,copy

__author__ = "Sattwik Pati aka ICE!V!an"
__copyright__ = "NA"
__license__ = "NA"
__version__ = "NA"


##Optimizer
def MWS(model,val=False,kmax=1000,maxtries=1000,maxchanges=50,threshold=0,p=0.5):
    def change_to_maximize(soln, index,steps=10):
        evaluations = 0
        best = soln
        solution = soln
        low, high = model.var_bounds[index]
        delta = (high - low)/steps
        for k in xrange(0, steps):
            evaluations += 1
            solution[index] = low + delta*k
            if model.okay(solution) and model.type1(solution, best):
                best = list(solution)
        return best
        
    print("Model Name is " + model.model_name + ", Optimizer is Max Walk Sat")
    best_solution = model.get_neighbor()
    be_en = model.normalize_val(model.eval(best_solution))
    output = ""
    lives = 5
    previous_era = []
    current_era = []
    step = 10
    for i in xrange(0,maxtries):
        new_solution = model.get_neighbor()
        new_en = model.normalize_val(model.eval(new_solution))
        for j in xrange(0,maxchanges):
            record = " ."
            curr_en = new_en
            if curr_en<threshold:
                if len(previous_era) is not 0:
                    return previous_era
                else:
                    return current_era
            c =  random.randint(0,model.number_vars-1)
            oldsolution = copy.copy(new_solution)
            old_en = new_en
            if p< random.random():
                new_solution[c] = random.uniform(model.var_bounds[c][0],model.var_bounds[c][1])
            else:
                new_solution = change_to_maximize(new_solution, c)
                curr_en = model.normalize_val(model.eval(new_solution))
            if(old_en==curr_en):
                record = " ."
            elif(old_en>curr_en):
                record = " ?"
            else:
                if(old_en<curr_en):
                    record = " +"
            if(be_en<curr_en):
                best_solution = copy.copy(new_solution)
                be_en = curr_en
                record = " !"
            output += record
        if i % 100 is 0 and i is not 0:
            if len(previous_era) is not 0:
                lives += type2(current_era, previous_era, model)
                    
            previous_era = list(current_era)
            current_era = []
        else:
            current_era.append(new_solution)
                
        if lives <= 0:
            return previous_era
    if len(previous_era) is not 0:
        return previous_era
    else:
        return current_era
