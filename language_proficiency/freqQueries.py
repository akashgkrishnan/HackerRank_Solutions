#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
    hashTable = dict()
    for query in queries:
        if query[0] == 1:
            item = query[1]
            if item in hashTable:
                hashTable[item] += 1
            else:
                hashTable[item] = 1
        elif query[0] == 2:
            item = query[1]
            if item in hashTable:
                hashTable[item] -= 1
        else:
            for key, value in hashTable.items():
                if value == query[1]:
                    return key
            return 0



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
