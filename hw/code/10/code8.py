from __future__ import print_function, division
from time import strftime
from pprint import pprint
from GA import *
'''
importing optimizers
'''
from DE import *

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

__author__ = "Sattwik Pati aka ICE!V!an and Guduguntla Vamshi"
__copyright__ = "NA"
__license__ = "NA"
__version__ = "NA"



if __name__ == '__main__':
    #run(10,1,1)
    
    for _ in range(10):
        model = DTLZ7(3, 1)
        final_era = []
        for val in DE(model):
            final_era.append(val)
            print(final_era)
    
        final_era_val = [(compute_score([10,0.1,.1])) for val in final_era]
        print(sorted(final_era_val,reverse=True))
    
        print(compute_score([10,0.1,.1]))