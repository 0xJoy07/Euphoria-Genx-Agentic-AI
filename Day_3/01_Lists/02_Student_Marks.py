def analyze_marks(marks, pass_mark):
    passed = 0
    failed = 0

    for mark in marks:
        print(mark)
        if mark >= pass_mark:
            passed += 1
        else:
            failed += 1

    return passed, failed, max(marks), min(marks)


marks = [78, 45, 92, 67, 33, 89, 56, 95]
passed, failed, highest, lowest = analyze_marks(marks, 50)
print(passed)
print(failed)
print(highest)
print(lowest)
