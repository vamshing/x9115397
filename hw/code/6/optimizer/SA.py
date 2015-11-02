from __future__ import print_function, division
from time import strftime
from pprint import pprint
import math,random
from models import *


__author__ = "Sattwik Pati aka ICE!V!an"
__copyright__ = "NA"
__license__ = "NA"
__version__ = "NA"

    
##Model

##Optimizer
def run(model,val=False,kmax=1000,cooling=5):
    k = 0
    state = model.generate()
    en = model.compute_f(state)
    b_state,be_en = state,en
    reading = ""
    while k<kmax-1:
        k = k+1
        state_reading = " ."
        neigh_state = model.neighbor(state)
        neigh_en = model.compute_f(neigh_state)
        if neigh_en< be_en:
            state_reading = " !"
            b_state,be_en = neigh_state,neigh_en
        elif neigh_en< en:
            state_reading = " +"
            state,en = neigh_state,neigh_en
        elif math.e**((en - neigh_en)/((1-(k/kmax))**cooling))>random.random():
            state_reading = " ?"
            state,en = neigh_state,neigh_en
        reading +=  state_reading
        if  k % 25 == 0 :
            if(val==False):
                print(str(be_en)+reading)
            reading = ""
    if (val==True):
        return model.retrieve_objs()
    else:
        return b_state,be_en

##Initiator
def SA(model):
    print("### saDemo ##################################################")
    print("# " + strftime("%Y-%m-%d %H:%M:%S"))
    print("# Basic study.")
    #print("!!! Schaffer\n")
    #print("Schaffer\n")
    hi = 100
    low = -hi
    minobj,maxobj,name = run(model(hi,low),True)
    print("!!!",name,"\n")
    print(name,"\n")
    best,en = run(model(hi,low,maxobj,minobj))
    print("Best State",best)
    print("Best energy",float(en))