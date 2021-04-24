#!/bin/python3

arr =[]

def take_zeroth(elem):
    return elem[0]

for i in range(0,int(input())):
    a, b = map(int,input().split(" "))
    arr.append([a+b, i])

    
arr = sorted(arr, key=take_zeroth)

for each in arr:
    print(each[1]+1, end=" ")
    
