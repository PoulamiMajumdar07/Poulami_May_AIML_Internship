def analyze_result(name, roll, marks):
    total = sum(marks)
    average = total / len(marks)
    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "Fail"
    print("Student Name:", name)
    print("Roll Number:", roll)
    print("Marks:", marks)
    print("Total Marks:", total)
    print("Average Marks:", average)
    print("Grade:", grade)
    print("Subjects with marks below 40:")
    found = False
    for i in range(len(marks)):
        if marks[i] < 40:
            print("Subject", i + 1, ":", marks[i])
            found = True
    if not found:
        print("None")
name = "poulami"
roll = 25
marks = [85.5, 72.0, 39.5, 91.0, 67.5]

analyze_result(name, roll, marks)
