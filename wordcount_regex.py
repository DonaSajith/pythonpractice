import re

with open("data.txt", "r") as file:
    content = file.read()

matches = re.findall(r'\bPython\b', content)

print("Count:", len(matches))