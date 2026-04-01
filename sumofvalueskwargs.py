def sum_values(**kwargs):
    total = 0
    for value in kwargs.values():
        total += value
    return total

print(sum_values(a=20, b=50, c=100, d=150))   # 60