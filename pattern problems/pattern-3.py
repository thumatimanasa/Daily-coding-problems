'''
pattern 3
* * * * *
* * * *
* * *
* *
*
'''

n=int(input("enter value"))
for row in range(1,n+1):
    for col in range(1,n-row+1):
        print("*",end=' ')
    print()


n=int(input("enter value"))
for row in range(1,n+1):
    for col in range(1,n-row+1):
        print(col,end=' ')
    print()

