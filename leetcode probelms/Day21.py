#DATE: 25-09-25
# leetcode problem 628 
# maximum product of three numbers     


def max_number(lst):
      lst.sort()      #sort()  method is used to sort the elements in ascending order
      max1=lst[-1]* lst[-2]*lst[-3]   #it is used when elements are positive numbers
      max2=lst[0]*lst[1]*lst[-1]    #it is used when elements are both negitive and positive numbers
      return max(max1,max2)
result=max_number([1,2,3,4])  #function calling
#result=max_number([-100,-98,-1,2,3,4])
print(result)

    