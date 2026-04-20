try:
    age = int(input("Enter your age: "))
    if age <= 0 or age >= 135:
        raise ValueError("Age not appropriate")
    else:
        print("Your age is", age)
except ValueError as e:
    print("Error:",e)