try:
    a=int(input("Enter a number: "))
    result= 10/a
except ZeroDivisionError:
    print("Division Error")
except ValueError:
    print("Value Error")