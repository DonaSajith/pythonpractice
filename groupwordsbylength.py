words= ["hi", "hello", "world", "bye"]
group={}
for word in words:
    length = len(word)
    group.setdefault(length, []).append(word)
print(group)