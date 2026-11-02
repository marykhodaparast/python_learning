def generate_sales_report(orders):
    
    total_price_before_discount = 0
    number_of_discounted_orders = 0
    total_discount_price = 0
    total_price_after_discount = 0
    largest_order = 0

    for order in orders:
       order_total = order["price"] * order["quantity"]
       total_price_before_discount += order_total
       if order_total > largest_order:
         largest_order = order_total
        
       if order_total  > 2000:
         total_discount_price += 0.2 * order_total
         order_total = 0.8 * order_total
         number_of_discounted_orders += 1
       elif order_total > 1000:
          total_discount_price += 0.1 * order_total
          order_total = 0.9 * order_total
          number_of_discounted_orders += 1
            
                
       total_price_after_discount += order_total     
    
    return {
       "total_number_of_orders" : len(orders),
       "total_price_before_discount" :total_price_before_discount,
       "number_of_discounted_orders" : number_of_discounted_orders, 
       "total_discount_price" : total_discount_price,  
       "total_price_after_discount" : total_price_after_discount, 
       "largest_order" : largest_order
    }    
    


orders = [
    {"price": 200, "quantity": 2},
    {"price": 400, "quantity": 3},
    {"price": 150, "quantity": 2},
    {"price": 600, "quantity": 2}
]

output = generate_sales_report(orders)

print("Total number of orders is:", output["total_number_of_orders"])
print("Total price before discount is:", output["total_price_before_discount"])
print("Total number of discounted orders is:", output["number_of_discounted_orders"])
print("Total discount price is:", output["total_discount_price"])
print("Total price after discount is:", output["total_price_after_discount"])
print("Largest order price is:", output["largest_order"])

