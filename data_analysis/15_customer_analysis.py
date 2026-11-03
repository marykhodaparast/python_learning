def analyze_customers(customers):

    total_purchase_amount = 0   
    number_of_customers_with_purchases_at_least_1000 = 0
    avg_purchase = 0
    customer_with_max_purchase_name = ""
    max_purchase_amount = 0
    
    total_customers = len(customers)
     
    for customer in customers:
        total_purchase_amount += customer["purchases"]
        
        
        if customer["purchases"] > max_purchase_amount:
            max_purchase_amount = customer["purchases"]
            customer_with_max_purchase_name = customer["name"]
        
        if customer["purchases"] >= 1000:
           number_of_customers_with_purchases_at_least_1000 += 1
        
    avg_purchase = (total_purchase_amount / total_customers) if total_customers else 'Not Countable'
    
    return {
        "number_of_customers": total_customers,
        "total_purchases_amount": total_purchase_amount,
        "number_of_customers_with_purchases_at_least_1000": number_of_customers_with_purchases_at_least_1000,
        "customer_with_max_purchase": customer_with_max_purchase_name,
        "avg_purchase": avg_purchase
           
    }    
    
customers = [
    {"name": "Ali", "purchases": 1200},
    {"name": "Sara", "purchases": 500},
    {"name": "John", "purchases": 2500},
    {"name": "Mary", "purchases": 1800},
    {"name": "David", "purchases": 700}
]

output = analyze_customers(customers)

print("Number of Customers is:", output["number_of_customers"])
print("Total purchases amount is:", output["total_purchases_amount"])    
print("Number of customers with purchases at least 1000 is:", output["number_of_customers_with_purchases_at_least_1000"])
print("Customer with max purchase is:", output["customer_with_max_purchase"])
print("Avg purchase is:", output["avg_purchase"])