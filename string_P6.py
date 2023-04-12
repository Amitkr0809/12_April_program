# input = "aaaabbbbbccccccddddddddeeeeeeeffffff"
# output = abcdef

inp = "aaaabbbbbccccccddddddddeeeeeeeffffff"
t =set(inp)
print(t)
d = sorted(t)
print(d)
for i in d:
    print(i,end="")

