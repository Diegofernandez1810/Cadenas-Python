products = input("Enter the products separated by commas: ")

product_list = products.split(',')

for product in product_list:
    print(product.strip())
