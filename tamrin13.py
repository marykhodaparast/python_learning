orders = [
    {"price": 200, "quantity": 2},
    {"price": 400, "quantity": 3},
    {"price": 150, "quantity": 2},
    {"price": 600, "quantity": 2}
]

total_price = 0

for order in orders:
    order_total = order["price"] * order["quantity"]
    if order_total  > 2000:
        order_total = 0.8 * order_total
    elif order_total > 1000:
        order_total = 0.9 * order_total
            
    
    total_price += order_total
    
    
print("Total price after discount is:", total_price)    

       