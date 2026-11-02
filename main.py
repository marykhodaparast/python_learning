from fastapi import FastAPI

app = FastAPI()

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
        
    avg_purchase = (total_purchase_amount / total_customers) if total_customers else None
    
    return {
        "number_of_customers": total_customers,
        "total_purchases_amount": total_purchase_amount,
        "number_of_customers_with_purchases_at_least_1000": number_of_customers_with_purchases_at_least_1000,
        "customer_with_max_purchase": customer_with_max_purchase_name,
        "avg_purchase": avg_purchase
           
    }    
    
    
def analyze_inventory(products):
    
    number_of_products = len(products)
    total_value_of_store = 0
    total_stock_value = 0
    product_count_of_stock_less_than_5 = 0
    max_value_product = 0
    max_value_product_name = ""
    avg_stock_per_product = 0
    
    for product in products:
        value = product["stock"] * product["price"]
        total_value_of_store += value
        total_stock_value += product["stock"]
        if product["stock"] < 5:
            product_count_of_stock_less_than_5 += 1
            
        if value > max_value_product:
            max_value_product = value  
            max_value_product_name = product["name"]
             
    avg_stock_per_product = (total_stock_value / number_of_products) if number_of_products else None   
        
        
    return {
        "number_of_products": number_of_products,
        "total_value_of_store": total_value_of_store,
        "product_count_of_stock_less_than_5": product_count_of_stock_less_than_5,
        "max_value_product_name": max_value_product_name,
        "avg_stock_per_product": avg_stock_per_product
    }  
    
    
def analyze_transactions(transactions):
    
    number_of_transactions = len(transactions)
    number_of_successful_transactions = 0
    number_of_failed_transactions = 0
    total_amount_of_successful_transactions = 0
    max_successful_transaction = 0
    max_successful_transaction_user = ""
    avg_of_successful_transactions = 0
    
    for transaction in transactions:
        if transaction["status"] == "success":
            number_of_successful_transactions += 1
            total_amount_of_successful_transactions += transaction["amount"]
        
        if transaction["status"] == "failed":
            number_of_failed_transactions += 1    
            
        if transaction["status"] == "success" and transaction["amount"] > max_successful_transaction:
           max_successful_transaction = transaction["amount"]
           max_successful_transaction_user = transaction["user"]
            
    avg_of_successful_transactions = ( total_amount_of_successful_transactions / number_of_successful_transactions) if number_of_successful_transactions else None
    
    return {
        "number_of_transactions" : number_of_transactions,
        "number_of_successful_transactions": number_of_successful_transactions,
        "number_of_failed_transactions": number_of_failed_transactions,
        "total_amount_of_successful_transactions": total_amount_of_successful_transactions,
        "max_successful_transaction" : max_successful_transaction,
        "max_successful_transaction_user" : max_successful_transaction_user,
        "avg_of_successful_transactions": avg_of_successful_transactions
    }     
    

customers = [
    {"name": "Ali", "purchases": 1200},
    {"name": "Sara", "purchases": 500},
    {"name": "John", "purchases": 2500},
    {"name": "Mary", "purchases": 1800},
    {"name": "David", "purchases": 700}
]

products = [
    {"name": "Laptop", "price": 1200, "stock": 4},
    {"name": "Mouse", "price": 25, "stock": 20},
    {"name": "Keyboard", "price": 75, "stock": 8},
    {"name": "Monitor", "price": 300, "stock": 3},
    {"name": "USB Cable", "price": 10, "stock": 50}
]


transactions = [
    {"user": "Ali", "amount": 1200, "status": "success"},
    {"user": "Sara", "amount": 500, "status": "failed"},
    {"user": "John", "amount": 2500, "status": "success"},
    {"user": "Mary", "amount": 1800, "status": "success"},
    {"user": "David", "amount": 700, "status": "pending"},
    {"user": "Ali", "amount": 900, "status": "success"}
]


def generate_store_report(customers, products, transactions):
    
    return {
        "customers_report": analyze_customers(customers),
        "inventory_report": analyze_inventory(products),
        "transactions_report": analyze_transactions(transactions)
    }

report = generate_store_report(customers, products, transactions) 

@app.get("/report")

async def get_report():
    return report
    