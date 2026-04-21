with open("data.txt", "r") as file:
    content = file.read()

count = content.count("Python")
print("Count:", count)