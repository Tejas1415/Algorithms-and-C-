import sys
from itertools import combinations

def added(arr,m):
    perm = combinations(arr,m)
    ans = list()
    for i in perm:
        sums= sum(list(i))
        print('sums are',sums)
        ans.append(sums)

    print('show',ans)

    #for x in ans:
    ans=[x for x in ans if ans.count(x)<=1 ]
    print('after removal duplication',ans)

    all_sums=0
    all_sums=sum(ans)
    return all_sums

n,m = input().strip().split(' ')
n,m = [int(n), int(m)]
arr=list(map(int,input().strip().split(' ')))
result= added(arr,m)
print(result)

