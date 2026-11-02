orders = [
    {"price": 200, "quantity": 2},
    {"price": 400, "quantity": 3},
    {"price": 150, "quantity": 2},
    {"price": 600, "quantity": 2}
]

lowest_order = orders[0]["price"] * orders[0]["quantity"]

for order in orders:
    order_total = order["price"] * order["quantity"]
    if order_total < lowest_order:
        lowest_order = order_total
        
print("Lowest order:", lowest_order)        
       