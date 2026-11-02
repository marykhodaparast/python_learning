
def calculate_discount(price):
    if price >= 5000:
        return 30
    elif price >= 2000:
        return 20
    elif price >= 1000:
        return 10
    else:
        return 0


print(calculate_discount(2500))
print(calculate_discount(1500))
print(calculate_discount(500))
