try:
    divident = int(input("Enter a number: "))
    divisor = int(input("Enter a number: "))
    if divisor==0:
        raise ZeroDivisionError
    else:
        quotient = divident/divisor
        print(quotient)
except ZeroDivisionError:
    print("Division by zero")
except Exception as e:
    print(e)
finally:
    print("Program ended")
