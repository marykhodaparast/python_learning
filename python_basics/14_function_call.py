orders = [
    {"price": 200, "quantity": 2},
    {"price": 400, "quantity": 3},
    {"price": 150, "quantity": 2},
    {"price": 600, "quantity": 2}
]

total_price = 0;
avg_price = 0

for order in orders:
    order_total = order["price"] * order["quantity"]
    total_price += order_total
        
print("Avg price is:", total_price / 4)        
       