#leetcode problem 9
#check weather given number is palindrome or not
num=int(input("Enter number"))
rev=0
while num>0:
    digit=num%10 
    rev=rev*10+digit
    num=num//10
print(rev)
if num==rev:
    print("Given number is palindrome")
else:
    print("Given number is not palindrome")