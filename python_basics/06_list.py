orders = [
    {"price": 200, "quantity": 2},
    {"price": 400, "quantity": 3},
    {"price": 150, "quantity": 2},
    {"price": 600, "quantity": 2}
]

discounted_count = 0

for order in orders:
    order_total = order["price"] * order["quantity"]
    
    if order_total >= 1000: 
       discounted_count += 1
       print("Discount applied")
    else:
        print("No discount")   
       

print("Discounted orders:", discounted_count)
    
    
  