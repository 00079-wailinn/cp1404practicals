"""Number of items: 3
Price of item: 100
Price of item: 35.56
Price of item: 3.24
Total price for 3 items is $124.92  """


number_item = int(input("Number of items: "))
total_price_items = 0
while number_item < 0:
    print("Invalid number of items!")
    number_item = int(input("Number of items: "))

for item in range(number_item):
    item_price = float(input("Price of item: "))
    total_price_items += item_price

    if total_price_items > 100:
        discount = total_price_items * 0.1
        total_price_items -= discount

print(f"Total price for {number_item}items is ${total_price_items:.2f}")
