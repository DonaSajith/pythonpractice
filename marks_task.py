data = [
    ("meena", ["Math", "Physics"], {"Math": 85, "Physics": 90}),
    ("hamsa", ["Math", "Chemistry"], {"Math": 78, "Chemistry": 88}),
    ("pooja", ["Physics", "Chemistry"], {"Physics": 92, "Chemistry": 81})
]

meena, hamsa, pooja = data
name_1,subjects_1,marks_1 = meena
name_2,subjects_2,marks_2 = hamsa
name_3,subjects_3,marks_3 = pooja


total_meena = sum(marks_1.values())
print("Total marks of Meena:",total_meena)
total_hamsa = sum(marks_2.values())
print("Total marks of Hamsa:",total_hamsa)
total_pooja = sum(marks_3.values())
print("Total marks of Pooja:",total_pooja)


highest_marks= 0
if total_meena > total_hamsa and total_meena > total_pooja:
    highest_marks = total_meena
elif total_hamsa > total_meena and total_hamsa > total_pooja:
    highest_marks = total_hamsa
else:
    highest_marks = total_pooja
print("Highest marks:",highest_marks)


if highest_marks == total_meena:
    print("Meena has the highest total.")
elif highest_marks == total_hamsa:
    print("Hamsa has the highest total.")
else:
    print("Pooja has the highest total.")



keys = (name_1, name_2, name_3)
values = (total_meena, total_hamsa, total_pooja)
dict_marks = dict(zip(keys, values))
print(dict_marks)
