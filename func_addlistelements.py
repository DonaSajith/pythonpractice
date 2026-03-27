def add_elements(lst):
    sum=0

    for i in lst:
        sum+=i
    return sum

num=[1,2,3,4,5,6,7,8,9,10]
print("Sum of elements is", add_elements(num))