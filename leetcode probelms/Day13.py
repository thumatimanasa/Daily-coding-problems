x=int(input('enter value'))
y=int(input('enter value'))
z=int(input('enter value'))
value1=abs(z-x)
value2=abs(y-z)
if value1<value2:
    print(True)
else:
    print(False)