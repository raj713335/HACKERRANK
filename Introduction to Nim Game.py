"""
If there are two players 1,2 and two identical towers player 2 will always win.
ie. any move made by player 1 in tower1 can be made by player2 in tower2 However
if the towers are not equal player 1 will win, he can make thetowers identical.
Mathematically num (xor) num == 0 ? player2win ; player1win

For three towers [6,5,3] I can decompose this as [(4,2),(4,1),(2,1)]
 rearranging [4,4,2,2,1,1] you can see 2 towers of identical height therefore
player2 will win Mathematically 6 (xor) 5 (xor) 3 == 0 ? player2win ;
player1win this concept can be applied for more than 3 numbers

Mathematically 6 (xor) 5 (xor) 3 == 0 ? player2win ; player1win

this concept can be applied for more than 3 numbers
"""

for i in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    x = 0
    for j in l:
        x ^= j
        #print(x)
    print("Second" if x==0 else "First")
