def evennum_args(*args):
    for i in args:
        if i % 2 == 0:
            print(i)
evennum_args(1,2,3,4,5,6)