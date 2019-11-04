#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    l=len(word)
    x=ord(word[0])-97
    max=h[x]
    for j in range(1,l):
        x=ord(word[j])-97
        if h[x]>max:
            max=h[x]
    return max*l


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
