#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    for i in range(4):
        res=[(sum(arr[i][j:j+3])+arr[i+1][j+1]+sum(arr[i+2][j:j+3])) for j in range(4)]
    return max(res)
            
    # Write your code here

if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    print(result)