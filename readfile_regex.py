import re

with open("data.txt", "r") as file:
    for line in file:
        if re.search(r'error', line, re.IGNORECASE):
            print(line)