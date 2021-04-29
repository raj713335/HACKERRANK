#!/bin/python3


"""
Same as regular game of Nim!

Some insight: being able to add to the pile makes no
difference to a regular game of nim. If Player A has
a winning position in the game of nim, Player A may keep playing 
optimally as they would play a regular nim game. If, however, Player
B decides to add k items to a pile, putting Player A in a losing position,
Player A may add the same number, k, items to the same pile, reclaiming thier
winning position. Or, even better, Player A may simply remove the items added
by Player B.
"""
import math
import os
import random
import re
import sys

#
# Complete the 'pokerNim' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY c
#

def pokerNim(k, c):
    # Write your code here
    res=0
    for i in c:
        res^=i
    if(res):
        return("First")
    else:
        return("Second")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        c = list(map(int, input().rstrip().split()))

        result = pokerNim(k, c)

        fptr.write(result + '\n')

    fptr.close()
