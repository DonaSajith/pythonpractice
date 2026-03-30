numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
rev=[]
for i in range (len(numbers)-1,-1,-1):
    rev.append(numbers[i])
print("Reversed list",rev)