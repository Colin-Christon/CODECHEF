# cook your dish here
t=int(input())
while(t>0):
    battery_level = int(input()) # Input the initial battery level
    time = 0 # Initialize time to 0 minutes

    while battery_level != 50: # Continue looping until the battery level reaches 50%
        if battery_level < 50: # If battery level is less than 50%
            battery_level += 2 # Increase battery level by 2%
        else: # If battery level is greater than 50%
            battery_level -= 3 # Decrease battery level by 3%
        time += 1 # Increase time by 1 minute
    
    print(time) # Print the minimum time in which Chef can make the battery level reach exactly 50%
    t-=1
