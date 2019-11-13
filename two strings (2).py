#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
def marsExploration(s):
    l=len(s)
    i=0
    c=0
    while(i<l):
        if s[i]!='S':
            c=c+1
        i=i+1
        if s[i]!='O':
            c=c+1
        i=i+1
        if s[i]!='S':
            c=c+1
        i=i+1
    return c
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
