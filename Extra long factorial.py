#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    d=1
    for i in range(2,n+1):
        d=d*i
    print(d)

if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)
