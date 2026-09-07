amount = float(input("Enter shopping amount: "))

if amount >= 5000:
    discount = amount * 0.20
elif amount >= 3000:
    discount = amount * 0.10
else:
    discount = 0

final_amount = amount - discount

print("Discount:", discount)
print("Final Amount:", final_amount)