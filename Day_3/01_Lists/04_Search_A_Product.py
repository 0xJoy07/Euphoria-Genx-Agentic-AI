def search_product(products, product):
    if product in products:
        return f"{product} is available"
    return "Product not found"


products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer"]
product = "Mouse"
print(search_product(products, product))
