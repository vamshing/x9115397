
 
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

    
def SA(model,kmax=10**5,cooling=5,emax=0):
    
    print("Model Name is " + model.model_name + ", Optimizer is Simulated Annealing")
    
    # Base variables
    eMax = 0
    reading = ""

    # Start with a random value
    state = model.get_neighbor()
    en = model.normalize_val(model.eval(state))
    
    lives = 5
    previous_era = []
    current_era = []

    b_state,be_en = state,en

    i = 0
    while i < kmax - 1 and state > emax:
        state_reading = " ."
        neigh_state = model.get_neighbor()
        neigh_en = model.normalize_val(model.eval(neigh_state))
        
        if model.type1(neigh_state,b_state):
            state_reading = " !"
            b_state,be_en = neigh_state,neigh_en
        elif model.type1(neigh_state,state):
            state_reading = " +"
            state,en = neigh_state,neigh_en
        elif math.e**((en - neigh_en)/((1-(i/kmax))**cooling))>random.random():
            state_reading = " ?"
            state,en = neigh_state,neigh_en
        reading +=  state_reading
        if i % 100 is 0 and i is not 0:
            if len(previous_era) is not 0:
                lives += type2(current_era, previous_era, model)
                    
            previous_era = list(current_era)
            current_era = []
        else:
            current_era.append(neigh_state)
                
        if lives == 0:
            return previous_era
        i += 1
    return previous_era
