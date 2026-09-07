students = {
    "Rohit": {
        "age": 21,
        "marks": 85
    },
    "Amit": {
        "age": 20,
        "marks": 45
    },
    "Priya": {
        "age": 22,
        "marks": 92
    }
}

passed = 0
highest_marks = 0
top_student = ""

for name, data in students.items():
    age = data["age"]
    marks = data["marks"]
    print(name)
    print(age, marks)
    if marks >= 50:
        print("Pass")
        passed += 1
    else:
        print("Fail")
    if marks > highest_marks:
        highest_marks = marks
        top_student = name

print(passed)
print(top_student)
