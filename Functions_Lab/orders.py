prices = {
    "coffee": 1.50,
    "water": 1.00,
    "coke": 1.40,
    "snacks": 2.00
}

def total_order(order, quantity):
    if order in prices:
        return prices[order] * quantity

order_ = input()
quantity_ = int(input())
total_price = total_order(order_, quantity_)
print(f"{total_price:.2f}")
