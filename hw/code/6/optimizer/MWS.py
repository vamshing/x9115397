from __future__ import print_function, division
from time import strftime
from pprint import pprint
from models import *

import math,random,copy

__author__ = "Sattwik Pati aka ICE!V!an"
__copyright__ = "NA"
__license__ = "NA"
__version__ = "NA"


##Optimizer
def run(model,val=False,kmax=1000,maxtries=50,maxchanges=100,threshold=200,p=0.5):
    best_solution = model.generate()
    be_en = model.compute_f(best_solution)
    output = ""
    threshold = model.norm(threshold)
    for i in xrange(0,maxtries):
        model.dec_list = model.generate()
        for j in xrange(0,maxchanges):
            record = " ."
            curr_en = model.compute_f(model.dec_list)
            if curr_en>threshold:
                best_solution = copy.copy(model.dec_list)
                be_en = curr_en
                if (val==True):
                    return model.retrieve_objs()
                else:
                    print(output)
                    return best_solution,model.denorm(be_en)
            c =  random.randint(0,len(model.dec_list)-1)
            oldsolution = copy.copy(model.dec_list)
            old_en = curr_en
            if p< random.random():
                lives = 10
                while True:
                    model.dec_list[c] = random.uniform(model.lower_limits[c],model.upper_limits[c])
                    lives -=1
                    if((model.objective_fns())or(lives==0)):
                        curr_en = model.compute_f(model.dec_list)
                        break
                if((model.objective_fns()==False)and(lives==0)):
                    model.dec_list = copy.copy(oldsolution)
                    curr_en = model.compute_f(model.dec_list)
            else:
                model.dec_list = model.max_sol(c)
                curr_en = model.compute_f(model.dec_list)
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
def MWS(model):
    print("### saDemo ##################################################")
    print("# " + strftime("%Y-%m-%d %H:%M:%S"))
    print("# Basic study.")
    hi = 1
    low = 0
    minobj,maxobj,name = run(model(hi,low),True)
    print("!!!",name,"\n")
    print(name,"\n")
    best,en = run(model(hi,low,maxobj,minobj))
    print("Best State",best)
    print("Best energy",en)