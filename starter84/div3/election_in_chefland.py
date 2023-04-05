t=int(input())
while(t>0):
    n,x=map(int,input().split())
    li=list(map(int,input().split()))
    li.sort()
    flag=False
    for y in range(n):
        if(li[y]<x):
            continue
        else:
            res=n-y
            flag=True
            break
    if(flag):
        print(res)
    else:
        print(0)
    t-=1
