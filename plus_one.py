digits = [1,2,3]
length = len(digits)
value = 0
multiplier = 10 ** (length- 1)
i = 0
while length != 0 and i != length:
    value += int(digits[i] * multiplier)
    multiplier /= 10
    i += 1
value += 1
multi = 1
while value >= multi * 10:
    multi *= 10
digits = []
while int(multi) != 0:
    digits.append(value // multi)
    value = value % multi
    multi = multi // 10
print(digits)

