#map function with lambda function

numbers=[1,2,3,4,5]
squares=list(map(lambda x:x*x,numbers))
print(squares)



#map multiple iterables
numbers1=[1,2,3]
numbers2=[4,5,6]
addition=list(map(lambda x,y:x+y,numbers1,numbers2))
print(addition)


#using map to convert list strings to integers
str_numbers=['1','2','3']
convert_numbers=list(map(int,str_numbers))
print(convert_numbers)

#using map to covert lowercase to uppercase
fruits=['apple','banana','cherry']
upper_fruits=list(map(str.upper,fruits))
print(upper_fruits)





