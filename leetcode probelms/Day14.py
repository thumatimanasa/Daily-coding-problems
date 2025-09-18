#leetcode 3492
#maximum containers on a ship

def max_containers(n, w, maxWeight):
    deck_capacity = n * n  
    weight_capacity = maxWeight // w  
    return min(deck_capacity, weight_capacity)

print(max_containers(2, 3, 15))  
print(max_containers(3, 5, 20))  

