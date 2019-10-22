#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the squares function below.
def squares(a, b):
    c=0
    for i in range(a,b+1):
        s=math.sqrt(i)
        s=int(s)
        if s*s==i:
            c=c+1
            break;
    i=s+1
    while i*i<=b:
        c=c+1
        i=i+1
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
