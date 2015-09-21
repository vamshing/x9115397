from __future__ import division, print_function
import random

__author__ = "Sattwik Pati aka ICE!V!an"
__copyright__ = "NA"
__license__ = "NA"
__version__ = "NA"

def has_duplicates(lst):
    if all(x is None for x in lst) or len(lst)==0:
        return False
    new_lst = sorted(lst)
    for i in range(1,len(new_lst)-1):
        if (new_lst[i-1]==new_lst[i]):
            return True
    return False

def random_birthdays(num):
    birthday_lst = []
    for i in range(0,num):
        birthday_lst.append(random.randint(1,365))
    return birthday_lst

def birthday_paradox(num = 23,iteration=1000):
    dup_birthday_count = 0
    for i in range(0,iteration):
        birthday_lst = random_birthdays(num)
        if has_duplicates(birthday_lst):
            dup_birthday_count +=1
    return dup_birthday_count/iteration
    
if __name__ == '__main__':
    num = 23
    iteration = 100
    print ('group size:'+str(num))
    print ('number of iterations:'+str(iteration))
    print ("the probability of having the birthday on the same day is :",birthday_paradox(num,iteration))
                                                                                                                                
