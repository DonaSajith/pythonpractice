import re
with open("data.txt", "r") as file:
    content = file.read()

updated = re.sub(r'\d', '*', content)
with open("out.txt", "w") as file:
    file.write(updated)