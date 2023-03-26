# cook your dish here
t=int(input())
while(t>0):
    x,y=map(int,input().split())
    if((x<9)and (x*y<501)):
        print("YES")
    else:
        print("NO")
    t-=1
