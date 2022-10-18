s = "A man, a plan,df a canal: Panama"
str = ""
for i in s:
    if i.isalpha():
        str = str+i.lower()
for i in range(len(str)//2):
    if str[i] != str[-(i+1)]:
        print("false")

print("True")