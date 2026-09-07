employee = {
    "name": "Rohit",
    "age": 25,
    "department": "IT",
    "salary": 40000
}

print(employee["name"])
print(employee["salary"])
employee["salary"] = 45000
employee["city"] = "Kolkata"
del employee["age"]
print(employee)
