import math

shape = input("Enter the shape(circle, square, rectangle or traingle): ")

if shape == "circle":
    rad = float(input("Enter radius: "))
    area = math.pi * rad * rad
    print("Area of Circle:", area)

elif shape == "square":
    side = float(input("Enter side: "))
    area = side * side
    print("Area of Square:", area)

elif shape == "rectangle":
    length = float(input("Enter length: "))
    breadth = float(input("Enter breadth: "))
    area = length * breadth
    print("Area of Rectangle:", area)

elif shape == "triangle":
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    area = 0.5 * base * height
    print("Area of Triangle:", area)

else:
    print("Invalid choice")