#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    l=len(scores)
    maxs=scores[0]
    mins=scores[0]
    a=[0]*2
    for i in range(1,l):
        if maxs<scores[i]:
            a[0]=a[0]+1
            maxs=scores[i]
        elif mins>scores[i]:
            a[1]=a[1]+1
            mins=scores[i]
    return a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
