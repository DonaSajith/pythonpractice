def dict_merge(dict1, dict2):
    merged = dict1.copy()

    for key, value in dict2.items():
        if key in merged:
            merged[key] = [merged[key], value]
        else:
            merged[key] = value

    return merged


dict1 = {"a": 20, "b": 30, "c": 40}
dict2 = {"a": "Alice", "b": "Bob", "d": 80}
print(dict_merge(dict1, dict2))
