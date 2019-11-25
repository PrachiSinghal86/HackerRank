#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort2 function below.
def insertionSort2(n, arr):
    for i in range(1,n):
        j=i-1
        K=arr[i]
        while j>=0 and arr[j]>K:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=K
        for l in range(n):
            print(arr[l],end=" ")
        print()

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
