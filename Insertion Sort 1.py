#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    c=n
    m=arr[n-1]
    n=n-2
    while n>=0 and arr[n]>m:
        arr[n+1]=arr[n]
        n=n-1
        for i in range(c):
            print(arr[i],end=" ")
        print()
    arr[n+1]=m
    for i in range(c):
        print(arr[i],end=" ")


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
