#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the almostSorted function below.
def almostSorted(arr):
    l = len(arr)
    g = 0
    d = []
    lm = []
    i = 0
    e = -1
    while i < l:
        d.append(arr[i])
        i = i + 1
    d.sort()
    i = 0
    while i < l:
        if arr[i] != d[i] and g == 2:
            print('no')
            return
        if arr[i] != d[i] and g == 0:
            g = g + 1
            lm.append(i + 1)
            i = i + 1
            while i < l and arr[i] != d[i]:
                if arr[i] <= arr[i - 1]:
                    g = 2
                    lm.append(i + 1)
                    i = i + 1
                elif g == 2:
                    print('no')
                    return
        elif arr[i] != d[i] and g == 1:
            lm.append(i + 1)
            g = 2
            i = i + 1
        else:
            i = i + 1
    if len(lm) == 2:
        print("yes")
        print("swap", end=" ")
        print(lm[0], end=" ")
        print(lm[1])
    else:
        print("yes")
        print("reverse", end=" ")
        print(lm[0], end=" ")
        print(lm[len(lm) - 1])


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
