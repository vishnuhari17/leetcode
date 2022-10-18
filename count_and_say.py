n = 4
str = []
str2 = []
for i in range(0, n):

    if i == 0:
        str.append(1)
    else:
        count = 0
        for i in range(len(str) - 1):
            if str[i] == str[i + 1]:
                count += 1
            else:
                str2.append(count)
                str2.append(str[i])
        str2.append(count)
        str2.append(str[i])

print(str)
print(str2)
