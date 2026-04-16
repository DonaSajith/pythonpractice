def dict_merge(dict1, dict2):
    merged = dict1.copy()

    for key, value in dict2.items():
        if key in merged:
            merged[key] += value
        else:
            merged[key] = value
    return merged


dict1 = {"a": 20, "b": 30, "c": 40}
dict2 = {"a": 60, "b": 70, "d": 80}
print(dict_merge(dict1, dict2))
