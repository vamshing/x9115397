import sys
import random
import operator
sys.path
sys.path.append('/Users/vamshiguduguntla/Documents/CSC591/Github/x9115397/hw/code/9/models/')
from sk import a12

from DTLZ1 import *
from DTLZ3 import *
from DTLZ5 import *
from DTLZ7 import *

class GA:
    
    def __init__(self,model,num_candidates = 100,num_generations = 100,mutation_prob = 0.05):
        self.num_objectives = model.num_objectives
        self.num_decisions = model.num_decisions
        self.num_candidates = num_candidates
        self.num_generations = num_generations
        self.mutation_prob = mutation_prob
        self.lives = 5
        self.frontier = []
        self.frontier_new = []
        self.base_frontier = []
        self.main(model)
        
    def binary_domination(self,x,y):
        """
        Type I comparison
        Returns whether candidate x dominates candidate y (Binary domination)
        """
        x_obj_vec = model.function_value(x,model.num_decisions,model.num_objectives)
        y_obj_vec = model.function_value(y,model.num_decisions,model.num_objectives)
        
        for i in range(model.num_objectives):
            if x_obj_vec[i] < y_obj_vec[i]:
                return False
        return True
    
    
    def function_agg(self,x):
        """
        Returns the aggregate function value
        """
        x_obj_vec = model.function_value(x,model.num_decisions,model.num_objectives)
        return np.sum(x_obj_vec)
    
    
    def select(self,box):
        """
        Return the candidate pool for new frontier 80% from child and 20% from random parents
        """
        fr = []
        
        d = dict()
        
        for i in range(len(box)):
            d[i]  = self.function_agg(box[i])
            
        sorted_d = sorted(d.items(), key=operator.itemgetter(1),reverse=True)
        
        for j in range(int(self.num_candidates * .8)):
            fr.append(box[sorted_d[j][0]])    
        
        for k in range(int(self.num_candidates * .2)):
            fr.append(self.frontier[k])
        
        return fr
    
    def crossover(self,parent_1,parent_2,child):
        """
        Picks a random decision, take all dad's decisions up to that point, take alll mum's decisions after that point
        """
        while True:
            rand_int = random.randint(0,model.num_decisions)
            child.dec = list(np.array(parent_1)[:rand_int])+list(np.array(parent_2)[rand_int:])
            child.dec_2 = list(np.array(parent_1)[rand_int:])+list(np.array(parent_2)[:rand_int])
            if child.ok(child.dec) and child.ok(child.dec_2):
                return child
        
    def mutate(self,child):
        """
        Picks a candidate, returns the random decisions to create a new candidate
        """
        child.randomstate()
        return child
        
        
    def penalize_lives(self):
        
        """
        Type II comparison
        Compares between current frontier and the previous frontier
        if atleast one is better in the current frontier - dont penalize
        """
        for i in xrange(0,model.num_objectives):
            era_old=[]
            era_new=[]
            for j in xrange(0,len(self.frontier_new)):
                era_old.append(self.frontier[j][i])
                era_new.append(self.frontier_new[j][i])
            if (a12(era_new, era_old) > 0.5):
                return 5
        return -1    
    
                    
    def main(self,model):
        
        box =  [model.randomstate() for _ in range(self.num_candidates)]
        self.base_frontier = box
        self.frontier = box
        
        for i in range(self.num_generations):
            newbox = []
            for j in range(self.num_candidates):
                
                child = model
                sample = np.random.randint(0, len(self.frontier), size=2)
                parent_1 = self.frontier[sample[0]]
                parent_2= self.frontier[sample[1]]
                self.crossover(parent_1,parent_2,child)
                if random.random() < self.mutation_prob :
                    self.mutate(child)
                    
                newbox.append(child.dec)
                newbox.append(child.dec_2)
    
            self.frontier_new = []
            self.frontier_new = self.select(newbox)
            self.lives += self.penalize_lives()
            
            if self.lives == 0:
                break
            
            box = newbox
            self.frontier = self.frontier_new
            
            print '### Generation:',i,'No. of lives',self.lives
            
        return self.frontier_new


# In[14]:

model = DTLZ1(4,10)
state = model.randomstate()
GA(model)