#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulBinaryString function below.
def beautifulBinaryString(b):
    l=len(b)
    i=0
    c=0
    while(i<l-2):
        if b[i:i+3]=="010":
            
            d=b[:i+2]+"1"
            if (i+2)<l-1:
                b=d+b[i+3:]
            
            i=i+3
            c+=1
        else:
            i=i+1
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    b = input()

    result = beautifulBinaryString(b)

    fptr.write(str(result) + '\n')

    fptr.close()
