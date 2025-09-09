#calculate the total cost of items in a shopping cart

def calculate_total_cost(cart):
    total_cost=0
    for item in cart:
        total_cost+=item['price']*item['quantity']
    return total_cost

#example cart 
cart=[
    {'name':'apple','price':0.3,'quantity':3},
    {'name':'banana','price':0.5,'quantity':7},
    {'name':'grapes','price':0.7,'quantity':6},
]

#function calling
total_cost=calculate_total_cost(cart)
print(total_cost)