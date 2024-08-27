price = input("Enter the price of the product in euros (e.g., 12.34): ")

euros, cents = price.split('.')

print(f"Euros: {euros}")
print(f"Cents: {cents}")
