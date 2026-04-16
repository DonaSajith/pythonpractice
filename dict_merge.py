def dict_merge(dict1, dict2):
    dict1.update(dict2)
    return dict1


dict1 = {"a": 20, "b": 30, "c": 40}
dict2 = {"d": 60, "e": 70, "f": 80}
print(dict_merge(dict1, dict2))
