t=int(input())  #Number of test cases
while(t>0):
    x=int(input())  # Rank input
    print("YES") if x < 11 else print("NO")   #If Rank is less than 11 then Chef selected else No
    t-=1
