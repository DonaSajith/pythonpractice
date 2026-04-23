import json

data = {
  "users": [
    {
      "name": "Arjun Kumar",
      "age": 28,
      "email": "arjun.kumar@example.com",
      "phone": "+91-9876543210"
    },
    {
      "name": "Meena Sharma",
      "age": 34,
      "email": "meena.sharma@example.com",
      "phone": "+91-9123456780"
    },
    {
      "name": "Rohit Verma",
      "age": 25,
      "email": "rohit.verma@example.com",
      "phone": "+91-9988776655"
    },
    {
      "name": "Sneha Iyer",
      "age": 31,
      "email": "sneha.iyer@example.com",
      "phone": "+91-9090909090"
    },
    {
      "name": "Vikram Rao",
      "age": 40,
      "email": "vikram.rao@example.com",
      "phone": "+91-9555566666"
    }
  ]
}

with open("users.json", "w") as file:
    json.dump(data, file, indent=4)

import re
age = []

with open("users.json", "r") as file:
    for line in file:
        if re.search(r'age', line):
            print(line, end='')
            age.append(line)