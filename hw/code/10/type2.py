from __future__ import print_function, division
from time import strftime
from pprint import pprint
from models import *
from sk import a12
from sk import rdivDemo
import math,random
from GA import *

import math,random,copy

__author__ = "Sattwik Pati aka ICE!V!an"
__copyright__ = "NA"
__license__ = "NA"
__version__ = "NA"

def type2(era_one, era_two, model):
    for objective in model.get_objectives():
        era_one_objective = []
        era_two_objective = []
        for i in xrange(0, len(era_one)):
            era_one_objective.append(compute_score(era_one[i]))
            era_two_objective.append(compute_score(era_two[i]))
        if (a12(era_one_objective, era_two_objective) > 0.56):
            return 5
    return -1