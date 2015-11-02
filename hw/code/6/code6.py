from __future__ import print_function, division
from time import strftime
from pprint import pprint
'''
importing optimizers
'''
from optimizer.SA import SA
from optimizer.MWS import MWS
'''
importing models
'''
from models.Schaffer import Schaffer
from models.Osyczka import Osyczka
from models.Kursawe import Kursawe
#from models import *


import math,random,copy

__author__ = "Sattwik Pati aka ICE!V!an"
__copyright__ = "NA"
__license__ = "NA"
__version__ = "NA"


##Initiator
def hw6():
    '''
    print("### saDemo ##################################################")
    print("# " + strftime("%Y-%m-%d %H:%M:%S"))
    print("# Basic study.")
    print("!!! Osyczka\n")
    print("Osyczka\n")
    hi = 1
    low 
    MWS(Osyczka_model(hi,low),True)
    minobj,maxobj = MWS(Osyczka_model(hi,low),True)
    best,en = MWS(Osyczka_model(hi,low,maxobj,minobj))
    print("Best State",best)
    print("Best energy",en)
    '''
    for model in [Schaffer, Osyczka, Kursawe]:
        for optimizer in [SA,MWS]:
            optimizer(model)
    
if __name__ == "__main__":
  hw6()