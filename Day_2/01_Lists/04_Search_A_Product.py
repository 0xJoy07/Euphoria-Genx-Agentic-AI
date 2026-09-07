products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer"]

product = input("Enter product: ")

if product in products:
    print(f"{product} is available")
else:
    print("Product not found")
