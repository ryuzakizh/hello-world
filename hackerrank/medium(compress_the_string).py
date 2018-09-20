from itertools import groupby
string = input()
gr = groupby(string)
result = []
for stri,num in gr:
    c = len(list(num))
    result.append((c,int(stri)))
print(*(result),sep=" ")
