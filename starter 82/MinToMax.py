# cook your dish here
t=int(input())
while(t>0):
    n=int(input())
    a=list(map(int,input().split()))
    mi=min(a)
    a.sort()
    i=0
    for x in a:
        if(x==mi):
            i+=1
        else:
            break
    print(n-i)
    t-=1
