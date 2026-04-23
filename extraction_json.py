import re
age = []

with open("users.json", "r") as file:
    for line in file:
        if re.search(r'age', line):
            print(line, end='')
            age.append(line)