t=int(input())
while(t>0):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    ans=1
    if a==b:
        print("yes")
    elif a.count(1)==0:
        print("no")
    elif a[0]!=b[0] or a[n-1]!=b[n-1] :
        print("NO")
    else:
        for i in range(n):
            if a[i]!=b[i]:
                if a[i]==1 and b[i]==0:
                    ans=0
                    break
        if ans:
            print("yes")
        else:
            print("no")
    t-=1
