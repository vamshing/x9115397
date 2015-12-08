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

def run(decs=10,objs=2,iters=20):
    era_data = []
    model = DTLZ7(decs, objs)
    for i in xrange(1,iters+1):
        for optimizer in [MWS, SA, DE]:
            era_val = [model.normalize_val(model.eval(val)) for val in optimizer(model)]
            era_val.insert(0, str(optimizer.__name__) + str(i))
            if((i==1)or(i==iters)):
                era_data.append(era_val)
    print(rdivDemo(era_data))

if __name__ == '__main__':
    run(10,2,3)
<<<<<<< HEAD
    
=======
    
>>>>>>> e0e5c151b1e9b5dd8ead82f2c40e763aa77e447a
