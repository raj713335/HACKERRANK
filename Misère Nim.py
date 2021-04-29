#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce 

#
# Complete the 'misereNim' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY s as parameter.
#

def misereNim(s):
    # Write your code here
    if (set(s)=={1}) and n%2==1:
        return "Second"
    elif (set(s)=={1} and n%2==0):
        return "First"
    elif reduce((lambda x,y:x^y), s):
        return "First"
    else:
        return "Second"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        s = list(map(int, input().rstrip().split()))

        result = misereNim(s)

        fptr.write(result + '\n')

    fptr.close()

    
"""
The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along.This function is defined in “functools” module.

Working : 

At first step, first two elements of sequence are picked and the result is obtained.
Next step is to apply the same function to the previously attained result and the number just succeeding the second element and the result is again stored.
This process continues till no more elements are left in the container.
The final returned result is returned and printed on console.

"""


"""
https://en.wikipedia.org/wiki/Nim
"""
