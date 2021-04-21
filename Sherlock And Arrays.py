
for i in range(0, int(input())):
    x = input()
    flag=False
    arr = list(map(int, input().rstrip().split(" ")))
    if (len(arr) == 1):
        print("YES")
        continue

    left=sum(arr)
    right=0
    for j in range(0,len(arr)):   
        left-=arr[j]
        if (left==right):
            flag=True
            print("YES")
            break
        
        right+=arr[j]
    if(flag==False):
        print("NO")
        

