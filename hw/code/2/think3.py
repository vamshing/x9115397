
# coding: utf-8

# # Code 2
# Guduguntla Vamshi | 
# Sattwik Pati 

# # 3.1

# In[ ]:

repeat_lyrics()

def print_lyrics():
        print "I am sexy, and I know it!"
        print " Like a like a laila!"
        
def repeat_lyrics():
        print_lyrics()
        print_lyrics()

"""
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-1-3336ea505857> in <module>()
----> 1 repeat_lyrics()
      2 
      3 def print_lyrics():
      4         print "I am sexy, and I know it!"
      5         print " Like a like a laila!"

NameError: name 'repeat_lyrics' is not defined
# # 3.2
"""
# In[ ]:

def repeat_lyrics():
        print_lyrics()
        print_lyrics()
        
def print_lyrics():
        print "I am sexy, and I know it!"
        print " Like a like a laila!"
        
repeat_lyrics()
"""
I am sexy, and I know it!
 Like a like a laila!
I am sexy, and I know it!
 Like a like a laila!
 """
# # 3.3

# In[ ]:

def right_justify(s):
    print ' '*(70-len(s)),s
right_justify('allen')
"""

                                                                    allen"""
# # 3.4

# In[ ]:

def do_twice(f):
        f()
        f()

def print_spam():
        print 'spam'
        
do_twice(print_spam)

"""
spam
spam
"""
# In[ ]:

def do_twice(f,x):
        f(x)
        f(x)

def print_spam(x):
        print x
        
do_twice(print_spam,'spam')

"""
spam
spam
"""
# In[ ]:

def print_twice(x):
    print x
    print x
print_spam('spam ')

"""
spam 
spam """
# In[ ]:

def do_twice(f,x):
        print_twice(x)
        print_twice(x)
do_twice(print_spam,'spam')

"""
spam
spam
spam
spam
"""
# In[ ]:

def do_four(f,x):
    do_twice (f,x)
    do_twice (f,x)


# # 3.5

# In[ ]:

def print_once(x,y):
    print x*1,y*4,x*1,y*4,x*1

def print_four_times(x,y):
    print x*1,y*4,x*1,y*4,x*1
    print x*1,y*4,x*1,y*4,x*1
    print x*1,y*4,x*1,y*4,x*1
    print x*1,y*4,x*1,y*4,x*1
    
def print_grid():
    print_once('+','-')
    print_four_times('/',' ')
    print_once('+','-')
    print_four_times('/',' ')
    print_once('+','-')
    
print_grid()
"""
+ ---- + ---- +
/      /      /
/      /      /
/      /      /
/      /      /
+ ---- + ---- +
/      /      /
/      /      /
/      /      /
/      /      /
+ ---- + ---- +
"""
# In[ ]:

def print_once(x,y):
    print x*1,y*4,x*1,y*4,x*1,y*4,x*1,y*4,x*1

def print_four_times(x,y):
    print x*1,y*4,x*1,y*4,x*1,y*4,x*1,y*4,x*1
    print x*1,y*4,x*1,y*4,x*1,y*4,x*1,y*4,x*1
    print x*1,y*4,x*1,y*4,x*1,y*4,x*1,y*4,x*1
    print x*1,y*4,x*1,y*4,x*1,y*4,x*1,y*4,x*1
    
def print_grid():
    print_once('+','-')
    print_four_times('/',' ')
    print_once('+','-')
    print_four_times('/',' ')
    print_once('+','-')
    print_four_times('/',' ')
    print_once('+','-')
    print_four_times('/',' ')
    print_once('+','-')
    
print_grid()
"""
+ ---- + ---- + ---- + ---- +
/      /      /      /      /
/      /      /      /      /
/      /      /      /      /
/      /      /      /      /
+ ---- + ---- + ---- + ---- +
/      /      /      /      /
/      /      /      /      /
/      /      /      /      /
/      /      /      /      /
+ ---- + ---- + ---- + ---- +
/      /      /      /      /
/      /      /      /      /
/      /      /      /      /
/      /      /      /      /
+ ---- + ---- + ---- + ---- +
/      /      /      /      /
/      /      /      /      /
/      /      /      /      /
/      /      /      /      /
+ ---- + ---- + ---- + ---- +
"""



# # 4.2 - Turtle Flowers

# In[ ]:

import math
from swampy.TurtleWorld import *

def polyline(t, n, length, angle):
    """Draws n line segments.
    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        fd(t, length)
        lt(t, angle)


def arc(t, r, angle):
    """Draws an arc - This module contains code from Think Python by Allen B. Downey
    t: Turtle
    r: radius of arc
    angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    lt(t, step_angle/2)
    polyline(t, n, step_length, step_angle)
    rt(t, step_angle/2)

    
def petal(t,r,angle):
    for i in range(2):
        arc(t,r,angle)
        lt(t,180-angle)
        
def flower(t,r,n,angle):
    for i in range(n):
        petal(t,r,angle)
        lt(t,360.0/n)
    
def penupmove(t,length):
    pu(t)
    fd(t,length)
    pd(t)

if __name__ == '__main__':
    world = TurtleWorld()    

    bob = Turtle()
    bob.delay = 0.001
    flower(bob,100,7,60)
    penupmove(bob,200)
    
    flower(bob,100,10,60)
    penupmove(bob,200)
    
    flower(bob,250,20,18)
    penupmove(bob,200)
  
    wait_for_user()


# # 4.3 Turtle Pies

# In[ ]:

import math
from swampy.TurtleWorld import *
"""
Assuming that the vertices of the polygon fall on the circle,
there by subtending equal angles at the centre of the circle
"""
def triangles(t,n,r,angle):
    length = 2* r * math.sin(angle * 0.5 * math.pi / 180)
    for i in range(n):
        lt(t,(angle*.5))
        fd(t, r)
        lt(t, 90+(angle*.5))
        fd(t, length)
        lt(t, 90+(angle*.5))
        fd(t, r)
        lt(t, 180-(angle*.5))

def penupmove(t,length):
    pu(t)
    fd(t,length)
    pd(t)
    
def generator(t,n,r):
    angle = 360.0/n
    triangles(bob,n,100,angle)
    penupmove(t,r+100)   

if __name__ == '__main__':
    world = TurtleWorld()    
    bob = Turtle()
    bob.delay = 0.001
    
    #5-gon
    generator(bob,5,100)
    #6-gon
    generator(bob,6,100)
    #7-gon
    generator(bob,7,100)
    
    wait_for_user()


# In[ ]:


