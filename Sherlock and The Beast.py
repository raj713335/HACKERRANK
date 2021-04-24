for i in range(0, int(input())):
    digits = int(input())
    flag = False
    a, b = 0, 0
    for j in range(int(digits//3), -1 , -1):
        if ( digits-(3*j))%5==0:
            a=j
            b=(digits-(3*j))//5
            print((("5"*(a*3))+("3"*(b*5))))
            flag=True
            break
            
    if not flag:
        print(-1)
   
