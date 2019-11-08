#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    l=len(queries)
    a=[0]*(n+2)
    for m in range(l):
        i=queries[m][0]
        j=queries[m][1]
        k=queries[m][2]
        a[i]=a[i]+k
        a[j+1]=a[j+1]-k
    p=0
    q=0
    for m in range(1,n+1):
        p=p+a[m]
        q=max(p,q)
    return q





if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
