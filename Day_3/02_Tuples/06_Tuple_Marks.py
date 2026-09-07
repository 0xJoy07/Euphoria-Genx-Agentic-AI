def analyze_tuple_marks(marks):
    print(max(marks))
    print(min(marks))
    print(marks.count(92))
    print(marks.index(45))
    print(sum(marks))


marks = (78, 92, 85, 67, 92, 45, 92)
analyze_tuple_marks(marks)
