#!usr/bin /dev/python
import random as rn
import numpy as np

t=100
tf=0
f=0
val = [(0,0),(5,6),(6,3),(9,0),(8,0),(14,3),(9,7),(3,7),(12,7),(0,0)]
while t>tf:
    
    for i in range(0,10):
        print(f)
        f +=1
    t-=1    
#a= rn.randint
a=np.random.randint(low=0, high=5, size=10).tolist()
#print(rn.sample(range(1, 5), 10))
#a = rn.sample(range(1,(len(val)-3)), 1000)
print (a)