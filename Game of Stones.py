

"""You'll find that the first player will lose when the starting number of stones s is: 1,7,8,14,15,21,22... '
   '(i.e. when s % 7 < 2). With this knowledge in hand the code is trivial:"""

t = int(input())
for _ in range(t):
    s = int(input())
    if s % 7 < 2:
        print("Second")
    else:
        print("First")
