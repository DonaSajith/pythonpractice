import re
with open("data.txt", "r") as file:
    content = file.read()
phones = re.findall(r'\b\d{10}\b', content)
print(phones)