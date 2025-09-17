#leetcode problem 3622
#topic : math
#check divisibility by digit sum and product
def divisibility(n):
    original=n
    sum=0
    product=1
    while n>0:
        digit=n%10
        sum=sum+digit
        product=product*digit
        n=n//10
    addition=sum+product
    if original%addition==0:
        return True
    else:
        return False

print(divisibility(23))

