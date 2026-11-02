orders = [
    {"price": 200, "quantity": 2},
    {"price": 400, "quantity": 3},
    {"price": 150, "quantity": 2},
    {"price": 600, "quantity": 2}
]

small_count = 0
medium_count = 0
large_count = 0

for order in orders:
    order_total = order["price"] * order["quantity"]
    if order_total  < 500:
        small_count += 1
    elif order_total >=500 and order_total < 999:
        medium_count += 1
    elif order_total >= 1000:
        large_count += 1
        
print("Small count is:", small_count)
print("Medium count is:", medium_count)
print("Large count is:", large_count)            
      
       