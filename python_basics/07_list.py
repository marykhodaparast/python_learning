orders = [
    {"price": 200, "quantity": 2},
    {"price": 400, "quantity": 3},
    {"price": 150, "quantity": 2},
    {"price": 600, "quantity": 2}
]

largest_order = 0

for order in orders:
    order_total = order["price"] * order["quantity"]
    if order_total > largest_order:
        largest_order = order_total
        
print("Largest order:", largest_order)        
       