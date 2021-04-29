"""
1. The ith square has i squares (0 1 2 .... i-1) before it, so for each coin in current
square you actually has i ways to move, so it's like having i stones in a standard nim game.
The coins aren't the stones in the Nim's term. The slots before the current square are.

2. The number of coins in each square is just a flag, if initially some square has even number
of coins, no matter what the first player did, all the changes can be cancel out by putting
all rest of the coins in current square (will be an odd number) to the same set of squares
the first player put onto.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nimbleGame' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY s as parameter.
#

def nimbleGame(s):
    # Write your code here
    x=0
    for i in range(1,len(s)):
        if s[i]%2:
            x^=i
    return "First" if x else "Second"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        s = list(map(int, input().rstrip().split()))

        result = nimbleGame(s)

        fptr.write(result + '\n')

    fptr.close()
