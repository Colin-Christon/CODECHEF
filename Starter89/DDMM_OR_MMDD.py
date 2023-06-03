t=int(input())
while(t>0):
    date=input()
    if(int(date[0:2]) <13 and int(date[3:5])<13):
        print("BOTH")
    elif(int(date[0:2])<13):
        print("MM/DD/YYYY")
    else:
        print("DD/MM/YYYY")
    t-=1
