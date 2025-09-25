#DATE : 24-09-2025
#leetcode problem 728
#self dividing number
def number(n):
    original=n
    while n>0:
        d=n%10  #extract each digit
        if d==0 or original%d!=0:
            return False
        n=n//10
    return True
def self_dividing_numbers(left, right):
    result = []
    for num in range(left, right + 1):
        if number(num):
            result.append(num)
    return result
print(number(10))
