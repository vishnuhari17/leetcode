num=int(input("Enter Number : "))
value = ""
integer = [["I",1],["IV",4],["V",5],["IX",9],["X",10],["XL",40],["L",50],["XC",90], ["C",100],["CD",400],["D",500],["CM",900],["M",1000]]
for sym, val in reversed(integer):
    if num//val:
        count = num//val
        value += (sym*count)
        num = num % val
print(value)