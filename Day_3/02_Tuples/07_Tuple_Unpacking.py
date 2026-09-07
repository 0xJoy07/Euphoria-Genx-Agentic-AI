def show_student(student):
    name, age, course, marks = student
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Course: {course}")
    print(f"Marks: {marks}")


student = ("Amit", 20, "Python", 88)
show_student(student)
