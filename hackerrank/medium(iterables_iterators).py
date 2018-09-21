import math
f = math.factorial
n = int(input())
a = input().count('a')
indices = int(input())
denom = f(n)//(f(indices)*f(n-indices))
nota = n-a
if indices>nota:
    p=1.0
else:
    numer = f(nota)//(f(indices)*f(nota-indices))
    p = 1 - numer/denom
print(p)
