#linear search logic

arr=[23,12,24,6,50,45]
target=50
def linear_search(arr,target):
    size=len(arr)
    for index in range(0,size):
        if arr[index]==target:
            return index
    return -1
result=linear_search(arr,target)
print(result)
