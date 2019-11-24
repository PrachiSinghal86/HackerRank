#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the quickSort function below.
def quickSort(arr):
    p = arr[0]
    n = len(arr)
    i = 0

    for k in range(1, n):
        if arr[k] <= p:
            i = i + 1
            t = arr[k]
            arr[k] = arr[i]
            arr[i] = t
    t = arr[0]
    arr[0] = arr[i]
    arr[i] = t
    return arr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
