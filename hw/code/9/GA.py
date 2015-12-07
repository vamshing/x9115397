
# coding: utf-8

# In[59]:

import sys
import random
sys.path
sys.path.append('/Users/vamshiguduguntla/Documents/Python-Programs/models/')

from DTLZ1 import *
from DTLZ3 import *
from DTLZ5 import *
from DTLZ7 import *

class GA:
    
    def __init__(self,model,num_candidates = 100,num_generations = 1000,mutation_prob = 0.05):
        self.num_objectives = model.num_objectives
        self.num_decisions = model.num_decisions
        self.num_candidates = num_candidates
        self.num_generations = num_generations
        self.mutation_prob = mutation_prob
        self.lives = 0
        self.num_lives = 5
        self.frontier = []
        self.frontier_new = []
        self.best_frontier = []
        self.base_frontier = []
        self.main(model)
        
    def binary_domination(self,x,y):
        """
        Returns whether candidate x dominates candidate y (Binary domination)
        """
        x_obj_vec = model.function_value(x)
        y_obj_vec = model.function_value(y)
        
        for i in range(model.num_objectives):
            if x_obj_vec[i] <= y_obj_vec[i]:
                return False
        return True
    
    
    def select(self,box):
        """
        Return the candidate which has binary dominated candidates in the box
        """
        fr = []
        for x in box:
            selection = 1
            for y in box:
                if self.binary_domination(y,x):
                    selection = -1
                    break
            if selection == 1:
                fr.append(x)
        return fr
    
    
    def crossover(self,parent_1,parent_2,child):
        """
        Picks a random decision, take all dad's decisions up to that point, take alll mum's decisions after that point
        """
        while True:
            rand_int = random.randint(0,model.num_decisions)
            child.dec = list(np.array(parent_1)[:rand_int])+list(np.array(parent_2)[rand_int:])
            if child.ok():
                return child
        
    def mutate(self,child):
        """
        Picks a candidate, returns the random decisions to create a new candidate
        """
        child.randomstate()
        return child
        
    
    def update_best_frontier(self,best_frontier,frontier_new):
        """
        Updates the best frontier by comparing with the candidates in the frontier_new
        set the lives to 0 if the new frontier is better than baseline frontier else increments it
        """
        t = []
        for x in self.frontier_new:
            for y in self.best_frontier:
                if self.binary_domination(x,y):
                    t.append(x)
                    self.best_frontier.pop(y)
        
        if len(t) > 0:
            self.best_frontier.extend(t)
            self.lives = 0
        else:
            if self.check_for_worse():
                self.lives = 0
            else:
                self.lives += 1
    
    def check_for_worse(self):
        """
        Checks if the frontier_new is good compared to the baseline population
        """
        for x in self.frontier_new:
            for y in self.base_frontier:
                if self.binary_domination(x,y):
                    return True
                break
        return False
        
    def main(self,model):
        
        box =  [model.randomstate() for _ in range(self.num_candidates)]
        self.base_frontier = self.select(box)
        self.frontier = self.select(box)
        self.best_frontier = self.frontier
        
        for i in range(self.num_generations):
            newbox = []
            for j in range(self.num_candidates):
                child = model
                sample = np.random.randint(0, len(self.frontier), size=2)
                parent_1 = self.frontier[sample[0]]
                parent_2= self.frontier[sample[1]]
                self.crossover(parent_1,parent_2,child)
                
                if random.random() < self.mutation_prob * (self.lives):
                    self.mutate(child)
                newbox.append(child.dec)
            
            self.frontier_new = []
            self.frontier_new = self.select(box)
            self.update_best_frontier(self.best_frontier,self.frontier_new)
            
            if self.lives == self.num_lives:
                break
            
            box = newbox
            self.frontier = self.frontier_new
            
            print '### Generation:',i,'No. of lives left',self.num_lives - self.lives
            
        return self.best_frontier


# In[102]:

model = DTLZ1(2,10)
state = model.randomstate()
GA(model)


# In[ ]:




# In[ ]:



