def split_even_odd(numbers):
    even_numbers = []
    odd_numbers = []

    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)

    return even_numbers, odd_numbers


numbers = [12, 7, 25, 18, 30, 41, 56, 63, 80]
even_numbers, odd_numbers = split_even_odd(numbers)
print("Even:", even_numbers)
print("Odd:", odd_numbers)
