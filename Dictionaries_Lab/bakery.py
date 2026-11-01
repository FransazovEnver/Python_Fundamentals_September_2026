table_of_stock = input().split()

stock_dict = {}

for stock in range(0, len(table_of_stock), 2):
    food = table_of_stock[stock]
    quantity = int(table_of_stock[stock + 1])
    stock_dict[food] = quantity
print(stock_dict)