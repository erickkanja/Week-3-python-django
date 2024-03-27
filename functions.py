def calculate_discount(price, discount_percent):
  if discount_percent >= 20:
    print(price - (discount_percent / 100 * price))
  else:
    print(price)

price = float(input("How much is the item before the discount?"))
discount = float(input("What is the discount percentage?"))

final_price = calculate_discount(price, discount)
print(final_price)