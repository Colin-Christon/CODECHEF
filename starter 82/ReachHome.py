t=int(input())
while(t>0):
    x,y=map(int,input().split())
    if(5*x<y):
        print('NO')
    else:
        print("YES")
    t-=1
