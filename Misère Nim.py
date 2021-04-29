"""
Thought I might share some observations that helped me come up with an algorithm. If anyone sees a mistake in my reasoning, or has an easier way to think through this problem, I'd be happy to hear about it.

tl;dr

If player 1 starts with an xor value of zero, player 1 loses unless the piles are: [1,1], [1,1,1,1], etc.
If player 1 starts with an xor value other than zero, player 1 wins unless the piles are: [1], [1,1,1], etc.
Observations:

1) The last losing position of every game will have exactly one stone and one active pile. 
Ignoring the piles with zero, we can represent the basic losing position like this: [1].

2) There are exactly two ways to put your opponent in this losing position:

You have exactly one remaining pile, and the number of stones > 1 (e.g., [8]), or
You have exactly two remaining piles, one of which has only one stone (e.g., [1,8]).
3) The only "winning position" from (2) that has an xor value of 0 is [1,1].

4) If player 1 starts with an xor value of zero, player 1 loses unless the piles are: [1,1], [1,1,1,1], etc.

5) If player 1 starts with an xor value other than zero, player 1 wins unless the piles are: [1], [1,1,1], etc.

Oberservations (4) and (5) are enough to come up with an algorithm. You can see my solution here. But why do (4) and (5) hold?

I'll ignore the cases where each pile has one stone, since those cases are easy.

Let's suppose player p has an xor value of zero.

a) Every time p makes a move, their opponent can counter to put them back into an xor position of zero.

b) The opponent will never put p in [1,1], [1,1,1,1], etc., because that would require the opponent to pass up a winning position 
(such as [1,8], [1,1,1,8],etc.)

c) So these two things together mean that the opponent will never put p in a winning position, which establishes (4).

Now let's suppose player p has an xor value other than zero.

d) As long as at least one pile has more than 1 stone, p can give their opponent an xor value of 0, which establishes (5).
"""

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
