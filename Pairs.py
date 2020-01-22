#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k, arr):
    l=len(arr)
    arr.sort()
    c=0
    for i in range(l-1):
        j=i+1
        while j<l:
            if arr[j]-arr[i]==k:
                c=c+1
                break
            if arr[j]-arr[i]>k:
                break
            j=j+1
    return c


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
