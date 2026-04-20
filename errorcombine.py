try:
    num = int(input("Enter a number: "))
    d= num/0
except ValueError:
    print("Error: Please enter a number")
except ZeroDivisionError:
    print("Error: Division by zero")
except Exception as e:
    print(e)