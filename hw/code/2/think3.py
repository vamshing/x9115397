
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



print 'helo'