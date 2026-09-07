salary = float(input("Enter your salary: "))

if salary >= 100000:
    tax = salary * 0.20
elif salary >= 50000:
    tax = salary * 0.10
else:
    tax = salary * 0.05

print("Tax:", tax)
