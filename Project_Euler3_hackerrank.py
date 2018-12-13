
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    sq= int(n**.5)
    x=1
    while n%2 ==0:
        n=n//2
        x=2
    for i in range(3,sq+1,2):
        while n%i ==0:
            n=n//i
            if i>x:
                x=i
    if n>x:
        x=n
    print(x)