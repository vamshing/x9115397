from __future__ import print_function, division
from time import strftime
from pprint import pprint
import math,random,copy

__author__ = "Sattwik Pati aka ICE!V!an"
__copyright__ = "NA"
__license__ = "NA"
__version__ = "NA"

upper_limits=[10, 10, 5, 6, 5, 10]
lower_limits=[0, 0, 1, 0, 1, 0]
steps = 10
p = 0.5
maxtries = 100
maxchanges = 50
threshold = 200

def objective_fns(dec_list):
    objectives = []
    objectives.extend([dec_list[0] + dec_list[1] - 2,
    6 - dec_list[0] - dec_list[1],
    2 - dec_list[1] + dec_list[0],
    2 - dec_list[0] + 3*dec_list[1],
    4 - dec_list[3] - (dec_list[2] - 3)**2,
    (dec_list[4] - 3)**3 + dec_list[5] - 4
    ])
    for c in objectives:
        if c < 0:
            return False
    return True

def osyczka(dec_list):
    f1 = -(25 * (dec_list[0] - 2)**2 + (dec_list[1] - 2)**2 + (dec_list[2] - 1)**2 * (dec_list[3] - 4)**2 + (dec_list[4] - 1)**2)
    f2 = sum([i**2 for i in dec_list])
    return (f1+f2)
    
def random_sol():
    while True:
        dec_list = []
        for i,j in zip(upper_limits,lower_limits):
            dec_list.append(random.uniform(j,i))
        
        if objective_fns(dec_list):
            return dec_list
            
def max_sol(solution,c):
    iter = (upper_limits[c]-lower_limits[c])/steps
    best_solution = solution
    for i in xrange(1,steps+1):
        solution[c] = lower_limits[c] + iter*i
        if objective_fns(solution)==False:
            continue
        if (osyczka(solution)>osyczka(best_solution)):
            print(osyczka(best_solution),osyczka(solution))
            best_solution = solution
    return best_solution
    
def maxwalksat():
    best_solution = random_sol()
    output = ""
    for i in xrange(0,maxtries):
        solution = random_sol()
        for j in xrange(0,maxchanges):
            record = " ."
            if osyczka(solution)>threshold:
                best_solution = copy.copy(solution)
                return best_solution
            c =  random.randint(0,5)
            oldsolution = copy.copy(solution)
            if p< random.random():
                lives = 10
                while True:
                    solution[c] = random.uniform(lower_limits[c],upper_limits[c])
                    lives -=1
                    if((objective_fns(solution))or(lives==0)):
                        break
                if((objective_fns(solution)==False)and(lives==0)):
                    solution = copy.copy(oldsolution)
                if(osyczka(oldsolution)==osyczka(solution)):
                    record = " ."
                else:
                    record = " ?"
            else:
                solution = max_sol(solution,c)
                record = " +"
                if(osyczka(oldsolution)==osyczka(solution)):
                    record = " ."
                '''elif (best_solution < solution):
                    record = " !"
                    best_solution = solution'''
            if(osyczka(best_solution)<osyczka(solution)):
                best_solution = copy.copy(solution)
                record = " !"
            output += record
    return best_solution,output

if __name__ == '__main__':
    best_solution,output = maxwalksat()
    be = osyczka(best_solution)
    print(output)
    print(best_solution,be)
    
