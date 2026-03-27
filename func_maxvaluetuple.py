def max_tuple(tup):
    max_val = tup[0]

    for i in tup:
        if i > max_val:
            max_val = i
    return max_val

tuple=(12, 15, 13, 87, 24)
print("Maximum value is", max_tuple(tuple))