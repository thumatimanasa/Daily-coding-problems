#leetcode problem 231
#power of two
# (without using loops) by binary bits
n=int(input("enter number"))
if (n&n-1)==0:
    print(f"Number {n} is power of 2")
else:
    print(f"Number {n} is not a power of 2 ")

