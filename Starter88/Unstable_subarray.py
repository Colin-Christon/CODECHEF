t=int(input())              #test cases
while(t>0):
    n=int(input())
    arr=list(map(int,input().split()))         #array input
    d={}
    cnt=0
    for x in arr:                               #finding frequency of each element
        if(x in d):
            d[x]+=1
        else:
            d.setdefault(x,0)
            d[x]+=1
    
    for x in d:
        cnt+=(d[x]*(d[x]-1))//2                 #for each frequency find possible pair combination 
    
    num_of_ways=(n*(n-1))//2               #Total pairs 
    print(num_of_ways-cnt)
    t-=1
