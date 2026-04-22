import re

error_lines = []

with open("serial.log", "r") as file:
    for line in file:
        if re.search(r'ERROR', line):
            print(line, end='')
            error_lines.append(line)

with open("log.txt", "w") as file:
    for line in error_lines:
        file.write(line)
