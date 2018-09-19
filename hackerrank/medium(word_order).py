from collections import OrderedDict
n = int(input())
words = []
dicto = OrderedDict()
for i in range(n):
    ask = input()
    words.append(ask)
for word in words:
    dicto[word] = dicto.get(word,0) + 1
val = list(dicto.values())
print(len(val))
for t in val:
    print(t,end = " ")
