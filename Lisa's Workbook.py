#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the workbook function below.
def workbook(n, k, arr):
    pr = 0
    p = 1
    s = 0

    for i in range(n):
        if arr[i] % k == 0:
            no = int(arr[i] / k)
        else:
            no = arr[i] // k
            no = no + 1

        for j in range(0, no):
            if p >= j * k + 1 and p <= (j + 1) * (k):

                if p <= arr[i]:
                    s = s + 1

            p = p + 1
    return s


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
