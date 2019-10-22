#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    l=len(s)
    x=int(n/l)
    c=s.count('a')
    c=c*x
    d=n-(x*l)
    p=s[0:d]
    m=p.count('a')
    c=c+m
    return c




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
