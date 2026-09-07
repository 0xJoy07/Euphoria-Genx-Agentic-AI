def analyze_student_marks(marks, pass_mark):
    passed = 0
    highest_mark = 0

    for name, mark in marks.items():
        status = "Pass" if mark >= pass_mark else "Fail"
        print(f"{name} - {mark} - {status}")
        if mark >= pass_mark:
            passed += 1
        if mark > highest_mark:
            highest_mark = mark

    return passed, highest_mark


marks = {
    "Rohit": 85,
    "Amit": 45,
    "Priya": 92,
    "Neha": 67,
    "Rahul": 38
}
passed, highest_mark = analyze_student_marks(marks, 50)
print(passed)
print(highest_mark)
