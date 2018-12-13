import random

x=random.randrange(3,6)    #checking how randrange works. Not belonging to this program.
print(x)

import sys


def kangaroo(x1, v1, x2, v2):
    # Complete this function
    while x1 != x2:             # check if they meet. manually adding their velocity
        x1 += v1
        x2 += v2

        if x1 > 1000000 or x2 > 1000000:      #Limits can be applied if necessery, or provided in the program
           return 'NO'          # will the kangaroos meet before 10000 feet?
           break
        continue
    else:
        return 'Yes'


x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)
