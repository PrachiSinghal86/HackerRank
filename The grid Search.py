#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the gridSearch function below.
def gridSearch(G, P):
    x1 = len(G)
    y1 = len(G[0])
    x2 = len(P)
    y2 = len(P[0])
    for i in range(x1):
        for j in range(y1):
            if G[i][j] == P[0][0]:
                r = i
                c = j
                l = 0
                for p in range(x2):
                    if i + x2 > x1 or j + y2 > y1 or P[p] != G[r + p][c:c + y2]:
                        l = 1

                        break
                if l == 0:
                    return 'YES'

    return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        RC = input().split()

        R = int(RC[0])

        C = int(RC[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        rc = input().split()

        r = int(rc[0])

        c = int(rc[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        fptr.write(result + '\n')

    fptr.close()
