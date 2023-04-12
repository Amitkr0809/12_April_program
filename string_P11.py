# Program to count Occurrence Of Vowels & Consonants in a String.

inp = input("enter String : ")
Vo_count = 0
Co_count = 0
for i in inp:
    if i in ("a","e","i","o","u"):
        Vo_count = Vo_count + 1
    else:
        Co_count = Co_count + 1

print("Number of vowels in given string :",Vo_count)
print("Number of Consonants in given string :",Co_count)
