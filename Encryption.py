#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the encryption function below.
def encryption(s):
    l = len(s)
    x = math.sqrt(l)
    c = math.ceil(x)
    f = math.floor(x)
    if c * f >= l:
        r = f;
    else:
        r = c;
    i = 0
    j = 0
    st = ""
    while (i < c):
        while (j < r):
            if (j * c + i) < l:
                st = st + s[j * c + i]

            j = j + 1
        st = st + " "
        j = 0

        i = i + 1
    return st


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
