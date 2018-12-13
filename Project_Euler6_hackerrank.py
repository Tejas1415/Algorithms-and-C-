import sys

def ans(n):
    val=(((n**4)-(n**2))/4) +((n**3)-n)/6
    return val

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    result=ans(n)
    print(int(result))