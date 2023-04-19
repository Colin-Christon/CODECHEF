t=int(input())
while(t>0):
    n,m=map(int,input().split())
    print("Yes") if m*36>=n else print("No")
    t-=1
