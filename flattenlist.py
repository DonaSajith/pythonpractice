my_list = [1, 2, 3, [4, 5, 6], 7, 8, 9]
lst=[]

for i in my_list:
    if isinstance(i, list):
        lst.extend(i)
    else:
        lst.append(i)
print(lst)
total= sum(lst)
print(total)