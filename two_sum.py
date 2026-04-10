num = [2, 7, 8, 65, 87, 43, 35]
target = 100
d = {}

for i, n in enumerate(num):
    diff = target - n
    if diff in d:
        print([d[diff], i])
    d[n] = i