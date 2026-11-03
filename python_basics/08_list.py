orders = [
    {"price": 200, "quantity": 2},
    {"price": 400, "quantity": 3},
    {"price": 150, "quantity": 2},
    {"price": 600, "quantity": 2}
]

orders_with_discount = 0
order_total_price = 0

for order in orders:
    order_total = order["price"] * order["quantity"]
    if order_total >= 1000: 
        order_total_price += order_total
        orders_with_discount += 1
        
        
print("The number of orders with discount is:", orders_with_discount)
print("Total amount of discounted orders:" , order_total_price)        
        
        

       