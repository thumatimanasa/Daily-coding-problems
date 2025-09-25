#Date : 23-09-2025
#leetcode problem 2651
#calculated delayed and arrival time

def reach_time(arrival_time,delayed_time):
    time=arrival_time+delayed_time
    return time%24    #modulus operator is used to convert time in 24 hours format
print(reach_time(12,2))
    
