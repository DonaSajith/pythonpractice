import re

with open("data.txt", "r") as file:
    content = file.read()

emails = re.findall(r'\b[\w.-]+@[\w.-]+\.\w+\b', content)

print(emails)