def count_kwargnum(**kwargs):
    return len(kwargs)
print(count_kwargnum(a=1, b=2, c=3))