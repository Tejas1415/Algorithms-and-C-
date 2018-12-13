import sys

def digits1(n):
    sums=0
    for i in n:
        sums = sums + int(i)
    return sums


def p(n):
    x= 2**int(n)
    d=digits1(str(x))
    #ans=digits1(str(d))
    return d

t = int(input().strip())
for a0 in range(t):
    n = input().strip()

    result=p(n)
    print(result)
