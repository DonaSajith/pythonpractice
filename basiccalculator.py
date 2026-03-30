num1= int(input("Enter the first number: "))
num2= int(input("Enter the second number: "))
op_symbol = input("Enter a operator +,-,* or /: ")
if op_symbol == "+":
    sum = num1 + num2
    print("The sum of two numbers is", sum)
elif op_symbol == "-":
    diff = num1 - num2
    print("The difference of two numbers is", diff)
elif op_symbol == "*":
    prod = num1 * num2
    print("The product of two numbers is", prod)
elif op_symbol == "/":
    if num2!=0:
        quot = num1 / num2
        print("The quotient of two numbers is", quot)
    else:
        print("Invalid number")
