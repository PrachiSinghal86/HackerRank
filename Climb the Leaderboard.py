#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    n = len(scores)
    m = len(alice)
    d = m - 1
    r = 1
    l = []
    ra = []
    ra.append(1)
    for i in range(1, n):
        if scores[i] == scores[i - 1]:
            ra.append(r)
        else:
            r = r + 1
            ra.append(r)
    i = 0
    while (i < n):
        if d >= 0:
            if alice[d] >= scores[i]:
                l.append(ra[i])

                d = d - 1
            else:
                i = i + 1
        else:
            break
    ls = ra[n - 1] + 1

    for j in range(d + 1):
        l.append(ls)

    l.reverse()
    return l


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
