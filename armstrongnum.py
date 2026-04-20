def is_armstrong(num):
    number = num
    total = 0
    while num > 0:
        digit = num % 10
        total += digit ** 3
        num //= 10
    return total == number

try:
    n = int(input("Enter a number: "))
    if is_armstrong(n):
        print(n, "is an Armstrong number")
    else:
        print(n, "is not an Armstrong number")
except ValueError:
    print("Invalid input! Please enter a valid integer")