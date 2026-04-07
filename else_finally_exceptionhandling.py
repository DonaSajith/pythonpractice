try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Error in conversion")
else:
    print("Success:", num)
finally:
    print("Execution finished")