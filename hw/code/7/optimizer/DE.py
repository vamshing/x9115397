from __future__ import print_function, division
from time import strftime
from pprint import pprint
import math,random,copy
from models import *


__author__ = "Sattwik Pati aka ICE!V!an"
__copyright__ = "NA"
__license__ = "NA"
__version__ = "NA"

    
##Model

##Optimizer
def run(model,val=False,maxtries=50,maxchanges=100,f=0.75,crossover=0.3):
    output = ""
    best_solution = model.generate()
    nos_dec = len(best_solution)
    test_space = [best_solution]
    for i in xrange(1,maxchanges):
        new_solution = model.generate()
        test_space.append(new_solution)
        if(model.compute_f(new_solution)<model.compute_f(best_solution)):
            best_solution = copy.copy(new_solution)
    for i in xrange(0,maxtries):
        new_space = []
        for j in xrange(0,len(test_space)):
            record = " ."
            roster = range(len(test_space))
            roster.remove(j)
            reference_sol = test_space[j]
            while True:
                empty_sol = [0]*nos_dec
                sample_picks = random.sample(roster,3)
                selected = [test_space[a] for a in sample_picks]
                r = random.randint(0,nos_dec-1)
                for k in xrange(0,nos_dec):
                    if ((random.random()<crossover) or (k == r)):
                        empty_sol[k]=selected[0][k]+f*(selected[1][k]-selected[2][k])
                    else:
                        empty_sol[k] = reference_sol[k]
                model.dec_list = copy.copy(empty_sol)
                if(model.objective_fns()):
                    break
            if(model.compute_f(empty_sol)<model.compute_f(best_solution)):
                best_solution = copy.copy(empty_sol)
                record = " !"
            elif(model.compute_f(empty_sol)<model.compute_f(reference_sol)):
                record = " +"
            output +=record
            new_space.append(empty_sol)
        test_space = copy.copy(new_space)
    if (val==True):
        return model.retrieve_objs()
    else:
        print(output)
        return best_solution,model.compute_f(best_solution)

##Initiator
def DE(model):
    print("### saDemo ##################################################")
    print("# " + strftime("%Y-%m-%d %H:%M:%S"))
    print("# Basic study.")
    #print("!!! Schaffer\n")
    #print("Schaffer\n")
    hi = 100
    low = -hi
    #run(model(hi,low),False)
    minobj,maxobj,name = run(model(hi,low),True)
    print("!!!",name,"\n")
    print(name,"\n")
    best,en = run(model(hi,low,maxobj,minobj))
    print("Best State",best)
    print("Best energy",float(en))