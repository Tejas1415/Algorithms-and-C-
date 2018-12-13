import sys
from itertools import permutations
import math


n=int(input())
a=list(range(2,n+1))
perm=permutations(a,2)

s=set()
for i in list(perm):
    s.add(int(math.pow(list(i)[0],list(i)[1])))
for i in a:
    s.add(i**i)
print(len(s))
