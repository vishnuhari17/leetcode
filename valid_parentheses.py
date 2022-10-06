s = input("Enter the string")
stack = []
check = {')':'(','}':'{',']':'['}
for i in s:
    if i in check:
        if stack and stack[-1] == check[i]:
            stack.pop()
        else:
            print("False")
    else:
        stack.append(i)
print("True") if not stack else print("False")