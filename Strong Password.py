#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumNumber function below.
def minimumNumber(n, password):
    s = 0
    c = 0
    no = 0
    sp = 0
    for i in range(n):
        if ord(password[i]) >= 65 and ord(password[i]) <= 90:
            c = 1
        elif ord(password[i]) >= 97 and ord(password[i]) <= 122:
            s = 1
        elif ord(password[i]) >= 48 and ord(password[i]) <= 57:
            no = 1
        else:
            sp = 1
        if c == 1 and sp == 1 and s == 1 and no == 1:
            break

            return x
    d = 4 - sp - c - s - no
    if n < 6:
        x = 6 - n
        if x >= d:
            return x
    return d

    # Return the minimum number of characters to make the password strong


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
