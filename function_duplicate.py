def find_duplicates(lst):
    set1 = set()
    duplicates = []
    for i in lst:
        if i in set1:
            if i not in duplicates:
                duplicates.append(i)
        else:
            set1.add(i)
    return duplicates

lst = [10, 20, 30, 40, 20, 40, 50, 60, 70, 60]
print(find_duplicates(lst))