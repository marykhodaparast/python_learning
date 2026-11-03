def analyze_inventory(products):
    
    number_of_products = len(products)
    total_value_of_store = 0
    total_stock_value = 0
    product_count_of_stock_less_than_5 = 0
    max_value_product = 0
    max_value_product_name = ""
    avg_price_value = 0
    
    for product in products:
        value = product["stock"] * product["price"]
        total_value_of_store += value
        total_stock_value += product["stock"]
        if product["stock"] < 5:
            product_count_of_stock_less_than_5 += 1
            
        if value > max_value_product:
            max_value_product = value  
            max_value_product_name = product["name"]
             
    avg_price_value = (total_stock_value / number_of_products) if number_of_products else 'Not countable'   
        
        
    return {
        "number_of_products": number_of_products,
        "total_value_of_store": total_value_of_store,
        "product_count_of_stock_less_than_5": product_count_of_stock_less_than_5,
        "max_value_product_name": max_value_product_name,
        "avg_price_value": avg_price_value
    }    
    
    
products = [
    {"name": "Laptop", "price": 1200, "stock": 4},
    {"name": "Mouse", "price": 25, "stock": 20},
    {"name": "Keyboard", "price": 75, "stock": 8},
    {"name": "Monitor", "price": 300, "stock": 3},
    {"name": "USB Cable", "price": 10, "stock": 50}
]

output = analyze_inventory(products)

print("Number of products is:", output["number_of_products"])   
print("Total value of store is:", output["total_value_of_store"])
print("Product count with stock less than 5 is:", output["product_count_of_stock_less_than_5"])
print("Max value product name is:", output["max_value_product_name"]) 
print("Average price value of the store is:", output["avg_price_value"])
        
    