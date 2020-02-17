#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pangrams function below.
def pangrams(s):
    f=0
    for i in range(26):
        if s.count(chr(97+i))==0 and s.count(chr(65+i))==0:
            print(chr(97+i))
            f=1
            break
    if f==1:
        return "not pangram"
    else:
        return "pangram"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
