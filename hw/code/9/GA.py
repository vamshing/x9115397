import sys
import random
import operator
import time
import datetime
sys.path
sys.path.append('/Users/vamshiguduguntla/Documents/CSC591/Github/x9115397/hw/code/9/models/')
from sk import a12

from DTLZ1 import *
from DTLZ3 import *
from DTLZ5 import *
from DTLZ7 import *

class GA:
    
    def __init__(self,model,num_candidates = 10,num_generations = 10,mutation_prob = 0.05):
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
   
    def min_max(self, box):
        """
        Returns the maximum and minimum objective function vectors to calculate hypervolume
        """
        max_vector = [np.max([model.function_value(x,model.num_decisions,model.num_objectives)[i] for x in box]) for i in range(model.num_objectives)]
        min_vector = [np.min([model.function_value(x,model.num_decisions,model.num_objectives)[i] for x in box]) for i in range(model.num_objectives)]

        return max_vector, min_vector
    
    def select(self,box):
        """
        Selection Operation
        Return the candidate pool for new frontier 80% from child and 20% from random parents
        """
        fr = []
        d = dict()
        
        for i in range(len(box)):
            d[i]  = self.function_agg(box[i])
        sorted_d = sorted(d.items(), key=operator.itemgetter(1),reverse=True)
        
        for j in range(int(self.num_candidates * .9)):
            fr.append(box[sorted_d[j][0]])    
        
        for k in range(int(self.num_candidates * .1)):
            fr.append(self.frontier[k])
        
        return fr
    
    def crossover(self,parent_1,parent_2,child):
        """
        Crossover operation
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
        Mutation operation
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
            if (a12(era_new, era_old) > 0.4):
                return 5
        return -1    
    
    def inbox(self, pebble, frontier):
        """
        Helper function to the Hypervolume
        """
        for x in frontier:
            fun_vector = model.function_value(x,model.num_decisions,model.num_objectives)
            for i in range(model.num_objectives):
                if pebble[i] < fun_vector[i]:
                    return False
        return True

    def hypervolume(self, frontier, min_vector, max_vector, n=10):
        """
        Calculates the Hypervolume in given size
        """
        count = 0.0
        for i in range(n):
            pebble = [random.uniform(min_vector[k], max_vector[k]) for k in range(model.num_objectives)]
            if self.inbox(pebble, frontier):
                count += 1.0
        return (count/(n*1.0))
                   
    def main(self,model):
        
        box =  [model.randomstate() for _ in range(self.num_candidates)]
        #self.base_frontier = box
        self.frontier = box
        max_vector, min_vector = self.min_max(box)
        
        for i in range(self.num_generations):
            newbox = []
            '''Generation'''
            for j in range(self.num_candidates):    
                child = model
                sample = np.random.randint(0, len(self.frontier), size=2)
                parent_1 = self.frontier[sample[0]]
                parent_2= self.frontier[sample[1]]
                '''Cross-Over'''
                self.crossover(parent_1,parent_2,child)
                '''Mutation'''
                if random.random() < self.mutation_prob :
                    self.mutate(child)
                '''New generation'''    
                newbox.append(child.dec)
                newbox.append(child.dec_2)
            '''Selection of the fitttest''' 
            self.frontier_new = []
            self.frontier_new = self.select(newbox)
            self.lives += self.penalize_lives()
            '''Early termination'''
            if self.lives == 0:
                break
            
            box = newbox
            self.frontier = self.frontier_new
            #print '# Generation:',i,'No. of lives',self.lives
        '''Best frontier and hypervolume'''    
        #print '*******************'
        #print 'Total Generations:',i
        #print 'Measured Hypervolume:',
        hv = self.hypervolume(self.frontier_new, min_vector, max_vector)
        return [hv,i]

if __name__ == '__main__':
    
    models = [DTLZ1,DTLZ3,DTLZ5,DTLZ7]
    model_text = ["DTLZ1", "DTLZ3", "DTLZ5", "DTLZ7"]
    objectives = [2,4,6,8]
    decisions =  [10,20,40]
    baseline = 10

    for model_type, text in zip(models, model_text):
        print '**',datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'),'**'
        print '**Optimizing**',model_type
        print '--------Baseline Study for :',baseline,'simulations--------'
        print '\n'
        for decs in decisions:
            for objs in objectives:
                print 'Decisions : ',decs,'Objectives: ',objs
                result = [] 
                for i in range(baseline):
                    model =  model_type(objs, decs)
                    result.append(GA(model).main(model))

                print 'Mean Hypervolume: ',np.mean([result[_][0] for _ in range(len(result))])
                print 'SD   Hypervolume: ',np.std([result[_][0] for _ in range(len(result))])
                print 'Mean Generations: ',int(np.mean([result[_][1] for _ in range(len(result))]))
                print '\n'
