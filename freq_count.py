def count_num(list1):
    set1 = set(list1)
    unique_num=[]
    for i in list1:
        if i in set1:
            if i not in unique_num:
                unique_num.append(i)
        else:
            set1.add(i)
    print(unique_num)
    freq = {}
    for i in list1:
        freq[i] = freq.get(i, 0) + 1
    print(freq)

list1=[1,2,3,1,2,1]
count_num(list1)
