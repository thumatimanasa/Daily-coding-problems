#filter function is used to filter the specific items based on condition

#example: filter the even numbers from the given set of numbers
numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
def even(num):
    if num%2==0:
        return True
even_numbers=list(filter(even,numbers))
print(even_numbers)

#filter function with lambda function
lst=[1,2,3,4,5,6,7,8,9]
greater_than_five=list(filter(lambda x:x>5,lst))
print(greater_than_five)


#filter with a lambda function and multiple conditions
even_and_greater_than_five=list(filter(lambda x:x>5 and x%2==0,lst))
print(even_and_greater_than_five)


#to the check the person age is greaterthan 25
person=[
    {'name':'manas','age':25},
    {'name':'mani','age':35},
    {'name':'manaswi','age':29}
]
def age_greater_than_25(person):
    return person['age']>25
age=list(filter(age_greater_than_25,person))
print(age)