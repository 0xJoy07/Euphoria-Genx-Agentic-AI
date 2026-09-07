marks = [78, 45, 89, 32, 67, 91, 56, 74]

passed = 0
failed = 0
highest_mark = marks[0]

for mark in marks:
    print("Mark:", mark)
    if mark >= 50:
        passed += 1
    else:
        failed += 1
    
    if mark > highest_mark:
        highest_mark = mark

print("Passed:", passed)
print("Failed:", failed)
print("Highest Mark:", highest_mark)
