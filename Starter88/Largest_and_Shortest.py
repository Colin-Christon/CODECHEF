t=int(input())
while(t>0):
    n=int(input())
    ar=list(map(int,input().split()))       #input list
    arr=list(set(ar))                       #remove duplicate elements 
    arr2=arr.sort()                     #sorting list 
    print(arr[-1]+arr[-2])
    t-=1
