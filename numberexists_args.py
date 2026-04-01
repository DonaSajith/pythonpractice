def check_number(x, *args):
    for num in args:
        if num == x:
            return "Found"
    return "Not Found"

print(check_number(2, 2, 1, 4, 5, 7))