"""pattern 2
* * * *
* * * *
* * * *
* * * *
""" 
n=int(input("enter value"))
for row in range(1,n+1):
    for col in range(1,n+1):
        print("*",end=' ')
    print()

"""
pattern 2
1 2 3 4
1 2 3 4
1 2 3 4
1 2 3 4
"""
n=int(input("enter value"))
for row in range(1,n+1):
    for col in range(1,n+1):
        print(col,end=' ')
    print()