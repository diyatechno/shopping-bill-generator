item = input("Enter your item name:")
price = int(input("Enter your item price:"))
quantity = int(input("Enter your items quantity:"))
total_bill = price * quantity

print("=" * 35)
print("    shopping bill     ")
print("=" * 35)
print(f"Item       : {item}")
print(f"Price      : ₹{price}")
print(f"Quantity   : {quantity}")
print(f"Total Bill : ₹{total_bill}")
print("Thank you for buying from our shop, Please visit again")