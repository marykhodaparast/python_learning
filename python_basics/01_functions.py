def calculate_discount(price):
    output = 0
    
    if price >= 1000:
      output = price - 0.1 * price
    else:
      output = price
    return output


print(calculate_discount(2000))
print(calculate_discount(500))