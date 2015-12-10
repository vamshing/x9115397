from __future__ import print_function, division
from time import strftime
from pprint import pprint
from type2 import type2
import math,random,copy
from models import *
from GA import *

def DE(model):

    def build_frontier():
        new_frontier = []
        for _ in xrange(10):
            neighbor = model.get_neighbor()
            while model.okay(neighbor) is False:
                neighbor = model.get_neighbor()
            new_frontier.append(neighbor)

        return new_frontier
        
    def get_frontier_neighbors(cur):
        seen = []
        while len(seen) < 3:
            rand_index = random.randint(0, 9)
            if rand_index == cur:
                continue
            if rand_index not in seen:
                seen.append(rand_index)
                
        return seen

    def get_mutation(seen):
        soln = []
        for j in xrange(model.number_vars):
            l , m = model.var_bounds[j]
            inter = (frontier[seen[0]][j] + 0.75 * (frontier[seen[1]][j] - frontier[seen[2]][j]))
            if inter >= l and inter <= m:
                soln.append(inter)
            else:
                soln.append(frontier[seen[random.randint(0, 2)]][j])
        return soln
    


    print("Model Name : " + 'Genetic Algorithm on DTLZ5(2,10)' + ", Optimizer : differential evolution")
    frontier = build_frontier()
    print('Built the frontier',len(frontier))
    e = compute_score(frontier[0])
    best_sol = frontier[0]
    
    eras = 5
    previous_era = []
    current_era = []

    k_max = 100
    k = 0
    cf = 0.3
    threshold = 0

    while k < k_max:
        output = ""
        

        for i, solution in enumerate(frontier):
            seen = get_frontier_neighbors(i)
            mutation = frontier[seen[0]]
            cur_e = compute_score(solution)
            out = "."
            if cf < random.random():
                #if model.type1(mutation, solution):
                cur_e = compute_score(mutation)
                frontier[i] = mutation
                out += "+"
         
            else:
                mutation = get_mutation(seen)
                #if model.okay(mutation) and model.type1(mutation, solution):
                frontier[i] = mutation
                cur_e = model.eval(mutation)
                out = "+"
                        
                """
                if model.type1(solution, best_sol) and model.normalize_val(cur_e) >= threshold:
                out = "?"
                e = cur_e
                best_sol = frontier[i]
                """
               
            output += out
            k += 1
            if k % 5 is 0:
                # print ("%.5f,  %20s" % (model.normalize_val(e), output))
                output = ""
                
            if k % 20 is 0 and k is not 0:
                if len(previous_era) is not 0:
                    eras += type2(current_era, previous_era, model)
                    
                previous_era = list(current_era)
                current_era = []
            else:
                current_era.append(solution)
                
            if eras == 0:
                print("Early Termination " + str(k) + " : " + str(eras))
                return previous_era
        print(k) 
    return previous_era