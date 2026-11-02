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
            
    avg_of_successful_transactions = ( total_amount_of_successful_transactions / number_of_successful_transactions) if number_of_successful_transactions else 'Not Countable'
    
    return {
        "number_of_transactions" : number_of_transactions,
        "number_of_successful_transactions": number_of_successful_transactions,
        "number_of_failed_transactions": number_of_failed_transactions,
        "total_amount_of_successful_transactions": total_amount_of_successful_transactions,
        "max_successful_transaction_user" : max_successful_transaction_user,
        "avg_of_successful_transactions": avg_of_successful_transactions
    }   
    
    
transactions = [
    {"user": "Ali", "amount": 1200, "status": "success"},
    {"user": "Sara", "amount": 500, "status": "failed"},
    {"user": "John", "amount": 2500, "status": "success"},
    {"user": "Mary", "amount": 1800, "status": "success"},
    {"user": "David", "amount": 700, "status": "pending"},
    {"user": "Ali", "amount": 900, "status": "success"}
]

output = analyze_transactions(transactions)

print("Number of all transactions is:", output["number_of_transactions"])
print("Number of successful transactions is:", output["number_of_successful_transactions"])  
print("Number of failed transactions is:", output["number_of_failed_transactions"])  
print("Total amount of successful transactions is:", output["total_amount_of_successful_transactions"])   
print("Max successful transaction user is:", output["max_successful_transaction_user"])  
print("Average of successful transactions is:", output["avg_of_successful_transactions"]) 
      
            
    
