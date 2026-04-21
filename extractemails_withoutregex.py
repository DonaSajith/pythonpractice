with open("data.txt", "r") as file:
    words = file.read().split()

emails = []

for word in words:
    if "@" in word and "." in word:
        emails.append(word)

print(emails)