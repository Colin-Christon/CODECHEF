t=int(input())    #test cases
while(t>0):
    online, offline = map(int, input().split())
    
    if(online*0.9 == offline):   #if both price are same after 10% discount on online food
        print("EITHER")
    elif(online*0.9 < offline):   #if online price less than offline 
        print("ONLINE")
    else:
        print("DINING")             
    t-=1
