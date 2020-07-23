#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(string):

    if not string:
        return


    slowIdx = 0
    fastIdx = 1
    deleteCount = 0
    while fastIdx < len(string):
        if string[slowIdx] == string[fastIdx]:
            deleteCount += 1
            fastIdx += 1
            continue
        slowIdx = fastIdx
        fastIdx += 1
    return deleteCount

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
