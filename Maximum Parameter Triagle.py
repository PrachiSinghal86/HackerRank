#!/bin/python3

import math
import os
import random
import re
import sys
import array


# Complete the maximumPerimeterTriangle function below.
def maximumPerimeterTriangle(sticks):
    l = len(sticks)
    sticks.sort()
    ans = [-1] * 3
    s = [-1] * 1
    maxp = 0
    for i in range(l - 2):
        if sticks[i] + sticks[i + 1] > sticks[i + 2]:
            if maxp <= sticks[i] + sticks[i + 1] + sticks[i + 2]:
                maxp = sticks[i] + sticks[i + 1] + sticks[i + 2]
                ans[0] = sticks[i]
                ans[1] = sticks[i + 1]
                ans[2] = sticks[i + 2]
    if ans[0] == -1:
        return s
    else:
        return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
