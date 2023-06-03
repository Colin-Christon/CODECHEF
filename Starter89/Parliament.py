t=int(input())
while(t>0):
    n,x=map(int,input().split())
    if(x*2 <n):
        print("NO")
    else:
        print("YES")
    t-=1
