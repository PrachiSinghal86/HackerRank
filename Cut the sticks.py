#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    l=len(arr)
    w=[]
    while(len(arr)>0):
        w.append(len(arr))
        m=min(arr)
        for j in range(len(arr)):
            arr[j]=arr[j]-m
        while(arr.count(0)):
            arr.remove(0)
    return w



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
