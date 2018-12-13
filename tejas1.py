import sys


def climbingLeaderboard(scores, alice):
    def ranking(alice_score):
        count = 1
        scores.append(alice_score)
        scores = scores.sort(reverse=True)
        for i in range(1, len(scores)):
            rank = list()
            rank.append(count)
            if scores[i] == scores[i - 1]:
                rank.append(count)
            else:
                count += 1
                rank.append(count)
        ind = scores.index(alice_score)
        new_rank = rank[ind]
        return new_rank

    for alice_score in alice:
        result1 = ranking(alice_score)
        return result1
        # result


if __name__ == "__main__":
    n = int(input().strip())
    scores = list(map(int, input().strip().split(' ')))
    m = int(input().strip())
    alice = list(map(int, input().strip().split(' ')))
    result = climbingLeaderboard(scores, alice)
    print("\n".join(map(str, result)))
