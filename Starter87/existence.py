t=int(input())
while(t>0):
    x,y=map(int,input().split(" "))
    if ((x**2) - 2*y)**2 == 0:
        print("Yes")
    else:
        print("No")
    t-=1
