name= input("Enter your name: ")
marks= int(input("Enter your marks: "))
if marks >=90:
    grade= "A plus"
elif marks >=80:
    grade= "A"
elif marks >=70:
    grade= "B"
elif marks >=60:
    grade= "C"
elif marks >=50:
    grade= "D"
else:
    grade= "F"

print("Name:", name)
print("Marks:", marks)
print("Grade:", grade)