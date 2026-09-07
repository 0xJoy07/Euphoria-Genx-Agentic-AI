def count_long_cities(cities):
    count = 0

    for city in cities:
        print(city)
        if len(city) > 5:
            print(city)
            count += 1

    return count


cities = ("Kolkata", "Delhi", "Mumbai", "Chennai", "Pune")
count = count_long_cities(cities)
print(count)
