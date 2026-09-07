marks = {
    "Rohit": 85,
    "Amit": 45,
    "Priya": 92,
    "Neha": 67,
    "Rahul": 38
}

passed = 0
highest_mark = 0

for name, mark in marks.items():
    status = "Pass" if mark >= 50 else "Fail"
    print(f"{name} - {mark} - {status}")
    if mark >= 50:
        passed += 1
    if mark > highest_mark:
        highest_mark = mark

print(passed)
print(highest_mark)
