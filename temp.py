# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sys
print(sys.platform)
print(2**100)
x='Spam!'
print(x*8)

# %%
123+222
1.5*4
2**100
len(str(2**1000000))
#%%
import math
print(math.pi)
print(math.sqrt(85))
#%%
import random
print(random.random())
random.choice([1,2,3,4])
#%%
a='Hello'
num=10
type(a)
type(num)
#%%
S = 'Spam'
len(S)
print(S[0])
S[-1]
S[0:3]
S[1:]
S
S[:3]
S[:-1]
S[:]
#%%
"""
Strings are immutable. But you can change it in a
different way """

S = 'shrubbery'
L = list(S)
print(L)
L[0] = 'c'
print("".join(L))

#%%
""" String Op """

s="Hello"
print(s.find('ll'))
s.replace('ll', 'oo')
#%%
line='aaa,bbb,cccc'
line.split(',')

line.upper()
s="Hey"
s.isalpha()
#%%
line1 = 'hfs,dsf,sdgf\n'
line1.rstrip()
line1.rstrip().split(',')
#%%

"""Formatting"""
'%s, eggs, and %s' % ('spam1', 'SPAM!')          

'{0}, eggs, and {1}'.format('spam2', 'SPAM!')    

'{}, eggs, and {}'.format('spam3', 'SPAM!')      
