balance = 10000

while True:
    amount = int(input("Enter withdrawal amount: "))
    if amount == 0:
        print("Thank you!")
        break
    
    if amount > balance:
        print("Insufficient Balance")
    else:
        balance -= amount
        print("Remaining balance:", balance)
