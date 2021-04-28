"""
I drowed a table 15x15 starting from 0,0 to 14,14. It represents what player1 does. It looks like this :

W -> win ; L -> lose

"LLWWLLWWLLWWLLW",
"LLWWLLWWLLWWLLW",
"WWWWWWWWWWWWWWW",
"WWWWWWWWWWWWWWW",
"LLWWLLWWLLWWLLW",
"LLWWLLWWLLWWLLW",
"WWWWWWWWWWWWWWW",
"WWWWWWWWWWWWWWW",
"LLWWLLWWLLWWLLW",
"LLWWLLWWLLWWLLW",
"WWWWWWWWWWWWWWW",
"WWWWWWWWWWWWWWW",
"LLWWLLWWLLWWLLW",
"LLWWLLWWLLWWLLW",
"WWWWWWWWWWWWWWW", ;

you should drow it by walking on its diagonals like that : 0,0 -> 0,1 -> 1,0 -> 0,2 -> 1,1 -> 2,0 -> ... till end.
"""


for _ in range(0, int(input())):
    x, y = map(int, input().split(" "))

    x = x % 4
    y = y % 4
    if (y == 0) or (y == 3) or (x == 0) or (x == 3):
        print("First")
    else:
        print("Second")

    # x1, y1 = x, y
    # x2, y2 = x, y
    # x3, y3 = x, y
    # x4, y4 = x, y
    # flag = True
    #
    # turn = 0
    #
    # while flag:
    #     count = 0
    #     # print(count)
    #     if ((x1 - 2) >= 1) and ((x1 - 2) <= 15) and (((y1 + 1) >= 1) and ((y1 + 1) <= 15)):
    #         x1, y1 = x1 - 2, y1 + 1
    #         print(x1, y1, turn, 1)
    #         count += 1
    #     if ((x2 - 2) >= 1) and ((x2 - 2) <= 15) and (((y2 - 1) >= 1) and ((y2 - 1) <= 15)):
    #         x2, y2 = x2 - 2, y2 - 1
    #         print(x2, y2, turn, 2)
    #         count += 1
    #     if ((x3 + 1) >= 1) and ((x3 + 1) <= 15) and (((y3 - 2) >= 1) and ((y3 - 2) <= 15)):
    #         x3, y3 = x3 + 1, y3 - 2
    #         print(x3, y3, turn, 3)
    #         count += 1
    #     if ((x4 - 1) >= 1) and ((x4 - 1) <= 15) and (((y4 - 2) >= 1) and ((y4 - 2) <= 15)):
    #         x4, y4 = x4 - 1, y4 - 2
    #         print(x4, y4, turn, 4)
    #         count += 1
    #
    #     if count == 0:
    #         flag = False
    #     else:
    #         turn += 1
    #
    # if turn % 2 == 0:
    #     print("Second")
    # else:
    #     print("First")








