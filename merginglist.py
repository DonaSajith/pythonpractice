lst1 = [10, 20, 50, 100, 200]
lst2 = [30, 50, 100, 250, 300]
merged_lst = lst1 + lst2
unique = []
for i in merged_lst:
    if i not in unique:
        unique.append(i)

print("Merged list without duplicates:", unique)