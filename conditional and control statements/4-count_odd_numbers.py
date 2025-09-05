#leetcoode problem-1523
#count odd numbers in the interval range
low=int(input("enter number"))
high=int(input("enter number"))
range=(high-low+1)//2 #count total numbers in the range and half them
if low%2!=0 and high%2!=0:  #both high and low are odd
    print(range+1)
else:
    print(range)