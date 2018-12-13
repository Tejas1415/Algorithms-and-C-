import sys

def Products(n):
    product=1
    for i in n:
        product = product * int(i)
    return product

def p(n,k):
    s=list()
    for i in range(n-k+1):
        a=num[i:i+k]
        prod=Products(a)
        s.append(prod)
    return max(s)

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    result=p(n,k)
    print(result)




