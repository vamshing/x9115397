from __future__ import print_function, division
from time import strftime
from pprint import pprint

import sys

import math,random

import math,random,copy

__author__ = "Sattwik Pati aka ICE!V!an"
__copyright__ = "NA"
__license__ = "NA"
__version__ = "NA"

class Model:

    def __init__(self):
        self.model_name = None
        self.min_bound = sys.maxint
        self.max_bound = -self.min_bound
        self.lo = sys.maxint
        self.hi = -self.lo
        self.constraints = None
        self.number_vars = 0
        self.var_bounds = []
        self.baseline_count = 10**4

    def okay(self, _):
        return True
        
    def type1(self, solution, sb):
        return cdom(solution, sb, self)

    def get_neighbor(self):
        x = list()
        
        for i, j in self.var_bounds:
            if isinstance(i, int) and isinstance(j, int):
                x.append(random.randint(i, j))
            else:
                x.append(random.uniform(i, j))
        
        return x

    def baselines(self):
        self.lo = sys.maxint
        self.hi = -self.lo

        for _ in xrange(0, 100):

            while True:
                soln = self.get_neighbor()
                if self.okay(soln):
                    break

            energy = self.eval(soln)

            if energy > self.hi:
                self.hi = energy

            if energy < self.lo:
                self.lo = energy

    def normalize_val(self, value):
        return (value - self.lo)/(self.hi - self.lo)

    def eval(self, x):
        energy = 0
        for obj in self.get_objectives():
            energy += obj(x)

        return energy

    def get_objectives(self):
        return None

    def get_baselines(self):
        return self.lo, self.hi

def loss1(k, x, y):
    return (x - y) if better(k) == lt else (y - x)


def exp_loss(k, x, y, n):
    return math.exp(loss1(k, x, y) / n)


def loss(x1, y1, base_model):
    x, y = objs(x1, base_model), objs(y1, base_model)
    n = min(len(x), len(y))  # lengths should be equal
    losses = [exp_loss(k, xi, yi, n) for k, (xi, yi) in enumerate(zip(x, y))]
    # print losses
    return sum(losses) / n


def cdom(x, y, base_model):
    # "x dominates y if it losses least"
    return loss(x, y, base_model) < loss(y, x, base_model)


def gt(x, y): return x > y


def lt(x, y): return x < y


def better(i): return lt


def objs(can, base_model):
    return [compute_score(can)]