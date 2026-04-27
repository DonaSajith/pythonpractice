def student_marks(data):
    total_student= {}

    for name, subjects, marks in data:
        total = sum(marks.values())
        total_student[name] = total
        print(f"Total marks of {name}: {total}")


    highest_student = max(total_student, key=total_student.get)
    highest_marks = total_student[highest_student]
    print("Highest marks:", highest_marks)
    print(f"{highest_student} has the highest total.")
    print(total_student)
    return total_student, highest_student, highest_marks


data = [
    ("meena", ["Math", "Physics"], {"Math": 85, "Physics": 90}),
    ("hamsa", ["Math", "Chemistry"], {"Math": 78, "Chemistry": 88}),
    ("pooja", ["Physics", "Chemistry"], {"Physics": 92, "Chemistry": 81})
]

student_marks(data)