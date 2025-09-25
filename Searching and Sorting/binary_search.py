sorted_arr=[10,26,34,45,50,58,67]
target=50
def binary_search(arr,target):
    size=len(sorted_arr)
    start=0
    end=size-1
    while start<=end:
        mid=(start+end)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            start=mid+1
        elif arr[mid]>target:
            end=mid-1
    return -1
result=binary_search(sorted_arr,target)
print(result)
