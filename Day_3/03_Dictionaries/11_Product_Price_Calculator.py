def analyze_products(products):
    total = 0
    most_expensive_product = ""
    cheapest_product = ""
    highest_price = 0
    lowest_price = None

    for product, price in products.items():
        print(f"{product} - {price}")
        total += price
        if price > highest_price:
            highest_price = price
            most_expensive_product = product
        if lowest_price is None or price < lowest_price:
            lowest_price = price
            cheapest_product = product

    return total, most_expensive_product, cheapest_product


products = {
    "Laptop": 50000,
    "Mouse": 800,
    "Keyboard": 1500,
    "Headphones": 2000
}
total, most_expensive_product, cheapest_product = analyze_products(products)
print(f"Total: {total}")
print(f"Most Expensive: {most_expensive_product}")
print(f"Cheapest: {cheapest_product}")
