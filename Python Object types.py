# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 11:19:18 2024

@author: anusha
"""
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

#%%
B= bytearray(b'spam')
B.extend(b'eggs')
print(B)
print(B.decode())
#%%
""" Type Specific operation """
S='Spam'
S.find('pa')
print(S)
print(S.replace('pa', 'XYZ'))
print(S)
dir(S)
help(S.replace)
#%%
S = 'A\nB\tC'
print(len(S))

print(ord('\n'))""" \n is a byte with the binary value 10 in ASCII """
 #%%
"""Pattern Matching """
import re
match = re.match('Hello[ \t]*(.*)world', 'Hello         Python world')
print(match.group(1))

#%%
"""Lists - are mutable"""
l = [123, 'spam', 1.23]
len(l)
print(l*2)
l.append('NI')
print(l)
l.pop(0)
print(l)
#%%
m=['bb','aa','cc']
m.sort()
print(m)
m.reverse()
print(m)
#%%
 M = [[1, 2, 3],               
[4, 5, 6],               
[7, 8, 9]]
 print(M[1])
 
#List Comprehensions
# Collect the items in column 2
col2 = [row[1] for row in M]  
print(col2)

#Add 1 to each item in column 2
print( [row[1] + 1 for row in M] )

#Collect a diagonal from matrix
print( [M[i][i] for i in [0, 1, 2]] )

#Repeat characters in a string
print([c * 2 for c in 'spam'])
#%%
list(range(4))
list(range(-6,7,2))

[[x ** 2, x ** 3] for x in range(4)]  
[[x, x / 2, x * 2] for x in range(-6, 7, 2) if x > 0]
#%%
#Generators
M = [[1, 2, 3],               
[4, 5, 6],               
[7, 8, 9]]

G= (sum(row) for row in M)
print(next(G))
print(next(G))
print(next(G))

#%%
#Maps doing same as above
M = [[1, 2, 3],               
[4, 5, 6],               
[7, 8, 9]]
list(map(sum,M))

#%% 
#Create a set of row sums
M = [[1, 2, 3],               
[4, 5, 6],               
[7, 8, 9]]
{sum(row) for row in M}

#Create key value table of row sums
{i : sum(M[i]) for i in range(3)} 

# List of character ordinals
[ord(x) for x in 'spaam']    

#Sets remove duplicates
{ord(x) for x in 'spaam'} 

# Dictionary keys are unique
{x: ord(x) for x in 'spaam'} 

# Generator of values
(ord(x) for x in 'spaam')  

#%%
#Arbitary Nesting
s=[[1,2,3],
   [4,5,6],
   [7,8,9]]
print(s)
#%%
#Dictionaries

d= {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
print(d['food'])
print(d['quantity']+1)

#Create keys by assignment
D={}
D['name']='Bob'
print(D)

#%%
""" As we’ll learn later, we can also make dictionaries by passing to the dict type name 
either keyword arguments (a special name=value syntax in function calls), or the result
 of zipping together sequences of keys and values obtained at runtime (e.g., from files).
 """
bob1= dict(name='Bob', job='dev', age=40)
print(bob1)

bob2 = dict(zip(['name','job','age'], ['Bob','dev',40]))
print(bob2)

#%%

#Nested
rec = {'name': {'first': 'Bob', 'last': 'Smith'},
 'jobs': ['dev', 'mgr'],
 'age':  40.5}

print(rec['name'])
print(rec['name']['last'])

print(rec['jobs'])
rec['jobs'].append('janitor')
print(rec['jobs'])
print(rec['jobs'][-1])














































