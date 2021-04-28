"""
The whole point being that each player would like to make the height 1 of whatever tower it chooses,
because 1 evenly divides all other numbers. So the answer only depends on number of towers being odd or even,
except for the case when starting height of towers is 1, in that case 1 always loses because it can't make any moves.
"""


for _ in range(int(input())):
    number_tower, tower_length = map(int, input().split(" "))
    
    if tower_length == 1:
        print(2)
    else:
        if number_tower % 2 == 0:
            print(2)
        else:
            print(1)
