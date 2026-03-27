dict = {"a": 100, "b": 50, "c": 75}

max_key = max(dict, key=dict.get)
print("Key with max value:", max_key)