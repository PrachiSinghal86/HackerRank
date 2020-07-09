#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndMinimax function below.


def sherlockAndMinimax(arr, p, q):
    mx=-1
    k=-1
    arr=sorted(arr)
    l=len(arr)-1
    i=0
    ans=-1
    f=-1
    if(p<arr[0]):
        mx=arr[0]-p
        ans=p
        
        f=0
        if(q>arr[0]):
            p=arr[0]
        else:
            return q
    else:
        while(i<l-1):
            if arr[i]==p or (arr[i]<p and arr[i+1]>p):
                f=i
                break
            i+=1
    
    while f<l:
        c=(arr[f+1]+arr[f])//2
        if(c>=p and c<=q):
            tm=min(abs(arr[f+1]-c),abs(arr[f]-c))
            if mx<tm:
                mx=tm
                ans=c
                
        elif c>q:
            tm=abs(arr[f]-q)
            if mx<tm:
                mx=tm
                ans=q
                return q
            break
        
        f+=1;
    if q>arr[l]:
        if mx<q-arr[l]:
            return q

    return ans



            
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    pq = input().split()

    p = int(pq[0])

    q = int(pq[1])

    result = sherlockAndMinimax(arr, p, q)

    fptr.write(str(result) + '\n')

    fptr.close()
