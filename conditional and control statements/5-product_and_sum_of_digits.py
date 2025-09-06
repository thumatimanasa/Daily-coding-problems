#leetcode problem : 1281
#subtract the product and sum of digits of an integer

number=int(input("enter the number"))
sum=0
product=1
while number>0:
    digit=number%10    #extract last digit
    sum=sum+digit       #add last digit to sum
    product=product*digit   #product the last digit
    number=number//10        #removes last digit
print(f"product :{product}")
print(f"sum:{sum}")
result=product-sum
print(f"product-sum:{result}")