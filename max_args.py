def maximum(*args):
    maximum = args[0]
    for i in args:
        if i > maximum:
            maximum = i
    return maximum

print(maximum(14,17,19,87,74,80,25,39,46))