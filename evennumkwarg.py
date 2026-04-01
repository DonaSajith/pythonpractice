def even_values(**kwargs):
    for key, value in kwargs.items():
        if value % 2 == 0:
            print(key, ":", value)

even_values(a=11, b=52, c=33, d=14, e=67, f=45)