import sys



def climbingLeaderboard(m,n,scores, alice):
    rank=[]
    for i in range(0,m):
        count = 1
        scores.append(alice[i])
        #print(scores)
        scores.sort(reverse=True)
        rank.append(1)
        for j in range(1, len(scores)):
            if (scores[j] == scores[j - 1]):
                rank.append(count)
            else:
                count += 1
                rank.append(count)

        print(rank[(scores.index(alice[i]))])
    return rank






n = int(input().strip())
scores = list(map(int, input().strip().split(' ')))
m = int(input().strip())
alice = list(map(int, input().strip().split(' ')))
result = climbingLeaderboard(m,n,scores, alice)
#print("\n".join(map(str, result)))