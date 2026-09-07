def update_employee(employee, salary, city, remove_key):
    print(employee["name"])
    print(employee["salary"])
    employee["salary"] = salary
    employee["city"] = city
    del employee[remove_key]
    return employee


employee = {
    "name": "Rohit",
    "age": 25,
    "department": "IT",
    "salary": 40000
}
updated_employee = update_employee(employee, 45000, "Kolkata", "age")
print(updated_employee)
