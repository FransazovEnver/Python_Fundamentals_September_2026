stock_data = input().split()

stock = {}

for stock_index in range(0, len(stock_data), 2):
    product = stock_data[stock_index]
    quantity = stock_data[stock_index + 1]
    stock[product] = quantity

product_to_search = input().split()

for product in product_to_search:
    if product in stock:
        print(f"We have {stock[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")