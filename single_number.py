memory = []
for i in nums:
    if i in memory:
        memory.remove(i)
    else:
        memory.append(i)
for i in memory:
    return i