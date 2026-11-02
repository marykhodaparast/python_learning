
prices = [2500, 1500, 500, 6000, 3200]

for price in prices:
    if price >= 5000:
        final_price = price * 0.7
    elif price >= 2000:
        final_price = price * 0.8
    elif price >= 1000:
        final_price = price * 0.9
    else:
        final_price = price

    print(final_price)
