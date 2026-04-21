with open("data.txt", "r") as file:
    content = file.read()

updated = content.replace("Python", "Java")

with open("output.txt", "w") as file:
    file.write(updated)
with open("output.txt", "r") as file:
    print(file.read())