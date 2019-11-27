#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    f=0
    e=0
    if p==1 or p==n:
        return f
    elif p>n-2 and n%2!=0:
        return e
    elif p>n-2 and n%2==0:
        return 1

    elif p<=int(n/2):
        f=int(p/2)
        return f
    else:
        e=n-p
        f=int(e/2)
        return f

    #
    # Write your code here.
    #

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
