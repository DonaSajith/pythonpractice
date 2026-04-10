marks= {"math": 90, "science": 80, "economy": 70, "history": 80, "english": 90}
max_value = max(marks.values())
max_keys = [k for k, v in marks.items() if v == max_value]

print(max_keys)