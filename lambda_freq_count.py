list1 = [1, 2, 3, 1, 2, 1]
freq = dict(map(lambda x: (x, list1.count(x)), list1))
print(freq)