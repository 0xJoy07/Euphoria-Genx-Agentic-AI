secret = 25

while True:
    guess = int(input("Enter your guess: "))
    if guess > secret:
        print("Too High")
    elif guess < secret:
        print("Too Low")
    else:
        print("Correct! You guessed it.")
        break
