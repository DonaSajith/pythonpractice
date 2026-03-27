lst = [10, 20, 30, 40, 20, 40, 50, 60, 70, 60]
set1 = set()
dup = []

for i in lst:
    if i in set1:
        if i not in dup:
            dup.append(i)
    else:
        set1.add(i)

print("Duplicates in list:", dup)