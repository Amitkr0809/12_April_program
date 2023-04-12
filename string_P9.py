# Program to convert lowercase vowel to uppercase in string.

inp = input("enter String : ")
out = " "
for i in inp:
    if i in ("a","e","i","o","u"):
        out= out + i.upper()
    else:
        out = out + i
print(out)






