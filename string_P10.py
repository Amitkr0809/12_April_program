# Program to delete vowels in a given string.

inp = input("enter String : ")
out = " "
for i in inp:
    if i in ("a","e","i","o","u"):
        out= out + i.replace(i,"")
    else:
        out = out + i
print(out)