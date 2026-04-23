import json
with open("users.json", "r") as file:
    data = json.load(file)

dict = {}
for user in data["users"]:
    dict[user["name"]] = user["age"]
print(dict)