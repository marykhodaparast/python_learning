def calculate_total(price, quantity):
    return price * quantity

total = calculate_total(150, 3)

if total >= 400:
    print("Large order")
else:
    print("Small order")

print(total)