from __future__ import print_function, division
from time import strftime
from pprint import pprint
'''
importing optimizers
'''
from optimizer.SA import SA
from optimizer.MWS import MWS
from optimizer.DE import DE

import random
import sys
import math
'''
importing stats
'''
from sk import a12
from sk import rdivDemo
'''
importing models
'''
from models.DTLZ7 import DTLZ7

__author__ = "Sattwik Pati aka ICE!V!an"
__copyright__ = "NA"
__license__ = "NA"
__version__ = "NA"

if __name__ == '__main__':
            
    era_collection = []
    text = ["MWS", "SA", "DE"]
    ct = 0
    model = DTLZ7(10, 2)
    i = 0
    for _ in xrange(0, 20):
        i += 1
        for optimizer in [MWS, SA, DE]:
            era_val = [model.normalize_val(model.eval(val)) for val in optimizer(model)]
            era_val.insert(0, text[ct%3] + str(i))
            era_collection.append(era_val)
            ct += 1
    print(rdivDemo(era_collection))