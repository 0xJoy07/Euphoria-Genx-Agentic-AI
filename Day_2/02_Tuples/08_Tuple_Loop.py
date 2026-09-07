cities = ("Kolkata", "Delhi", "Mumbai", "Chennai", "Pune")

count = 0

for city in cities:
    print(city)
    if len(city) > 5:
        print(city)
        count += 1

print(count)
