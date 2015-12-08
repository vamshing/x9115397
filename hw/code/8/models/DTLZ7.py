from __future__ import print_function, division
from time import strftime
from pprint import pprint
from Model import *
import math,random

import math,random,copy

__author__ = "Sattwik Pati aka ICE!V!an"
__copyright__ = "NA"
__license__ = "NA"
__version__ = "NA"

class DTLZ7(Model):

    def __init__(self, num_dec, num_obj):
        Model.__init__(self)
        self.model_name = DTLZ7.__name__
        self.number_vars = num_dec
        self.number_obj = num_obj
        self.var_bounds = []
        for _ in xrange(self.number_vars):
            self.var_bounds.append((0.0,1.0))
        self.baselines()
        
    def eval(self, x):
        energy = 0
        for obj in self.get_objectives():
            energy += obj(x)

        return energy

    def gx(self, x):
        y = 0.0
        for i in xrange(0, self.number_vars):
            y += x[i]
        return(9*y/self.number_vars)

    def hx(self, f, g, x):
        y = 0.0
        for i in xrange(0, self.number_obj - 1):
            y += (f[i](x) / (1 + g)) * (1 + math.sin(3 * math.pi * f[i](x)))
        return self.number_obj - y

    def last_obj(self, x, f):
        g = 1 + self.gx(x)
        res = (1 + g) * self.hx(f, g, x)
        return res

    def obj(self, x, i):
        return x[i]

    def get_objectives(self):
        f = [None] * self.number_obj
        for i in xrange(0, self.number_obj - 1):
            f[i] = lambda x : self.obj(x, i)
        f[self.number_obj - 1] = lambda x : self.last_obj(x, f)

        return f