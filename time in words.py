#!/bin/python3

import math
import os
import random
import re
import sys


def dtw(i):
    switcher = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        21: "twenty one",
        22: "twenty two",
        23: "twenty three",
        24: "twenty four",
        25: "twenty five",
        26: "twenty six",
        27: "twenty seven",
        28: "twenty eight",
        29: "twenty nine",

    }
    return switcher.get(i)


# Complete the timeInWords function below.
def timeInWords(h, m):
    s = dtw(h)
    if m == 00:

        return s + " o' clock"
    elif m == 15:
        return "quarter past " + s
    elif m == 45:
        s = dtw(h + 1)
        return "quarter to " + s
    elif m == 30:
        return "half past " + s
    else:
        if m < 30:
            d = dtw(m)
            if m == 1:
                return d + " minute past " + s
            else:

                return d + " minutes past " + s
        else:
            d = dtw(60 - m)
            s = dtw(h + 1)
            return d + " minutes to " + s


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
