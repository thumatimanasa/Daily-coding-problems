#leetcode problem :412
#write a program for fizzbuzz

n=int(input("enter number"))
def fizzbuzz(n):
    for i in range(1,n+1):
        if i%3==0 and i%5==0:
            print("FizzBuzz")
        elif i%3==0:
            print("fizz")
        elif i%5==0:
            print("buzz")
        else:
            print(i)
    return 1
fizzbuzz(n)
