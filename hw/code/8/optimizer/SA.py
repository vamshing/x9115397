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

    
def SA(model):
    
    def get_probability(cur_energy, neighbor_energy, count):
        return math.exp((cur_energy - neighbor_energy)/count)

    print("Model Name : " + model.model_name + ", Optimizer : simulated annealing")
    
    # Base variables
    kMax = 10**5
    eMax = 0
    output = ""

    # Start with a random value
    start_val = model.get_neighbor()
    cur_energy = model.normalize_val(model.eval(start_val))
    
    eras = 5
    previous_era = []
    current_era = []

    best_energy = cur_energy
    best_val = start_val
    cur_val = start_val
    i = 1
    while i < kMax - 1 and cur_energy > eMax:
        mutated_neighbor = model.get_neighbor()
        while model.okay(mutated_neighbor) is False:
            mutated_neighbor = model.get_neighbor()
        
        neighbor_energy = model.normalize_val(model.eval(mutated_neighbor))

        if model.type1(mutated_neighbor, best_val):
            best_energy = neighbor_energy
            best_val = mutated_neighbor
            output += "!"

        if model.type1(mutated_neighbor, cur_val):
            cur_energy = neighbor_energy
            cur_val = mutated_neighbor
            output += "+"

        elif get_probability(cur_energy, neighbor_energy,  (1 - i/kMax)**4) > random.random():
            cur_val = mutated_neighbor
            cur_energy = neighbor_energy
            output += "?"
        else:
            output += "."

        if i % 25 == 0:
            # print ("%6d : %.5f,  %25s" % (i, best_energy, output))
            output = ""
            cur_energy = 1
            
        if i % 100 is 0 and i is not 0:
            if len(previous_era) is not 0:
                eras += type2(current_era, previous_era, model)
                    
            previous_era = list(current_era)
            current_era = []
        else:
            current_era.append(mutated_neighbor)
                
        if eras == 0:
            print("Early Termination " + str(i) + " : " + str(eras))
            return previous_era

        i += 1

    return previous_era