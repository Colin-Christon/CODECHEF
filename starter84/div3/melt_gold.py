import math
t=int(input())
while(t>0):
    melt,temp=map(int,input().split())
    x=1
    dif=melt-temp
    if(dif==1):
        print(x)
    else:
        
        n = math.ceil((-1 + math.sqrt(1 + 8*dif)) / 2)
        print(n)
    t-=1
