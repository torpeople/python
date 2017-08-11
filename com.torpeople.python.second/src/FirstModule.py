'''
Created on Aug 9, 2017

@author: hliu
'''
def add(a,b):
    return a+b

def addFixedValue(a):
    y = 5
    return y +a

#comments
xx = add(1, 2)
print (xx)
print (addFixedValue(1))
assert(1==2)