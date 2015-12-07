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
def MWS(model):

    def change_to_maximize(soln, index):
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
        return best, evaluations


    print("Model Name : " + model.model_name + ", Optimizer : max walk sat")
    
    max_tries = 1000
    max_changes = 50
    p = 0.5
    threshold = 0
    steps = 10
    
    eras = 5
    previous_era = []
    current_era = []

    evals = 0
    init_soln = model.get_neighbor()
    while model.okay(init_soln) is False and model.normalize_val(model.eval(init_soln)) > threshold:
        init_soln = model.get_neighbor()

    for i in xrange(0, max_tries):
        output = str()
        new_soln = model.get_neighbor()
        while model.okay(new_soln) is False:
            new_soln = model.get_neighbor()

        for j in xrange(0, max_changes):
            result = str()
            if model.normalize_val(model.eval(new_soln)) < threshold:
                if len(previous_era) is not 0:
                    return previous_era
                else:
                    return current_era

            c = random.randint(1, model.number_vars) - 1
            if p < random.random():
                copy_list = list(new_soln)
                i, j = model.var_bounds[c]
                if isinstance(i, int) and isinstance(j, int):
                    copy_list[c] = random.randrange(i, j)
                else:
                    copy_list[c] = random.uniform(i, j)

                if model.okay(copy_list) and model.normalize_val(model.eval(new_soln)) >= threshold:
                    new_soln = copy_list
                    result = "?"
                else:
                    result = "."
            else:
                copy_list, t_evals = change_to_maximize(list(new_soln), c)
                evals += t_evals
                if copy_list == new_soln:
                    result = "."
                else:
                    new_soln = copy_list
                    result = "+"
            output += result
            if model.type1(new_soln, init_soln) and model.normalize_val(model.eval(new_soln)) >= threshold:
                init_soln = list(new_soln)

        # print "Evals : " + str(evals) + " Current Best Energy : " + \
        #       str(model.normalize_val(model.eval(init_soln))) + " " + output
              
        if i % 100 is 0 and i is not 0:
            if len(previous_era) is not 0:
                eras += type2(current_era, previous_era, model)
                    
            previous_era = list(current_era)
            current_era = []
        else:
            current_era.append(new_soln)
                
        if eras <= 0:
            print("Early Termination " + str(i) + " : " + str(eras))
            return previous_era
    if len(previous_era) is not 0:
        return previous_era
    else:
        return current_era