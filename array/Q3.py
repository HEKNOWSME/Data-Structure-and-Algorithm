stock_prices = [100.5, 107.3, 109.2, 111.1, 109.4, 107.0, 106.9]
maximum = 0
for price in stock_prices:
    if price > maximum:
        maximum = price
minimum = min(stock_prices)
print('maximum', maximum)
print('minimum', minimum)
