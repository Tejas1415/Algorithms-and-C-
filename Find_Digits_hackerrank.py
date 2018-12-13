# hacker_rank_Problem
import sys


def findDigits(n):
    count = 0
    Convert1 = list(str(n))
    for i in range(0, len(Convert1)):       # avoid unnecessery extracting each digit, then subtract etc. Directly convert to string.
        if int(Convert1[i]) > 0:
            rem = n % int(Convert1[i])
            if rem == 0:
                count += 1
    return count


if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        result = findDigits(n)
        print(result)