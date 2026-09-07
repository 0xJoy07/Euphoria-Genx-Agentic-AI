marks = [78, 45, 92, 67, 33, 89, 56, 95]

passed = 0
failed = 0

for mark in marks:
    print(mark)
    if mark >= 50:
        passed += 1
    else:
        failed += 1

print(passed)
print(failed)
print(max(marks))
print(min(marks))
